---
name: anuncios-motion-3d
description: Crea anuncios de vídeo vertical 9:16 en motion graphics 3D (Three.js + GSAP) con render fotograma a fotograma, locución ElevenLabs (mujer y hombre), música ElevenLabs encajada al beat, efectos de sonido sintetizados y la caricatura de Diego como personaje. Es el sistema con el que se hicieron los 21 anuncios de Custom Soft Lab (sep-2026). Úsala cuando Diego pida «anuncios con motion», «vídeos 3D como los de Custom Soft Lab», «una tanda nueva de anuncios de vídeo», «reels animados sin grabar», o anuncios en vídeo para cualquier marca sin rodaje.
---

# Anuncios motion 3D (sistema Custom Soft Lab)

El motor vive en `~/Claude/deliverables/anuncio-motion-csl/`. **No lo copies ni lo reescribas: trabaja dentro de esa carpeta** y reutiliza sus piezas. Salida por defecto en `~/Downloads/Anuncio-Custom-Soft-Lab/` (cámbiala en `hacer.sh` si es otra marca).

Cada anuncio sale en tres versiones de 1080×1920: `NN-slug-DURs-vertical-sin-voz.mp4`, `…-voz-mujer.mp4` y `…-voz-hombre.mp4`.

## Piezas

| Fichero | Qué hace |
|---|---|
| `motor3d.js` | Escena Three.js de estudio: `mundo()`, `actor()` (caricatura con boca a la voz y poses), `movil()`, `tablet()`, `portatil()`, `panel()`, `montar(tl, W, actores, dur)` que expone `window.seek` |
| `kit3d.js` | Piezas encima del motor: `lienzo()` (textura canvas 2D), `losa()`, `plano()`, `brillo()`, `chispas()`, `ayudas(tl, C)` → `{up, cam, tit, sal, golpe, pop, flash}`, `ctaHTML()` + `ctaAnim()`, `ui()` (pantallas de programa con marca de ejemplo), `logoCSL()` |
| `comun.js` | Texto por líneas con máscara (`.ln>span`), grano |
| `cNN-slug.html` | Un anuncio = un HTML: CSS + textos `.T` + escena + `gsap.timeline({paused:true})` + `window.SFX` + `montar(...)`. Plantilla de referencia: `c09-30dias.html` |
| `voz/pNN/guion.tsv` | Guion: `inicio⇥fin⇥frase` por línea (segundos) |
| `el_tts.py` / `el_locucion.py` | ElevenLabs TTS por frase (con contexto anterior/siguiente), recorte de silencios, `tempo` para que quepa en su hueco (máx. 1,15), `plan-<voz>.txt` y `env-<voz>.js` (amplitud para la boca) |
| `musica_generar.py` | Música con ElevenLabs Music (`/v1/music`, instrumental, sin intro); prompts por anuncio en el dict `P` |
| `musica_el.py` + `beats.py` | Recorta la pista para que un beat caiga en el golpe visual clave; la alarga en bloques de 16 beats si se apaga |
| `sfx2.py` | Sintetiza los efectos de `window.SFX = [[t, 'tipo', ganancia?], …]` (tick, whoosh, swoosh, impact, hit, ding, riser, thud, cash, stamp, paper, scribble, boing, rev, sub…; mira el fichero para la lista completa) |
| `render.py` | Playwright hace `seek` fotograma a fotograma (30 fps) y lo pasa por pipe a ffmpeg (x264 CRF 17) |
| `mezcla.py` | Voz con ducking sobre música + SFX, loudnorm |
| `hacer.sh` | Todo el anuncio de una vez: `./hacer.sh c09-30dias p09 15 09-treinta-dias-15s` |
| `prev.sh` / `frames.py` | Lámina de 9 fotogramas para revisar antes de renderizar |
| `verificar.py` / `sync.py` | Whisper: comprueba que cada frase se entiende y que la mezcla final va sincronizada con el guion |
| `personaje/` + `personaje.py` | Hoja de la caricatura de Diego (Gemini, fondo verde recortado a PNG por pose) |

## Flujo para un anuncio nuevo

1. **Idea y guion.** Una metáfora visual por anuncio: torre, llaves, dominó, taxímetro, plano… Mira los 21 que ya existen para no repetir. El gancho sale de `~/.claude/hook-vault/` y el texto se pasa por `anti-patrones-ia-redaccion.md`. Escribe `voz/pNN/guion.tsv` con frases cortas y huecos realistas (unas 2,5 palabras por segundo).
2. **Afirmaciones.** Solo lo que la web y el contrato digan de verdad: plazo, garantía, «el código es tuyo» solo si la cesión está firmada. Nada de precios sin el OK de Diego y nada de marcas reales en las pantallas: usa marcas de ejemplo.
3. **Voces.** Arranca un servidor desde la carpeta: `python3 -m http.server 8792 &`. Después lanza `python3 el_locucion.py voz/pNN DUR mujer` y lo mismo con `hombre`; las voces son `RgXx32WYOGrd7gFNifSf` (mujer) y `43h7ymOnaaYdWr3dRbsS` (hombre). Si sale «¡LARGO!», acorta la frase en lugar de acelerarla. Luego `python3 verificar.py voz/pNN mujer`. `voces.sh` hace la tanda entera y te dice cuántos caracteres gasta.
4. **Música.** Añade el prompt a `P` en `musica_generar.py` y ejecútalo. Después `python3 musica_el.py musica-el/pNN.mp3 DUR GOLPE musica-cNN.wav`, donde GOLPE es el segundo del impacto visual principal.
5. **Escena.** Copia la estructura de `c09-30dias.html`:
   - textos `.T` con `.ln>span`;
   - `mundo({...})`, objetos con `losa`, `lienzo` y `plano`, y `actor(W, { env: window.ENV, poses: [[t, 'hablar'|'pulgar'|'sorprendido'|'senala-der'…]] })`;
   - timeline con `cam()`, `tit()` y `sal()`, sincronizado con los tiempos del guion;
   - cada golpe visual lleva su SFX en `S`, y el anuncio cierra con `ctaHTML` + `ctaAnim`.
6. **Revisión antes de renderizar.** `./prev.sh cNN-slug "0,1.5,3,…"`, y abre la lámina que queda en el scratchpad. Comprueba que el texto no se sale, que nada queda tapado por la caricatura, que no se ven cortes y que el CTA se lee.
7. **Render final.** `./hacer.sh cNN-slug pNN DUR NN-slug-DURs`. Lo imprime: resolución 1080x1920, códec aac, duración, loudness integrado (unos −15 LUFS) y pico por debajo de −1 dBTP.
8. **Comprobación.** Ejecuta `python3 sync.py <salida-voz-mujer.mp4> voz/pNN`, mira 3 o 4 fotogramas del mp4 final y termina con `pkill -f "http.server 8792"`.

## Trampas conocidas

- **Disco:** cada render tira de GB en temporales. `esperar_disco.sh` para si quedan menos de 1,5 GB libres. Borra los `v-*.mp4` y `r-*.log` que sobren.
- **Render determinista:** nada de `Date.now()` ni `Math.random()` sin semilla en el HTML. Todo tiene que depender de `t`, porque `render.py` salta a cada fotograma.
- **Texturas:** `montar` espera a que carguen. Si una pantalla sale negra, la imagen no estaba servida (revisa BASEURL y el puerto).
- **Meta:** los anuncios nuevos nacen con «Retoques de vídeo» y «Añadir detalles al diseño del anuncio» activados. Apágalos. Comprueba también que cada anuncio lleva su vídeo: en sep-2026 se publicaron 4 sin vídeo y Meta puso una imagen vieja.
- **Instagram orgánico:** se sube desde el móvil. Business Suite recorta a 4:5 si no se fuerza el 9:16, y la extensión de Chrome no programa reels.
- **Coste:** ElevenLabs cobra por caracteres de TTS y por minutos de música. Para una tanda de 15, mira el saldo antes y después (`voces.sh` ya lo hace).

## Otra marca

Cambia paleta, tipografía y `logoCSL()` → logo de la marca en `kit3d.js`. Si la marca no es Custom Soft Lab, no uses la caricatura de Diego: pon `actor` a `visible=false` o genera un personaje nuevo con `personaje.py` y su referencia. Cambia también la carpeta de salida (`D=` en `hacer.sh`) y los textos del CTA.
