---
name: carousel-centrado-ecsstudio
description: "Crea carruseles de Instagram para ECSSTUDIO / @thediegoalvarez con diseno centrado y stickers emoji. Fondo blanco, Montserrat 900, acento rojo #b03035, todo centrado, emoji sticker representativo en cada slide, DIEGO ALVAREZ en header, DESLIZA en footer. Output: HTML navegable + PNGs a 1080px listos para subir. Activar cuando Diego pida un carrusel centrado, carousel con stickers, diseno blanco con emojis, o el estilo de carrusel con numeros grandes y stickers. Tambien activar cuando pida regenerar o ajustar slides del estilo blanco centrado que ya hemos hecho."
---

# Carrusel Centrado ECSSTUDIO

Sistema de diseño para carruseles Instagram con fondo blanco, contenido centrado y stickers emoji representativos. Es el formato visual establecido en producción para @thediegoalvarez.

**Output por ejecución:**
1. HTML navegable con todos los slides
2. PNGs a 1080px de ancho listos para publicar

---

## Tokens de diseño (no cambiar)

```
Fondo:          #ffffff
Negro:          #0d0d0d
Rojo acento:    #b03035
Gris cuerpo:    #555555
Gris muted:     #aaaaaa
Gris línea:     #e0e0e0

Fuente:         Montserrat (Google Fonts) — weights 400, 700, 900
Frame:          420px × 540px
Escala PNG:     1080 / 420 = 2.571×
Padding lados:  24-28px

Header:         DIEGO ÁLVAREZ (izquierda, 900, 10px) + numeración (derecha, #bbb)
Footer izq:     punto rojo 9px + @thediegoalvarez (10px, #aaa, 700)
Footer der:     píldora negra "DESLIZA →" (excepto último slide)
```

---

## Tipos de slide disponibles

| Tipo | Cuándo usar |
|---|---|
| `portada_numero` | Hook con cifra grande como ancla visual (ej: 50K, 3X, 90%) |
| `portada_texto` | Hook con texto impactante en 2-3 líneas, última en rojo |
| `step` | Slide de contenido con sticker + label + título + cuerpo |
| `moraleja` | Penúltimo slide de conclusión/insight, título con acento rojo |
| `cta` | Último slide: COMENTA + KEYWORD en rojo grande + Y TE MANDO EL DOCUMENTO |

---

## Asignación de stickers

Usar siempre un emoji que represente el contenido del slide, no decorativo:

| Contenido | Sticker |
|---|---|
| Captación / Instagram / canal | 📲 |
| Vídeo / grabación / frame | 🎬 |
| Comentarios / keyword / conversación | 💬 |
| Secuencias / stories / flujo | 🔁 |
| Energía / alcance / impacto | ⚡ |
| Automatización / bot / ManyChat | 🤖 |
| Señal / alcance masivo / Trial | 📡 |
| Resultado / reserva / objetivo | 🎯 |
| Insight / aprendizaje / clave | 💡 |
| Advertencia / error / problema | ⚠️ |
| Embudo / recorrido | 🔽 |
| CTA / conversación | 💬 o 🔍 |
| Calendario / semana tipo | 📅 |
| Portada general negocio | 📲 |

---

## Proceso paso a paso

### PASO 1 — Definir el contenido

Antes de escribir código, tener claro:
- **Hook de portada:** cifra grande (portada_numero) o texto impactante (portada_texto)
- **Número de slides de contenido:** 3-6 (uno por punto, concepto o paso)
- **Tipo de cada slide:** step / moraleja
- **Keyword del CTA:** SPRINT, EMBUDO, GUION, DIAGNÓSTICO, CONTROL...
- **Copy de cada slide:** máx 3 líneas de cuerpo. Frases cortas. Sin explicaciones largas.

**Regla de copy para carrusel:**
- Título: 2-4 palabras. Impacto máximo.
- Cuerpo: máx 3 líneas de 35-40 chars. No más.
- Si hay duda, menos texto siempre.

### PASO 2 — Generar el HTML

Leer: `references/design-system.md`

Usar el boilerplate completo y las funciones de slide.
Guardar en: `/mnt/user-data/outputs/carousel_[tema].html`

### PASO 3 — Exportar PNGs

Leer: `references/playwright-export.md`

Guardar en: `/mnt/user-data/outputs/carousel_[tema]_slides/`

Presentar todos los archivos con `present_files`.

---

## Reglas de diseño (no negociables)

**SIEMPRE centrado:**
- Sticker emoji
- Label en rojo (PASO 01, EL PROBLEMA, LA CLAVE...)
- Título principal
- Texto de cuerpo
- Todo el contenido de portada y CTA

**SIEMPRE a la izquierda:**
- Nada. En este formato todo va centrado.

**Jerarquía visual por slide:**
1. Sticker — primera cosa que el ojo ve
2. Label en rojo pequeño — contexta
3. Título en negro grande — el mensaje
4. Separador fino — respiro visual
5. Cuerpo en gris — el detalle

**Portada con número grande:**
- El número ocupa el 60-70% del ancho del frame
- Siempre en rojo #b03035
- La frase contexto arriba en muted (10-12px, gris)
- "AL MES.", "MÍNIMO.", "EN 90 DÍAS." debajo en negro/gris

**CTA slide:**
- Sin numeración en header
- "COMENTA" en negro, ~26px
- KEYWORD en rojo, entre 58px (11+ chars) y 80px (5-7 chars)
- "Y TE MANDO EL DOCUMENTO." en negro, ~22px
- Sin DESLIZA → en footer

---

## Referencias

| Archivo | Cuándo leerlo |
|---|---|
| `references/design-system.md` | SIEMPRE — contiene el CSS completo, las funciones de slide y el boilerplate HTML |
| `references/playwright-export.md` | Para exportar PNGs — script Python completo |
