---
name: calco-referencia
description: "Copia la edición de un vídeo de referencia (reel, anuncio, short) midiéndolo fotograma a fotograma, y la convierte en un estilo de Calco/Impulso Cut que se aplica a nuestros brutos. Mide en local la composición, los subtítulos (tipografía, píldora, colores, troceo, sincronía, animación), el motion y las transiciones, el b-roll, el sonido (música, SFX, niveles) y el ritmo. Luego unos agentes verifican cada medida contra los fotogramas y sale una especificación más un styleN. Úsala cuando Diego pase un vídeo y pida «edítalo igual que este», «analiza este vídeo frame a frame», «copia esta edición», «hazme un estilo como el de este reel» o «quiero que mis vídeos queden así». No sirve para cortar un bruto con un estilo que ya existe (eso es edicion-de-videos-ia) ni para sacar clips de un vídeo largo (clips-cortos-de-videos-largos)."
---

# Calco de referencia: medir un vídeo y convertirlo en estilo

La idea es copiar la edición de un vídeo de otro (cómo está montado) para aplicarla a nuestro contenido. Nada se estima a ojo si se puede medir: cada número de la especificación sale de un fotograma, una caja de OCR o una curva de audio, y dice de qué fichero sale.

## 0. Entrada

- Un fichero local o un enlace. Si es un enlace, `yt-dlp -f "bv*+ba/b" -o ref.mp4 <url>`.
- Si el vídeo viene a menos de 1080 px de ancho (las descargas de Instagram suelen venir a 360 o 720), se mide igual, pero todas las medidas se pasan a un lienzo de 1080x1920. Hay que avisar de que en tipografía y bordes finos el margen de error es mayor.
- Si es de otro creador, se copia la edición, no lo que es suyo: ni su música, ni su logo, ni sus marcas de agua, ni las capturas de sus b-roll.

## 1. Medir, en local y en unos 70 s por minuto de vídeo

```bash
python3 ~/.claude/skills/calco-referencia/scripts/analizar.py <video> ~/.claude/skills/calco-referencia/referencias/<id>
```

Deja en `referencias/<id>/`:

| fichero | qué es |
|---|---|
| `meta.json` | resolución, fps, duración |
| `frames/` | todos los fotogramas a 360 px (el n corresponde a t = (n-1)/fps) |
| `ocr_frames/` + `ocr.jsonl` | 10 fps a 1080 px, con el texto y su caja (Vision de macOS, binario `scripts/ocr`) |
| `subtitulos.json` | eventos de texto: entrada, salida, centro, alto en px@1920, colores (k-means) y desfase respecto a la voz |
| `cortes.json` | cortes duros y transiciones graduales (umbral adaptativo por MAD), plano medio y cortes por minuto |
| `movimiento.json` | por fotograma: cambio de histograma y de píxel, más la escala y el desplazamiento (ORB y afín) para ver zooms y paneos |
| `palabras.json` | transcripción palabra a palabra con whisper.cpp large-v3-turbo, en local |
| `audio.json` | golpes fuertes con bandas (sub/voz/aire), centroide, distancia al corte más cercano y RMS cada 50 ms |
| `layout.json` + `full/` | por plano: el fotograma central a resolución nativa, los rectángulos grandes (tarjetas) y el color de fondo arriba, abajo y en los bordes |
| `hojas/` | hoja de contacto a 1 fotograma por segundo y tiras de 6 fotogramas alrededor de cada corte |

El OCR también lee el texto que sale dentro del b-roll. Para quedarse solo con los subtítulos, se filtra por la franja vertical que se repite (la moda de `centro_y`) y por el color de fondo de la píldora.

## 2. Analizar por apartados y verificar (workflow)

Se lanza un agente por apartado, todos con los datos de arriba y ffmpeg, cv2 y librosa para medir más:

1. **Composición:** fondo, tarjetas (x, y, w, h, radio, sombra, barra de título), encuadre de la persona y línea temporal de layouts.
2. **Subtítulos:** familia y peso de la letra, altura de mayúscula, colores hex, padding y radio de la píldora, posición según el layout, palabras por bloque, reglas de troceo, sincronía con la voz y animación de entrada (fotograma a fotograma).
3. **Motion:** tipo, duración en fotogramas y curva de cada corte y transición, zooms y paneos, animaciones del b-roll. Cada efecto, como receta de keyframes.
4. **Sonido:** música (si hay, BPM y nivel respecto a la voz), ducking, cada SFX clasificado por espectro y atado a su evento visual.
5. **Ritmo:** estructura (gancho, desarrollo, CTA), corte de silencios, cada cuánto cambia algo y qué b-roll va con cada idea.
6. **Mapeo a Calco:** qué soporta ya el motor (`~/Documents/Claude/calco`), qué componentes hay que crear y el borrador del `styleN.json`.

Cada apartado pasa por un verificador que intenta refutar las medidas con su propio método. Si corrige un valor, manda el valor corregido. Después, un agente sintetiza `referencias/<id>/especificacion.md` y `referencias/<id>/styleN.json`.

El workflow de referencia, usado con el primer vídeo, está en `scripts/workflow-analisis.js`. Para otro vídeo se cambian `R` y `VIDEO`.

## 3. Construir el estilo en Calco

1. Se lee la sección 10 de la especificación: qué existe y qué falta.
2. Lo que falte (layouts, píldora, transiciones) se crea como componente nuevo de la plantilla, sin tocar las plantillas aprobadas (`diego`, style1 a style4).
3. Se registra el preset en `calco/presets.json` y `calco/data/presets.json`, y la ficha en `~/.claude/skills/edicion-de-videos-ia/styles/styleN.json`, con su fila en la tabla de esa skill.
4. Música y SFX salen de nuestra librería, eligiendo los que se parezcan al tipo y la duración medidos.

## 4. Comprobar que se parece de verdad

- Se renderiza un bruto nuestro con el estilo nuevo, a ser posible un vertical de Diego hablando a cámara.
- Se monta una comparación lado a lado: `scripts/comparar.py <referencia> <render> <salida>` saca pares de fotogramas del mismo tipo de momento (gancho, b-roll, subtítulo, final) y una tabla de medidas de referencia frente a render (alto de letra, colores, posición de la píldora, duración de bloque, plano medio y cortes por minuto).
- Cualquier diferencia de más de un 5 % en posición o tamaño, o de más de 8 de ΔE en color, se corrige antes de enseñarlo.
- Antes del render completo, se miran fotogramas sueltos con `remotion still`, como en edicion-de-videos-ia.
- A Diego se le enseña la comparación lado a lado, no solo el render.

## Trampas

- **Descargas de Instagram a 360x640:** las medidas de tipografía tienen un error de ±2 px@1920 y los colores de zonas pequeñas salen mezclados por la compresión. Hay que medir en zonas planas grandes de la píldora o del fondo.
- **Whisper en local:** marca el inicio de las palabras con unos 100-200 ms de error. La sincronía del subtítulo se da como mediana de muchos bloques, nunca a partir de uno solo.
- **Golpes de audio:** las consonantes oclusivas de la voz también salen como golpe. Un golpe solo cuenta como SFX si tiene mucho aire o mucho sub y además cae a ±80 ms de un evento visual.
- **ORB en planos con texto o pantallas:** la escala estimada se dispara con poca textura (`inl` bajo). Antes de dar un zoom por bueno, hay que verlo en los fotogramas.
- **Flujo de producción:** el render se sube al Cut (MCP `impulso-cut`), nunca al editor local. Nada se publica sin que Diego lo vea.
