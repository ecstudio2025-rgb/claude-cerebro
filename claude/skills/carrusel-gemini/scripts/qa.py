"""Revisión visual de los slides ya montados, con Gemini como segundo par de ojos.

Busca lo que el renderizador no puede saber solo: texto colado dentro del arte
generado, contraste insuficiente, arte que contradice el copy, caras raras.

Uso:
    python3 qa.py ./salida
    python3 qa.py ./salida --json
"""

import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import gemini  # noqa: E402

PROMPT = """Eres un director de arte revisando los slides de un carrusel de Instagram
antes de publicarlo. Te paso las imágenes en orden.

Para CADA slide, revisa:
1. legible: ¿se lee todo el texto sin esfuerzo a tamaño móvil? ¿hay contraste
   suficiente entre el texto y lo que tiene detrás?
2. texto_cortado: ¿alguna palabra sale del lienzo, se solapa con otro elemento
   o se pisa con una imagen?
3. texto_en_arte: ¿aparece alguna letra, palabra, número o logo DENTRO de la
   fotografía o ilustración? (debería ser cero: el arte va sin tipografía)
4. arte_coherente: ¿la imagen acompaña a lo que dice el texto o lo contradice?
5. respiracion: ¿hay huecos muertos enormes o elementos apelotonados?

Sé duro y concreto. No elogies. Si algo está bien, dilo en una palabra.

Devuelve SOLO este JSON:
{"slides":[{"n":1,"legible":true,"texto_cortado":false,"texto_en_arte":false,
"arte_coherente":true,"respiracion":"ok","problemas":["..."],"veredicto":"ok|revisar|rehacer"}],
"peor_slide":1,"resumen":"una frase"}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("--json", action="store_true", help="volcar el JSON crudo")
    args = ap.parse_args()

    carpeta = pathlib.Path(args.carpeta)
    slides = sorted(carpeta.glob("slide_*.png"))
    if not slides:
        sys.exit(f"No hay slide_*.png en {carpeta}")
    if len(slides) > 10:
        print(f"Aviso: {len(slides)} slides; Instagram admite 10 como máximo.")

    r = gemini.texto(PROMPT, modelo=gemini.MODELO_VISION, json_estricto=True,
                     imagenes=[str(p) for p in slides])

    if args.json:
        print(json.dumps(r, indent=2, ensure_ascii=False))
        return

    for s in r.get("slides", []):
        marcas = []
        if not s.get("legible"):
            marcas.append("ilegible")
        if s.get("texto_cortado"):
            marcas.append("texto cortado")
        if s.get("texto_en_arte"):
            marcas.append("LETRAS EN EL ARTE")
        if not s.get("arte_coherente"):
            marcas.append("arte incoherente")
        estado = s.get("veredicto", "?")
        print(f"slide {s.get('n'):>2} [{estado}] {', '.join(marcas) or '—'}")
        for p in s.get("problemas", []):
            print(f"          · {p}")
    print(f"\n{r.get('resumen', '')}")
    malos = [s["n"] for s in r.get("slides", [])
             if s.get("veredicto") in ("revisar", "rehacer")]
    if malos:
        print("Rehacer con: " + " ".join(
            f"build.py carrusel.json --out {carpeta} --slide {n}" for n in malos))


if __name__ == "__main__":
    main()
