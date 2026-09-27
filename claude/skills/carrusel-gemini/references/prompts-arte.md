# Cómo se le pide el arte a Gemini

## La regla que ordena todo lo demás

**Gemini no escribe ni una letra.** El arte va sin tipografía y el texto lo pone
después `render.py` con Montserrat de verdad.

Esto no es una preferencia estética, es un fallo medido. Pidiéndole a
`gemini-3-pro-image` una portada con el texto "5 ERRORES QUE HACEN QUE TU
INSTAGRAM NO VENDA", devolvió **"5 ERFORES"**, con la erre convertida en efe y
minúsculas coladas dentro de una palabra en mayúsculas. En inglés falla menos; en
español, con tildes y con eñes, falla lo suficiente como para no arriesgar un
carrusel de cliente.

`gemini.py` añade la prohibición de texto a todos los prompts automáticamente
(`REGLA_SIN_TEXTO`). Aun así, en el prompt no describas rótulos, carteles,
pantallas con interfaz ni libros abiertos con texto: el modelo intenta escribir
lo que ve implícito. `qa.py` revisa después si se ha colado alguna letra.

## Qué pedir

Un objeto o una escena, no un concepto. Los conceptos ("el éxito", "la
productividad") devuelven stock corporativo con flechas azules.

| En vez de | Pide |
|---|---|
| "el problema de no vender" | "un móvil apagado boca abajo sobre una mesa de despacho, junto a un café frío a medias" |
| "planificación de contenido" | "una hoja de cuaderno cuadriculado con una línea ascendente dibujada a boli rojo, luz rasante" |
| "nuestro servicio" | "mesa de montaje de vídeo de lado en penumbra, monitores apagados reflejando la ventana" |

Un prompt que funciona lleva: **objeto concreto + superficie + luz + plano**.
La luz es lo que separa la foto de marca del stock: "luz lateral dura de ventana,
sombra larga cruzando la mesa" hace más por la pieza que tres adjetivos.

## El acento rojo

El `#b03035` entra por un objeto físico, no por un filtro: un boli, un cable, un
marcapáginas, una silla. Así el arte pertenece a la marca sin parecer teñido.
Basta con uno por imagen; dos ya es una imagen roja.

## Coherencia de serie

`build.py` usa el arte del **primer slide con imagen** como ancla de estilo y lo
pasa como referencia visual al resto. Por eso todas las fotos de un carrusel
parecen del mismo día de rodaje.

Consecuencia práctica: si cambias el prompt del slide 1, cambia el ancla y con
ella toda la serie. Si solo quieres tocar el slide 5, toca el 5.

## El estilo base

Vive en `ESTILO_BASE`, dentro de `build.py`, y se concatena a cada prompt. Para
un cliente que no sea ECSSTUDIO, no toques el script: pon `estilo_arte` en el
JSON del carrusel y sustituye la paleta entera.

## Coste y caché

Nano Banana Pro (`gemini-3-pro-image`) a 2K ronda los 0,12-0,15 $ por imagen. Un
carrusel con cuatro imágenes son unos 0,50 $.

El arte se cachea por firma (modelo + aspecto + tamaño + prompt + ancla). Repetir
el build no vuelve a pagar lo que no ha cambiado: un rebuild completo sin tocar
prompts tarda menos de un segundo. Cambia una coma del prompt y ese slide se
regenera.

- `--sin-arte`: monta los slides sobre fondo plano, gratis, para revisar el copy
  y el reparto antes de gastar. **Empieza siempre por aquí.**
- `--rapido`: usa `gemini-3.1-flash-image`, más barato y menos fino.
- `--slide N`: rehace uno solo.

## Cuando el arte sale mal

No pelees con el mismo prompt tres veces. Cambia el objeto. Si pediste "una mesa
con un móvil" y sale un anuncio de operador, pide "el reflejo de una ventana en
la pantalla apagada de un móvil". El modelo obedece mejor a lo raro y concreto
que a lo genérico repetido con más adjetivos.
