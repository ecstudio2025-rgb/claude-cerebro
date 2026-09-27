"""Compone los slides del carrusel: arte de Gemini + tipografía real (Montserrat).

Gemini pone el arte. El texto NO lo escribe Gemini nunca: lo dibuja PIL con la
fuente real, porque los modelos de imagen cometen erratas en español
(comprobado: "ERFORES" en vez de "ERRORES").

Lienzo: 1080 x 1350 (4:5, el formato con más altura que permite Instagram).
"""

import pathlib

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1350
MARGEN = 84

FUENTES = pathlib.Path.home() / "Library" / "Fonts"
BLACK = str(FUENTES / "Montserrat-Black.ttf")
BOLD = str(FUENTES / "Montserrat-Bold.ttf")
SEMI = str(FUENTES / "Montserrat-SemiBold.ttf")
MEDIUM = str(FUENTES / "Montserrat-Medium.ttf")


def fuente(ruta, size):
    return ImageFont.truetype(ruta, size)


def _ancho(font, texto):
    return font.getbbox(texto)[2] - font.getbbox(texto)[0]


def _alto_linea(font):
    a = font.getbbox("HÁgjq")
    return a[3] - a[1]


def envolver(font, texto, max_ancho):
    """Parte el texto en líneas que caben en max_ancho."""
    lineas = []
    for parrafo in texto.split("\n"):
        palabras = parrafo.split()
        if not palabras:
            lineas.append("")
            continue
        actual = palabras[0]
        for p in palabras[1:]:
            if _ancho(font, actual + " " + p) <= max_ancho:
                actual += " " + p
            else:
                lineas.append(actual)
                actual = p
        lineas.append(actual)
    return lineas


def ajustar(texto, ruta_fuente, max_ancho, max_alto, size_max, size_min=18,
            interlineado=1.06, lineas_fijas=None):
    """Baja el cuerpo hasta que el bloque cabe. Devuelve (font, lineas, alto)."""
    size = size_max
    while size >= size_min:
        f = fuente(ruta_fuente, size)
        lineas = lineas_fijas if lineas_fijas else envolver(f, texto, max_ancho)
        cabe_ancho = all(_ancho(f, ln) <= max_ancho for ln in lineas)
        paso = int(size * interlineado)
        alto = paso * len(lineas)
        if cabe_ancho and alto <= max_alto:
            return f, lineas, alto, paso
        size -= 2
    f = fuente(ruta_fuente, size_min)
    lineas = lineas_fijas if lineas_fijas else envolver(f, texto, max_ancho)
    paso = int(size_min * interlineado)
    return f, lineas, paso * len(lineas), paso


def escribir_bloque(d, lineas, font, x, y, paso, color, acento=None,
                    color_acento=None):
    """Dibuja líneas. Si una línea contiene `acento`, esa parte va en color_acento."""
    for ln in lineas:
        if acento and color_acento and acento in ln:
            antes, _, despues = ln.partition(acento)
            cx = x
            if antes:
                d.text((cx, y), antes, font=font, fill=color)
                cx += _ancho(font, antes)
            d.text((cx, y), acento, font=font, fill=color_acento)
            cx += _ancho(font, acento)
            if despues:
                d.text((cx, y), despues, font=font, fill=color)
        else:
            d.text((x, y), ln, font=font, fill=color)
        y += paso
    return y


def escribir_tracking(d, texto, font, x, y, color, tracking=3):
    for ch in texto:
        d.text((x, y), ch, font=font, fill=color)
        x += _ancho(font, ch) + tracking
    return x


def encajar_arte(ruta, ancho, alto):
    """Recorta el arte al centro para llenar la caja sin deformar."""
    img = Image.open(ruta).convert("RGB")
    escala = max(ancho / img.width, alto / img.height)
    img = img.resize((int(img.width * escala) + 1, int(img.height * escala) + 1),
                     Image.LANCZOS)
    ix = (img.width - ancho) // 2
    iy = (img.height - alto) // 2
    return img.crop((ix, iy, ix + ancho, iy + alto))


def velo(img, base=0, desde=0.45, opacidad=225, hacia="abajo"):
    """Oscurece el arte para que el texto se lea.

    `base` es un velo plano sobre toda la imagen (0-255) y encima cae un
    degradado que se acumula `hacia` abajo o hacia arriba. Sin esto, un texto
    blanco sobre una ventana o un monitor encendido se pierde.
    """
    capa = Image.new("L", (1, img.height), base)
    for y in range(img.height):
        t = y / img.height
        if hacia == "arriba":
            t = 1 - t
        v = 0 if t < desde else int(((t - desde) / (1 - desde)) ** 1.4 * opacidad)
        capa.putpixel((0, y), min(255, base + v))
    capa = capa.resize(img.size)
    negro = Image.new("RGB", img.size, (0, 0, 0))
    return Image.composite(negro, img, capa)


def scrim(img, desde=0.45, opacidad=225):
    return velo(img, base=0, desde=desde, opacidad=opacidad, hacia="abajo")


# --- Cromo común ----------------------------------------------------------

def cabecera(d, marca, indice, total, color, saltar_num=False):
    f = fuente(SEMI, 24)
    escribir_tracking(d, marca["nombre"].upper(), f, MARGEN, 62, color, 2)
    if not saltar_num:
        txt = f"{indice:02d} / {total:02d}"
        d.text((W - MARGEN - _ancho(f, txt), 62), txt, font=f, fill=color)


def pie(d, marca, color, rojo, deslizar=True):
    f = fuente(SEMI, 24)
    y = H - 92
    d.ellipse([MARGEN, y + 8, MARGEN + 16, y + 24], fill=rojo)
    d.text((MARGEN + 30, y), marca["handle"], font=f, fill=color)
    if deslizar:
        txt = "DESLIZA →"
        fw = fuente(BOLD, 22)
        tw = _ancho(fw, txt)
        x0 = W - MARGEN - tw - 44
        d.rounded_rectangle([x0, y - 8, W - MARGEN, y + 42], radius=25,
                            fill=color)
        d.text((x0 + 22, y + 2), txt, font=fw, fill="#ffffff")


# --- Layouts --------------------------------------------------------------

def _colores(marca):
    return (marca.get("negro", "#111111"), marca.get("rojo", "#b03035"),
            marca.get("fondo", "#ffffff"))


def slide_portada(s, marca, arte, indice, total):
    """Hook arriba sobre blanco, arte a sangre en la banda inferior."""
    negro, rojo, fondo = _colores(marca)
    img = Image.new("RGB", (W, H), fondo)
    alto_arte = int(H * 0.46)
    if arte:
        img.paste(encajar_arte(arte, W, alto_arte), (0, H - alto_arte))
    d = ImageDraw.Draw(img)

    cabecera(d, marca, indice, total, negro, saltar_num=True)

    hook = s["hook"]
    lineas = hook if isinstance(hook, list) else None
    texto = "\n".join(hook) if isinstance(hook, list) else hook
    caja_alto = H - alto_arte - 200
    f, lineas, alto, paso = ajustar(
        texto.upper(), BLACK, W - MARGEN * 2, caja_alto, 152, 46,
        interlineado=1.0, lineas_fijas=[l.upper() for l in lineas] if lineas else None,
    )
    y = H - alto_arte - 70 - alto
    escribir_bloque(d, lineas, f, MARGEN, y, paso, negro,
                    acento=(s.get("acento") or "").upper() or None,
                    color_acento=rojo)
    d.rectangle([MARGEN, y - 44, MARGEN + 90, y - 34], fill=rojo)
    return img


def slide_portada_full(s, marca, arte, indice, total):
    """Arte a sangre, degradado y hook blanco abajo."""
    negro, rojo, fondo = _colores(marca)
    img = encajar_arte(arte, W, H) if arte else Image.new("RGB", (W, H), "#111111")
    img = scrim(img, desde=0.30, opacidad=232)
    d = ImageDraw.Draw(img)
    cabecera(d, marca, indice, total, "#ffffff", saltar_num=True)

    hook = s["hook"]
    lineas = hook if isinstance(hook, list) else None
    texto = "\n".join(hook) if isinstance(hook, list) else hook
    f, lineas, alto, paso = ajustar(
        texto.upper(), BLACK, W - MARGEN * 2, int(H * 0.5), 112, 46,
        interlineado=1.0, lineas_fijas=[l.upper() for l in lineas] if lineas else None,
    )
    y = H - 150 - alto
    escribir_bloque(d, lineas, f, MARGEN, y, paso, "#ffffff",
                    acento=(s.get("acento") or "").upper() or None,
                    color_acento="#ff5a5f" if rojo == "#b03035" else rojo)
    pie(d, marca, "#ffffff", rojo, deslizar=False)
    return img


def _cuerpo_con_label(s, marca, arte, indice, total, numero=None):
    negro, rojo, fondo = _colores(marca)
    img = Image.new("RGB", (W, H), fondo)
    alto_arte = 0
    if arte:
        # La banda corta 140px antes del borde: el pie va sobre blanco y se lee
        # siempre, dé la foto clara u oscura.
        alto_arte = int(H * 0.30)
        img.paste(encajar_arte(arte, W, alto_arte), (0, H - 140 - alto_arte))
        alto_arte += 140
    d = ImageDraw.Draw(img)
    cabecera(d, marca, indice, total, negro)

    y = 190
    if numero:
        fnum = fuente(BLACK, 132)
        d.text((MARGEN, y - 40), numero, font=fnum, fill=rojo)
        y += 118
    elif s.get("label"):
        fl = fuente(BOLD, 26)
        escribir_tracking(d, s["label"].upper(), fl, MARGEN, y, rojo, 3)
        y += 62

    tope = H - alto_arte - (60 if alto_arte else 190)
    ft, lt, altot, pasot = ajustar(s["titulo"].upper(), BLACK, W - MARGEN * 2,
                                   int((tope - y) * 0.55), 84, 40, interlineado=1.02)
    y = escribir_bloque(d, lt, ft, MARGEN, y, pasot, negro,
                        acento=(s.get("acento") or "").upper() or None,
                        color_acento=rojo)

    if s.get("cuerpo"):
        y += 36
        fc, lc, altoc, pasoc = ajustar(s["cuerpo"], MEDIUM, W - MARGEN * 2 - 40,
                                       tope - y, 40, 22, interlineado=1.45)
        escribir_bloque(d, lc, fc, MARGEN, y, pasoc, "#3a3a3a")

    pie(d, marca, negro, rojo, deslizar=True)
    return img


def slide_contexto(s, marca, arte, indice, total):
    return _cuerpo_con_label(s, marca, arte, indice, total)


def slide_contenido(s, marca, arte, indice, total):
    return _cuerpo_con_label(s, marca, arte, indice, total,
                             numero=s.get("numero"))


def slide_entrega(s, marca, arte, indice, total):
    """El slide que enseña el lead magnet: mockup del recurso al centro.

    Orden de reparto: cabecera, label, título, cuerpo anclado abajo y el mockup
    ocupando exactamente el hueco que sobra. Así el texto nunca pisa la imagen.
    """
    negro, rojo, fondo = _colores(marca)
    img = Image.new("RGB", (W, H), "#f4f2ef")
    d = ImageDraw.Draw(img)
    cabecera(d, marca, indice, total, negro)

    y = 180
    if s.get("label"):
        escribir_tracking(d, s["label"].upper(), fuente(BOLD, 26), MARGEN, y,
                          rojo, 3)
        y += 58
    ft, lt, altot, pasot = ajustar(s["titulo"].upper(), BLACK, W - MARGEN * 2,
                                   240, 72, 36, interlineado=1.02)
    y = escribir_bloque(d, lt, ft, MARGEN, y, pasot, negro,
                        acento=(s.get("acento") or "").upper() or None,
                        color_acento=rojo)

    suelo = H - 175  # por encima del pie
    if s.get("cuerpo"):
        # Caja generosa y suelo de 22px: aquí se explica qué es el recurso y una
        # letra de 20 no se lee en el móvil. Si no cabe, sobra copy.
        fc, lc, altoc, pasoc = ajustar(s["cuerpo"], MEDIUM, W - MARGEN * 2 - 40,
                                       190, 32, 22, interlineado=1.4)
        escribir_bloque(d, lc, fc, MARGEN, suelo - altoc, pasoc, "#3a3a3a")
        suelo -= altoc + 40

    if arte:
        techo = y + 44
        caja_h = min(suelo - techo, 660)
        caja_w = min(int(caja_h * 0.78), W - MARGEN * 2 - 120)
        if caja_h > 220 and caja_w > 180:
            caja_h = int(caja_w / 0.78)
            x = (W - caja_w) // 2
            my = techo + max(0, (suelo - techo - caja_h) // 2)

            sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(sombra).rectangle(
                [x + 10, my + 20, x + caja_w + 10, my + caja_h + 20],
                fill=(120, 112, 102, 150))
            sombra = sombra.filter(ImageFilter.GaussianBlur(22))
            img.paste(sombra, (0, 0), sombra)
            img.paste(encajar_arte(arte, caja_w, caja_h), (x, my))
            d = ImageDraw.Draw(img)

    pie(d, marca, negro, rojo, deslizar=True)
    return img


def slide_cta(s, marca, arte, indice, total):
    """COMENTA + KEYWORD gigante en rojo + qué recibe."""
    negro, rojo, fondo = _colores(marca)
    img = Image.new("RGB", (W, H), fondo)
    d = ImageDraw.Draw(img)
    cabecera(d, marca, indice, total, negro)

    pre = (s.get("pre") or "COMENTA").upper()
    kw = s["keyword"].upper()
    post = s.get("post") or ""

    fpre = fuente(BLACK, 74)
    fkw, lkw, altokw, pasokw = ajustar(kw, BLACK, W - MARGEN * 2, 300, 190, 60,
                                       interlineado=1.0)
    fpost, lpost, altopost, pasopost = ajustar(post.upper(), BLACK,
                                               W - MARGEN * 2, 240, 56, 30,
                                               interlineado=1.12)

    total_alto = 74 + 30 + altokw + 34 + altopost
    y = (H - total_alto) // 2 - 20
    d.text((MARGEN, y), pre, font=fpre, fill=negro)
    y += 74 + 30
    y = escribir_bloque(d, lkw, fkw, MARGEN, y, pasokw, rojo)
    y += 34
    escribir_bloque(d, lpost, fpost, MARGEN, y, pasopost, negro)

    pie(d, marca, negro, rojo, deslizar=bool(s.get("deslizar")))
    return img


def slide_venta(s, marca, arte, indice, total):
    """Cierre comercial: fondo negro, oferta y siguiente paso."""
    negro, rojo, fondo = _colores(marca)
    img = Image.new("RGB", (W, H), "#111111")
    if arte:
        img = velo(encajar_arte(arte, W, H), base=120, desde=0.25,
                   opacidad=150, hacia="arriba")
    d = ImageDraw.Draw(img)
    cabecera(d, marca, indice, total, "#ffffff")

    y = 210
    if s.get("label"):
        escribir_tracking(d, s["label"].upper(), fuente(BOLD, 26), MARGEN, y,
                          "#ff5a5f" if rojo == "#b03035" else rojo, 3)
        y += 60
    ft, lt, altot, pasot = ajustar(s["titulo"].upper(), BLACK, W - MARGEN * 2,
                                   440, 80, 38, interlineado=1.02)
    y = escribir_bloque(d, lt, ft, MARGEN, y, pasot, "#ffffff",
                        acento=(s.get("acento") or "").upper() or None,
                        color_acento="#ff5a5f" if rojo == "#b03035" else rojo)

    if s.get("cuerpo"):
        y += 40
        fc, lc, altoc, pasoc = ajustar(s["cuerpo"], MEDIUM, W - MARGEN * 2 - 40,
                                       320, 38, 22, interlineado=1.45)
        y = escribir_bloque(d, lc, fc, MARGEN, y, pasoc, "#d8d4d0")

    if s.get("boton"):
        fb = fuente(BOLD, 32)
        txt = s["boton"].upper()
        tw = _ancho(fb, txt)
        by = H - 250
        d.rounded_rectangle([MARGEN, by, MARGEN + tw + 76, by + 84], radius=42,
                            fill=rojo)
        d.text((MARGEN + 38, by + 24), txt, font=fb, fill="#ffffff")

    pie(d, marca, "#ffffff", rojo, deslizar=False)
    return img


LAYOUTS = {
    "portada": slide_portada,
    "portada_full": slide_portada_full,
    "contexto": slide_contexto,
    "contenido": slide_contenido,
    "entrega": slide_entrega,
    "cta": slide_cta,
    "venta": slide_venta,
}


def render_slide(s, marca, arte, indice, total):
    fn = LAYOUTS.get(s.get("layout"))
    if not fn:
        raise ValueError(f"Layout desconocido: {s.get('layout')}. "
                         f"Válidos: {', '.join(LAYOUTS)}")
    return fn(s, marca, arte, indice, total)
