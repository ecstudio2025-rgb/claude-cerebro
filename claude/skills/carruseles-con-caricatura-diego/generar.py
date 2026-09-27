#!/usr/bin/env python3
"""Generador de carruseles con la caricatura de Diego.

Genera la ESCENA limpia (Gemini) UNA vez y la cachea; el texto se compone
aparte encima. Asi cambiar textos NO regenera imagenes.

Uso:
    python3 generar.py carruseles.json <salida>            # todos
    python3 generar.py carruseles.json <salida> RITMO VENTA # solo esos ids
    python3 generar.py carruseles.json <salida> --solo-texto  # recompone texto
                                                              # desde escenas cache
El JSON: lista de carruseles {id, carpeta, slides:[{texto, roja, escena}]}.
"""
import json, sys, pathlib, time
import compose as C

# --- PRESET DE ESTILO (no tocar salvo rediseño) --------------------------------
ESTILO = ("Ilustracion de caricatura profesional semiplana de la MISMA persona de "
          "la foto de referencia (parecido exacto: cara delgada, pomulos marcados, "
          "pelo oscuro rizado bajo gorra beige lisa sin texto, perilla fina, aros "
          "en las orejas, piercing en la nariz, collar de cuentas, camisa oscura "
          "con ribete rojo). Sombreado suave en dos tonos, contorno limpio, sin "
          "3D, sin anime. ")

HERO = ("ILUSTRACION VERTICAL 4:5. ENCUADRE OBLIGATORIO: el personaje aparece de "
        "PECHO HACIA ARRIBA ocupando la MITAD INFERIOR, con la cabeza claramente "
        "separada del borde superior; el TERCIO SUPERIOR es aire oscuro sin nada "
        "importante. Escena ambientada de NEGOCIO que ilustra la idea en el fondo. "
        "Paleta negro #141414, rojo carmin #b03035, crema y grises. Luz "
        "cinematografica. PROHIBIDO: texto, letras, numeros, carteles escritos, "
        "pantallas con palabras, logotipos. Tampoco camaras, tripodes, microfonos, "
        "focos ni mesas de montaje. ESCENA: ")


def escena(desc):
    return C.gemini(f"{ESTILO}{HERO}{desc}")


def construir(carrusel, salida, solo_texto=False, pausa=1.0):
    d = salida / carrusel["carpeta"]
    cache = d / ".escenas"
    cache.mkdir(parents=True, exist_ok=True)
    print(f"\n=== {carrusel['id']} ({len(carrusel['slides'])} slides) ===", flush=True)
    for i, s in enumerate(carrusel["slides"], 1):
        dest = d / f"slide-{i:02d}.png"
        raw = cache / f"slide-{i:02d}.png"          # escena limpia cacheada
        roja = s.get("roja")
        if not raw.exists():
            if solo_texto:
                print(f"  [{i}] sin escena cache, saltada", flush=True); continue
            png = escena(s["escena"])
            if png is None:
                print(f"  [{i}] FALLO escena", flush=True); continue
            raw.write_bytes(png)
            time.sleep(pausa)
        # compone el texto sobre la escena limpia (siempre; barato)
        C.hero_safe(s["texto"], str(raw), dest, roja=roja, scene_is_path=True)
        print(f"  [{i}] {dest.name}", flush=True)


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    data = json.loads(pathlib.Path(sys.argv[1]).read_text())
    salida = pathlib.Path(sys.argv[2]); salida.mkdir(parents=True, exist_ok=True)
    args = sys.argv[3:]
    solo_texto = "--solo-texto" in args
    filtro = {a for a in args if not a.startswith("--")}
    for car in data:
        if filtro and car["id"] not in filtro: continue
        construir(car, salida, solo_texto=solo_texto)
    print("\nlisto", flush=True)


if __name__ == "__main__":
    main()
