---
name: consejo
description: >
  Convoca un Consejo de agentes decisores para dictaminar si una idea es DE VERDAD buena.
  Cada decisor la juzga desde una lente distinta (mercado, cliente, economía, riesgo,
  ejecución), se revisan entre sí en anónimo, y un Presidente emite el dictamen final:
  GO / NO-GO / GO-SI, con puntuación, el riesgo que la mata, condiciones y una prueba mínima.
  Úsala cuando el usuario quiera validar o evaluar una idea o decisión —de negocio, producto,
  campaña, inversión, contratación o estrategia—, se pregunte "¿es buena idea…?", "¿merece la
  pena…?", "¿debería hacer…?", "¿esto tiene sentido?", o pida una segunda opinión, un GO/NO-GO,
  un veredicto, un pre-mortem, o que "mi consejo" o un panel delibere. Trigger: /consejo
---

# /consejo

Un consejo de decisores que delibera si una idea es realmente buena. Inspirado en el LLM
Council: varios agentes opinan por separado, se critican en anónimo, y un Presidente
sintetiza el dictamen. Aquí cada decisor es un **agente de Claude** con una lente propia.

## Uso

```
/consejo <idea>                      # consejo completo sobre la idea
/consejo                             # si no hay idea, pregunta cuál es
/consejo --rapido <idea>             # salta la revisión cruzada (más barato/rápido)
/consejo --decisores mercado,economia <idea>   # solo un subconjunto de decisores
/consejo --callado <idea>            # muestra solo el dictamen final, sin el detalle por decisor
/consejo --guardar <idea>            # además, guarda el dictamen en un archivo/Notion
```

## El consejo (los agentes decisores)

| Agente | Lente | La pregunta que le obsesiona |
|---|---|---|
| `consejo-mercado`   | Mercado y competencia | ¿Hay demanda real, tamaño y hueco defendible? ¿Por qué ahora? |
| `consejo-cliente`   | Cliente y deseo | ¿Un ICP claro con un dolor urgente y caro que pagaría YA? |
| `consejo-economia`  | Economía / unit economics | ¿Gana dinero, a qué CAC y cuándo llega el beneficio? |
| `consejo-riesgo`    | Riesgo y compliance | Pre-mortem: si esto explota, ¿por qué y cuánto duele? |
| `consejo-ejecucion` | Ejecución y foco | ¿Ejecutable ya, primer euro pronto, sin fragmentar el foco? |
| `consejo-presidente`| Síntesis | Integra todo y dicta GO / NO-GO / GO-SI. |

## Cómo deliberar (procedimiento al invocar la skill)

**Paso 0 — Encuadrar la idea.**
Lee la idea. Si le falta lo esencial para juzgarla (qué es, para quién, y cómo gana dinero),
haz **como máximo 1-2 preguntas** o asume supuestos razonables y **decláralos** al arrancar.
Nunca bloquees el consejo por falta de detalle: los decisores estiman.
Si la idea toca el negocio del usuario y hay contexto relevante disponible (su ICP, su regla
de foco/ingresos, su cartera, números reales en memoria o Notion), reúnelo **tú una vez** y
pásalo a todos los decisores dentro del encuadre. No hagas que cada decisor lo busque.

**Paso 1 — Opiniones independientes (en paralelo).**
Lanza los decisores **a la vez, en un solo mensaje con varias llamadas al Agent tool** (son
independientes). Por defecto los cinco; si hay `--decisores`, solo esos.
A cada uno le pasas el mismo encuadre: `IDEA + supuestos declarados + contexto relevante`.
Cada decisor NO ve a los demás. Usa `subagent_type` = el nombre del agente
(`consejo-mercado`, `consejo-cliente`, `consejo-economia`, `consejo-riesgo`,
`consejo-ejecucion`).
> Si algún `subagent_type consejo-*` no estuviera disponible todavía (agente recién creado),
> usa `general-purpose` y pega en el prompt el rol correspondiente de la tabla de arriba.

**Paso 2 — Revisión cruzada anónima (omitir si `--rapido`).**
Recoge los cinco veredictos y **anonimízalos** (Decisor A, B, C, D, E — sin decir qué lente
es cada uno). Vuelve a lanzar cada decisor en paralelo pasándole los veredictos anónimos de
los demás con esta consigna:
> "Aquí están las valoraciones anónimas del resto del consejo. Señala puntos ciegos o errores,
> di con quién chocas y por qué, y **ajusta tu propio veredicto solo si algo te hace cambiar**.
> Devuelve tu veredicto final en el mismo formato."
Una ronda por defecto (`--rondas N` para más). Esto reduce el sesgo y hace aflorar el desacuerdo.

**Paso 3 — El Presidente.**
Invoca `consejo-presidente` pasándole los veredictos **finales** de todos los decisores
(y una nota de cuánto se movieron en la revisión cruzada). Emite el dictamen.

**Paso 4 — Presentar.**
Muestra **primero el DICTAMEN** (el bloque del Presidente). Debajo, salvo `--callado`, un
resumen de una línea por decisor con su voto (p. ej. `Mercado 7/10 GO · Economía 4/10 NO-GO…`).
Si el usuario quiere, ofrece ver el detalle completo de un decisor o guardar el dictamen.

## Rúbrica: qué hace a una idea "de verdad buena"

Una idea realmente buena puntúa alto en **demanda/deseo + economía + ejecutabilidad** y **no
tiene un riesgo mortal irreversible sin mitigar**. Señales de alarma que el consejo caza:
- Enamoramiento del fundador: mucho entusiasmo, poco cliente que pague.
- "Sin competencia" (suele = sin mercado).
- Facturación confundida con beneficio; CAC ignorado.
- Tercer/cuarto frente que fragmenta el foco antes de consolidar el primero.
- Downside grande e irreversible tratado como "no va a pasar".

Una idea puede ser brillante *en abstracto* y mala *para esta persona ahora*: por eso pesan
tanto ejecución y foco, no solo el atractivo del mercado.

## Notas

- **Modelos:** decisores en `sonnet` (rápidos, 5 en paralelo), Presidente en `opus` (la
  síntesis es lo de mayor palanca). Editable en cada archivo de `~/.claude/agents/consejo-*`.
- **Coste:** completo = 5 decisores × (1 + rondas) + 1 presidente. `--rapido` = 5 + 1.
- **Sesga hacia la honestidad:** el consejo existe para evitar perseguir una mala idea con
  energía de idea buena — y para no matar una buena idea por miedo. Un GO-SI honesto suele
  ser más útil que un sí o un no.
- **No decide por ti:** entrega un dictamen argumentado y una prueba mínima; la decisión
  final es del usuario.
