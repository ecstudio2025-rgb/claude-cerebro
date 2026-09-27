"""Consulta el Hook Vault (4.550 ganchos) de guiones-virales-master5.

La base vive en la skill hermana; aquí no se duplica, se lee:
    ../guiones-virales-master5/references/hook-vault/hooks.json

Cada gancho: {id, category_num, category, template, example, psychology, goal}.
Las plantillas están en inglés a propósito (el patrón psicológico es universal);
se adaptan al español al usarlas, nunca se pegan tal cual.

Uso como CLI:
    python3 hooks.py --categorias 01,08 --objetivo "Get Views" -n 10
    python3 hooks.py --buscar mistake -n 5
    python3 hooks.py --categorias                       # lista las 15 categorías
"""

import argparse
import hashlib
import json
import pathlib
import random

VAULT = (pathlib.Path(__file__).resolve().parents[2] / "guiones-virales-master5"
         / "references" / "hook-vault" / "hooks.json")

# Categorías que sirven para una PORTADA de carrusel (paran el scroll en frío).
# Fuera: 11 humor (difícil sin cara), 12 tendencia (caduca), 13 visual (es de
# primer frame de vídeo), transicionales (van a mitad de pieza, no al principio).
PORTADA = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]

# Qué categoría pide cada intención. El deseo primitivo (SSDD) es ortogonal:
# cualquier categoría puede atacar cualquier deseo.
POR_ANGULO = {
    "intriga": ["01", "02"],
    "miedo": ["03", "01"],
    "senalar": ["04", "10"],
    "autoridad": ["05", "09"],
    "deseo": ["06", "07"],
    "contra": ["08", "02"],
    "lista": ["09", "01"],
    "pregunta": ["10", "04"],
}


def cargar():
    if not VAULT.exists():
        raise SystemExit(f"No encuentro el Hook Vault en {VAULT}")
    return json.loads(VAULT.read_text())


def categorias():
    return cargar()["categories"]


def candidatos(categorias_num=None, objetivo=None, buscar=None, n=40,
               semilla=None):
    """Devuelve una muestra variada de ganchos.

    Reparte la muestra entre las categorías pedidas en vez de coger los N
    primeros: si no, salen 40 variantes del mismo patrón y Gemini elige entre
    clones. La semilla hace la selección reproducible para un mismo tema.
    """
    H = cargar()["hooks"]
    cats = [c for c in (categorias_num or PORTADA)]
    pool = [h for h in H if h["category_num"] in cats]
    if objetivo:
        filtrado = [h for h in pool if h["goal"] == objetivo]
        # 'Get Sales' solo tiene 6 ganchos en todo el vault: si el filtro deja
        # la muestra en nada, se ignora en vez de devolver una lista vacía.
        if len(filtrado) >= max(n, 10):
            pool = filtrado
    if buscar:
        t = buscar.lower()
        pool = [h for h in pool
                if t in h["template"].lower() or t in h["example"].lower()]
    if not pool:
        return []

    rnd = random.Random(
        int(hashlib.sha1((semilla or "x").encode()).hexdigest()[:8], 16))
    por_cat = {}
    for h in pool:
        por_cat.setdefault(h["category_num"], []).append(h)
    for v in por_cat.values():
        rnd.shuffle(v)

    salida, i = [], 0
    while len(salida) < n and any(por_cat.values()):
        for c in sorted(por_cat):
            if por_cat[c] and len(salida) < n:
                salida.append(por_cat[c].pop())
        i += 1
        if i > n:
            break
    return salida


def formatear(hs):
    return "\n".join(
        f"[{h['id']}] ({h['category']} · {h['goal']})\n"
        f"  PLANTILLA: {h['template']}\n"
        f"  EJEMPLO:   {h['example']}\n"
        f"  PSICOLOGÍA: {h['psychology']}"
        for h in hs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--categorias", nargs="?", const="", default=None,
                    help="lista '01,08'; sin valor, imprime las 15 categorías")
    ap.add_argument("--objetivo", default=None,
                    help="Get Views | Get Followers | Get Engagement | Get Saves | Get Sales")
    ap.add_argument("--buscar", default=None, help="término en inglés")
    ap.add_argument("-n", type=int, default=10)
    ap.add_argument("--semilla", default=None)
    args = ap.parse_args()

    if args.categorias == "":
        for c in categorias():
            print(f"{c['num']}  {c['emoji']} {c['name']:<32} {c['count']:>4}  "
                  f"{', '.join(c['triggers'][:3])}")
        return

    cats = args.categorias.split(",") if args.categorias else None
    hs = candidatos(cats, args.objetivo, args.buscar, args.n, args.semilla)
    if not hs:
        print("Sin resultados. Prueba otra categoría o quita --buscar.")
        return
    print(formatear(hs))


if __name__ == "__main__":
    main()
