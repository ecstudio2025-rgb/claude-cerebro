# Cómo rankea Google de verdad

Qué se sabe del mecanismo con fuente primaria, qué se deduce de la filtración y del juicio
antimonopolio, y qué es folclore. Mismo sistema de grados que el resto de la base (A/B/C/D/X,
ver [00](00-INDICE.md)). En SEO casi no hay grado A: Google no publica experimentos. Aquí **B**
significa "lo confirma Google por escrito o bajo juramento", y **C** "lo sugieren documentos
internos o patentes, sin peso conocido".

Compilado el 24-sep-2026. Lo marcado **caduca: revisar trimestral** depende de actualizaciones.

---

## 1. Las cuatro fuentes y cuánto vale cada una

| Fuente | Qué aporta | Límite |
|---|---|---|
| Documentación de Search Central | Lo que Google admite | Escrita para no dar pistas a spammers |
| Juicio DOJ contra Google (2023-2025) | Testimonio jurado de ingenieros y opinión del juez | Describe sistemas, no pesos |
| Filtración de la Content Warehouse API (may-2024) | 14.014 atributos internos | No dice qué se usa ni cuánto pesa. Fishkin lo avisa él mismo |
| Patentes | Ideas que Google registró | Una patente no prueba uso. Muchas nunca se implantan |

Regla práctica: si algo aparece en dos de las cuatro, lo trato como real. Si solo está en una
patente, es hipótesis.

- Filtración, análisis original: [SparkToro, 27-may-2024](https://sparktoro.com/blog/an-anonymous-source-shared-thousands-of-leaked-google-search-api-documents-with-me-everyone-in-seo-should-see-them/)
  y [iPullRank / Mike King](https://ipullrank.com/google-algo-leak). Resumen neutral en
  [Search Engine Land, may-2024](https://searchengineland.com/google-search-document-leak-ranking-442617).

---

## 2. Lo que está confirmado

### Los clics cuentan, y mucho — grado B

Pandu Nayak, vicepresidente de Search, confirmó bajo juramento **NavBoost**: un sistema que
reordena resultados con datos agregados de clics de una ventana móvil de **13 meses** (antes de
2017 eran 18). Lo describió como una de las señales importantes. La filtración trae atributos con
nombres que encajan: `goodClicks`, `badClicks`, `lastLongestClicks`.

- [Resumen del testimonio, Hobo](https://www.hobo-web.co.uk/google-vs-doj/) ·
  [análisis de SEJ sobre clics](https://www.searchenginejournal.com/the-facts-about-google-click-signals-rankings-and-seo/572827/)

Durante años Google dijo en público que el CTR era demasiado ruidoso para rankear. El juicio lo
desmiente. Lo que no confirma: que el "CTR" de tu página suba tu posición de forma lineal, ni que
comprar clics funcione. NavBoost trabaja sobre patrones agregados de mucha gente y a lo largo de
meses.

Consecuencia que sí es accionable: **el título y la descripción son palanca de ranking indirecta**,
no solo de CTR. Y el "último clic largo" (el usuario no vuelve a Google) es lo que se premia. Una
página que resuelve la búsqueda y la termina gana; una que obliga a volver a la lista, pierde.

### Hay una puntuación de calidad por sitio — grado B

La opinión del juez Mehta sobre remedios (2-sep-2025) recoge una señal de calidad de página,
**Q\***, en gran parte independiente de la consulta, que el testimonio llama "increíblemente
importante" contra las granjas de contenido. La filtración trae `siteAuthority`. La patente de
Navneet Panda de 2015 describe una puntuación de calidad del sitio entero.

- [PPC Land sobre la opinión de remedios](https://ppc.land/google-court-ruling-reveals-quality-signals-derived-from-webpage-content/) ·
  [patente US9031929B1, "Site quality score"](https://patents.google.com/patent/US9031929B1/en)

Consecuencia: **las páginas malas arrastran a las buenas**. Por eso el sistema de contenido útil
(ahora dentro del core) actúa a nivel de sitio.

### Topicalidad: anclas, cuerpo, clics — grado B

Del juicio sale el esquema "ABC" de la topicalidad (T\*): **A**nchors (el texto de los enlaces que
apuntan a la página), **B**ody (los términos del documento) y **C**licks. Y la opinión del juez
indica que la mayoría de las señales de calidad salen del propio contenido, no de fuera.

- [Search Engine Land, "The ABCs of Google ranking signals"](https://searchengineland.com/google-abc-ranking-signals-455360)

Traducción: el texto de la página y el texto de los enlaces (también internos) siguen pesando.
No se murió la on-page.

### Modelos de lenguaje en el ranking — grado B

**RankEmbed / RankEmbedBERT**: modelos entrenados con 70 días de registros de búsqueda más las
puntuaciones de los evaluadores humanos. Los evaluadores no tocan tu web, pero su criterio entrena
los modelos. Por eso leer las directrices de evaluadores sirve (ver [22](22-seo-contenido-y-autoridad-tematica.md)).

### Sistemas nombrados por Google — grado B

La guía oficial lista 17 sistemas activos. Los que más importan a un sitio de servicios: BERT y
neural matching (entender la intención aunque no pongas la palabra exacta), **passage ranking**
(rankea fragmentos de una página larga), **site diversity** (en general, dos resultados máximo por
sitio), reliable information, reviews, spam detection, PageRank. El "helpful content system" dejó
de existir como sistema aparte en **marzo de 2024**: se integró en el core.

- [Guía de sistemas de ranking, act. 10-dic-2025](https://developers.google.com/search/docs/appearance/ranking-systems-guide)

### Chrome se usa — grado C tirando a B

La filtración trae `chromeInTotal` y `chrome_trans_clicks` (para elegir las páginas principales
de un dominio, las que salen como sitelinks). El juicio habla de señales de popularidad. Google
negaba usar Chrome para rankear. Peso: desconocido.

### Evaluadores y listas blancas — grado C

Atributos de la filtración sugieren que las valoraciones de evaluadores (plataforma EWOK) entran
en sistemas, y hay banderas tipo `isElectionAuthority` o `isCovidLocalAuthority`. Afecta a nichos
YMYL, no a software B2B ni a una clínica dental.

---

## 3. Lo que la gente cree que sabe y no está claro

| Idea | Grado | Por qué |
|---|---|---|
| "Sandbox" para dominios nuevos | C | La filtración trae `hostAge`, descrito como usado para aislar spam fresco. Google lo niega en abstracto. Lo que sí está medido: solo el **1,74%** de páginas nuevas llega al top 10 en un año ([Ahrefs, 15-may-2025](https://ahrefs.com/blog/how-long-does-it-take-to-rank-in-google-and-how-old-are-top-ranking-pages/)). Sandbox o no, el efecto práctico es el mismo |
| Links ya no importan | X | PageRank sigue listado como sistema core. La filtración añade que el índice donde vive el enlazante (según sus clics) decide si el enlace cuenta. Un enlace desde una página que nadie visita vale poco |
| Links lo son todo | X | La opinión del juez: la mayor parte de la calidad sale del contenido |
| Marca como factor | C | Muchos módulos de la filtración identifican entidades y marcas; la patente de Panda usa búsquedas de marca contra enlaces. Dirección coherente, sin peso |
| Autoría como señal | C | Hay atributos de autor en la filtración. Google dice que E-E-A-T no es un factor ([guía de inicio](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)). Lo que cuenta es lo que el autor hace verificable, no el schema |
| Ganancia de información | C | Patente [US11354342B2](https://patents.google.com/patent/US11354342B2/en): puntúa lo que un documento aporta sobre lo ya visto por el usuario. Nació en el contexto de un asistente, no del ranking web. La idea es sensata; la prueba de uso no existe |
| Frescura como bonus general | X | Solo cuenta en consultas que la merecen (sistema de frescura). Cambiar la fecha sin cambiar el contenido no hace nada útil |

---

## 4. Mitos: grado X, se corrigen si alguien los trae

| Mito | Qué dice la fuente primaria |
|---|---|
| **Palabras clave LSI** | El LSI es una técnica de indexación de 1988 que Google no usa. Mueller: "no existe tal cosa". Lo que sí existe: modelos de lenguaje que entienden sinónimos y contexto, que hacen irrelevante la lista de "LSI" |
| **Densidad de palabra clave** | La guía de inicio: el relleno viola las políticas. No hay porcentaje ideal. La lista de "términos" de Surfer o POP es correlación con el top 10, no una regla de Google |
| **DA / DR / Authority Score como métrica de Google** | Son métricas de Moz, Ahrefs y Semrush calculadas con sus rastreadores. Google no las ve. Útiles para comparar, inútiles como objetivo o como precio de un enlace |
| **Número de palabras mínimo** | "No hay recuento mágico" (guía de inicio, act. 10-dic-2025). Whitespark 2026 registra que "volumen de contenido en páginas de servicio" cayó 40 puestos |
| **Meta keywords** | Google no la usa. Desde 2009 |
| **Penalización por contenido duplicado** | No existe como penalización. Es ineficiente y Google elige una URL canónica. Distinto: copiar en masa sí es spam |
| **Palabra clave en el dominio** | Efecto mínimo (hay un sistema específico, "exact match domain", para que no dé ventaja) |
| **E-E-A-T es un factor de ranking** | "No, no lo es", dice Google. Es el marco con el que los evaluadores juzgan. Las señales que lo aproximan sí existen |
| **Google penaliza el contenido hecho con IA** | La política castiga la escala sin valor, con o sin IA ([políticas de spam, act. 28-ago-2026](https://developers.google.com/search/docs/essentials/spam-policies)) |
| **El schema sube posiciones** | No es factor de ranking. Da elegibilidad a resultados enriquecidos, y cada vez hay menos (ver [23](23-seo-tecnico-local-y-ia.md)) |
| **Orden y cantidad de encabezados** | Accesibilidad, no ranking (guía de inicio) |
| **Tasa de rebote de Analytics** | Google no usa GA. Lo que usa son sus propios clics (NavBoost). Mismo fenómeno medido por otro sitio, no la métrica de GA |
| **Señales sociales directas** | Sin prueba. Lo que puede pasar es indirecto: difusión que produce búsquedas de marca y enlaces |
| **Manipular el CTR con bots** | Grado D. Hay vendedores. NavBoost trabaja sobre 13 meses agregados y Google filtra clics anómalos. Riesgo alto, prueba nula |
| **Subdominio contra subcarpeta** | La guía dice que da igual a efectos de Google. Grado C para la opinión contraria, que existe y tiene casos, sin control |

---

## 5. Las actualizaciones: qué son y cómo se leen

**Core updates** (grado B sobre la mecánica): cambios amplios varias veces al año, no dirigidos a
un sitio. Lo que dice Google sobre recuperarse
([core updates, act. 10-dic-2025](https://developers.google.com/search/docs/appearance/core-updates)):

- Hay que revisar las páginas que más cayeron con las preguntas de autoevaluación.
- Algunos cambios se notan en días; otros tardan **meses**, y a menudo hasta la siguiente core.
- Nada de arreglos rápidos por rumor. **No borrar contenido salvo que no tenga arreglo**: borrados
  masivos pueden señalar que el contenido se hizo para buscadores.

Calendario reciente (**caduca: revisar trimestral**):

| Update | Fechas | Nota |
|---|---|---|
| Marzo 2026 core | 27-mar a 8-abr-2026 | |
| Mayo 2026 core | 21-may a 2-jun-2026 | Google: "contenido relevante y satisfactorio de todo tipo de sitios" |
| Discover core | completado 27-feb-2026 | Solo Discover |

- [Anuncio de mayo 2026, Search Central en X](https://x.com/googlesearchc/status/2057487931250499886)

Cifra que circula: en mayo 2026, el **24,1%** de páginas del top 10 cayó fuera del top 100
([seo-kreativ](https://www.seo-kreativ.de/en/blog/google-may-2026-core-update-started/)). Es
dato de herramienta de tercero sobre su panel de palabras clave: **grado C**. Sirve para decir que
fue muy volátil; no para calcular nada.

**Cómo leer una caída sin engañarse** (regla 3 de [08](08-reglas-de-criterio.md) aplicada a SEO):

1. ¿Coincide con una update confirmada? Si no, mirar primero técnico (indexación, robots,
   redirecciones, caída del servidor).
2. ¿Cayó el sitio entero o unas URLs? Todo el sitio apunta a calidad de sitio o a acción manual.
   Unas URLs, a intención o a competencia.
3. ¿Bajaron clics con impresiones estables? Entonces puede ser la SERP (AI Overview nueva, más
   anuncios), no tu posición. Ver [23](23-seo-tecnico-local-y-ia.md).
4. No tocar nada durante el despliegue. Medir dos semanas después de que Google lo dé por
   terminado.

---

## 6. Las políticas de spam que importan en 2026

Fuente: [políticas de spam, act. 28-ago-2026](https://developers.google.com/search/docs/essentials/spam-policies). Grado B.

- **Contenido a escala abusivo**: muchas páginas hechas para manipular el ranking y no para ayudar.
  Da igual si las hizo una IA, un scraper o un equipo en Filipinas. Lo que se juzga es la
  intención y el valor, no la herramienta.
- **Abuso de reputación del sitio** (parasite SEO): contenido de terceros en un dominio fuerte para
  aprovechar su ranking. Desde noviembre de 2024 la supervisión del dueño no lo salva. **Y desde el
  30-ago-2026, en el EEE (España incluida) la acción manual ya no degrada directamente esa sección**:
  Google la separa del resto del sitio y la deja rankear por sus propios méritos. Fuera del EEE sí
  degrada. Es consecuencia de la investigación de la Comisión bajo la DMA
  ([SEJ, ago-2026](https://www.searchenginejournal.com/google-updates-site-reputation-abuse-policy-removes-penalties-in-eea/587423/)).
  **Caduca: revisar trimestral.** Esto no convierte el parasite SEO en buena idea en España: la
  sección aislada rankea sin la autoridad del dominio, que era todo el truco.
- **Abuso de dominios caducados**: comprar un dominio con historial para meter contenido sin
  relación. Relevante cuando alguien te vende "un dominio con DR 40 para arrancar".
- **Páginas puerta (doorways)**: páginas casi iguales por ciudad o variante que embudan a un mismo
  sitio. Es lo que hay que vigilar en SEO local y programático.
- **Spam de enlaces**: comprar, intercambiar, guest posts con anclas optimizadas en serie.

---

## 7. Lo que sale de todo esto

1. **Satisfacer la búsqueda hasta el final** es la señal que Google confirmó bajo juramento. Diseñar
   la página para que el usuario no tenga que volver a la lista.
2. **La calidad es de sitio.** Diez páginas buenas y cuarenta flojas rankean peor que diez buenas.
3. **El texto y las anclas siguen pesando.** La on-page no es cosa del pasado.
4. **Un dominio nuevo tarda.** 1,74% de páginas nuevas en el top 10 al año. Presupuestar 6-12 meses
   antes de esperar leads orgánicos, y decirlo en la propuesta.
5. **Las métricas de terceros (DA, DR) no son de Google.** No se prometen ni se venden.
6. **Ante una caída, primero técnico, luego SERP, luego calidad.** Y no borrar a lo loco.
