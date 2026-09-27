# Sistema visual y esquema del JSON

Lienzo **1080 × 1350** (4:5). Es el formato con más altura que permite Instagram
en el feed: ocupa más pantalla que el cuadrado y se lee mejor.

## Marca (por defecto ECSSTUDIO / @thediegoalvarez)

| Token | Valor |
|---|---|
| Fondo | `#ffffff` (el layout `entrega` usa `#f4f2ef`, el `venta` va en negro) |
| Texto | `#111111` |
| Acento | `#b03035` |
| Cuerpo | `#3a3a3a` |
| Titulares | Montserrat Black, mayúsculas, interlineado 1.0-1.02 |
| Cuerpo | Montserrat Medium, interlineado 1.45 |
| Márgenes | 84 px |

Las fuentes se leen de `~/Library/Fonts`. Todos los tamaños se autoajustan: el
texto largo baja de cuerpo hasta caber, nunca se sale ni se corta. Si un titular
sale minúsculo, el problema es el copy, no el renderizador: acórtalo.

Sobre fondo oscuro (`portada_full`, `venta`) el acento cambia a `#ff5a5f`
automáticamente. El `#b03035` sobre negro no tiene contraste suficiente.

## Layouts

| Layout | Campos | Notas |
|---|---|---|
| `portada` | `hook` (lista de líneas o texto), `acento`, `art` | Hook sobre blanco, foto a sangre en la banda inferior (46%). Sin numeración ni pie. |
| `portada_full` | igual | Foto a sangre con degradado y hook blanco abajo. Para temas con más carga emocional. |
| `contexto` | `label`, `titulo`, `cuerpo`, `art` | Label rojo pequeño con tracking. |
| `contenido` | `numero`, `titulo`, `cuerpo`, `art` | Número rojo grande. Con `art`, banda inferior del 30%. |
| `entrega` | `label`, `titulo`, `cuerpo`, `art` | Fondo hueso, mockup centrado con sombra. El `art` es el recurso. |
| `cta` | `keyword`, `pre`, `post` | Keyword en rojo al tamaño máximo. |
| `venta` | `label`, `titulo`, `cuerpo`, `boton`, `art` | Fondo negro o foto muy velada. |

`acento` funciona en `portada`, `contexto`, `contenido`, `entrega` y `venta`: es
el fragmento de texto que se pinta en rojo. Tiene que estar **contenido literal**
en una línea del titular; si el ajuste automático parte esa línea en dos, el
acento no se pinta. Palabras cortas y del final funcionan mejor.

## Esquema

```json
{
  "marca": {"nombre": "Diego Álvarez", "handle": "@thediegoalvarez",
            "rojo": "#b03035", "negro": "#111111", "fondo": "#ffffff"},
  "keyword": "GUION",
  "estilo_arte": "(opcional) sustituye el estilo base para otro cliente",
  "slides": [
    {"layout": "portada", "hook": ["LÍNEA 1", "LÍNEA 2"], "acento": "LÍNEA 2",
     "art": "prompt de la foto, sin texto"},
    {"layout": "contexto", "label": "El problema", "titulo": "...", "cuerpo": "..."},
    {"layout": "contenido", "numero": "01", "titulo": "...", "cuerpo": "..."},
    {"layout": "entrega", "label": "Lo que te llevas", "titulo": "...",
     "cuerpo": "...", "art": "mockup del recurso"},
    {"layout": "cta", "keyword": "GUION", "pre": "Comenta",
     "post": "y te mando la plantilla por privado"},
    {"layout": "venta", "label": "...", "titulo": "...", "cuerpo": "...",
     "boton": "Escríbeme SPRINT", "art": "..."}
  ]
}
```

En `hook`, la lista fuerza el corte de línea exacto (así se controla dónde cae la
palabra roja). Un string suelto lo parte el renderizador.

## Cuánto texto cabe

| Sitio | Tope real |
|---|---|
| Hook de portada | 3 líneas, 4-6 palabras por línea |
| Título de contenido | 5-6 palabras |
| Cuerpo | 45-55 palabras; a partir de ahí baja de cuerpo y se lee mal en el móvil |
| Post del CTA | 6-8 palabras |

## Chrome

Cabecera: nombre a la izquierda con tracking, `0X / 0Y` a la derecha (la portada
no lleva numeración). Pie: punto rojo + handle a la izquierda, píldora negra
`DESLIZA →` a la derecha, que desaparece en el último slide.

En los layouts con banda de foto, la banda corta 140 px antes del borde inferior
para que el pie caiga siempre sobre blanco. Sin eso, el handle se volvía ilegible
sobre las fotos claras.
