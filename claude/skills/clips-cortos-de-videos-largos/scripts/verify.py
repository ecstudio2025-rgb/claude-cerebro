#!/usr/bin/env python3
"""Transcribe cada clip ya renderizado y enseña como empieza y como acaba,
para comprobar que ninguno arranca ni termina a media palabra."""
import json, subprocess, os, glob

import os, shutil

def _bin(env, *cands):
    """Ruta de un binario: variable de entorno > PATH > rutas tipicas."""
    if os.environ.get(env): return os.environ[env]
    for c in cands:
        p = shutil.which(c) if "/" not in c else (c if os.path.exists(c) else None)
        if p: return p
    return cands[-1]

WC    = _bin("WHISPER_CLI", "/opt/homebrew/bin/whisper-cli", "whisper-cli")
MODEL = os.environ.get("WHISPER_MODEL") or next(
    (m for m in [
        os.path.expanduser("~/Claude/projects/content-panel/scripts/video-pipeline/models/ggml-small.bin"),
        os.path.expanduser("~/models/ggml-small.bin"),
        "/opt/homebrew/share/whisper.cpp/models/ggml-small.bin",
    ] if os.path.exists(m)), "")
if not MODEL:
    raise SystemExit("no encuentro el modelo de whisper: exporta WHISPER_MODEL=/ruta/ggml-small.bin")
FF    = _bin("FFMPEG", "/usr/local/bin/ffmpeg", "/opt/homebrew/bin/ffmpeg", "ffmpeg")
FPR   = _bin("FFPROBE", "/opt/homebrew/bin/ffprobe", "ffprobe")
for f in sorted(glob.glob('clips/*.mp4')):
    cid = os.path.basename(f)[:-4]
    w = f"/tmp/v_{cid}.wav"
    subprocess.run([FF, "-y", "-v", "error", "-i", f, "-vn", "-ac", "1", "-ar", "16000", w], check=True)
    subprocess.run([WC, "-m", MODEL, "-f", w, "-l", "es", "-oj", "-of", f"/tmp/v_{cid}"],
                   check=True, capture_output=True)
    d = json.load(open(f"/tmp/v_{cid}.json"))['transcription']
    txt = ' '.join(s['text'].strip() for s in d)
    dur = subprocess.run([FPR, "-v", "error", "-show_entries",
                          "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout.strip()
    print(f"\n{cid}  {float(dur):.1f}s")
    print(f"  ▶ {txt[:90]}")
    print(f"  ⏹ …{txt[-90:]}")
    os.remove(w); os.remove(f"/tmp/v_{cid}.json")
