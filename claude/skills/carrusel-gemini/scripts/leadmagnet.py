"""Genera el lead magnet que promete el carrusel: PDF A4 brandeado.

El carrusel pide una keyword y promete un recurso. Este script fabrica ese
recurso para que la promesa se cumpla el mismo día, no "cuando lo prepare".

Uso:
    python3 leadmagnet.py leadmagnet.json --out ./salida/plantilla.pdf
    python3 leadmagnet.py leadmagnet.json --out ./salida/plantilla.pdf --portada-art

Con --portada-art llama a Gemini para la imagen de portada (sin texto: el título
lo pone reportlab con la fuente real).
"""

import argparse
import json
import pathlib
import sys

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

sys.path.insert(0, str(pathlib.Path(__file__).parent))

FUENTES = pathlib.Path.home() / "Library" / "Fonts"
W, H = A4
M = 56


def registrar_fuentes():
    for nombre, fichero in [("Mont-Black", "Montserrat-Black.ttf"),
                            ("Mont-Bold", "Montserrat-Bold.ttf"),
                            ("Mont-Semi", "Montserrat-SemiBold.ttf"),
                            ("Mont", "Montserrat-Medium.ttf")]:
        pdfmetrics.registerFont(TTFont(nombre, str(FUENTES / fichero)))


def envolver(c, texto, fuente, size, ancho):
    c.setFont(fuente, size)
    lineas = []
    for parrafo in texto.split("\n"):
        palabras = parrafo.split()
        if not palabras:
            lineas.append("")
            continue
        actual = palabras[0]
        for p in palabras[1:]:
            if c.stringWidth(actual + " " + p, fuente, size) <= ancho:
                actual += " " + p
            else:
                lineas.append(actual)
                actual = p
        lineas.append(actual)
    return lineas


def bloque(c, texto, fuente, size, x, y, ancho, interlineado=1.5, color="#2c2c2c"):
    c.setFillColor(HexColor(color))
    c.setFont(fuente, size)
    for ln in envolver(c, texto, fuente, size, ancho):
        c.drawString(x, y, ln)
        y -= size * interlineado
    return y


def titulo_ajustado(c, texto, x, y, ancho, size=34, minimo=18):
    while size > minimo:
        lineas = envolver(c, texto, "Mont-Black", size, ancho)
        if len(lineas) <= 3:
            break
        size -= 2
    c.setFont("Mont-Black", size)
    for ln in envolver(c, texto, "Mont-Black", size, ancho):
        c.drawString(x, y, ln)
        y -= size * 1.12
    return y


def pie_pagina(c, marca, n):
    c.setFont("Mont", 8)
    c.setFillColor(HexColor("#9a9a9a"))
    c.drawString(M, 30, marca.get("handle", ""))
    c.drawRightString(W - M, 30, str(n))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("--out", default="./leadmagnet.pdf")
    ap.add_argument("--portada-art", action="store_true",
                    help="genera la imagen de portada con Gemini")
    args = ap.parse_args()

    datos = json.loads(pathlib.Path(args.json).read_text())
    marca = datos.get("marca", {})
    rojo = marca.get("rojo", "#b03035")
    negro = marca.get("negro", "#111111")

    registrar_fuentes()
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(out), pagesize=A4)

    # --- Portada ---
    arte = None
    if args.portada_art and datos.get("portada_art"):
        import gemini
        destino = out.parent / "arte" / "leadmagnet_portada.png"
        try:
            arte = gemini.generar_arte(datos["portada_art"], destino,
                                       aspect="1:1")
        except gemini.GeminiError as e:
            print(f"portada sin arte ({e})")

    if arte:
        # Recorte previo a la proporción de la banda: si dejo que reportlab
        # ajuste el 1:1 dentro de la caja, deja franjas blancas a los lados.
        from PIL import Image as PILImage
        banda_w, banda_h = int(W * 2), int(H * 0.48 * 2)
        foto = PILImage.open(arte).convert("RGB")
        escala = max(banda_w / foto.width, banda_h / foto.height)
        foto = foto.resize((int(foto.width * escala) + 1,
                            int(foto.height * escala) + 1), PILImage.LANCZOS)
        ix = (foto.width - banda_w) // 2
        iy = (foto.height - banda_h) // 2
        recorte = out.parent / "arte" / "leadmagnet_banda.png"
        foto.crop((ix, iy, ix + banda_w, iy + banda_h)).save(recorte)
        c.drawImage(ImageReader(str(recorte)), 0, H * 0.52, width=W,
                    height=H * 0.48, mask="auto")
    c.setFillColor(HexColor(rojo))
    c.rect(M, H * 0.44, 46, 6, stroke=0, fill=1)
    c.setFillColor(HexColor(negro))
    y = titulo_ajustado(c, datos["titulo"].upper(), M, H * 0.38, W - M * 2, 36)
    if datos.get("subtitulo"):
        bloque(c, datos["subtitulo"], "Mont", 13, M, y - 14, W - M * 2 - 60,
               color="#5a5a5a")
    c.setFillColor(HexColor("#9a9a9a"))
    c.setFont("Mont-Semi", 10)
    c.drawString(M, 70, marca.get("nombre", "").upper())
    c.drawString(M, 54, marca.get("handle", ""))
    c.showPage()

    # --- Intro ---
    pagina = 2
    y = H - M - 20
    if datos.get("intro"):
        c.setFillColor(HexColor(rojo))
        c.setFont("Mont-Bold", 10)
        c.drawString(M, y, "ANTES DE EMPEZAR")
        y -= 30
        c.setFillColor(HexColor(negro))
        y = bloque(c, datos["intro"], "Mont", 12, M, y, W - M * 2, 1.6,
                   "#2c2c2c")
        y -= 26

    # --- Secciones ---
    for i, s in enumerate(datos.get("secciones", []), 1):
        alto_estimado = 90 + len(s.get("cuerpo", "")) * 0.32 + \
            len(s.get("checklist", [])) * 22
        if y - alto_estimado < 90:
            pie_pagina(c, marca, pagina)
            c.showPage()
            pagina += 1
            y = H - M - 20

        c.setFillColor(HexColor(rojo))
        c.setFont("Mont-Black", 26)
        c.drawString(M, y, f"{i:02d}")
        c.setFillColor(HexColor(negro))
        y = titulo_ajustado(c, s["titulo"].upper(), M + 46, y + 4,
                            W - M * 2 - 46, 17)
        y -= 8
        if s.get("cuerpo"):
            y = bloque(c, s["cuerpo"], "Mont", 11.5, M + 46, y, W - M * 2 - 46,
                       1.55)
        for item in s.get("checklist", []):
            y -= 6
            c.setFillColor(HexColor("#ffffff"))
            c.setStrokeColor(HexColor(rojo))
            c.setLineWidth(1.2)
            c.rect(M + 46, y - 2, 10, 10, stroke=1, fill=0)
            bloque(c, item, "Mont", 11, M + 66, y, W - M * 2 - 66, 1.4)
            y -= 18
        y -= 26

    # --- Cierre / acción de venta ---
    cierre = datos.get("cierre")
    if cierre:
        # Alto calculado, no fijo: con un alto de 190 el botón se comía la
        # última línea del cuerpo en cuanto el texto crecía una línea.
        ancho_txt = W - M * 2 - 56
        n_tit = len(envolver(c, cierre["titulo"].upper(), "Mont-Black", 18,
                             ancho_txt))
        n_cue = len(envolver(c, cierre.get("cuerpo", ""), "Mont", 10.5,
                             ancho_txt)) if cierre.get("cuerpo") else 0
        alto = 42 + 26 + n_tit * 22 + 8 + n_cue * 16 + \
            (52 if cierre.get("cta") else 0) + 30
        if y - alto < 70:
            pie_pagina(c, marca, pagina)
            c.showPage()
            pagina += 1
            y = H - M - 20
        c.setFillColor(HexColor("#111111"))
        c.rect(M, y - alto, W - M * 2, alto, stroke=0, fill=1)
        yc = y - 42
        c.setFillColor(HexColor("#ff5a5f" if rojo == "#b03035" else rojo))
        c.setFont("Mont-Bold", 9)
        c.drawString(M + 28, yc, (cierre.get("label") or "SIGUIENTE PASO").upper())
        yc -= 26
        c.setFillColor(HexColor("#ffffff"))
        c.setFont("Mont-Black", 18)
        for ln in envolver(c, cierre["titulo"].upper(), "Mont-Black", 18,
                           W - M * 2 - 56):
            c.drawString(M + 28, yc, ln)
            yc -= 22
        yc -= 8
        if cierre.get("cuerpo"):
            yc = bloque(c, cierre["cuerpo"], "Mont", 10.5, M + 28, yc,
                        ancho_txt, 1.5, "#cfcbc7")
        if cierre.get("cta"):
            yc -= 18
            c.setFillColor(HexColor(rojo))
            ancho_cta = c.stringWidth(cierre["cta"].upper(), "Mont-Bold", 11) + 40
            c.roundRect(M + 28, yc - 12, ancho_cta, 30, 15, stroke=0, fill=1)
            c.setFillColor(HexColor("#ffffff"))
            c.setFont("Mont-Bold", 11)
            c.drawString(M + 48, yc - 3, cierre["cta"].upper())

    pie_pagina(c, marca, pagina)
    c.save()
    print(f"lead magnet -> {out.resolve()} ({pagina} páginas)")


if __name__ == "__main__":
    main()
