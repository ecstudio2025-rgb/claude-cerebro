---
name: carrusel-gemini
description: "Genera carruseles de Instagram virales de punta a punta con la API de Gemini: el gancho de portada sale del Hook Vault de 4.550 ganchos etiquetados por psicología, Gemini escribe el copy slide a slide y las fotos, y la tipografía se compone en local con Montserrat. El carrusel entrega un lead magnet (PDF brandeado que también se fabrica aquí) y abre una acción de venta. Valida con la calculadora viral del Máster 5.0, monta los PNG a 1080x1350, pasa un control de calidad visual con Gemini y deja escritos el caption y el flujo de DM. Usar cuando Diego pida un carrusel con imágenes generadas, un carrusel con IA o con Gemini, un carrusel que capte leads, un carrusel con lead magnet, un carrusel que venda, un imán de leads en carrusel, hooks o ganchos de portada para carrusel, o el recurso descargable que acompaña a un carrusel. Para un carrusel de solo texto sin arte generado, usar carousel-ecsstudio."
---

> ## ⚠️ FILTRO ANTI-IA — OBLIGATORIO Y TOTAL
> Aplica a TODO lo que produzca esta skill: el copy de los slides, el lead magnet, el caption, los mensajes de DM Y TAMBIÉN el marco, la calculadora y mi propia narración al usarla. Checklist y antídotos: `/Users/diego/.claude/anti-patrones-ia-redaccion.md`.
>
> **Antes de entregar, relee y elimina si aparece:**
> - Negación retórica "no es X, es Y" / "no se trata de… sino de…" (el tell nº1; vigílalo en moralejas y remates).
> - Raya (—) decorativa: cuéntalas. Si hay más de una o dos en todo el texto, reescríbelas con coma, punto o paréntesis.
> - Cadenas de flecha `→` y `=` en prosa: dilo con palabras.
> - Tríadas mecánicas · doble adjetivo · léxico inflado (potenciar, clave, desbloquear, elevar, transformar) · calcos del inglés.
> - Título o caption con dos puntos + subtítulo · aperturas con halago o preámbulo · negritas y emojis en serie · frases todas del mismo largo.
> - Sobrecorrección: frase-remate corta como tic ("Punto.", "Ya está.") · auto-elogio del propio output · reutilizar el mismo esqueleto de una pieza a otra · concesiva de molde ("suena raro, pero…") · moraleja-aforismo de calendario.
>
> **Haz esto:** una postura que se moje · un dato concreto y verificable · ritmo irregular que nazca del contenido · alguna imperfección · cada carrusel con arquitectura propia.

# Carrusel Gemini — viral, con lead magnet y con venta

Carrusel de Instagram generado de punta a punta con la API de Gemini: **escribe el
copy, elige el gancho del Hook Vault y hace las fotos**. Lo único que no toca son
las letras dentro de la imagen. Cada ejecución deja siete cosas listas: guion,
slides PNG, lead magnet en PDF, caption, flujo de DM, oferta de venta y el JSON
para reeditarlo.

## Las dos decisiones que definen esta skill

**1. El gancho sale del Hook Vault, no de la cabeza del modelo.** Pedirle a
cualquier modelo "una portada sobre X" devuelve una portada que *describe* X:
correcta y muerta ("5 errores que hacen que tu Instagram no venda"). Con las 4.550
plantillas del vault delante, etiquetadas por disparador psicológico, el modelo
elige un mecanismo y lo rellena. Sale otra cosa: "el formato de vídeo que te trae
reservas sin publicar a diario". `guion.py` no deja escribir portadas sin pasar
por ahí.

**2. Gemini no escribe ni una letra dentro de las imágenes.** Se probó: pidiéndole
a `gemini-3-pro-image` una portada con "5 ERRORES QUE HACEN QUE TU INSTAGRAM NO
VENDA", devolvió **"5 ERFORES"**. En español falla lo bastante como para no jugarse
un carrusel de cliente. El reparto: Gemini hace la foto, `render.py` escribe
encima con Montserrat real. Y Gemini vuelve a entrar al final como revisor visual
de los slides montados.

## Cuándo NO usar esta skill

- Carrusel solo tipográfico, sin arte generado → `carousel-ecsstudio`.
- Guion de Reel o Trial Híbrido → `guiones-virales-master5`.
- Stories → `references/stories.md` de `guiones-virales-master5`.

---

## Inputs

Preguntar en **una sola pasada** lo que falte. Si está en el chat o en las
memorias, extraerlo y no preguntar.

| Input | Default | Campo del brief |
|---|---|---|
| Concepto / tema | — obligatorio | `tema` |
| Seguidor ideal (más ancho que el cliente) | Deducirlo del tema | `seguidor_ideal` |
| Deseo primitivo | Dinero | `deseo` |
| Lead magnet (qué se regala) | Proponer 2 según el tema; por defecto plantilla de un folio | `lead_magnet` |
| Keyword CTA | Sugerir 2-3 de la jerarquía ECSSTUDIO | `keyword` |
| Acción de venta | Sprint 360 con keyword SPRINT | `oferta` |
| Marca | Diego Álvarez / @thediegoalvarez | `marca` |
| Nº de slides | 8-9 | `slides` |

---

## Paso 1 — Calculadora viral

Leer `../guiones-virales-master5/references/calculadora-viralidad.md` y puntuar las
6 dimensiones (filtro 5, filtro 50, referencia viral, mercado SSDD, tendencia,
controversia). Multiplicador de carrusel: **×1.2**.

Enseñar la puntuación con los Sí/No explícitos **antes** de escribir nada.
Por debajo de 6, proponer 2-3 ajustes y esperar. No se monta un carrusel con la
base condenada.

## Paso 2 — Diseñar el lead magnet ANTES del guion

Leer `references/lead-magnet-y-venta.md`.

Decidir qué hueco va a dejar el carrusel abierto y cuál es el recurso que lo
rellena. Se hace ahora, no después: si se deja para el final, la portada acaba
prometiendo cosas que luego hay que fabricar.

## Paso 3 — Brief

Escribir `brief.json` (plantilla en `templates/brief.ejemplo.json`): tema,
seguidor ideal, deseo, lead magnet con su promesa, keyword, oferta, marca y
número de slides. Es lo que alimenta a Gemini en los dos pasos siguientes.

`objetivo` mapea la columna `goal` del vault: `Get Views` por defecto. `Get Sales`
solo tiene 6 ganchos en toda la base, así que `hooks.py` lo ignora si deja la
muestra en nada.

## Paso 4 — Ganchos del Hook Vault

```bash
cd ~/Documents/Claude/habilidades-virales/carrusel-gemini/scripts
python3 guion.py --brief brief.json --solo-ganchos --out carrusel.json
```

Devuelve **seis portadas**, cada una de una plantilla y una categoría psicológica
distintas, con su id del vault, el disparador y por qué encaja con este tema.
Se guardan en `carrusel.ganchos.json`.

**Enseñárselas a Diego y esperar a que elija.** Es el paso donde se decide si el
carrusel existe: el 80% del resultado está en esa portada.

Para trastear la base a mano: `python3 hooks.py --categorias` lista las 15
categorías con sus disparadores, y `--categorias 01,08 --objetivo "Get Views"
-n 10` saca muestra. Detalle de cada categoría en
`../guiones-virales-master5/references/hook-vault/README.md`.

Si ninguno convence, otra tirada cambia la muestra: `--categorias 03,04,10` o
subir `--banco 60`. No escribir la portada a mano salvo que Diego lo pida.

## Paso 5 — El carrusel entero

```bash
python3 guion.py --brief brief.json --hook 01-0203 --out carrusel.json
```

Gemini escribe los ocho slides con el gancho elegido, la arquitectura de
conversión, el tono ECSSTUDIO y el filtro anti-IA dentro del prompt, e incluye
los prompts de arte de cada slide. Valida el JSON y reintenta una vez si algo no
cuadra (acento partido, cuerpo pasado de palabras, keyword cambiada).

**Leerlo entero antes de montar.** Lo que hay que mirar con lupa:
- Que no se haya inventado un nicho y lo arrastre todo el carrusel (rompe el
  filtro 50). El prompt ya lo prohíbe, pero tiende a ello.
- Que los slides de contenido dejen el hueco que rellena el lead magnet.
- El filtro anti-IA, con el checklist delante.

Editar el JSON a mano lo que haga falta. Es un archivo de texto; el guion es de
Diego, no del modelo. Esquema completo en `references/sistema-visual.md`,
prompts de arte en `references/prompts-arte.md`.

## Paso 6 — Montar

```bash
cd ~/Documents/Claude/habilidades-virales/carrusel-gemini/scripts

python3 build.py carrusel.json --out ./salida --sin-arte   # borrador gratis
python3 build.py carrusel.json --out ./salida              # con arte de Gemini
python3 build.py carrusel.json --out ./salida --slide 5    # rehacer uno
```

Siempre `--sin-arte` primero para ver el reparto del texto. El arte se cachea por
prompt: rehacer el build no vuelve a pagar lo que no ha cambiado (1 s frente a
25 s por imagen). Cuatro imágenes rondan los 0,50 $.

## Paso 7 — Control de calidad

```bash
python3 qa.py ./salida
```

Gemini mira los slides montados y busca lo que el renderizador no puede saber:
letras coladas en el arte, contraste insuficiente, texto pisado, arte que
contradice al copy. Encontró bugs reales durante el desarrollo (el handle del pie
ilegible sobre las fotos claras salió de aquí), así que merece la pena pasarlo.

Ahora bien, tira a severo: marca "rehacer" en slides que se leen sin problema y
llama vacío al aire de un diseño editorial. Es un segundo par de ojos, no un
juez. Mirar el PNG y decidir. Lo que sí es siempre real: `texto_en_arte` y
`texto_cortado`. Devuelve el comando exacto para rehacer los slides flojos.

## Paso 8 — Lead magnet

```bash
python3 leadmagnet.py leadmagnet.json --out ./salida/recurso.pdf --portada-art
```

PDF A4 brandeado: portada con foto, intro, secciones numeradas con checklist y
bloque de cierre negro con la acción de venta dentro. Plantilla en
`templates/leadmagnet.ejemplo.json`.

## Paso 9 — Caption, DM y venta

Del caption: dos frases y la keyword. Nada de párrafos.

El flujo de DM (tres mensajes: entrega, pregunta abierta, puente) y las tres
temperaturas de la acción de venta están en `references/lead-magnet-y-venta.md`.

## Paso 10 — Entrega

Enseñar los PNG y el PDF al usuario, en orden, con el caption y el flujo de DM
debajo. Decir qué queda pendiente de su lado (cablear la keyword en ManyChat,
subir el PDF donde lo sirva el bot).

---

## Clave de la API

Vive en `~/.config/ecsstudio/gemini.env`, fuera de esta carpeta a propósito:
`Documents/Claude` se comparte y sincroniza. Los scripts la leen de ahí o de la
variable `GEMINI_API_KEY`. Nunca meter la clave en el JSON ni en la skill.

## Modelos

| Uso | Modelo | Dónde |
|---|---|---|
| Ganchos y copy | `gemini-3.1-pro-preview` | `guion.py` |
| Arte | `gemini-3-pro-image` (Nano Banana Pro) | `build.py`, `leadmagnet.py` |
| Arte barato | `gemini-3.1-flash-image` con `--rapido` | `build.py` |
| QA visual | `gemini-3.1-pro-preview` | `qa.py` |

## El flujo entero, seguido

```bash
cd ~/Documents/Claude/habilidades-virales/carrusel-gemini/scripts
python3 guion.py --brief brief.json --solo-ganchos --out carrusel.json  # 6 portadas
python3 guion.py --brief brief.json --hook 01-0203 --out carrusel.json  # el copy
python3 build.py carrusel.json --out ./salida --sin-arte                # borrador
python3 build.py carrusel.json --out ./salida                           # con fotos
python3 qa.py ./salida
python3 leadmagnet.py leadmagnet.json --out ./salida/recurso.pdf --portada-art
```

Dos paradas obligatorias con Diego: **después de los ganchos** (elige él) y
**después del copy** (se lee entero antes de gastar en imágenes).

## Referencias

| Archivo | Cuándo |
|---|---|
| `references/arquitectura-conversion.md` | Paso 5 — reparto de slides, transiciones, regla del hueco |
| `references/lead-magnet-y-venta.md` | Pasos 2 y 9 — qué regalar, keyword, DM, oferta |
| `references/sistema-visual.md` | Paso 5 — layouts, esquema JSON, topes de texto |
| `references/prompts-arte.md` | Paso 5 — cómo pedirle el arte a Gemini y qué cuesta |
| `../guiones-virales-master5/references/calculadora-viralidad.md` | Paso 1 |
| `../guiones-virales-master5/references/hook-vault/README.md` | Paso 4 — las 15 categorías y cuándo tirar de cada una |
| `../guiones-virales-master5/references/hook-vault/guia-ctas.md` | Paso 9 — las 8 fórmulas de CTA |
| `../guiones-virales-master5/references/30-ganchos.md` | Paso 4 solo si se escribe la portada a mano |

## Dependencias

Python 3 con Pillow y reportlab (ya instalados), Montserrat en `~/Library/Fonts`
(instalado), la clave de Gemini y el Hook Vault de la skill hermana
`guiones-virales-master5` (`hooks.py` lo lee de ahí, no lo duplica: si se mueve
esa carpeta, esta skill se queda sin ganchos). Sin navegador, sin Playwright,
sin npm.

## Plantillas

| Archivo | Qué es |
|---|---|
| `templates/brief.ejemplo.json` | El encargo que come `guion.py` |
| `templates/carrusel.ejemplo.json` | Un carrusel real generado con el gancho 01-0203 |
| `templates/leadmagnet.ejemplo.json` | La plantilla de los 5 filtros, en PDF |
