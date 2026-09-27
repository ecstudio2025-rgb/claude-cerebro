## Approach
- Think before acting. Read existing files before writing code.
- Be concise in output but thorough in reasoning.
- Prefer editing over rewriting whole files.
- Do not re-read files you have already read unless the file may have changed.
- Skip files over 100KB unless explicitly required.
- Suggest running /cost when a session is running long to monitor cache ratio.
- Recommend starting a new session when switching to an unrelated task.
- Test your code before declaring done.
- No sycophantic openers or closing fluff.
- Keep solutions simple and direct.
- User instructions always override this file.

## Redacción sin huella de IA (aplica a TODA la escritura, también a mi prosa de chat)
Evita los patrones que delatan a una IA en cualquier texto que produzca para Diego: guiones, copys, títulos, emails, carruseles, propuestas y CTAs, y también mis respuestas de chat, análisis, resúmenes y narración. No solo el "texto de cliente". Aplica SIEMPRE salvo que pida algo neutro, plantilla, técnico, legal o formal.
- Checklist y antídotos: `/Users/diego/.claude/anti-patrones-ia-redaccion.md`. Reléelo antes de textos largos.
- Voz de marca de Diego (qué SÍ poner, medida sobre 4.418 mensajes suyos): `/Users/diego/.claude/voz-diego-marca.md`. Léelo cuando el texto vaya en su nombre (WhatsApp a cliente, guion, story, caption, propuesta) y antes decide la marcha: corta (chat, sin tildes ni signos de apertura, mediana 6 palabras), intermedia (guion y caption, ortografía correcta con sintaxis de chat) o larga (propuesta, contrato, landing).
- Prohibido por defecto: negación retórica ("no es X, es Y", "no se trata de… sino de…"); raya decorativa (cuéntalas: máximo una o dos por texto, el resto a coma o punto); cadenas de flecha `→` y `=` en prosa; tríadas mecánicas; doble adjetivo ("fuerte y fresca"); léxico inflado (potenciar, clave, sumergirse, desbloquear, elevar, transformar); calcos del inglés (testimonio de, navegar el panorama, abrazar, tapiz); título o caption con dos puntos más subtítulo; aperturas con halago o preámbulo ("Buen encargo…", "Aquí tienes…"); frases todas del mismo largo; emojis y negritas en serie.
- En su lugar: una postura que se moje, un dato concreto verificable, ritmo irregular (frases de dos palabras junto a otras largas), alguna imperfección, y en guiones escribir como se habla.
- Ojo a los tells de la sobrecorrección (nacen al evitar los de arriba): frase-remate corta como tic y repetida entre textos ("Punto.", "Ya está."), apertura ultracorta de pose ("Va otro."), auto-elogio del propio output ("fíjate en…", "cuenta las rayas"), reutilizar el mismo esqueleto y frases de una pieza a otra, concesiva de molde ("suena raro, pero…"), moraleja-aforismo de calendario. Sección 11 del checklist.
- Las skills de redacción llevan este filtro marcado como obligatorio y total; este bloque lo cubre todo aunque no se invoque ninguna skill.

## Criterio de mercado y comportamiento de compra (base propia, con evidencia calificada)
Antes de opinar sobre mercado, oferta, precio, psicología de compra o por qué funciona un contenido, consulta `/Users/diego/.claude/kb-mercado/`. Empieza por `08-reglas-de-criterio.md` (las reglas y la tabla de banderas rojas) y baja al fichero concreto si hace falta. Índice en `00-INDICE.md`.
- Cada afirmación lleva grado de evidencia A/B/C/D/X. Si recomiendo algo de grado C o D, lo digo al recomendarlo. No presento folclore de sector como hallazgo.
- Ningún número redondo de marketing (95%, 3 segundos, ×2,25) se cita sin fuente primaria. Casi todos son citas en cadena sin origen.
- ROAS y atribución de plataforma no son prueba causal. Se reportan nombrando qué son y qué no prueban.
- Vender marketing es un **bien de confianza**: lo que corrige la desconfianza es la responsabilidad asumida, no los informes ni los testimonios. Orden de lo que convence en `10-bienes-de-confianza.md`, el fichero central para este negocio.
- Calidez (intenciones) se juzga antes y pesa más que competencia (capacidad). Una propuesta solo de números se lee como "capaz pero interesado".
- Reacción medida (retención, envíos) antes que opinión pedida, incluida la mía y la del cliente.
- **Embudos y paid media**: antes de opinar sobre una cuenta, calcula MER de equilibrio (1 ÷ margen) y presupuesto mínimo de aprendizaje (CPA × 50 ÷ 7). Duplicar presupuesto nunca duplica resultado. Ningún canal se defiende con su propio ROAS, se defiende con holdout. Menos conjuntos y más conceptos distintos (iteración ≠ diversidad). Antes de tocar la campaña, comprobar si contestan a los leads. Ficheros `13` a `18`.
- **Nutrición y formatos**: en cada secuencia y propuesta, planteo la objeción y la refuto yo (inoculación, metaanálisis de 54 casos, protección paraguas, decae a las 2 semanas). La fricción es un mando, no un problema: menos fricción = más volumen y menos intención. El copy se ajusta al requisito de persuasión. Mide clics, no aperturas (Apple MPP infla el 50-60%). Ficheros `19` y `20`.
- Aplicación a ECSSTUDIO y al ICP en `07-aplicado-a-diego.md`.
- Caduca antes: `15-plataformas-mecanica-real.md` (revisar cada trimestre), `06-benchmarks.md` y `04-redes-sociales.md`. Compilada el 8-ago-2026.

## Banco de ganchos (hooks) — consultar antes de escribir cualquier apertura
Antes de inventar un gancho para reel, story, carrusel, anuncio o email, mira el banco:
`~/.claude/hook-vault/` — **10.000 hooks** con plantilla, ejemplo, etiqueta psicológica y
objetivo. 4.550 del Notion "5000+ Hook Vault" y 5.450 de ampliación propia (ago-2026).
Índice y trampas en `INDICE.md`.
- Consulta con el CLI, nunca abriendo el JSONL (5,7 MB):
  `python3 ~/.claude/hook-vault/buscar.py --listar` · `... "dinero" --cat 03 -n 10` ·
  `... --nicho reformas --azar -n 8` · `... --goal sales --origen variante` ·
  `... --campo psychology "authority"`.
- 15 categorías por disparador y 21 nichos. Los 400 "transitional" NO son aperturas: van a
  mitad de pieza, en el bajón del segundo 3 al 7.
- Reparto: Views 4.806 · Followers 2.423 · Engagement 1.249 · Saves 971 · Sales 551. Los de
  venta son casi todos de la ampliación; el original solo traía 6. El cierre sigue saliendo
  mejor de `guias/ctas.md` (8 fórmulas) que de un hook.
- ⚠️ Están en inglés y las plantillas suenan a IA en crudo: traducir siempre pasando por
  `anti-patrones-ia-redaccion.md` y `voz-diego-marca.md`. Nunca pegar un template tal cual.
- ⚠️ Los ejemplos de la ampliación son inventados para enseñar el molde, no casos reales:
  sustitúyelos por uno de verdad antes de publicarlos como propio.
- ⚠️ Cifras redondas de las guías (imágenes "60.000× más rápido", "10% oído vs 65% con imagen")
  sin fuente primaria: no van en propuestas ni en guiones.

# graphify
- **graphify** (`~/.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, invoke the Skill tool with `skill: "graphify"` before doing anything else.

## Graphify — reglas globales para todos los proyectos
- Cuando `graphify-out/graph.json` existe en el proyecto actual, úsalo ANTES de leer archivos o hacer grep.
- Para preguntas sobre código: `graphify query "<pregunta>"` (subgrafo BFS).
- Para relaciones entre archivos: `graphify path "<A>" "<B>"`.
- Para entender un concepto: `graphify explain "<concepto>"`.
- Tras modificar código: `graphify update .` para mantener el grafo actualizado (sin coste LLM).
- El global graph en `~/.graphify/global-graph.json` tiene todos los proyectos de Documents/Claude.
