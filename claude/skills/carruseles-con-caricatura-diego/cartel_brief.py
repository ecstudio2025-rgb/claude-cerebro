import compose as C, pathlib, time
out = pathlib.Path("/Users/diego/Documents/Claude/carruseles-virales-master5/CARTEL-BRIEF")
(out/".e").mkdir(parents=True, exist_ok=True)

BASE = ("CARTEL VERTICAL 4:5 cinematografico, composicion frontal centrada. "
        "PROTAGONISTA: el MISMO personaje de la imagen de referencia (misma cara, gorra "
        "beige lisa sin texto, perilla fina, aros, piercing en la nariz, collar de "
        "cuentas, camisa negra con ribete rojo), de cuerpo medio, centrado en primer "
        "plano, mas iluminado que el resto. {pose} "
        "PALETA: negro #141414 y grises dominantes, unico acento rojo carmin #b03035 "
        "en el contraluz. Luz cinematografica dura, humo suave, mucha profundidad. "
        "COMPOSICION: la MITAD INFERIOR queda oscura y despejada para el titulo. "
        "Sin texto, sin letras, sin numeros, sin logotipos, sin carteles escritos. "
        "FONDO: {fondo}")

SLIDES = [
 {"lineas":["\"Que me lleven","las redes\" es","TIRAR EL DINERO"], "acento":2,
  "pose":"brazos cruzados, expresion seria y esceptica.",
  "fondo":"una fila simetrica de figuras anonimas sin rostro con traje, tres a cada lado, en formacion; billetes cayendo al suelo entre ellas.",
  "callouts":[{"texto":"No pregunta","cx":0.17,"cy":0.20,"ax":0.13,"ay":0.42},
              {"texto":"No mide","cx":0.83,"cy":0.20,"ax":0.87,"ay":0.42}]},
 {"lineas":["Salvo que te","pregunten esto","ANTES DE FIRMAR"], "acento":2,
  "pose":"levantando el dedo indice avisando, gesto de alto.",
  "fondo":"una gran mesa de reuniones oscura con un contrato de papel en el centro y una pluma, ambiente de despacho."},
 {"lineas":["Cuánto vale","para ti","UN CLIENTE NUEVO"], "acento":2,
  "pose":"frotando los dedos como quien cuenta dinero, mirada directa.",
  "fondo":"una figura de cliente iluminada con una etiqueta de precio colgando, y detras una caja registradora abierta."},
 {"lineas":["Qué te preguntan","justo antes","DE COMPRAR"], "acento":2,
  "pose":"inclinado escuchando con la mano en la oreja.",
  "fondo":"un mostrador con una clienta gesticulando al otro lado y grandes bocadillos de dialogo vacios flotando."},
 {"lineas":["Y qué te dijo","el último que se fue","SIN COMPRAR"], "acento":2,
  "pose":"mirando de lado con gesto de resignacion.",
  "fondo":"una puerta abierta por la que se marcha una figura de espaldas, dejando un producto abandonado en el mostrador."},
 {"lineas":["Sin esas respuestas:","contenido bonito","Y FACTURAS PUNTUALES"], "acento":2,
  "pose":"señalando a un lado con desgana.",
  "fondo":"un escaparate impecable y decorado sin ningun cliente, y al lado un cajon rebosante de facturas."},
 {"lineas":["No harán contenido","que lo venda.","LO DECORAN"], "acento":2,
  "pose":"brazos cruzados, expresion firme de veredicto.",
  "fondo":"dos locales enfrentados: uno lleno de adornos y vacio de gente, otro sobrio y con cola de clientes en la puerta."},
 {"lineas":["Las 9 preguntas","que hago antes","COMENTA BRIEF"], "acento":2,
  "pose":"señalando a camara con media sonrisa de complicidad.",
  "fondo":"un tablero de oficina con nueve fichas de papel en blanco alineadas y bien iluminadas."},
]

for i, s in enumerate(SLIDES, 1):
    raw = out/".e"/f"s{i:02d}.png"
    if not raw.exists():
        png = C.gemini(BASE.format(pose=s["pose"], fondo=s["fondo"]))
        if png is None:
            print(f"[{i}] FALLO"); continue
        raw.write_bytes(png); time.sleep(1)
    C.cartel(s["lineas"], str(raw), out/f"slide-{i:02d}.png",
             acento=s["acento"], callouts=s.get("callouts"), scene_is_path=True)
    print(f"[{i}] slide-{i:02d}.png", flush=True)
print("listo")
