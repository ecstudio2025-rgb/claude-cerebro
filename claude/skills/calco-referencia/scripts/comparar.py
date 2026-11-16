#!/usr/bin/env python3
"""Compara un render nuestro con la referencia, con las mismas medidas.

Uso: python3 comparar.py <dir_analisis_referencia> <render.mp4> <dir_salida>

Analiza el render con analizar.py (si no está analizado ya) y saca:
  comparacion.json  tabla medida a medida (referencia, render, diferencia, ok)
  lado_a_lado/      pares de fotogramas (ref | render) en momentos equivalentes por fracción de duración
"""
import json, subprocess, sys
from pathlib import Path
import numpy as np
import cv2

HERE = Path(__file__).resolve().parent


def hex2lab(h):
    rgb = np.uint8([[[int(h[5:7], 16), int(h[3:5], 16), int(h[1:3], 16)]]])  # BGR
    return cv2.cvtColor(rgb, cv2.COLOR_BGR2LAB)[0, 0].astype(float) * [100 / 255, 1, 1] - [0, 128, 128]


def delta_e(a, b):
    return float(np.linalg.norm(hex2lab(a) - hex2lab(b)))


def subs_principales(d):
    s = json.load(open(d / "subtitulos.json"))
    # subtítulo = texto que coincide con una palabra hablada (el texto del b-roll no suele coincidir)
    s = [e for e in s if e["frames_ocr"] >= 2 and e.get("color") and "desfase_vs_voz_s" in e]
    if not s:
        return [], None
    ys = np.array([round(e["centro_y"], 2) for e in s])
    vals, cnt = np.unique(ys, return_counts=True)
    moda = vals[cnt.argmax()]
    franja = [e for e in s if abs(e["centro_y"] - moda) < 0.1]
    return franja, float(moda)


def resumen(d):
    meta = json.load(open(d / "meta.json"))
    cortes = json.load(open(d / "cortes.json"))
    subs, moda = subs_principales(d)
    r = {"duracion_s": meta["dur"], "cortes_por_min": cortes["cortes_por_min"],
         "plano_mediana_s": cortes["plano_mediana_s"], "subs_centro_y": moda}
    if subs:
        r["subs_alto_px_1920"] = float(np.median([e.get("alto_px_1920", e["alto_px"] * 1920 / meta["h"]) for e in subs]))
        r["subs_dur_mediana_s"] = float(np.median([e["dur"] for e in subs]))
        r["subs_palabras_mediana"] = float(np.median([e["palabras"] for e in subs]))
        r["subs_color_fondo"] = max((e["color"]["colores"][0] for e in subs), key=[e["color"]["colores"][0] for e in subs].count)
        des = [e["desfase_vs_voz_s"] for e in subs if "desfase_vs_voz_s" in e]
        r["subs_desfase_voz_mediana_s"] = float(np.median(des)) if des else None
    return r


def main():
    ref, render, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    out.mkdir(parents=True, exist_ok=True)
    rd = out / "analisis_render"
    if not (rd / "layout.json").exists():
        subprocess.run([sys.executable, str(HERE / "analizar.py"), str(render), str(rd)], check=True)
    a, b = resumen(ref), resumen(rd)
    tabla = []
    for k in a:
        va, vb = a.get(k), b.get(k)
        fila = {"medida": k, "referencia": va, "render": vb}
        if isinstance(va, (int, float)) and isinstance(vb, (int, float)) and va:
            fila["dif_pct"] = round(100 * (vb - va) / abs(va), 1)
            fila["ok"] = abs(fila["dif_pct"]) <= 5 or k == "duracion_s"
        elif isinstance(va, str) and isinstance(vb, str) and va.startswith("#"):
            fila["delta_e"] = round(delta_e(va, vb), 1)
            fila["ok"] = fila["delta_e"] <= 8
        tabla.append(fila)
    json.dump(tabla, open(out / "comparacion.json", "w"), indent=1, ensure_ascii=False)
    # lado a lado en 8 puntos de la duración
    la = out / "lado_a_lado"; la.mkdir(exist_ok=True)
    ma, mb = json.load(open(ref / "meta.json")), json.load(open(rd / "meta.json"))
    for k, frac in enumerate([0.02, 0.1, 0.25, 0.4, 0.55, 0.7, 0.85, 0.97]):
        imgs = []
        for m in (ma, mb):
            t = frac * m["dur"]
            p = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", m["video"], "-frames:v", "1",
                                "-vf", "scale=540:960", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
            imgs.append(cv2.imdecode(np.frombuffer(p.stdout, np.uint8), cv2.IMREAD_COLOR))
        if all(i is not None for i in imgs):
            cv2.imwrite(str(la / f"{k}_{int(frac*100):02d}pct.jpg"), np.hstack(imgs))
    for f in tabla:
        print(f)


if __name__ == "__main__":
    main()
