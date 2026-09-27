---
name: clips cortos de videos largos
description: "Saca clips verticales 9:16 con hook quemado de una grabación larga (masterclass, webinar, directo, podcast, entrevista, VSL). Cada clip es una idea entera: entra con gancho y sale con la idea rematada, nunca a media frase. Úsala cuando Diego pida sacar clips/cortes/reels de un vídeo largo o de un directo, trocear una masterclass, hacer piezas para Instagram o TikTok de una grabación de Zoom, o cuando diga 'sácame todos los clips que puedas de esto'. Trigger: clips de un vídeo largo, trocear masterclass, cortes del directo, reels del webinar."
---

# Clips cortos de vídeos largos

## Lo que decide si el clip sirve

1. **Duración mínima**: la que pida Diego. Si no dice nada, 45 s. Un clip de 20 s
   se lee como un recorte suelto; a partir de 45 s ya cabe una idea con desarrollo.
2. **Una idea por clip, con arco**: gancho → desarrollo → remate. Se elige el rango
   por el arco, no por la frase suelta que suena bien.
3. **Bordes limpios**: nunca arrancar ni cerrar a media palabra, y no dejar colgando
   un «¿vale? Ok» ni un «o sea…» al final.
4. **Sin duplicados**: si el tema aparece en dos grabaciones, va la versión que mejor
   se explica. Dos clips casi iguales queman el feed.

## Pipeline

```bash
# 0. transcribir en local (nunca por API)
#    whisper.cpp: /opt/homebrew/bin/whisper-cli -m ggml-small.bin -f audio.wav -l es -oj
#    para tiempos por palabra: faster-whisper large-v3 int8 (ojo, se come la RAM)

# 1. silencios + bloques de lectura + aviso de bucle de whisper
python3 scripts/preparar.py src/v1.mp4 v1

# 2. leer transcripts/v1_bloques.txt entero y elegir los rangos

# 3. ver qué hay en pantalla en cada momento elegido, para el montaje
python3 scripts/contactsheet.py src/v1.mp4 174 312 405 ...   # y Read /tmp/cs/sheet.jpg

# 4. escribir spec_v1.json (ver formato abajo) y ajustar bordes al silencio
python3 scripts/prep.py spec_v1.json 45     # imprime cómo entra y cómo sale cada clip

# 5. renderizar
python3 scripts/render.py spec_v1.json

# 6. verificar: re-transcribe cada clip ya montado y enseña entrada y salida
python3 scripts/verify.py

# 7. rehacer los que corten mal: sub-spec con solo esos clips y volver al paso 5
```

### Formato del spec

```json
{
 "src": "/ruta/v1.mp4",
 "sil": "/ruta/audio/sil_v1.json",
 "tr":  "/ruta/transcripts/v1.json",
 "out": "/ruta/clips",
 "color": "0xFA9600",
 "handle": "@klapptalles",
 "crop_slide": "crop=960:540:0:90",
 "crop_cara":  "crop=320:180:960:270",
 "clips": [
  {"id":"ak01","tag":"Su historia","hook":"Me fui a Berlín sin saber alemán",
   "layout":"dual","ranges":[[143.8,201.2]]}
 ]
}
```

`ranges` admite varios trozos: se concatenan en orden, sirve para saltarse una
interrupción en mitad de una explicación buena.

### Montajes

- **dual** — cara arriba, diapositiva debajo. El de por defecto en webinars.
- **slide** — solo la diapo, para tablas y ejemplos escritos.
- **cara** — solo la webcam, cuando la diapo no aporta.

### El hook

Va quemado pegado justo encima del vídeo: tag en color de marca, regla de 150 px,
titular en Montserrat Black. **Máximo 20 caracteres por línea**, 2 líneas en `dual`
y 3 en los otros. Un hook de más de 40 caracteres se parte mal en dual: cuéntalos
antes. El handle va abajo, en gris.

## Trampas (todas pisadas ya)

- **Whisper se queda en bucle al final de los ficheros largos.** En la masterclass
  de 95 min repitió «si un día no se puede hacer un orden» 900 veces desde el minuto
  77. `preparar.py` imprime el último bloque para que lo veas. La parte útil acaba
  donde empieza el bucle.
- **Los tiempos de segmento de whisper bailan hasta un segundo.** Para cortar manda
  `silencedetect`, no el transcript. Por eso `prep.py` ajusta cada borde al silencio
  más cercano.
- **Bruto ≠ neto.** El render quita los silencios de más de 0,7 s, así que un rango
  de 80 s acaba en unos 70 s de vídeo. Para clips de 45 s corta rangos de 55 s como
  mínimo. `prep.py` ya te da el neto estimado y marca los cortos.
- **Verificar SIEMPRE re-transcribiendo el clip montado.** En la última tanda, 9 de
  28 cortaban a media frase pese a tener el borde ajustado al silencio. Uno acababa
  literalmente en «hasta que todo se».
- **Comprobar la geometría del PIP con un frame** antes de dar por buenos los recortes.
  Cambia entre grabaciones aunque sean del mismo Zoom.
- **zsh no separa en palabras las variables sin comillas**: `for w in "a 1 2"; do cmd $w`
  pasa todo como un argumento. Haz los bucles en Python.
- **El cwd del Bash se reinicia entre llamadas.** Rutas absolutas o `cd` en la misma
  línea, o parecerá que se han borrado los clips.
- **Espacio en disco**: cada clip de 60-90 s pesa unos 8 MB, y las fuentes 200 MB cada
  una. Antes de una tanda de 30, mira `df -h`.

## Entregable

Además de los mp4, un `CLIPS.md` en la carpeta del proyecto con:

- tabla: id, origen, minuto original, duración, montaje, tema y hook
- orden sugerido de publicación (dolor primero, didácticos después, historia y prueba al final)
- una descripción de Instagram por clip, en primera persona de quien habla, con
  palabra clave al final para el DM automático

Las descripciones pasan por `anti-patrones-ia-redaccion.md` sí o sí: nada de
«no es X, es Y», ni rayas decorativas, ni tríadas.
