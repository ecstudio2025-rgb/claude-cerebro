import compose as C, pathlib, json, time, sys
OUT = pathlib.Path("/Users/diego/Documents/Claude/carruseles-virales-master5/CARTEL-30")
DATA = json.loads(pathlib.Path("/Users/diego/Documents/Claude/carruseles-virales-master5/cartel-30.json").read_text())

BASE = ("CARTEL VERTICAL 4:5 cinematografico, composicion frontal centrada, tipo poster. "
        "PROTAGONISTA: el MISMO personaje de la imagen de referencia (misma cara, gorra "
        "beige lisa sin texto, perilla fina, aros en las orejas, piercing en la nariz, "
        "collar de cuentas, camisa negra con ribete rojo), de cuerpo medio, centrado en "
        "primer plano, claramente mas iluminado que el fondo. "
        "PALETA: negro #141414 y grises dominantes, UNICO acento rojo carmin #b03035 en "
        "el contraluz y detalles. Luz cinematografica dura, contraluz marcado, humo "
        "suave, mucha profundidad de campo. "
        "COMPOSICION: la MITAD INFERIOR queda oscura y despejada para el titulo. "
        "PROHIBIDO: texto, letras, numeros, carteles escritos, logotipos, camaras, "
        "tripodes, microfonos, focos de video, mesas de montaje. "
        "ESCENA: ")

# etiquetas de portada por carrusel (las dos fallas que nombra la idea)
ETIQ = {
 "buzon":("Sin abrir","Sin cobrar"), "info":("Sin respuesta","Sin cierre"),
 "pienso":("Duda oculta","Venta perdida"), "orden":("Precio primero","Adiós cliente"),
 "cierre":("Sin llamada","Con venta"), "subir":("Mismo trabajo","Menos dinero"),
 "caro":("Nadie protesta","Cobras poco"), "tresmil":("Mismo servicio","Otro precio"),
 "regateo":("Regatea","No gana"), "descuento":("Bajas precio","Pierdes margen"),
 "perfil":("No se entiende","No escriben"), "bio":("Habla de ti","No de él"),
 "enlace":("Nadie pincha","Nadie llega"), "foto":("Mala foto","Menos clientes"),
 "destacados":("Sin orden","Sin venta"), "molesta":("Gustas a todos","No vendes"),
 "nicho":("Muchos curiosos","Cero clientes"), "despedir":("Mucho trabajo","Poco margen"),
 "cuanto":("Solo precio","Sin contexto"), "sector":("Hablas a todos","No compra nadie"),
 "pide":("Publicas","No pides"), "antes":("Vendes de golpe","Nadie compra"),
 "gratis":("Das todo","Nadie paga"), "publico":("Precio oculto","Curiosos"),
 "problema":("Tu método","Le da igual"), "NOVENTA":("El 90%","No compra"),
 "DOSANOS":("Dos años","Mismo dinero"), "TRIPLE":("Peor que tú","Factura más"),
 "ENTIENDEN":("No se entiende","No se compra"), "CONSEJOS":("Consejos gratis","Cero facturas"),
}
CALL_POS = [{"cx":0.17,"cy":0.19,"ax":0.13,"ay":0.42},{"cx":0.83,"cy":0.19,"ax":0.87,"ay":0.42}]

def portada_fondo(cid):
    return ("una fila simetrica de figuras humanas anonimas sin rostro, tres a cada lado "
            "del protagonista, mas oscuras y desaturadas, en formacion, ambiente de "
            "negocio en penumbra con profundidad")

objetivo = sys.argv[1:] or None
for car in DATA:
    cid = car["id"]
    if objetivo and cid not in objetivo: continue
    d = OUT / cid.lower(); cache = d/".e"; cache.mkdir(parents=True, exist_ok=True)
    print(f"\n=== {cid} ({len(car['slides'])}) ===", flush=True)
    for i, s in enumerate(car["slides"], 1):
        dest = d/f"slide-{i:02d}.png"; raw = cache/f"s{i:02d}.png"
        if not raw.exists():
            esc = portada_fondo(cid) if i == 1 else s["escena"]
            pose = ("el protagonista con los brazos cruzados y expresion seria y firme; "
                    "detras, ") if i == 1 else ""
            png = C.gemini(BASE + pose + esc)
            if png is None:
                print(f"  [{i}] FALLO", flush=True); continue
            raw.write_bytes(png); time.sleep(1)
        calls = None
        if i == 1 and cid in ETIQ:
            calls = [dict(CALL_POS[k], texto=ETIQ[cid][k]) for k in (0,1)]
        C.cartel([s["l1"], s["l2"], s["l3"]], str(raw), dest,
                 acento=2, callouts=calls, scene_is_path=True)
        print(f"  [{i}] ok", flush=True)
print("\nlisto", flush=True)
