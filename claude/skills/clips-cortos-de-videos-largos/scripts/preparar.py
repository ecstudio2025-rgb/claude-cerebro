#!/usr/bin/env python3
"""Prepara el material de un vídeo largo: silencios, bloques de lectura y frames.
Uso: preparar.py <video.mp4> <id>      (id = v1, v2, pod3...)

Deja:
  audio/sil_<id>.json            silencios [inicio, fin] para cortar y desilenciar
  transcripts/<id>_bloques.txt   texto en bloques de 22s con timestamp, para leer y elegir
La transcripción (transcripts/<id>.json, formato whisper.cpp) tiene que existir ya.
"""
import json, os, re, shutil, subprocess, sys

def _bin(env, *cands):
    """Ruta de un binario: variable de entorno > PATH > rutas tipicas."""
    if os.environ.get(env): return os.environ[env]
    for c in cands:
        p = shutil.which(c) if "/" not in c else (c if os.path.exists(c) else None)
        if p: return p
    return cands[-1]

FF = _bin("FFMPEG", "/usr/local/bin/ffmpeg", "/opt/homebrew/bin/ffmpeg", "ffmpeg")
vid, vid_id = sys.argv[1], sys.argv[2]
os.makedirs('audio', exist_ok=True); os.makedirs('transcripts', exist_ok=True)

raw = subprocess.run([FF, "-v", "info", "-i", vid, "-vn",
                      "-af", "silencedetect=n=-32dB:d=0.35", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', raw)]
en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', raw)]
sil = [[a, b] for a, b in zip(st, en)]
json.dump(sil, open(f'audio/sil_{vid_id}.json', 'w'))
print(f"{len(sil)} silencios -> audio/sil_{vid_id}.json")

tr = f'transcripts/{vid_id}.json'
if os.path.exists(tr):
    d = json.load(open(tr))['transcription']
    out = []; cur = []; t0 = None
    for s in d:
        a = s['offsets']['from'] / 1000; b = s['offsets']['to'] / 1000
        t = s['text'].strip()
        if not t: continue
        if t0 is None: t0 = a
        cur.append(t)
        if b - t0 >= 22:
            out.append(f"[{int(t0//60):02d}:{t0%60:04.1f}|{t0:.1f}] " + " ".join(cur)); cur = []; t0 = None
    if cur: out.append(f"[{int(t0//60):02d}:{t0%60:04.1f}|{t0:.1f}] " + " ".join(cur))
    open(f'transcripts/{vid_id}_bloques.txt', 'w').write("\n".join(out))
    print(f"{len(out)} bloques -> transcripts/{vid_id}_bloques.txt")
    print(f"ÚLTIMO BLOQUE (comprueba que whisper no se ha quedado en bucle):\n{out[-1][:200]}")
else:
    print(f"falta {tr}: transcribe primero con whisper.cpp / faster-whisper")
