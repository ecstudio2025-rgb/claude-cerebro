---
name: EDICION DE VIDEOS IA
description: "Edita vídeos verticales (talking head) con IA aplicando estilos guardados sobre la plataforma Calco. Úsala cuando Diego quiera editar/montar un vídeo crudo, cortar silencios y repeticiones, o aplicar un estilo de edición (style1 = 'Edicion dinamica unicamara (CRUDO CORTADO)'). Trigger: editar vídeo, montar reel, cortar crudo, aplicar estilo de edición, style1."
---

# EDICION DE VIDEOS IA

Edita vídeos verticales 9:16 con IA en la plataforma **Calco** (`~/Documents/Claude/calco`).
Cada estilo guardado es un preset reproducible. Los estilos viven en `styles/` de esta skill
y como presets en `calco/data/presets.json`.

## Estilos guardados

| id | nombre | para qué |
|----|--------|----------|
| **style1** | Edicion dinamica unicamara (CRUDO CORTADO) | Talking head de una cámara con el bruto YA cortado/corto. Corta silencios/repeticiones y monta el estilo viral completo (subs 2 tamaños, zoom controlado con origen en la cara, quemados+SFX, música por temática, b-roll semántico, stickers con rotoscopia). |
| **style2** | Edicion dinamica unicamara (CRUDO SIN CORTAR) | Igual pero para una toma CRUDA LARGA sin editar: además del corte de silencios/repeticiones, gpt-5.5 recorta a ≤1 min por CONTEXTO (elige frases prescindibles conservando el arco). Mismo estilo visual/audio. Ambos fuerzan máx. 60s. |
| **style4** | motion 4 edicion dinamica | Igual que style3 (mismos subs, cortes, SFX, música y recorte a 1 min) pero con **zoom AGRESIVO**: encuadre base hasta 1.42× y, sobre todo, empuje dentro de cada plano casi al doble (`intra` 0.086→0.154). Preset `motion-4-edicion-dinamica`. Aprobado por Diego el 19-jul. |
| **style3** | Edicion dinamica unicamara (MOTION 3D) | Como style2 + MOTION GRAPHICS: en 2-4 momentos conceptuales, cutaway a pantalla completa sobre negro con un OBJETO 3D real (cerebro/llave/billetes/lupa...), cintas dorada+blanca que fluyen, círculo y caption con glow+subrayado. El 3D se renderiza en vivo (@remotion/three, requiere gl:'angle'). |

La ficha completa de cada estilo (params, features y pipeline) está en `styles/<id>.json`.
`style1` ⇄ preset `cruda-cortada` en la plataforma.

## Reglas aprendidas (feedback de Diego — mandan sobre cualquier default)

1. **Los ejemplos son ejemplos, no plantillas.** Cuando Diego pasa una referencia de
   motion, es para captar el NIVEL, no para clonarla. Hay que ser ORIGINAL: inventar
   el motion según el contexto de la frase, y variar el TIPO de motion. Nunca repetir
   siempre el mismo recurso (p. ej. objeto 3D en círculo) — no siempre hace falta 3D.
2. **Densidad de motion**: mínimo **4-5 motions por vídeo** si dura más de 30-45s.
3. **Riser solo si el contexto lo pide.** No ponerlo en todos los arranques: solo
   cuando el hook crea EXPECTATIVA que el riser deba sostener.
4. **La música cambia según la temática** — y no se repite pista entre vídeos.
5. **Máximo 1 minuto siempre** (recorte por contexto si hace falta).
6. **Verificar SIEMPRE** con frames del render real antes de dar algo por bueno.
7. **Objetos 3D con pertinencia LITERAL** (feedback 22-jul, tras aprobar style3):
   el objeto debe representar directamente algo que se DICE en la frase elegida
   (mente→cerebro, buscar→lupa, dinero→billetes). Nada de metáforas rebuscadas
   (máscara por "disfrazado" en un guion clínico = error). Si ningún objeto encaja
   de forma evidente, tipografía (bigtext/quote) gana siempre. Guardas DURAS en
   `calco/engine/director.mjs`: en guiones sensibles (salud mental/terapia/dolor)
   los objetos agresivos ni se ofrecen ni pasan (demon-mask, dragon, tigre,
   unicornio), y los arriesgados exigen su palabra literal en la frase elegida
   (OBJ_REQUIERE_PALABRA). Las escenas de motion NUNCA arrancan en los últimos
   5s visibles.
8. **Subtítulos: UN solo acento** (aprobado 22-jul): base blanca + amarillo
   #FFE12E solo en los énfasis del director; `secondaryColor: null` en la
   plantilla diego — el azul queda FUERA de todos los estilos, render y editor.

## Editar desde Claude Code (MCP `impulso-cut`) — camino preferido

La plataforma de edición (Impulso Cut) tiene MCP propio registrado en ~/.claude.json
(herramientas `mcp__impulso-cut__*`; si no aparecen, reinicia la sesión). Flujo:
0. **SIEMPRE con proyecto**: todo lo que se edite con esta skill debe quedar
   reflejado en un proyecto de la plataforma. `editar_videos {…, proyecto:"<cliente
   o campaña>"}` — acepta nombre o id y lo CREA si no existe. `proyectos` lista y
   detalla. Se pueden lanzar lotes de proyectos distintos a la vez (multiproyecto:
   se encolan juntos y la plataforma los muestra editándose en tiempo real).
1. `editar_videos {videos:[rutas absolutas], estilo, proyecto}` — admite VARIOS de
   golpe (cola en serie); prepara solo el HLG/HDR de iPhone (tonemap automático).
   Estilos: `estilos`.
2. `estado {id}` hasta 'listo' (transcribe→corta→dirige→acorta, minutos por vídeo).
3. `correccion {id, texto}` — cambios en tiempo real en español libre.
4. `render {id}` → MP4 final (Remotion: subs, zooms, motion 3D, SFX, música, −14 LUFS).
5. `abrir_editor {id}` → el trabajo cargado en el timeline de Impulso Cut (planos con
   jump cuts, subtítulos karaoke por palabra, música) para que Diego remate a mano;
   el panel IA del editor tiene el mismo chat de correcciones. Las escenas de MOTION
   se VEN de verdad en el preview: el motor renderiza cada escena como mini-MP4
   (`POST /api/projects/<calcoId>/render-scenes`, frameRange de Remotion, pixel-igual
   al render final) y entran como clips de vídeo en la pista superior "Motion IA"
   (muteados: la voz sigue debajo). El pipeline los genera solo (etapa "escenas 3D");
   una corrección los refresca por firma del plan.
`adoptar_proyecto_calco {calcoId}` trae al editor un proyecto ya procesado en Calco.
La cadena se autoarranca sola: MCP → API :8788 → motor Calco :4610.

### Lotes grandes (10+ vídeos)
La cola procesa **3 trabajos a la vez** (`CUT_CONCURRENCIA`, default 3; en el VPS
de 2 vCPU no subir de ahí) y el motor pasa **los renders de uno en uno** por una
puerta global — dos Remotion a la vez revientan la máquina. Por eso:
- `POST /api/ai/proyectos/<id>/render` lanza el MP4 de TODOS los trabajos listos
  del proyecto y contesta al instante (202); el estado se sigue en la lista.
- `POST /api/ai/jobs/<id>/render?async=1` para uno solo sin bloquear.
- Cuenta con ~10-15 min de render por vídeo en el servidor: un lote de 10 son
  horas de renders, aunque los 10 quedan **editables** mucho antes (el pipeline
  va en paralelo). Para ver el montaje no hace falta esperar al MP4.

## Aplicar un estilo a un vídeo

1. **Arranca la plataforma** (si no corre): preview `calco`, o `npm run dev --prefix calco`
   → API :4610 + web :4611. Requiere `OPENAI_API_KEY` y `CALCO_LLM_MODEL=gpt-5.5` en `calco/.env`.
2. **Prepara el vídeo**: si es 4K/horizontal/otro códec, transcodéalo a 1080×1920 h264
   (`ffmpeg -i IN -vf "scale=-2:1920,crop=1080:1920" -r 30 -c:v libx264 -crf 20 -c:a aac out.mp4`).
   Ojo al espacio de color de origen: la rotoscopia (`tools/matte.py`) lo detecta solo
   (BT.2020 de móvil → convierte a bt709; bt709 → intacto).
3. **Súbelo con el preset del estilo**:
   `curl -F "video=@out.mp4" -F "preset=cruda-cortada" http://localhost:4610/api/projects`
   (o desde la web: selector "Estilo al subir" → sube).
4. El pipeline corre solo: transcribe → corta silencios+repeticiones → director IA
   (énfasis/hook/CTA/energía) → recursos IA (música/b-roll/stickers por temática) →
   rotoscopia → deja el proyecto `listo`. La rotoscopia (b-roll detrás de la persona)
   se genera en segundo plano; pon `plan.media.hasCutout=true` cuando `cutout.webm` exista.
5. **Verifica el corte** (clave en crudo): sin silencios largos, sin solapes, repeticiones
   fuera. **Verifica siempre con `remotion still` frames sueltos ANTES del render completo.**
6. **Render**: `curl -X POST http://localhost:4610/api/projects/<id>/render` → MP4 en
   `calco/data/projects/<id>/renders/`.

## Correcciones por texto

Chat de la plataforma (o `POST /api/projects/<id>/corrections {text}`): gpt-5.5 traduce
lenguaje libre a operaciones deterministas. Ej.: «corta de 0:12 a 0:15», «quita la frase
"..."», «subtítulos más grandes», «sin zooms», «estilo: subtítulos arriba en verde neón»,
«plantilla clusters», «deshaz». 20 niveles de undo.

## Guardar un estilo nuevo

Desde la web: botón **★ Guardar estilo** sobre un proyecto ya afinado → nombre → queda como
preset. Por API: `POST /api/presets {name, fromProject:<id>}`. Para registrarlo también en
esta skill, añade `styles/<id>.json` con params + features + pipeline y una fila a la tabla.

## Detalle técnico del estilo

Ver `styles/style1.json` (pipeline completo). Notas de la plataforma en
`calco/README.md` y en la memoria del proyecto ([[project_calco_editor]]).
