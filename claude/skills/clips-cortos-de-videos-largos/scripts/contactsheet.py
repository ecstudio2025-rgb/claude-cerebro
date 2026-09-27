#!/usr/bin/env python3
"""Hoja de contactos con un frame por clip candidato, para decidir el montaje
(dual / slide / cara) sin abrir el vídeo 28 veces.
Uso: contactsheet.py <video.mp4> 174 312 405 ...   (segundos)
Deja /tmp/cs/sheet.jpg — ábrelo con la herramienta Read.
"""
import os, shutil, subprocess, sys

def _bin(env, *cands):
    """Ruta de un binario: variable de entorno > PATH > rutas tipicas."""
    if os.environ.get(env): return os.environ[env]
    for c in cands:
        p = shutil.which(c) if "/" not in c else (c if os.path.exists(c) else None)
        if p: return p
    return cands[-1]

FF = _bin("FFMPEG", "/usr/local/bin/ffmpeg", "/opt/homebrew/bin/ffmpeg", "ffmpeg")
vid = sys.argv[1]; ts = [float(x) for x in sys.argv[2:]]
os.makedirs('/tmp/cs', exist_ok=True)
for f in os.listdir('/tmp/cs'): os.remove('/tmp/cs/' + f)
for i, t in enumerate(ts, 1):
    subprocess.run([FF, "-y", "-v", "error", "-ss", str(t), "-i", vid, "-frames:v", "1",
                    "-vf", f"scale=427:240,drawtext=text='{i}':fontsize=40:fontcolor=yellow:"
                           "box=1:boxcolor=black:x=5:y=5", f"/tmp/cs/{i:02d}.jpg"], check=True)
cols = 4
subprocess.run([FF, "-y", "-v", "error", "-pattern_type", "glob", "-i", "/tmp/cs/*.jpg",
                "-filter_complex", f"tile={cols}x{(len(ts)+cols-1)//cols}",
                "-frames:v", "1", "/tmp/cs/sheet.jpg"], check=True)
print("/tmp/cs/sheet.jpg")
