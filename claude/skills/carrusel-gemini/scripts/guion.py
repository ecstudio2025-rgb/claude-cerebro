"""Gemini escribe el carrusel entero: ganchos del Hook Vault y copy slide a slide.

Dos pasadas, en este orden:

    python3 guion.py --brief brief.json --solo-ganchos
        -> 6 ganchos de portada adaptados al español, cada uno con su id del
           vault y su disparador psicológico. Se elige uno.

    python3 guion.py --brief brief.json --hook 08-0063 --out carrusel.json
        -> el carrusel completo listo para build.py

El gancho sale SIEMPRE de una plantilla del Hook Vault (4.550 ganchos etiquetados
por psicología). Sin esa base, el modelo escribe portadas correctas y muertas:
describen el tema en vez de abrir un bucle.

El filtro anti-IA de Diego viaja dentro del prompt, no se aplica después.
"""

import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import gemini  # noqa: E402
import hooks  # noqa: E402

ANTI_IA = pathlib.Path.home() / ".claude" / "anti-patrones-ia-redaccion.md"

METODO = """METODOLOGÍA (Máster 5.0 + ECSSTUDIO). No es decoración: rige cada frase.

1. El 80% del valor está en la portada. Si no para el scroll, lo demás no existe.
2. Filtro 5: lo entendería un niño de cinco años. Cero jerga.
3. Filtro 50: de cien personas random en la calle, cincuenta se quedarían.
4. La portada NO filtra cliente ideal. Atrae ancho. El cierre ya estrecha.
5. Nivel de conciencia 0-1: el lector no sabe que tiene el problema, o lo intuye
   y no sabe nada técnico.
6. Regla del hueco: los slides de contenido dan el QUÉ y dejan abierto el CÓMO.
   Ese hueco exacto es lo que rellena el lead magnet. Si el carrusel lo cuenta
   todo, nadie pide el recurso.
7. La keyword del CTA es específica y con beneficio concreto.
8. El slide de venta va al final, después del CTA, y habla solo al que ya ha
   decidido que quiere resolverlo pero no quiere hacerlo él.

TONO ECSSTUDIO:
- Español de España. Directo. Premium sin humo. Como habla un tío que ya lo ha
  hecho, no como un coach que lo ha leído.
- Prohibido: la palabra "sistema" como concepto central, claims garantizados,
  tono de guru, urgencia inventada.
- Las cifras, como ejemplo histórico ("un cliente pasó de 0 a 5 reservas en tres
  meses"), nunca como promesa.
- Cada slide de contenido lleva algo concreto: un número, un ejemplo, una escena.
  Un slide que solo tiene opinión es relleno.
- Si el encargo no da un nicho, NO te inventes uno. Un ejemplo concreto es
  obligatorio, pero si el carrusel entero va de dentistas cuando el encargo
  hablaba de negocios en general, se pierde a los otros noventa y nueve lectores
  y muere el filtro 50. Ejemplos concretos y variados, de sectores distintos, y
  ninguno que haga falta conocer para entender la frase."""

ESQUEMA = """ESQUEMA DE SALIDA (JSON, sin markdown, sin comentarios):

{"slides":[
 {"layout":"portada","hook":["LÍNEA 1","LÍNEA 2","LÍNEA 3"],"acento":"trozo en rojo",
  "art":"prompt de foto en español, sin texto"},
 {"layout":"contexto","label":"El problema","titulo":"...","cuerpo":"..."},
 {"layout":"contenido","numero":"01","titulo":"...","cuerpo":"...","art":"(opcional)"},
 {"layout":"entrega","label":"Lo que te llevas","titulo":"...","cuerpo":"...","art":"mockup del recurso"},
 {"layout":"cta","keyword":"KEYWORD","pre":"Comenta","post":"y te mando ..."},
 {"layout":"venta","label":"...","titulo":"...","cuerpo":"...","boton":"Escríbeme X","art":"..."}
]}

TOPES DE TEXTO (pasarse encoge la letra hasta que no se lee en el móvil):
- hook: 3 líneas como mucho, 4-6 palabras por línea. La lista fija el corte de
  línea exacto; parte donde quieras que caiga la palabra roja.
- acento: tiene que aparecer LITERAL dentro de UNA sola línea del hook (no puede
  estar partido entre dos líneas), y va al final. Cortito: 1-3 palabras.
- titulo: 5-6 palabras.
- cuerpo: 45-55 palabras como máximo. En el slide 'entrega', 35: comparte sitio
  con el mockup del recurso.
- post del cta: 6-8 palabras.
- numero: "01", "02"... como string.

ARTE (campo art, opcional salvo en portada y entrega):
- Objeto concreto + superficie + luz + plano. Nunca un concepto abstracto.
- Ni una letra, ni un cartel, ni una pantalla con interfaz: el texto lo compone
  otro programa con la fuente real.
- El rojo de marca entra por un objeto físico (un boli, un cable, una silla), uno
  por imagen.
- Sin caras mirando a cámara, sin stock corporativo sonriente."""


def leer_anti_ia():
    if ANTI_IA.exists():
        return ("FILTRO ANTI-IA — OBLIGATORIO. Si el texto cae en uno de estos "
                "patrones, no sirve. Reléelo antes de responder:\n\n"
                + ANTI_IA.read_text())
    return ("FILTRO ANTI-IA: nada de 'no es X, es Y', ni rayas decorativas, ni "
            "tríadas, ni léxico inflado (potenciar, clave, transformar), ni "
            "títulos con dos puntos y subtítulo, ni frases todas del mismo largo.")


def contexto_brief(b):
    lm = b.get("lead_magnet", {})
    of = b.get("oferta", {})
    return f"""EL ENCARGO

Tema: {b['tema']}
Seguidor ideal (a quién le habla, más ancho que el cliente): {b.get('seguidor_ideal', 'sin definir')}
Deseo primitivo que ataca: {b.get('deseo', 'dinero')}
Lead magnet que se regala: {lm.get('nombre', '—')} — promete: {lm.get('promesa', '—')}
Keyword del CTA: {b.get('keyword', 'GUION')}
Oferta de pago del cierre: {of.get('nombre', '—')} — {of.get('que_incluye', '—')}
Botón de venta: {of.get('cta', '—')}
Marca: {b.get('marca', {}).get('nombre', 'Diego Álvarez')} ({b.get('marca', {}).get('handle', '@thediegoalvarez')})
Slides totales: {b.get('slides', 8)}"""


PROMPT_GANCHOS = """Eres el copywriter de ECSSTUDIO. Escribes portadas de carrusel
de Instagram que paran el scroll en España.

{brief}

{metodo}

BANCO DE GANCHOS (Hook Vault, {n} plantillas en inglés etiquetadas por psicología).
Elige de aquí. Las plantillas son el patrón; el texto final es tuyo, en español de
España, con el tema del encargo dentro:

{banco}

TAREA: seis ganchos de portada. Cada uno de una plantilla DISTINTA del banco y de
categoría psicológica distinta, para que no se pisen entre ellos.

Reglas del gancho:
- Máximo 3 líneas, 4-6 palabras por línea. Es lo único que se lee en el feed.
- Abre un bucle o mete al lector en un coste hundido. Si describe el tema en vez
  de abrir algo, no vale.
- No filtra cliente ideal. Lo entiende cualquiera.
- Nada de traducir la plantilla: se coge el mecanismo y se escribe de cero.
- "acento" es el trozo que irá en rojo: literal dentro de UNA línea, al final,
  1-3 palabras.

{anti_ia}

Devuelve SOLO este JSON:
{{"ganchos":[{{"vault_id":"08-0063","categoria":"Controversy & Hot Takes",
"psicologia":"el disparador, en español, una frase","lineas":["...","..."],
"acento":"...","por_que":"por qué funciona con este tema, una frase seca"}}]}}"""


PROMPT_CARRUSEL = """Eres el copywriter de ECSSTUDIO. Escribes el carrusel entero.

{brief}

{metodo}

GANCHO YA ELEGIDO (respétalo, es la portada; puedes pulir la puntuación pero no
cambiar el mecanismo):
Plantilla del vault [{hook_id}] — {hook_cat}
Psicología: {hook_psi}
Líneas: {hook_lineas}
Acento (rojo): {hook_acento}

{esquema}

{anti_ia}

ÚLTIMO AVISO SOBRE EL CUERPO: no escribas el mismo párrafo seis veces con
distinto sujeto. Cada slide de contenido tiene que poder sostenerse solo si
alguien le hace una captura. Ritmo irregular: frases de dos palabras junto a
otras largas.

Devuelve SOLO el JSON del esquema, empezando por {{"slides":."""


LAYOUTS = {"portada", "portada_full", "contexto", "contenido", "entrega", "cta",
           "venta"}


def validar(datos, brief):
    """Comprueba lo que rompe el render o el embudo. Devuelve lista de fallos."""
    fallos = []
    slides = datos.get("slides")
    if not isinstance(slides, list) or not slides:
        return ["no hay slides"]

    presentes = [s.get("layout") for s in slides]
    for l in presentes:
        if l not in LAYOUTS:
            fallos.append(f"layout desconocido: {l}")
    if presentes[0] not in ("portada", "portada_full"):
        fallos.append("el primer slide no es una portada")
    for obligatorio in ("entrega", "cta"):
        if obligatorio not in presentes:
            fallos.append(f"falta el slide '{obligatorio}'")

    for i, s in enumerate(slides, 1):
        l = s.get("layout")
        if l in ("portada", "portada_full"):
            hook = s.get("hook") or []
            if isinstance(hook, list) and len(hook) > 3:
                fallos.append(f"slide {i}: el hook tiene {len(hook)} líneas (máx 3)")
            ac = s.get("acento")
            if ac and isinstance(hook, list) and not any(ac in ln for ln in hook):
                fallos.append(f"slide {i}: el acento '{ac}' no está literal en "
                              f"ninguna línea del hook, no se pintaría en rojo")
        if l in ("contexto", "contenido", "entrega", "venta"):
            if not s.get("titulo"):
                fallos.append(f"slide {i}: sin titulo")
            n = len((s.get("cuerpo") or "").split())
            if n > 70:
                fallos.append(f"slide {i}: cuerpo de {n} palabras (máx ~55)")
        if l == "cta":
            kw = s.get("keyword", "")
            if not kw:
                fallos.append(f"slide {i}: cta sin keyword")
            elif kw.upper() != brief.get("keyword", kw).upper():
                fallos.append(f"slide {i}: keyword '{kw}' distinta de la del "
                              f"brief '{brief.get('keyword')}'")
    return fallos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--brief", required=True)
    ap.add_argument("--solo-ganchos", action="store_true")
    ap.add_argument("--hook", default=None,
                    help="id del vault del gancho elegido (p.ej. 08-0063)")
    ap.add_argument("--out", default="carrusel.json")
    ap.add_argument("--banco", type=int, default=40,
                    help="cuántas plantillas del vault ve el modelo")
    ap.add_argument("--categorias", default=None, help="p.ej. 01,03,08")
    args = ap.parse_args()

    brief = json.loads(pathlib.Path(args.brief).read_text())
    cats = args.categorias.split(",") if args.categorias else brief.get("categorias")
    banco = hooks.candidatos(cats, brief.get("objetivo", "Get Views"),
                             n=args.banco, semilla=brief["tema"])
    if not banco:
        sys.exit("El vault no devolvió candidatos. Revisa --categorias.")

    if args.solo_ganchos or not args.hook:
        p = PROMPT_GANCHOS.format(
            brief=contexto_brief(brief), metodo=METODO, n=len(banco),
            banco=hooks.formatear(banco), anti_ia=leer_anti_ia())
        r = gemini.texto(p, json_estricto=True)
        for g in r.get("ganchos", []):
            print(f"\n[{g.get('vault_id')}] {g.get('categoria')}")
            for ln in g.get("lineas", []):
                print(f"    {ln.upper()}")
            print(f"    rojo: {g.get('acento')}")
            print(f"    {g.get('psicologia')}")
            print(f"    → {g.get('por_que')}")
        print(f"\nElige uno:  guion.py --brief {args.brief} --hook <id> "
              f"--out carrusel.json")
        pathlib.Path(args.out).with_suffix(".ganchos.json").write_text(
            json.dumps(r, indent=2, ensure_ascii=False))
        return

    elegido = next((h for h in banco if h["id"] == args.hook), None)
    guardado = pathlib.Path(args.out).with_suffix(".ganchos.json")
    adaptado = None
    if guardado.exists():
        prev = json.loads(guardado.read_text())
        adaptado = next((g for g in prev.get("ganchos", [])
                         if g.get("vault_id") == args.hook), None)
    if not elegido and not adaptado:
        sys.exit(f"El id {args.hook} no está ni en el banco de este tema ni en "
                 f"{guardado.name}. Lanza --solo-ganchos primero.")

    p = PROMPT_CARRUSEL.format(
        brief=contexto_brief(brief), metodo=METODO, esquema=ESQUEMA,
        anti_ia=leer_anti_ia(),
        hook_id=args.hook,
        hook_cat=(adaptado or {}).get("categoria") or elegido["category"],
        hook_psi=(adaptado or {}).get("psicologia") or elegido["psychology"],
        hook_lineas=json.dumps((adaptado or {}).get("lineas", []),
                               ensure_ascii=False),
        hook_acento=(adaptado or {}).get("acento", ""))

    datos = gemini.texto(p, json_estricto=True)
    datos.setdefault("marca", brief.get("marca", {}))
    datos.setdefault("keyword", brief.get("keyword"))
    if brief.get("estilo_arte"):
        datos["estilo_arte"] = brief["estilo_arte"]
    datos["_hook_vault"] = args.hook

    fallos = validar(datos, brief)
    if fallos:
        print("Reintento: el JSON venía con fallos")
        for f in fallos:
            print(f"  · {f}")
        datos2 = gemini.texto(
            p + "\n\nTu intento anterior tenía estos fallos, corrígelos sin "
            "cambiar lo que ya estaba bien:\n- " + "\n- ".join(fallos),
            json_estricto=True)
        datos2.setdefault("marca", brief.get("marca", {}))
        datos2.setdefault("keyword", brief.get("keyword"))
        datos2["_hook_vault"] = args.hook
        fallos2 = validar(datos2, brief)
        if len(fallos2) < len(fallos):
            datos, fallos = datos2, fallos2

    pathlib.Path(args.out).write_text(
        json.dumps(datos, indent=2, ensure_ascii=False))
    print(f"carrusel -> {args.out} ({len(datos['slides'])} slides, "
          f"gancho {args.hook})")
    if fallos:
        print("Quedan avisos que revisar a mano:")
        for f in fallos:
            print(f"  · {f}")


if __name__ == "__main__":
    main()
