"""Orquesta el carrusel: JSON -> arte de Gemini -> slides PNG 1080x1350.

Uso:
    python3 build.py carrusel.json --out ./salida
    python3 build.py carrusel.json --out ./salida --sin-arte     # borrador rápido, gratis
    python3 build.py carrusel.json --out ./salida --rapido       # modelo flash-image
    python3 build.py carrusel.json --out ./salida --slide 3      # rehace solo el slide 3

El arte se cachea por prompt: repetir el build no vuelve a pagar los slides que
no han cambiado. Cambia el prompt de `art` y solo ese se regenera.
"""

import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import gemini  # noqa: E402
import render  # noqa: E402

ESTILO_BASE = (
    "Fotografía y dirección de arte editorial premium, luz natural dura con "
    "sombras marcadas, paleta sobria (blancos rotos, negro, gris cemento) con "
    "un único acento rojo oscuro #b03035. Composición limpia, mucho aire, "
    "sin caras reconocibles mirando a cámara. Estética de revista de negocio, "
    "nada de stock corporativo sonriente, nada de render 3D azul de IA."
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json", help="ruta al carrusel.json")
    ap.add_argument("--out", default="./salida")
    ap.add_argument("--sin-arte", action="store_true",
                    help="no llama a Gemini; slides sobre fondo plano")
    ap.add_argument("--rapido", action="store_true",
                    help="usa gemini-3.1-flash-image (más barato, menos fino)")
    ap.add_argument("--slide", type=int, default=None,
                    help="rehace solo ese número de slide (1-indexado)")
    args = ap.parse_args()

    datos = json.loads(pathlib.Path(args.json).read_text())
    marca = datos.get("marca", {})
    slides = datos["slides"]
    total = len(slides)

    out = pathlib.Path(args.out)
    (out / "arte").mkdir(parents=True, exist_ok=True)

    modelo = gemini.MODELO_IMAGEN_RAPIDO if args.rapido else gemini.MODELO_IMAGEN
    estilo = datos.get("estilo_arte", ESTILO_BASE)

    # Ancla de estilo: SIEMPRE el arte del primer slide que lleva imagen, exista
    # ya o se genere ahora. Si dependiera del orden de ejecución, rehacer un
    # slide suelto con --slide cambiaría su firma y Gemini lo regeneraría
    # distinto, rompiendo la coherencia de la serie.
    primero = next((i for i, s in enumerate(slides, 1) if s.get("art")), None)
    ruta_ancla = out / "arte" / f"arte_{primero:02d}.png" if primero else None
    ancla = ruta_ancla if ruta_ancla and ruta_ancla.exists() else None

    hechos = []
    for i, s in enumerate(slides, 1):
        if args.slide and i != args.slide:
            ruta_prev = out / f"slide_{i:02d}.png"
            if ruta_prev.exists():
                hechos.append(ruta_prev)
            continue

        arte = None
        if s.get("art") and not args.sin_arte:
            destino = out / "arte" / f"arte_{i:02d}.png"
            prompt = f"{s['art']}\n\nEstilo: {estilo}"
            try:
                arte = gemini.generar_arte(
                    prompt, destino, aspect="4:5", modelo=modelo,
                    referencia=None if i == primero else ancla,
                )
                if i == primero:
                    ancla = arte
                print(f"  arte slide {i}: ok")
            except gemini.GeminiError as e:
                print(f"  arte slide {i}: FALLA ({e}) -> sigue sin arte")
                arte = None

        img = render.render_slide(s, marca, arte, i, total)
        ruta = out / f"slide_{i:02d}.png"
        img.save(ruta, "PNG", optimize=True)
        hechos.append(ruta)
        print(f"slide {i:02d}/{total} [{s['layout']}] -> {ruta}")

    print(f"\n{len(hechos)} slides en {out.resolve()}")


if __name__ == "__main__":
    main()
