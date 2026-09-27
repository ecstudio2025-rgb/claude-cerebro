#!/usr/bin/env python3
"""Clips 9:16 con hook quemado a partir de una grabacion larga.
Una pasada por clip: input-seek -> layout -> corta rangos + quita silencios ->
lienzo 1080x1920 -> hook (tag + regla + titular) + handle.
Layouts: cara | slide | dual.
Uso: render.py <spec.json>
"""
import json, os, shutil, subprocess, tempfile, sys

def _bin(env, *cands):
    """Ruta de un binario: variable de entorno > PATH > rutas tipicas."""
    if os.environ.get(env): return os.environ[env]
    for c in cands:
        p = shutil.which(c) if "/" not in c else (c if os.path.exists(c) else None)
        if p: return p
    return cands[-1]

# ffmpeg tiene que traer drawtext (el de Homebrew lo trae)
FF  = _bin("FFMPEG", "/usr/local/bin/ffmpeg", "/opt/homebrew/bin/ffmpeg", "ffmpeg")
FPR = _bin("FFPROBE", "/opt/homebrew/bin/ffprobe", "ffprobe")

spec = json.load(open(sys.argv[1]))
SRC = spec["src"]
SIL = json.load(open(spec["sil"])) if spec.get("sil") else []
OUT = spec.get("out", "clips"); os.makedirs(OUT, exist_ok=True)

FONTS = spec.get("fonts_dir", os.path.expanduser("~/Library/Fonts"))
FB    = spec.get("font_black", f"{FONTS}/Montserrat-Black.ttf")
FBOLD = spec.get("font_bold",  f"{FONTS}/Montserrat-Bold.ttf")
FSEMI = spec.get("font_semi",  f"{FONTS}/Montserrat-SemiBold.ttf")
for f in (FB, FBOLD, FSEMI):
    if not os.path.exists(f): sys.exit(f"falta la fuente {f}: instala Montserrat o pon font_black/font_bold/font_semi en el spec")
COLOR = spec.get("color", "0xB03035")          # naranja: 0xFA9600
FS = 58; FS_TAG = 34; MAXC = 20
HANDLE = spec.get("handle", "")
SILMIN = spec.get("silmin", 0.7); PAD = 0.12

# geometria del fuente. Por defecto, grabacion de Zoom 1280x720 con la diapo
# a la izquierda y la webcam en un PIP a la derecha. Comprobar SIEMPRE con un
# frame antes de dar por buenos estos recortes.
CROP_SLIDE = spec.get("crop_slide", "crop=960:540:0:90")
CROP_CARA  = spec.get("crop_cara",  "crop=320:180:960:270")


def wrap(t, m, maxlines=3):
    out = []; cur = ""
    for w in t.split():
        if cur and len(cur) + 1 + len(w) > m: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    if cur: out.append(cur)
    return out[:maxlines]


def desilence(a, b, sils):
    cuts = []
    for s0, s1 in sils:
        if s1 - s0 < SILMIN: continue
        c0 = max(s0 + PAD, a); c1 = min(s1 - PAD, b)
        if c1 - c0 > 0.05 and c0 < b and c1 > a: cuts.append((c0, c1))
    cuts.sort(); segs = []; cur = a
    for c0, c1 in cuts:
        if c0 > cur: segs.append((cur, c0))
        cur = max(cur, c1)
    if cur < b: segs.append((cur, b))
    return [(s, e) for s, e in segs if e - s > 0.25]


tmp = tempfile.mkdtemp(); ok = 0
for c in spec["clips"]:
    cid = c["id"]; ranges = c["ranges"]; layout = c.get("layout", "cara")
    span0 = max(0, min(r[0] for r in ranges) - 0.3)
    span1 = max(r[1] for r in ranges) + 0.3
    dur = span1 - span0
    sil_rel = [(s - span0, e - span0) for s, e in SIL if e > span0 and s < span1]
    finals = []
    for r in ranges:
        finals.extend(desilence(r[0] - span0, r[1] - span0, sil_rel))
    if not finals:
        finals = [(r[0] - span0, r[1] - span0) for r in ranges]
    n = len(finals)

    fc = []
    if layout == "dual":
        fc.append(f"[0:v]{CROP_CARA},scale=1080:-2:flags=lanczos,unsharp=5:5:0.8:5:5:0.0,setsar=1[cara]")
        fc.append(f"[0:v]{CROP_SLIDE},scale=1080:-2:flags=lanczos,setsar=1[slide]")
        fc.append("[cara][slide]vstack=inputs=2,pad=1080:1920:0:380:color=black[base]")
    elif layout == "slide":
        fc.append(f"[0:v]{CROP_SLIDE},scale=1080:-2:flags=lanczos,setsar=1,"
                  "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black[base]")
    else:  # cara
        fc.append(f"[0:v]{CROP_CARA},scale=1080:-2:flags=lanczos,unsharp=5:5:0.8:5:5:0.0,setsar=1,"
                  "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black[base]")

    fc.append("[base]split=" + str(n) + "".join(f"[vb{i}]" for i in range(n)))
    fc.append("[0:a]asplit=" + str(n) + "".join(f"[ab{i}]" for i in range(n)))
    inter = ""
    for i, (s, e) in enumerate(finals):
        fc.append(f"[vb{i}]trim={s:.3f}:{e:.3f},setpts=PTS-STARTPTS[v{i}]")
        fc.append(f"[ab{i}]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS[a{i}]")
        inter += f"[v{i}][a{i}]"
    fc.append(inter + f"concat=n={n}:v=1:a=1[cv][ca0]")
    fc.append("[ca0]highpass=85,loudnorm=I=-16:TP=-1.5:LRA=11[ca]")
    last = "[cv]"

    # bloque de hook, pegado justo encima del video
    top_video = 656 if layout != "dual" else 380
    maxl = 3 if layout != "dual" else 2
    lines = [l.upper() for l in wrap(c["hook"], MAXC, maxl)]
    nl = len(lines); lh = FS + 16
    y_hook = (top_video - 26) - (nl * FS + (nl - 1) * 16)
    y_rule = y_hook - 24; y_tag = y_hook - 64

    tf = os.path.join(tmp, f"{cid}_t.txt")
    open(tf, "w", encoding="utf-8").write(c["tag"].upper())
    fc.append(f"{last}drawtext=fontfile='{FBOLD}':textfile='{tf}':fontcolor={COLOR}:fontsize={FS_TAG}:"
              f"x=(w-text_w)/2:y={y_tag}[bg1]"); last = "[bg1]"
    fc.append(f"{last}drawbox=x=(iw-150)/2:y={y_rule}:w=150:h=5:color={COLOR}:t=fill[bg2]"); last = "[bg2]"
    for i, ln in enumerate(lines):
        lf = os.path.join(tmp, f"{cid}_{i}.txt")
        open(lf, "w", encoding="utf-8").write(ln)
        fc.append(f"{last}drawtext=fontfile='{FB}':textfile='{lf}':fontcolor=white:fontsize={FS}:"
                  f"borderw=2:bordercolor=black@0.5:x=(w-text_w)/2:y={y_hook + i * lh}[hk{i}]")
        last = f"[hk{i}]"
    if HANDLE:
        hf = os.path.join(tmp, f"{cid}_h.txt")
        open(hf, "w", encoding="utf-8").write(HANDLE)
        fc.append(f"{last}drawtext=fontfile='{FSEMI}':textfile='{hf}':fontcolor=0xBBBBBB:fontsize=34:"
                  f"x=(w-text_w)/2:y=1792[v]")
    else:
        fc.append(f"{last}null[v]")

    cmd = [FF, "-y", "-ss", f"{span0:.3f}", "-i", SRC, "-t", f"{dur:.3f}",
           "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[ca]",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", f"{OUT}/{cid}.mp4"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode == 0:
        d = subprocess.run([FPR, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                            f"{OUT}/{cid}.mp4"], capture_output=True, text=True).stdout.strip()
        ok += 1; print(f"OK {cid} [{layout}] {float(d):.0f}s | {' / '.join(lines)}", flush=True)
    else:
        print(f"ERR {cid}: {r.stderr[-400:]}", flush=True)
print(f"\n{ok}/{len(spec['clips'])} renderizados en {OUT}")
