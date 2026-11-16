export const meta = {
  name: 'calco-referencia-analisis',
  description: 'Analiza un reel de referencia por dimensiones, verifica cada medida contra los fotogramas y sintetiza la especificación + style de Calco',
  phases: [
    { title: 'Medir', detail: 'un agente por dimensión sobre los datos extraídos' },
    { title: 'Verificar', detail: 'refutadores por dimensión contra los fotogramas' },
    { title: 'Sintetizar', detail: 'especificación única + mapeo a Calco' },
  ],
}

const R = '/Users/diego/.claude/skills/calco-referencia/referencias/Da-vHaDjwCS'
const VIDEO = '/Users/diego/Claude/docs/revolutia/videos/Da-vHaDjwCS.mp4'
const CALCO = '/Users/diego/Documents/Claude/calco'

const COMUN = `Analizas el reel de referencia ${VIDEO} (360x640, 25 fps, 48,3 s; vertical de un creador que habla de IA) para que después se pueda replicar su EDICIÓN exactamente en nuestro motor (Calco, Remotion, salida 1080x1920 30fps).
Ya hay datos extraídos en ${R}:
- meta.json; frames/ (TODOS los fotogramas a 360px, 000001.jpg = t 0.00, fotograma n = t (n-1)/25); full/ (un PNG por plano a resolución nativa); ocr_frames/ (10 fps a 1080 de ancho, 000001.jpg = t 0.0, n = (n-1)/10)
- movimiento.json (por fotograma: hist, pix, scale, dx, dy estimados entre consecutivos), cortes.json, layout.json, subtitulos.json (OCR agrupado; incluye texto de las capturas de b-roll, ojo: los subtítulos son la píldora morada), ocr.jsonl, palabras.json (whisper palabra a palabra), audio.json (onsets fuertes con bandas, rms cada 50 ms), audio44k.wav, hojas/ (contacto 1/s y alrededor de cada corte).
Puedes usar Bash con ffmpeg, python3 (cv2, numpy, librosa) para medir más: recortes, zoom a regiones, perfiles de color, diferencias entre fotogramas. Mira imágenes con Read (puedes crear recortes ampliados en ${R}/trabajo/<tu-dimension>/). No toques nada fuera de ${R}/trabajo/.
Toda medida espacial exprésala en coordenadas de un lienzo 1080x1920 (multiplica px de 360x640 por 3) y además en fracción 0-1. Tiempos en segundos y en fotogramas a 25 fps. Cada afirmación con evidencia: qué fichero/fotograma lo muestra. Si algo no se puede medir con certeza, dilo y da el rango. Nada inventado.`

const DIMS = [
  { key: 'composicion', prompt: `DIMENSIÓN: COMPOSICIÓN Y LAYOUT. Describe todos los layouts que aparecen y cuándo: fondo (degradado: colores hex arriba/abajo/esquinas, dirección, viñeta, grano), tarjetas/ventanas (posición x,y,w,h exactas, radio de esquina, borde, sombra, barra de título con los 3 puntos: tamaño, color, separación), dónde va la persona (recorte, escala, encuadre de la cara), dónde va el b-roll (contain/cover, fondo de la ventana), y los planos a pantalla completa. Línea temporal completa: para cada tramo, qué layout. Mide con píxeles (busca bordes con perfiles de columna/fila).` },
  { key: 'subtitulos', prompt: `DIMENSIÓN: SUBTÍTULOS. Solo la píldora de subtítulos (no el texto dentro del b-roll). Mide: tipografía (familia probable, peso, si es mayúsc/minúsc, tracking; compara forma de letras: 'a','g','y','ñ', números), altura de mayúscula y x-height en px@1080, color de texto y de píldora (hex exactos de zonas planas), padding horizontal/vertical, radio de esquina, sombra/borde, posición (centro x,y) y por qué cambia (0.467 vs 0.535: relación con el layout), cuántas palabras por bloque (distribución), reglas de corte de bloques (puntuación, pausas), duración de cada bloque, sincronía con palabras.json (adelanto/retraso), si hay palabra resaltada distinta, animación de entrada/salida (mira frames/ consecutivos a 25 fps alrededor de 5 cambios de bloque: pop, escala, fade, nada). Lista completa de bloques con t_ini, t_fin, texto.` },
  { key: 'motion', prompt: `DIMENSIÓN: MOTION Y TRANSICIONES. Para cada corte de cortes.json y cada transición: tipo (corte seco, fundido, deslizamiento, zoom, máscara), duración en frames, curva (lineal/ease-out/spring: mide posición/escala frame a frame), qué se mueve (b-roll dentro de la ventana, la ventana, la persona). Detecta zooms y paneos dentro de planos (movimiento.json scale/dx/dy, verifícalo visualmente), punch-ins en la persona, animaciones del b-roll (grabaciones de pantalla, cursor, textos tipo 'Pretty Freaking Cool', tarjetas que entran). Cómo entra y sale el layout de pantalla completa del final. Da por cada efecto una receta reproducible (keyframes).` },
  { key: 'sonido', prompt: `DIMENSIÓN: SONIDO. Con audio44k.wav y librosa: ¿hay música de fondo? (energía en huecos sin voz según palabras.json, armónicos estables, tempo/BPM con beat_track), su nivel relativo a la voz en dB y si hay ducking. Efectos de sonido: para cada onset fuerte decide si es SFX (whoosh, pop, click, boom, riser, tecla) o consonante de voz; clasifica por espectro (centroide, sub, aire, duración, envolvente) y relaciónalo con cortes, entradas de b-roll y cambios de subtítulo. Haz espectrogramas PNG de 6-8 momentos y míralos. Mide loudness global (pico, RMS). Resultado: tabla t, tipo, evento visual asociado, nivel; y reglas ("cada entrada de b-roll lleva whoosh de ~250 ms a -18 dB").` },
  { key: 'ritmo', prompt: `DIMENSIÓN: RITMO Y ESTRUCTURA. Con palabras.json, cortes.json, layout.json y hojas/: estructura narrativa por tramos (gancho 0-3 s, desarrollo, CTA final 'comenta KEYS'), cómo se cortan los silencios (huecos entre palabras: distribución; ¿hay jump cuts en la persona?), duración de planos de b-roll vs persona, cada cuántos segundos cambia algo visual, qué tipo de b-roll se usa para cada idea (captura web, logo, texto grande, grabación de pantalla) y cómo se relaciona con lo que dice en ese momento. Saca reglas que un director IA pueda aplicar a otro guion.` },
  { key: 'calco', prompt: `DIMENSIÓN: MAPEO A NUESTRO MOTOR. NO analices el vídeo en detalle; mira la hoja ${R}/hojas/1_por_segundo.jpg y 3-4 PNG de ${R}/full/ para entender el estilo (fondo degradado morado, ventana tipo navegador arriba con b-roll, persona en tarjeta abajo, píldora morada de subtítulos en la junta, final a pantalla completa). Luego estudia el motor ${CALCO} (engine/, templates, presets.json, data/presets.json, componentes Remotion Main.tsx, cómo se definen estilos y plantillas, cómo se elige b-roll, SFX y música; skill ~/.claude/skills/edicion-de-videos-ia/SKILL.md y styles/*.json). Entrega: qué partes del estilo ya soporta Calco y con qué parámetros, qué falta (componentes nuevos: layout split con ventana, píldora, etc.), ficheros exactos a crear/modificar con su ruta y qué hacer en cada uno, y el borrador del JSON de un style5 con la misma forma que style4.json. No modifiques ningún fichero de Calco.` },
]

const MED = {
  type: 'object',
  properties: {
    dimension: { type: 'string' },
    resumen: { type: 'string' },
    medidas: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, que: { type: 'string' }, valor: { type: 'string' }, evidencia: { type: 'string' }, confianza: { type: 'string', enum: ['alta','media','baja'] } },
      required: ['id','que','valor','evidencia','confianza'] } },
    reglas: { type: 'array', items: { type: 'string' } },
    linea_temporal: { type: 'string' },
    dudas: { type: 'array', items: { type: 'string' } },
  },
  required: ['dimension','resumen','medidas','reglas','dudas'],
}

const VER = {
  type: 'object',
  properties: {
    revisadas: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, veredicto: { type: 'string', enum: ['confirmada','corregida','refutada','no_verificable'] },
      valor_correcto: { type: 'string' }, prueba: { type: 'string' } }, required: ['id','veredicto','prueba'] } },
    faltantes: { type: 'array', items: { type: 'string' } },
  },
  required: ['revisadas','faltantes'],
}

const resultados = await pipeline(
  DIMS,
  d => agent(`${COMUN}\n\n${d.prompt}\n\nDevuelve las medidas con id corto (p.ej. ${d.key}-01).`, { label: `medir:${d.key}`, phase: 'Medir', schema: MED }),
  (m, d) => {
    if (!m) return null
    if (d.key === 'calco') return { d: d.key, m, v: null }
    return agent(`${COMUN}\n\nOtro analista midió la dimensión ${d.key.toUpperCase()} y entregó esto:\n${JSON.stringify(m.medidas)}\n\nTu trabajo es REFUTAR. Para cada medida con confianza alta o media (máximo las 25 más importantes para replicar el estilo), compruébala tú de forma independiente contra los fotogramas/datos con tu propio método (nuevo recorte, nueva medición). Si el valor está mal, da el correcto con prueba. Señala también qué falta medir que sea imprescindible para que la copia quede idéntica.`, { label: `verificar:${d.key}`, phase: 'Verificar', schema: VER })
      .then(v => ({ d: d.key, m, v }))
  },
)

const ok = resultados.filter(Boolean)
log(`${ok.length}/${DIMS.length} dimensiones medidas`)

phase('Sintetizar')
const spec = await agent(`${COMUN}\n\nTienes las mediciones de cada dimensión y su verificación adversarial (usa SIEMPRE el valor corregido si el verificador lo corrigió; descarta lo refutado):\n${JSON.stringify(ok)}\n\nEscribe ${R}/especificacion.md: la ficha de edición definitiva para replicar este estilo en un lienzo 1080x1920 30 fps. Secciones: 1) Resumen en 5 líneas. 2) Lienzo y fondo. 3) Layouts (con coordenadas exactas) y línea temporal de qué layout va cuándo. 4) Subtítulos (tipografía, tamaños, colores hex, píldora, posición por layout, troceo, sincronía, animación). 5) Motion y transiciones (recetas con keyframes y curvas). 6) B-roll (tipos, cómo se elige, cómo se encaja). 7) Sonido (música, SFX por evento, niveles). 8) Ritmo (reglas para el director IA). 9) Lo que no se pudo medir y cómo se decide. 10) Mapeo a Calco: qué existe, qué hay que construir, ficheros. Además escribe ${R}/style5.json (misma forma que ~/.claude/skills/edicion-de-videos-ia/styles/style4.json, con un bloque "estilo_referencia" que contenga todos los parámetros numéricos medidos). Español, sin relleno. Devuelve la ruta de ambos ficheros y las 10 decisiones más importantes.`, { label: 'sintetizar', phase: 'Sintetizar' })

return { dimensiones: ok.map(r => ({ d: r.d, n: r.m.medidas.length, corregidas: r.v ? r.v.revisadas.filter(x => x.veredicto !== 'confirmada').length : null })), spec }
