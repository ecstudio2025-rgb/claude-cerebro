#!/usr/bin/env python3
"""Ajusta los bordes al silencio mas cercano y estima cuanto dura el clip ya
montado (el render quita los silencios de mas de 0.7s). Imprime como entra y
como sale cada clip para revisar gancho y cierre antes de renderizar.
Reescribe el spec con los bordes ya ajustados.
Uso: prep.py <spec.json> [minimo_segundos]
"""
import json, sys

spec = json.load(open(sys.argv[1]))
MIN = float(sys.argv[2]) if len(sys.argv) > 2 else 47.0
sil = json.load(open(spec['sil']))
tr = json.load(open(spec['tr']))['transcription']
W = 3.5; SILMIN = 0.7; PAD = 0.12


def snap_start(t):
    for s0, s1 in sil:
        if s0 - 0.05 <= t <= s1 + 0.05: return round(s1 - 0.10, 2)
    best = None
    for s0, s1 in sil:
        if s1 <= t and t - s1 <= W and (best is None or s1 > best): best = s1
    return round(best - 0.10, 2) if best else round(t, 2)


def snap_end(t):
    for s0, s1 in sil:
        if s0 - 0.05 <= t <= s1 + 0.05: return round(s0 + 0.15, 2)
    best = None
    for s0, s1 in sil:
        if s0 >= t and s0 - t <= W and (best is None or s0 < best): best = s0
    return round(best + 0.15, 2) if best else round(t, 2)


def neto(a, b):
    """segundos que quedan tras quitar los silencios largos"""
    fuera = 0.0
    for s0, s1 in sil:
        if s1 - s0 < SILMIN: continue
        c0 = max(s0 + PAD, a); c1 = min(s1 - PAD, b)
        if c1 > c0: fuera += c1 - c0
    return (b - a) - fuera


cortos = []
for c in spec['clips']:
    nr = [[snap_start(a), snap_end(b)] for a, b in c['ranges']]
    c['ranges'] = nr
    n = sum(neto(a, b) for a, b in nr)
    def dentro(s):
        x = s['offsets']['from'] / 1000; y = s['offsets']['to'] / 1000
        for a, b in nr:
            if min(y, b) - max(x, a) > 0.6 * (y - x): return True
        return False
    txt = ' '.join(s['text'].strip() for s in tr if dentro(s))
    flag = '  <<< CORTO' if n < MIN else ''
    if n < MIN: cortos.append(c['id'])
    print(f"--- {c['id']} {nr} bruto {sum(b-a for a,b in nr):.1f}s | neto ~{n:.1f}s{flag}")
    print(f"  ▶ {txt[:135]}")
    print(f"  ⏹ …{txt[-135:]}")
json.dump(spec, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
print(f"\ncortos: {cortos or 'ninguno'}")
