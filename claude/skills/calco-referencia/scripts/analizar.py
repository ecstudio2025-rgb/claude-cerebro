#!/usr/bin/env python3
"""Desmonta un vídeo de referencia en datos medibles.

Uso: python3 analizar.py <video> <dir_salida> [--ocr-fps 10]

Saca, todo en local:
  meta.json        resolución, fps, duración, códecs
  frames/          TODOS los fotogramas a 360 px de ancho (para medir)
  full/            fotogramas a resolución completa en cada corte y cada cambio de subtítulo
  cortes.json      cortes duros y transiciones (diferencia de histograma + diferencia de píxel)
  movimiento.json  por fotograma: energía de cambio, escala y desplazamiento estimados (zoom/pan)
  palabras.json    transcripción palabra a palabra (whisper.cpp large-v3-turbo, local)
  ocr.jsonl        texto en pantalla con caja, a --ocr-fps (Vision de macOS)
  subtitulos.json  eventos de subtítulo agrupados: texto, entrada, salida, caja, colores, alto en px
  audio.json       onsets (posibles SFX), RMS por 50 ms, bandas, silencio, picos alineados a cortes
  layout.json      rectángulos grandes por plano (tarjetas/ventanas), color de fondo dominante
  hojas/           hojas de contacto: 1 por segundo y 1 por corte
"""
import json, os, subprocess, sys, math, shutil
from pathlib import Path
import numpy as np
import cv2

HERE = Path(__file__).resolve().parent
WHISPER_MODEL = Path.home() / "whisper-models/ggml-large-v3-turbo-q5_0.bin"


def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw).stdout


def probe(video):
    j = json.loads(sh(["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(video)]))
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    a = next((s for s in j["streams"] if s["codec_type"] == "audio"), None)
    num, den = map(int, v["r_frame_rate"].split("/"))
    return {
        "w": int(v["width"]), "h": int(v["height"]), "fps": num / den,
        "dur": float(j["format"]["duration"]), "vcodec": v["codec_name"],
        "acodec": a["codec_name"] if a else None, "asr": int(a["sample_rate"]) if a else None,
        "nb_frames": int(v.get("nb_frames", 0) or 0),
    }


def extraer_frames(video, out, fps):
    d = out / "frames"
    if d.exists() and any(d.iterdir()):
        return sorted(d.glob("*.jpg"))
    d.mkdir(parents=True, exist_ok=True)
    sh(["ffmpeg", "-v", "error", "-i", str(video), "-vf", "scale=360:-2", "-q:v", "3", str(d / "%06d.jpg")])
    return sorted(d.glob("*.jpg"))


def medir_frames(frames, fps):
    """Cortes, energía y transformación entre fotogramas consecutivos."""
    orb = cv2.ORB_create(800)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    prev = prev_hist = prev_kp = prev_des = None
    filas = []
    for i, f in enumerate(frames):
        img = cv2.imread(str(f))
        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
        cv2.normalize(hist, hist)
        kp, des = orb.detectAndCompute(g, None)
        fila = {"i": i, "t": round(i / fps, 3), "luma": round(float(g.mean()), 2)}
        if prev is not None:
            fila["hist"] = round(float(cv2.compareHist(prev_hist, hist, cv2.HISTCMP_BHATTACHARYYA)), 4)
            fila["pix"] = round(float(np.abs(g.astype(np.int16) - prev.astype(np.int16)).mean()), 3)
            fila["scale"], fila["dx"], fila["dy"], fila["inl"] = 1.0, 0.0, 0.0, 0
            if des is not None and prev_des is not None and len(kp) > 20 and len(prev_kp) > 20:
                m = bf.match(prev_des, des)
                if len(m) >= 12:
                    a = np.float32([prev_kp[x.queryIdx].pt for x in m])
                    b = np.float32([kp[x.trainIdx].pt for x in m])
                    M, inl = cv2.estimateAffinePartial2D(a, b, method=cv2.RANSAC, ransacReprojThreshold=2.0)
                    if M is not None:
                        s = math.hypot(M[0, 0], M[1, 0])
                        fila["scale"] = round(float(s), 5)
                        fila["dx"], fila["dy"] = round(float(M[0, 2]), 2), round(float(M[1, 2]), 2)
                        fila["inl"] = int(inl.sum())
        filas.append(fila)
        prev, prev_hist, prev_kp, prev_des = g, hist, kp, des
    return filas


def detectar_cortes(filas, fps):
    h = np.array([f.get("hist", 0) for f in filas])
    p = np.array([f.get("pix", 0) for f in filas])
    # umbral adaptativo: mediana + k*MAD
    def thr(x, k):
        med = np.median(x); mad = np.median(np.abs(x - med)) + 1e-6
        return med + k * 1.4826 * mad
    th, tp = max(thr(h, 8), 0.25), max(thr(p, 8), 12)
    cortes = []
    for f in filas[1:]:
        if f["hist"] > th or f["pix"] > tp:
            if cortes and f["i"] - cortes[-1]["i"] <= 2:
                if f["hist"] > cortes[-1]["hist"]:
                    cortes[-1] = {"i": f["i"], "t": f["t"], "hist": f["hist"], "pix": f["pix"]}
                continue
            cortes.append({"i": f["i"], "t": f["t"], "hist": f["hist"], "pix": f["pix"]})
    # transiciones graduales: rachas de >=3 frames por encima de la mitad del umbral
    trans, run = [], []
    for f in filas[1:]:
        if f["hist"] > th * 0.35 or f["pix"] > tp * 0.35:
            run.append(f)
        else:
            if len(run) >= 3:
                trans.append({"desde": run[0]["t"], "hasta": run[-1]["t"], "frames": len(run)})
            run = []
    durs = np.diff([0] + [c["t"] for c in cortes] + [filas[-1]["t"]])
    return {"umbral_hist": round(float(th), 4), "umbral_pix": round(float(tp), 3), "cortes": cortes,
            "transiciones": trans,
            "plano_medio_s": round(float(durs.mean()), 3) if len(durs) else None,
            "plano_mediana_s": round(float(np.median(durs)), 3) if len(durs) else None,
            "cortes_por_min": round(len(cortes) / (filas[-1]["t"] / 60), 2) if filas[-1]["t"] else None}


def transcribir(video, out):
    wav = out / "voz16k.wav"
    sh(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-ac", "1", "-ar", "16000", str(wav)])
    base = out / "whisper"
    if not (out / "whisper.json").exists():
        subprocess.run(["whisper-cli", "-m", str(WHISPER_MODEL), "-l", "auto", "-ml", "1", "-sow",
                        "-ojf", "-of", str(base), "-f", str(wav)], check=True, capture_output=True)
    j = json.load(open(out / "whisper.json"))
    palabras = []
    for seg in j.get("transcription", []):
        txt = seg["text"].strip()
        if not txt or txt.startswith("["):
            continue
        a, b = seg["offsets"]["from"] / 1000, seg["offsets"]["to"] / 1000
        palabras.append({"w": txt, "a": round(a, 3), "b": round(b, 3)})
    return {"idioma": j.get("result", {}).get("language"), "palabras": palabras,
            "texto": " ".join(p["w"] for p in palabras)}


def analizar_audio(video, out, cortes):
    import librosa
    wav = out / "audio44k.wav"
    sh(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-ac", "1", "-ar", "44100", str(wav)])
    y, sr = librosa.load(str(wav), sr=44100, mono=True)
    hop = 512
    on_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop)
    onsets = librosa.onset.onset_detect(onset_envelope=on_env, sr=sr, hop_length=hop, units="frames", backtrack=False)
    S = np.abs(librosa.stft(y, n_fft=2048, hop_length=hop))
    freqs = librosa.fft_frequencies(sr=sr, n_fft=2048)
    cent = librosa.feature.spectral_centroid(S=S, sr=sr)[0]
    rms = librosa.feature.rms(S=S)[0]
    bandas = {"sub<120": (0, 120), "voz300-3k": (300, 3000), "aire>6k": (6000, 22050)}
    bE = {k: S[(freqs >= lo) & (freqs < hi)].sum(axis=0) for k, (lo, hi) in bandas.items()}
    tot = sum(bE.values()) + 1e-9
    fuerza_med = float(np.median(on_env[onsets])) if len(onsets) else 0
    ct = [c["t"] for c in cortes]
    ev = []
    for o in onsets:
        t = float(librosa.frames_to_time(o, sr=sr, hop_length=hop))
        st = float(on_env[o])
        if st < fuerza_med * 1.6:
            continue
        w = slice(o, min(o + 20, S.shape[1]))
        ev.append({
            "t": round(t, 3), "fuerza": round(st / (fuerza_med + 1e-9), 2),
            "centroide_hz": int(cent[o]),
            "sub": round(float(bE["sub<120"][w].sum() / tot[w].sum()), 3),
            "aire": round(float(bE["aire>6k"][w].sum() / tot[w].sum()), 3),
            "corte_mas_cercano_s": round(min((t - c for c in ct), key=abs), 3) if ct else None,
        })
    rms_db = librosa.amplitude_to_db(rms + 1e-9)
    paso = int(0.05 * sr / hop) or 1
    curva = [round(float(rms_db[i:i + paso].mean()), 1) for i in range(0, len(rms_db), paso)]
    # música de fondo: energía en tramos sin voz (entre palabras) => nivel de cama
    return {"onsets_fuertes": ev, "rms_db_cada_50ms": curva,
            "lufs_aprox_db": round(float(np.median(rms_db)), 1),
            "pico_db": round(float(rms_db.max()), 1),
            "nota": "fuerza = veces la mediana de onsets; sub alto = golpe/boom, aire alto = whoosh/riser/click"}


def ocr(out, video, meta, ocr_fps):
    d = out / "ocr_frames"
    if not (out / "ocr.jsonl").exists():
        d.mkdir(exist_ok=True)
        sh(["ffmpeg", "-v", "error", "-i", str(video), "-vf", f"fps={ocr_fps},scale=1080:-2", "-q:v", "2",
            str(d / "%06d.jpg")])
        r = subprocess.run([str(HERE / "ocr"), str(d)], check=True, capture_output=True, text=True)
        (out / "ocr.jsonl").write_text(r.stdout)


def colores_caja(img, box):
    """Color de fondo (píldora) y color de texto dentro de una caja normalizada."""
    H, W = img.shape[:2]
    x0, y0 = int(box["x"] * W), int(box["y"] * H)
    x1, y1 = int((box["x"] + box["w"]) * W), int((box["y"] + box["h"]) * H)
    pad = max(4, int(box["h"] * H * 0.35))
    roi = img[max(0, y0 - pad):min(H, y1 + pad), max(0, x0 - pad):min(W, x1 + pad)]
    if roi.size == 0:
        return None
    px = roi.reshape(-1, 3).astype(np.float32)
    k = 3
    _, lab, cen = cv2.kmeans(px, k, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0), 3,
                             cv2.KMEANS_PP_CENTERS)
    cnt = np.bincount(lab.ravel(), minlength=k)
    orden = np.argsort(-cnt)
    hexes = ["#%02X%02X%02X" % tuple(int(c) for c in cen[o][::-1]) for o in orden]
    return {"colores": hexes, "proporcion": [round(float(cnt[o] / cnt.sum()), 3) for o in orden]}


def agrupar_subtitulos(ocr_filas, out, meta, ocr_fps):
    """Agrupa líneas de texto en eventos (mismo texto en frames consecutivos)."""
    ev, eventos = [], {}
    for f in ocr_filas:
        tt = f["_t"]
        for o in f["items"]:
            key = (o["s"].strip().lower(), round(o["y"] * 20))
            e = eventos.get(key)
            if e and tt - e["fin"] <= 1.5 / ocr_fps:
                e["fin"] = tt
                e["n"] += 1
                e["cajas"].append(o)
            else:
                if e:
                    ev.append(e)
                eventos[key] = {"texto": o["s"].strip(), "ini": tt, "fin": tt, "n": 1, "cajas": [o]}
    ev.extend(eventos.values())
    ev.sort(key=lambda e: e["ini"])
    res = []
    for e in ev:
        cx = np.median([c["x"] + c["w"] / 2 for c in e["cajas"]])
        cy = np.median([c["y"] + c["h"] / 2 for c in e["cajas"]])
        h = np.median([c["h"] for c in e["cajas"]])
        w = np.median([c["w"] for c in e["cajas"]])
        res.append({"texto": e["texto"], "ini": e["ini"], "fin": round(e["fin"] + 1 / ocr_fps, 3),
                    "dur": round(e["fin"] + 1 / ocr_fps - e["ini"], 3), "frames_ocr": e["n"],
                    "centro_x": round(float(cx), 4), "centro_y": round(float(cy), 4),
                    "alto_px": round(float(h * meta["h"]), 1), "ancho_px": round(float(w * meta["w"]), 1),
                    "alto_px_1920": round(float(h * 1920), 1), "ancho_px_1080": round(float(w * 1080), 1),
                    "palabras": len(e["texto"].split()),
                    "caja_media": {"x": float(cx - w / 2), "y": float(cy - h / 2), "w": float(w), "h": float(h)}})
    return res


def layout(out, meta, cortes, video):
    """Por plano: fotograma central a resolución completa, rectángulos grandes y fondo."""
    full = out / "full"; full.mkdir(exist_ok=True)
    ts = [0] + [c["t"] for c in cortes] + [meta["dur"]]
    planos = []
    for i in range(len(ts) - 1):
        a, b = ts[i], ts[i + 1]
        mid = (a + b) / 2
        f = full / f"plano_{i:03d}_{mid:07.3f}.png"
        if not f.exists():
            sh(["ffmpeg", "-v", "error", "-y", "-ss", f"{mid:.3f}", "-i", str(video), "-frames:v", "1", str(f)])
        img = cv2.imread(str(f))
        if img is None:
            continue
        H, W = img.shape[:2]
        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ed = cv2.Canny(g, 30, 90)
        ed = cv2.dilate(ed, np.ones((3, 3), np.uint8))
        cnts, _ = cv2.findContours(ed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        rects = []
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            if w > W * 0.5 and h > H * 0.12 and w * h < W * H * 0.95:
                fill = cv2.contourArea(c) / (w * h + 1e-9)
                rects.append({"x": x, "y": y, "w": w, "h": h, "relleno": round(float(fill), 2)})
        rects = sorted(rects, key=lambda r: -r["w"] * r["h"])
        dedup = []
        for r in rects:
            if all(abs(r["x"] - d["x"]) > 12 or abs(r["y"] - d["y"]) > 12 or abs(r["h"] - d["h"]) > 12 for d in dedup):
                dedup.append(r)
        borde = np.concatenate([img[:8].reshape(-1, 3), img[-8:].reshape(-1, 3), img[:, :8].reshape(-1, 3), img[:, -8:].reshape(-1, 3)])
        arriba = img[:6].reshape(-1, 3).mean(0); abajo = img[-6:].reshape(-1, 3).mean(0)
        planos.append({"plano": i, "ini": round(a, 3), "fin": round(b, 3), "dur": round(b - a, 3), "frame": f.name,
                       "rects_grandes": dedup[:6],
                       "fondo_borde_hex": "#%02X%02X%02X" % tuple(int(v) for v in np.median(borde, 0)[::-1]),
                       "fondo_arriba_hex": "#%02X%02X%02X" % tuple(int(v) for v in arriba[::-1]),
                       "fondo_abajo_hex": "#%02X%02X%02X" % tuple(int(v) for v in abajo[::-1])})
    return planos


def hojas(out, video, meta, cortes):
    d = out / "hojas"; d.mkdir(exist_ok=True)
    cols = 8
    n = int(math.ceil(meta["dur"]))
    filas = int(math.ceil(n / cols))
    sh(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vf",
        f"fps=1,scale=200:-2,drawtext=text='%{{pts\\:hms}}':x=4:y=4:fontsize=16:fontcolor=yellow:box=1:boxcolor=black@0.6,tile={cols}x{filas}",
        "-frames:v", "1", str(d / "1_por_segundo.jpg")])
    # alrededor de cada corte: 3 antes, 3 después
    for k, c in enumerate(cortes[:60]):
        s = max(0, c["t"] - 3 / meta["fps"])
        sh(["ffmpeg", "-v", "error", "-y", "-ss", f"{s:.3f}", "-i", str(video), "-vf",
            "scale=180:-2,tile=6x1", "-frames:v", "1", str(d / f"corte_{k:03d}_{c['t']:07.3f}.jpg")])


def main():
    video = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2]).resolve(); out.mkdir(parents=True, exist_ok=True)
    ocr_fps = 10
    if "--ocr-fps" in sys.argv:
        ocr_fps = float(sys.argv[sys.argv.index("--ocr-fps") + 1])
    meta = probe(video); meta["video"] = str(video)
    json.dump(meta, open(out / "meta.json", "w"), indent=1)
    print("meta", meta, flush=True)

    frames = extraer_frames(video, out, meta["fps"])
    print("frames", len(frames), flush=True)
    filas = medir_frames(frames, meta["fps"])
    json.dump(filas, open(out / "movimiento.json", "w"))
    cort = detectar_cortes(filas, meta["fps"])
    json.dump(cort, open(out / "cortes.json", "w"), indent=1)
    print("cortes", len(cort["cortes"]), "plano medio", cort["plano_medio_s"], flush=True)

    pal = transcribir(video, out)
    json.dump(pal, open(out / "palabras.json", "w"), indent=1, ensure_ascii=False)
    print("palabras", len(pal["palabras"]), flush=True)

    aud = analizar_audio(video, out, cort["cortes"])
    json.dump(aud, open(out / "audio.json", "w"), indent=1)
    print("onsets fuertes", len(aud["onsets_fuertes"]), flush=True)

    ocr(out, video, meta, ocr_fps)
    norm = []
    for l in (out / "ocr.jsonl").read_text().splitlines():
        if not l.strip():
            continue
        j = json.loads(l)
        norm.append({"_t": round((int(j["f"].split(".")[0]) - 1) / ocr_fps, 3),
                     "items": [x for x in j["t"] if x["c"] >= 0.3 and x["s"].strip()]})
    subs = agrupar_subtitulos(norm, out, meta, ocr_fps)
    # colores de cada evento en el fotograma OCR del medio
    od = out / "ocr_frames"
    for s in subs:
        idx = int(round((s["ini"] + s["dur"] / 2) * ocr_fps)) + 1
        f = od / f"{idx:06d}.jpg"
        img = cv2.imread(str(f)) if f.exists() else None
        if img is not None:
            s["color"] = colores_caja(img, s["caja_media"])
    # sincronía con la voz: primera palabra hablada que coincide
    ws = pal["palabras"]
    import unicodedata, re
    def norm_w(x):
        x = unicodedata.normalize("NFKD", x.lower()); x = "".join(c for c in x if not unicodedata.combining(c))
        return re.sub(r"[^a-z0-9ñ]", "", x)
    for s in subs:
        first = norm_w(s["texto"].split()[0]) if s["texto"].split() else ""
        cands = [w for w in ws if norm_w(w["w"]) == first and abs(w["a"] - s["ini"]) < 1.5]
        if cands:
            w = min(cands, key=lambda w: abs(w["a"] - s["ini"]))
            s["desfase_vs_voz_s"] = round(s["ini"] - w["a"], 3)
    json.dump(subs, open(out / "subtitulos.json", "w"), indent=1, ensure_ascii=False)
    print("eventos de texto", len(subs), flush=True)

    lay = layout(out, meta, cort["cortes"], video)
    json.dump(lay, open(out / "layout.json", "w"), indent=1)
    hojas(out, video, meta, cort["cortes"])
    print("listo", out, flush=True)


if __name__ == "__main__":
    main()
