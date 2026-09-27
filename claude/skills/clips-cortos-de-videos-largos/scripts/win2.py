#!/usr/bin/env python3
"""Texto con tiempos de una ventana: win2.py v1 140 210"""
import json, sys
v = sys.argv[1]; a = float(sys.argv[2]); b = float(sys.argv[3])
tr = json.load(open(f'transcripts/{v}.json'))['transcription']
for s in tr:
    x = s['offsets']['from'] / 1000; y = s['offsets']['to'] / 1000
    if y >= a and x <= b: print(f"{x:8.2f} {y:8.2f} {s['text'].strip()[:100]}")
