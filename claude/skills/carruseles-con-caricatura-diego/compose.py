#!/usr/bin/env python3
"""Compositor v2: 4 layouts (portada, dato, contexto, cierre) con estructura
aprendida de las 3 referencias. Personaje a sangre + tipografía con jerarquía."""
import json, base64, urllib.request, pathlib, textwrap, time, io
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CFG = pathlib.Path.home() / ".config/ecsstudio/gemini.env"
KEY = [l.split("=")[-1].strip().strip('"').strip("'")
       for l in CFG.read_text().splitlines() if "AIza" in l][0]
URL = ("https://generativelanguage.googleapis.com/v1beta/models/"
       f"gemini-3-pro-image:generateContent?key={KEY}")

W, H = 1080, 1350
F = pathlib.Path.home() / "Library/Fonts"
BLACK, BOLD, LIGHT = str(F/"Montserrat-Black.ttf"), str(F/"Montserrat-Bold.ttf"), str(F/"Montserrat-Light.ttf")

PAL = {"crema": "#f2e8dc", "rojo": "#b03035", "negro": "#141414",
       "blanco": "#ffffff", "tinta": "#141414"}

ROOT = pathlib.Path(__file__).parent
REF = ROOT / "assets/diego-caricatura.png"


def gemini(prompt, ref=REF):
    parts = []
    if ref and ref.exists():
        parts.append({"inlineData": {"mimeType": "image/png",
                     "data": base64.b64encode(ref.read_bytes()).decode()}})
    parts.append({"text": prompt})
    body = json.dumps({"contents": [{"parts": parts}],
                       "generationConfig": {"responseModalities": ["IMAGE"]}}).encode()
    req = urllib.request.Request(URL, data=body,
                                 headers={"Content-Type": "application/json"})
    for i in range(3):
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                data = json.load(r)
            for p in data["candidates"][0]["content"]["parts"]:
                if "inlineData" in p:
                    return base64.b64decode(p["inlineData"]["data"])
        except Exception as e:
            print(f"    reintento {i+1}: {e}", flush=True); time.sleep(4)
    return None


def cortar_blanco(img, umbral=236):
    img = img.convert("RGBA"); px = img.load(); w, h = img.size
    pila = [(x, y) for x in range(w) for y in (0, h-1)]
    pila += [(x, y) for y in range(h) for x in (0, w-1)]
    visto = set()
    while pila:
        x, y = pila.pop()
        if (x, y) in visto or not (0 <= x < w and 0 <= y < h): continue
        visto.add((x, y)); r, g, b, a = px[x, y]
        if a and r >= umbral and g >= umbral and b >= umbral:
            px[x, y] = (r, g, b, 0)
            pila += [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return img.crop(img.getbbox())


def _wrap(draw, txt, font, max_w):
    out = []
    for linea in txt.split("\n"):
        palabras, cur = linea.split(" "), ""
        for p in palabras:
            t = (cur + " " + p).strip()
            if draw.textlength(t, font=font) <= max_w: cur = t
            else: out.append(cur); cur = p
        out.append(cur)
    return out


def _fit(draw, txt, path, max_w, start, min_s=40, max_lines=5):
    s = start
    while s > min_s:
        f = ImageFont.truetype(path, s)
        ls = _wrap(draw, txt, f, max_w)
        if len(ls) <= max_lines and all(draw.textlength(l, font=f) <= max_w for l in ls):
            return f, ls
        s -= 3
    f = ImageFont.truetype(path, min_s)
    return f, _wrap(draw, txt, f, max_w)


def _draw_lines(d, x, y, lines, font, fill, lh=1.14):
    step = int(font.size * lh)
    for l in lines:
        d.text((x, y), l, font=font, fill=fill); y += step
    return y


def _pega_sangre(card, scene_png, bg, alto_frac=0.6, lado="centro"):
    """Pega al personaje a sangre por el borde inferior."""
    img = cortar_blanco(Image.open(io.BytesIO(scene_png)))
    max_h = int(H * alto_frac); max_w = int(W * 0.92)
    ratio = min(max_w / img.width, max_h / img.height)
    nw, nh = int(img.width*ratio), int(img.height*ratio)
    img = img.resize((nw, nh), Image.LANCZOS)
    if lado == "centro": x = (W - nw)//2
    elif lado == "der": x = W - nw - 40
    else: x = 40
    card.paste(img, (x, H - nh), img)


def _draw_rich(d, tokens, x0, y0, font, base, rojo, max_w, lh=1.06):
    """Dibuja texto con wrap; los tokens marcados (t, True) van en rojo."""
    space = d.textlength(" ", font=font)
    step = int(font.size * lh)
    x, y = x0, y0
    for txt, es_rojo in tokens:
        w = d.textlength(txt, font=font)
        if x + w > x0 + max_w and x > x0:
            x = x0; y += step
        d.text((x, y), txt, font=font, fill=(rojo if es_rojo else base))
        x += w + space
    return y + step


def _tok(texto, roja=None):
    """Convierte texto a tokens; palabras en `roja` van marcadas en rojo.
    `roja` puede ser str o lista; las frases de varias palabras marcan cada palabra."""
    entradas = [] if roja is None else ([roja] if isinstance(roja, str) else list(roja))
    rojas = set()
    for e in entradas:
        for w in str(e).lower().split():
            rojas.add(w.strip(".,:'"))
    out = []
    for w in texto.split():
        limpio = w.strip(".,:'\"").lower()
        out.append((w, limpio in rojas and limpio != ""))
    return out


def hero(texto, scene_png, dest, roja=None, alto=0.62, fondo="negro"):
    """Layout unico: fondo negro, texto grande arriba, escena de Diego a sangre."""
    bg = PAL[fondo]; base = PAL["crema"] if fondo == "negro" else PAL["tinta"]
    card = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(card)
    # escena a sangre abajo
    if scene_png:
        img = cortar_blanco(Image.open(io.BytesIO(scene_png)))
        max_h = int(H*alto); max_w = int(W*0.98)
        ratio = min(max_w/img.width, max_h/img.height)
        nw, nh = int(img.width*ratio), int(img.height*ratio)
        img = img.resize((nw, nh), Image.LANCZOS)
        top = H - nh
        # degradado negro sobre el tercio superior de la escena -> funde con el negro
        grad = Image.new("L", (1, nh), 0)
        for i in range(nh):
            frac = i / nh
            grad.putpixel((0, i), int(255 * max(0, 1 - frac*3.2)))
        grad = grad.resize((nw, nh))
        negro = Image.new("RGBA", (nw, nh), (20, 20, 20, 255))
        negro.putalpha(grad)
        img = img.convert("RGBA"); img.alpha_composite(negro)
        card.paste(img, ((W-nw)//2, top), img)
    # texto arriba
    m = 70
    f, lines = _fit(d, texto, BLACK, W-2*m, 116, min_s=62, max_lines=4)
    # reconstruye tokens respetando el wrap de _fit
    y = m
    for ln in lines:
        _draw_rich(d, _tok(ln, roja), m, y, f, base, PAL["rojo"], W-2*m, 1.02)
        y += int(f.size*1.02)
    dest.parent.mkdir(parents=True, exist_ok=True); card.save(dest, quality=95)


def _fit_alto(draw, txt, path, max_w, start, min_s=32, max_lines=8):
    """Como _fit pero pensado para textos largos: baja mas y permite mas lineas."""
    s = start
    while s > min_s:
        f = ImageFont.truetype(path, s)
        ls = _wrap(draw, txt, f, max_w)
        if len(ls) <= max_lines and all(draw.textlength(l, font=f) <= max_w for l in ls):
            return f, ls
        s -= 2
    f = ImageFont.truetype(path, min_s)
    return f, _wrap(draw, txt, f, max_w)


def hero_full(texto, scene_png, dest, roja=None, scene_is_path=False):
    """Escena a pantalla completa (fondo ilustra el mensaje, Diego grande) con
    texto ADAPTATIVO: titulo grande si es corto, texto medio legible si es largo.
    El degradado oscuro cubre exactamente la altura del bloque de texto.
    `scene_png` puede ser bytes o, si scene_is_path=True, una ruta a la escena limpia."""
    card = Image.new("RGB", (W, H), PAL["negro"])
    if scene_png:
        src = Image.open(scene_png) if scene_is_path else Image.open(io.BytesIO(scene_png))
        img = src.convert("RGB")
        ratio = max(W/img.width, H/img.height)
        nw, nh = int(img.width*ratio), int(img.height*ratio)
        img = img.resize((nw, nh), Image.LANCZOS)
        card.paste(img, ((W-nw)//2, H-nh))
    d = ImageDraw.Draw(card)
    m = 66
    # tamaño segun longitud: cortos grandes (como gusta), largos medianos y legibles
    n = len(texto)
    start = 116 if n <= 42 else (92 if n <= 75 else (74 if n <= 120 else 60))
    f, lines = _fit_alto(d, texto, BLACK, W-2*m, start, min_s=40, max_lines=7)
    lh = 1.06
    step = int(f.size*lh)
    bloque_h = step*len(lines)
    # degradado oscuro que cubre el bloque de texto + un respiro por debajo
    lim = min(H, m + bloque_h + int(f.size*1.4))
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ov.load()
    for y in range(lim):
        frac = y/lim
        a = int(238 * max(0, 1 - frac**2*1.15))
        for x in range(W): od[x, y] = (17, 17, 17, a)
    card = Image.alpha_composite(card.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(card)
    y = m
    for ln in lines:
        _draw_rich(d, _tok(ln, roja), m, y, f, PAL["crema"], PAL["rojo"], W-2*m, lh)
        y += step
    dest.parent.mkdir(parents=True, exist_ok=True); card.save(dest, quality=95)


def portada(texto, keyword, scene_png, dest, fondo="negro"):
    bg = PAL[fondo]; fg = PAL["crema"] if fondo == "negro" else PAL["tinta"]
    card = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(card)
    m = 70
    font, lines = _fit(d, texto, BLACK, W-2*m, 118, min_s=64, max_lines=4)
    y = _draw_lines(d, m, m, lines, font, fg, 1.06)
    # subraya la keyword en rojo si aparece
    if scene_png: _pega_sangre(card, scene_png, bg, 0.58, "centro")
    dest.parent.mkdir(parents=True, exist_ok=True); card.save(dest, quality=95)


def dato(num, etiqueta, dest, fondo="negro", sub=""):
    bg = PAL[fondo]; fg = PAL["crema"] if fondo == "negro" else PAL["tinta"]
    card = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(card)
    f_num, ln = _fit(d, num, BLACK, W-120, 300, min_s=120, max_lines=2)
    th = int(f_num.size*1.05)*len(ln)
    y = (H-th)//2 - 40
    for l in ln:
        w = d.textlength(l, font=f_num); d.text(((W-w)//2, y), l, font=f_num, fill=PAL["rojo"] if fondo!="rojo" else fg); y += int(f_num.size*1.05)
    # etiqueta: baja el cuerpo hasta que cabe en el ancho
    es = 52
    while es > 26:
        f_e = ImageFont.truetype(BOLD, es)
        if d.textlength(etiqueta.upper(), font=f_e) <= W-140: break
        es -= 2
    we = d.textlength(etiqueta.upper(), font=f_e)
    d.text(((W-we)//2, y+30), etiqueta.upper(), font=f_e, fill=fg)
    if sub:
        f_s = ImageFont.truetype(LIGHT, 40); ls = _wrap(d, sub, f_s, W-160)
        yy = y+120
        for l in ls:
            w = d.textlength(l, font=f_s); d.text(((W-w)//2, yy), l, font=f_s, fill=fg); yy += 52
    dest.parent.mkdir(parents=True, exist_ok=True); card.save(dest, quality=95)


def antes_despues(a_num, a_lab, b_num, b_lab, titulo, dest, fondo="negro"):
    bg = PAL[fondo]; fg = PAL["crema"] if fondo == "negro" else PAL["tinta"]
    card = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(card)
    m = 70
    f_t, lt = _fit(d, titulo, BLACK, W-2*m, 92, min_s=56, max_lines=3)
    _draw_lines(d, m, m, lt, f_t, fg, 1.06)
    cy = 720
    # antes (apagado)
    f_n = ImageFont.truetype(BLACK, 130); f_l = ImageFont.truetype(BOLD, 46)
    gris = "#6b6b6b" if fondo == "negro" else "#9a8f80"
    wa = d.textlength(a_num, font=f_n); d.text(((W-wa)//2, cy-230), a_num, font=f_n, fill=gris)
    wal = d.textlength(a_lab.upper(), font=f_l); d.text(((W-wal)//2, cy-70), a_lab.upper(), font=f_l, fill=gris)
    # flecha roja
    ay = cy+70
    d.polygon([(W//2-60, ay), (W//2+20, ay), (W//2+20, ay-25), (W//2+80, ay+20),
               (W//2+20, ay+65), (W//2+20, ay+40), (W//2-60, ay+40)], fill=PAL["rojo"])
    # después (fuerte, rojo)
    wb = d.textlength(b_num, font=f_n); d.text(((W-wb)//2, cy+160), b_num, font=f_n, fill=PAL["rojo"] if fondo!="rojo" else fg)
    wbl = d.textlength(b_lab.upper(), font=f_l); d.text(((W-wbl)//2, cy+320), b_lab.upper(), font=f_l, fill=fg)
    dest.parent.mkdir(parents=True, exist_ok=True); card.save(dest, quality=95)


def contexto(texto, scene_png, dest, fondo="crema", con_persona=True):
    bg = PAL[fondo]; fg = PAL["tinta"] if fondo != "negro" else PAL["crema"]
    card = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(card)
    m = 70
    font, lines = _fit(d, texto, BOLD, W-2*m, 78, min_s=48, max_lines=4)
    y = _draw_lines(d, m, m, lines, font, fg, 1.16)
    if scene_png:
        if con_persona: _pega_sangre(card, scene_png, bg, 0.60, "centro")
        else:
            img = cortar_blanco(Image.open(io.BytesIO(scene_png)))
            hueco = H - y - m - 40
            ratio = min((W-2*m)/img.width, hueco/img.height)
            nw, nh = int(img.width*ratio), int(img.height*ratio)
            img = img.resize((nw, nh), Image.LANCZOS)
            card.paste(img, ((W-nw)//2, y+40+(hueco-nh)//2), img)
    dest.parent.mkdir(parents=True, exist_ok=True); card.save(dest, quality=95)


def cierre(texto, keyword, promesa, scene_png, dest, fondo="crema"):
    bg = PAL[fondo]; fg = PAL["tinta"]
    card = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(card)
    m = 70
    font, lines = _fit(d, texto, BOLD, W-2*m, 66, min_s=44, max_lines=3)
    y = _draw_lines(d, m, m, lines, font, fg, 1.16)
    # botón keyword rojo
    f_k = ImageFont.truetype(BLACK, 68)
    kw = f"COMENTA  {keyword.upper()}"
    tw = d.textlength(kw, font=f_k)
    bx0, by0 = (W-tw-90)//2, y+40
    d.rounded_rectangle([bx0, by0, bx0+tw+90, by0+130], radius=28, fill=PAL["rojo"])
    d.text((bx0+45, by0+28), kw, font=f_k, fill=PAL["crema"])
    # promesa
    f_p = ImageFont.truetype(LIGHT, 38); lp = _wrap(d, promesa, f_p, W-2*m)
    yy = by0+170
    for l in lp:
        w = d.textlength(l, font=f_p); d.text(((W-w)//2, yy), l, font=f_p, fill=fg); yy += 50
    if scene_png: _pega_sangre(card, scene_png, bg, 0.42, "centro")
    dest.parent.mkdir(parents=True, exist_ok=True); card.save(dest, quality=95)


def hero_safe(texto, scene_png, dest, roja=None, scene_is_path=False):
    """Layout SIN SOLAPE: el texto vive en una banda superior solida y la escena
    se escala para ocupar EXACTAMENTE el resto. El texto nunca tapa la cara."""
    card = Image.new("RGB", (W, H), PAL["negro"])
    d = ImageDraw.Draw(card)
    m = 64
    n = len(texto)
    start = 104 if n <= 45 else (86 if n <= 80 else (70 if n <= 125 else 58))
    f, lines = _fit_alto(d, texto, BLACK, W-2*m, start, min_s=40, max_lines=6)
    lh = 1.08
    step = int(f.size*lh)
    alto_texto = m + step*len(lines) + int(f.size*0.55)   # banda reservada
    # la escena ocupa el resto, anclada abajo, recortando por los lados si hace falta
    if scene_png:
        src = Image.open(scene_png) if scene_is_path else Image.open(io.BytesIO(scene_png))
        img = src.convert("RGB")
        alto_escena = H - alto_texto
        ratio = max(W/img.width, alto_escena/img.height)
        nw, nh = int(img.width*ratio), int(img.height*ratio)
        img = img.resize((nw, nh), Image.LANCZOS)
        # recorte centrado horizontal, anclado abajo verticalmente
        izq = (nw - W)//2
        arriba = nh - alto_escena
        img = img.crop((izq, arriba, izq+W, arriba+alto_escena))
        # funde el borde superior de la escena con la banda negra
        fund = 90
        grad = Image.new("L", (1, alto_escena), 255)
        for i in range(min(fund, alto_escena)):
            grad.putpixel((0, i), int(255*(i/fund)))
        img.putalpha(grad.resize((W, alto_escena)))
        card.paste(img, (0, alto_texto), img)
    d = ImageDraw.Draw(card)
    y = m
    for ln in lines:
        _draw_rich(d, _tok(ln, roja), m, y, f, PAL["crema"], PAL["rojo"], W-2*m, lh)
        y += step
    dest.parent.mkdir(parents=True, exist_ok=True); card.save(dest, quality=95)


def poster(lineas, scene_png, dest, acento=1, scene_is_path=False):
    """Layout cartel: escena a sangre, titulo ABAJO en varias lineas centradas,
    la linea `acento` en rojo, con separador de reglas encima."""
    card = Image.new("RGB", (W, H), PAL["negro"])
    if scene_png:
        src = Image.open(scene_png) if scene_is_path else Image.open(io.BytesIO(scene_png))
        img = src.convert("RGB")
        ratio = max(W/img.width, H/img.height)
        nw, nh = int(img.width*ratio), int(img.height*ratio)
        img = img.resize((nw, nh), Image.LANCZOS)
        card.paste(img, ((W-nw)//2, 0))
    d = ImageDraw.Draw(card)
    m = 60
    # cuerpo que quepa: bajamos hasta que la linea mas larga entra
    s = 96
    while s > 44:
        f = ImageFont.truetype(BLACK, s)
        if max(d.textlength(l, font=f) for l in lineas) <= W-2*m: break
        s -= 2
    lh = int(s*1.12)
    bloque = lh*len(lineas)
    base_y = H - m - bloque
    # velo oscuro sobre la zona del titulo
    ov = Image.new("RGBA", (W, H), (0,0,0,0)); od = ov.load()
    top = max(0, base_y - int(s*2.2))
    for y in range(top, H):
        fr = (y-top)/max(1,(H-top))
        a = int(236*min(1.0, fr*1.7))
        for x in range(W): od[x, y] = (17,17,17,a)
    card = Image.alpha_composite(card.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(card)
    # separador: dos reglas con un rombo rojo en medio
    sy = base_y - int(s*0.85)
    cx = W//2
    d.line([(cx-230, sy), (cx-40, sy)], fill=PAL["crema"], width=3)
    d.line([(cx+40, sy), (cx+230, sy)], fill=PAL["crema"], width=3)
    r = 13
    d.polygon([(cx, sy-r), (cx+r, sy), (cx, sy+r), (cx-r, sy)], fill=PAL["rojo"])
    y = base_y
    for i, l in enumerate(lineas):
        f = ImageFont.truetype(BLACK, s)
        w = d.textlength(l, font=f)
        col = PAL["rojo"] if i == acento else PAL["crema"]
        d.text(((W-w)//2, y), l, font=f, fill=col)
        y += lh
    dest.parent.mkdir(parents=True, exist_ok=True); card.save(dest, quality=95)


def _etiqueta(card, d, texto, caja_xy, ancla_xy):
    """Callout: cajita redondeada con texto + linea guia fina hasta el ancla."""
    f = ImageFont.truetype(BOLD, 26)
    lineas = texto.split("\n")
    tw = max(d.textlength(l, font=f) for l in lineas)
    th = len(lineas)*int(f.size*1.18)
    px, py = 18, 12
    x, y = caja_xy
    x0, y0 = x - tw/2 - px, y - th/2 - py
    x1, y1 = x + tw/2 + px, y + th/2 + py
    # linea guia primero (queda por debajo)
    d.line([ (x, y1), (ancla_xy[0], ancla_xy[1]) ], fill=PAL["crema"], width=2)
    d.ellipse([ancla_xy[0]-5, ancla_xy[1]-5, ancla_xy[0]+5, ancla_xy[1]+5], fill=PAL["crema"])
    d.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=PAL["rojo"])
    yy = y0 + py
    for l in lineas:
        w = d.textlength(l, font=f)
        d.text((x - w/2, yy), l, font=f, fill=PAL["crema"]); yy += int(f.size*1.18)


def cartel(lineas, scene_png, dest, acento=1, callouts=None, scene_is_path=False):
    """Layout cartel: escena a sangre, etiquetas con linea guia, titulo abajo
    centrado con la linea `acento` en rojo y halo."""
    card = Image.new("RGB", (W, H), PAL["negro"])
    if scene_png:
        src = Image.open(scene_png) if scene_is_path else Image.open(io.BytesIO(scene_png))
        img = src.convert("RGB")
        ratio = max(W/img.width, H/img.height)
        nw, nh = int(img.width*ratio), int(img.height*ratio)
        img = img.resize((nw, nh), Image.LANCZOS)
        card.paste(img, ((W-nw)//2, 0))
    d = ImageDraw.Draw(card)
    m = 56
    s = 92
    while s > 40:
        f = ImageFont.truetype(BLACK, s)
        if max(d.textlength(l, font=f) for l in lineas) <= W-2*m: break
        s -= 2
    f = ImageFont.truetype(BLACK, s)
    lh = int(s*1.10)
    bloque = lh*len(lineas)
    base_y = H - m - bloque
    # velo inferior
    ov = Image.new("RGBA", (W, H), (0,0,0,0)); od = ov.load()
    top = max(0, base_y - int(s*2.0))
    for y in range(top, H):
        fr = (y-top)/max(1,(H-top))
        a = int(242*min(1.0, fr*1.6))
        for x in range(W): od[x, y] = (17,17,17,a)
    card = Image.alpha_composite(card.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(card)
    # halo de la linea de acento
    halo = Image.new("RGBA", (W, H), (0,0,0,0)); hd = ImageDraw.Draw(halo)
    y = base_y
    for i, l in enumerate(lineas):
        if i == acento:
            w = hd.textlength(l, font=f)
            hd.text(((W-w)//2, y), l, font=f, fill=(176, 48, 53, 210))
        y += lh
    halo = halo.filter(ImageFilter.GaussianBlur(22))
    card = Image.alpha_composite(card.convert("RGBA"), halo).convert("RGB")
    d = ImageDraw.Draw(card)
    # separador
    sy = base_y - int(s*0.78); cx = W//2
    d.line([(cx-215, sy), (cx-38, sy)], fill=PAL["crema"], width=3)
    d.line([(cx+38, sy), (cx+215, sy)], fill=PAL["crema"], width=3)
    r = 12
    d.polygon([(cx, sy-r), (cx+r, sy), (cx, sy+r), (cx-r, sy)], fill=PAL["rojo"])
    # titulo
    y = base_y
    for i, l in enumerate(lineas):
        w = d.textlength(l, font=f)
        d.text(((W-w)//2, y), l, font=f, fill=(PAL["rojo"] if i == acento else PAL["crema"]))
        y += lh
    # etiquetas
    for c in (callouts or []):
        _etiqueta(card, d, c["texto"],
                  (int(c["cx"]*W), int(c["cy"]*H)),
                  (int(c["ax"]*W), int(c["ay"]*H)))
    dest.parent.mkdir(parents=True, exist_ok=True); card.save(dest, quality=95)
