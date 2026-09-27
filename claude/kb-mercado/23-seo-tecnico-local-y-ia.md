# SEO técnico, local y búsqueda con IA

Tres bloques que se mueven a velocidades distintas. El técnico cambia poco. El local cambia con
cada encuesta de Whitespark y cada prueba de Sterling Sky. El de IA cambia cada mes: **casi todo el
bloque 3 caduca: revisar trimestral**.

Grados como en [21](21-seo-como-rankea-google.md). Compilado el 24-sep-2026.

---

## 1. Técnico

### Presupuesto de rastreo: casi nunca es el problema — grado B

Google dice a quién le afecta ([crawl budget](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget)):

- sitios de **más de 1 millón de páginas** que cambian cada semana;
- sitios de **más de 10.000 páginas** que cambian cada día;
- cualquier sitio con muchas URLs en "Descubierta: actualmente sin indexar".

Una web de servicios de 20 páginas no tiene problema de rastreo. Si una página suya no se indexa, el
problema es calidad o duplicación, no presupuesto. Quien vende "optimización de crawl budget" a una
pyme está vendiendo humo.

Dos matices de la misma página que casi nadie aplica bien:

- `noindex` **no ahorra rastreo**: Google tiene que pedir la página para ver la etiqueta. Para no
  rastrear, `robots.txt`.
- Contenido retirado para siempre: **404 o 410**, no redirección a la portada.

### Análisis de logs: cuándo compensa — grado B/C

Sirve para ver qué pide Googlebot de verdad, no lo que dice Search Console. Compensa en sitios
grandes, en migraciones y cuando hay facetas o parámetros que generan URLs infinitas. En un sitio de
servicios pequeño, el informe de estadísticas de rastreo de Search Console basta. Uso concreto que
sí merece la pena en cualquier tamaño: confirmar que Googlebot y Bingbot reciben 200 y no un
bloqueo del firewall o de Cloudflare.

### Sitemaps — grado B

- Google **ignora `priority` y `changefreq`**.
- Usa `lastmod` solo si es **coherente y verificable**. Si todas las URLs llevan la fecha de hoy en
  cada despliegue, deja de fiarse.
- Solo URLs canónicas, indexables y que devuelvan 200. Nada con `noindex`.

### Core Web Vitals e INP — grado B sobre qué son, C sobre cuánto pesan

- **INP sustituyó a FID el 12-mar-2024.** Bueno ≤ 200 ms, malo > 500 ms, medido en el percentil 75
  de usuarios reales ([web.dev, INP](https://web.dev/articles/inp)). LCP bueno ≤ 2,5 s; CLS ≤ 0,1.
- Google dice que los usa sus sistemas de ranking, y también que buenos resultados **no garantizan**
  posiciones ([page experience](https://developers.google.com/search/docs/appearance/page-experience)).
  En la práctica es un desempate entre páginas de relevancia parecida.
- Se miden con **datos de campo** (CrUX). Un sitio con poco tráfico no tiene datos de campo y el
  informe de Search Console sale vacío. La nota de Lighthouse es de laboratorio y no es lo que usa
  Google.

Donde la velocidad sí pesa mucho es en conversión, no en ranking. Ver [17](17-conversion-y-captacion.md).

### JavaScript — grado B

Google renderiza JS, pero en una segunda cola. El contenido y los enlaces importantes deben estar en
el HTML servido. Y los rastreadores de IA (GPTBot, ClaudeBot, PerplexityBot) en general **no
ejecutan JS**: una web que pinta el texto en el navegador es invisible para ellos. Grado C sobre el
comportamiento de cada bot concreto, porque cambia.

### Datos estructurados: menos de lo que se vende — grado B

- No son factor de ranking. Dan elegibilidad para resultados enriquecidos.
- Google retiró **7 tipos** en junio de 2025 (Book Actions, Course Info, ClaimReview, Estimated
  Salary, Learning Video, Special Announcement, Vehicle Listing)
  ([Search Central, jun-2025](https://developers.google.com/search/blog/2025/06/simplifying-search-results)).
- **Los resultados enriquecidos de FAQ dejaron de mostrarse el 7-may-2026**. El marcado `FAQPage`
  sigue siendo válido y Google lo lee, pero ya no pinta nada en la SERP
  ([doc FAQPage](https://developers.google.com/search/docs/appearance/structured-data/faqpage);
  [SEJ, may-2026](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/)).
  **Caduca: revisar trimestral.**
- La guía de Google para IA generativa lo dice claro: el marcado **no es necesario** para aparecer
  en AI Overviews ni en AI Mode.

Lo que sigue mereciendo la pena: `Organization` o `LocalBusiness` coherente con el Perfil de
Empresa, `BreadcrumbList`, `Product`/`Review` donde aplique, `Article` con autor real.

### SEO de entidades y Knowledge Graph — grado C

Google organiza el conocimiento en entidades (personas, empresas, lugares) con atributos y
relaciones. La filtración trae varios módulos que identifican entidades y sus webs oficiales.
Lo práctico:

- Un nombre de empresa **único y consistente** en web, Perfil de Empresa, LinkedIn, directorios y
  registro mercantil.
- `Organization` con `sameAs` apuntando a los perfiles reales.
- Menciones en sitios que Google ya reconoce como entidades (prensa, asociaciones del sector,
  directorios serios). El panel de conocimiento aparece cuando hay suficientes fuentes coincidentes,
  no porque lo pidas.

### Bing — grado B

Importa más de lo que parece: alimenta a Copilot y a varios buscadores con IA. Directrices
reescritas el **27-feb-2026** ([SEJ](https://www.searchenginejournal.com/bing-adds-geo-to-official-guidelines-expands-ai-abuse-definitions/568442/);
[directrices](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)):

- Nombran el GEO por primera vez, sin garantizar nada.
- Suavizan la postura sobre contenido generado: lo problemático es la escala **sin revisión
  editorial**.
- Nueva sección de abuso: **inyección de instrucciones** para manipular sus modelos.
- `NOARCHIVE` saca la página de Copilot; `NOCACHE` limita la cita a URL, título y fragmento.
- Recomiendan **IndexNow** para avisar de altas, cambios y bajas.
- Bing Webmaster Tools tiene informe de rendimiento en IA (citas en Copilot) desde el 9-feb-2026.

---

## 2. Local

### Encuesta Whitespark 2026 — grado C (opinión experta, no experimento)

47 expertos, 187 factores, publicada el **6-nov-2025**
([Whitespark](https://whitespark.ca/local-search-ranking-factors/)).

Top del paquete local (mapa):

1. Categoría principal del Perfil de Empresa
2. Proximidad al punto de búsqueda
3. Palabras clave en el nombre del negocio
4. Dirección física en la ciudad de la búsqueda
5. Abierto en el momento de la búsqueda
6. Nota media alta
7. Dirección visible
8. Categorías adicionales
9. Cantidad de reseñas con texto
10. Chincheta bien colocada

Top del orgánico local: **una página dedicada por servicio** (primero), relevancia geográfica de la
palabra clave, calidad de los enlaces al dominio, palabra clave en el título de la página enlazada
desde el perfil, enlaces de dominios del sector.

Reparto por grupos en el mapa: perfil ~30%, reseñas ~18%, comportamiento ~15%, citas ~12%,
enlaces ~12%, on-page ~10%. Para visibilidad en búsqueda con IA: citas ~22%, reseñas ~18%,
on-page ~15%, perfil ~14%. Son porcentajes de una encuesta, no pesos del algoritmo.

Dato raro que vale oro: "volumen de contenido en páginas de servicio" **bajó 40 puestos**. La gente
quiere la receta, no el ensayo.

### Pruebas de Sterling Sky — grado C, con método visible

- **"Cerca de mí"**: 8.186 negocios en 200 ciudades, cinco categorías de servicio
  ([Sterling Sky, 2025](https://www.sterlingsky.ca/what-gets-you-ranking-for-near-me-2025/)).
  Dirección oculta correlaciona negativo; **la frecuencia mensual de reseñas pesa más que el total**;
  un cliente cayó con fuerza tras **18 días** sin reseñas nuevas; reseñas con texto mejor que solo
  estrellas; poner "cerca de mí" en la web no hizo nada.
- **Campos del perfil**: servicios, nombre, categoría, dirección, reseñas, web, horario y atributos
  mueven ranking; los servicios empezaron a contar en 24-72 h en su prueba de 2022, cuando en 2019
  no contaban ([Sterling Sky](https://www.sterlingsky.ca/services-in-google-business-profile-impact-ranking/)).
  **Las publicaciones del perfil no mostraron efecto en ranking** en su estudio específico.
- **Nombre con palabra clave**: en una prueba de Joy Hawkins, añadir "salad bar" al nombre subió un
  restaurante de no aparecer al puesto 4. Y es **contra las directrices** si no es el nombre real.
  Un competidor puede denunciarlo y Google lo corrige. Solo es legítimo si el nombre registrado lo
  incluye.

### Lo que sale para un negocio local

| Palanca | Grado | Coste | Nota |
|---|---|---|---|
| Categoría principal bien elegida | B/C | Cero | La decisión más rentable de todo el SEO local |
| Una página por servicio, enlazada desde el perfil | C | Bajo | Factor 1 del orgánico local |
| Flujo constante de reseñas con texto | C | Proceso | Frecuencia, no campañas de golpe |
| Dirección visible si hay local real | C | Cero | Negocio con área de servicio sin local: no inventarla |
| Servicios del perfil completos y granulares | C | Bajo | Mueve en días |
| Publicaciones del perfil | C (sin efecto en ranking) | Tiempo | Sirven para conversión, no para posición |
| Proximidad | B | No se toca | No se puede comprar. No prometer ranking en toda la ciudad |
| Páginas por ciudad sin sede | B (política) | | Página puerta |

Reseñas y ley: Google prohíbe incentivarlas y filtrarlas, y en la UE la Directiva Ómnibus
(2019/2161) considera práctica desleal las reseñas falsas o seleccionadas sin avisar. Pedirlas a
todos, sí; pagar o premiar, no.

---

## 3. Búsqueda con IA y GEO

**Caduca: revisar trimestral** todo este bloque.

### Cuánto tráfico se come el AI Overview

| Estudio | Método | Resultado | Grado |
|---|---|---|---|
| Ahrefs, 4-feb-2026 ([enlace](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update)) | 300.000 palabras clave, CTR agregado de Search Console, dic-2023 contra dic-2025, con y sin AIO | **-58%** de CTR en la posición 1 cuando hay AIO (antes -34,5% en abr-2025) | C (correlacional, lo dicen ellos) |
| Seer Interactive, 24-abr-2026 ([enlace](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update)) | 53 marcas, 5,47 M consultas, 2.430 M impresiones | CTR orgánico con AIO 2,36% contra 3,82% sin AIO (feb-2026). **Estar citado en el AIO da +120% de clics** frente a no estarlo, y aun así 38% menos que sin AIO | C (una cuenta pesa el 47% de un segmento; ellos lo avisan) |
| Pew Research, 22-jul-2025 ([enlace](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)) | Navegación real de 900 adultos de EE. UU., mar-2025 | Clic en resultado tradicional en el **8%** de visitas con resumen IA contra **15%** sin él; clic en las fuentes del resumen: **1%** | B (comportamiento observado, muestra pequeña, EE. UU.) |

Tres métodos distintos, misma dirección. Lo doy por bueno como dirección y no uso ninguna cifra
como constante. Google, por su parte, dice que los clics desde páginas con AIO son "de más calidad"
(más tiempo en el sitio) ([AI features](https://developers.google.com/search/docs/appearance/ai-features)):
afirmación de parte sin datos publicados, grado D.

En España los AI Overviews llegaron el **26-mar-2025**, en español
([marketing4ecommerce](https://marketing4ecommerce.net/ai-overviews-de-google-espana/)).

Dónde muerde: consultas **informativas**. Las transaccionales y locales se ven menos afectadas. Por
eso el orden de contenido de [22](22-seo-contenido-y-autoridad-tematica.md) pone el blog al final.

### Lo que dice Google sobre optimizar para su IA — grado B

Guía publicada el 15-may-2026, act. 10-jul-2026
([AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)):

- Las funciones de IA salen del **mismo índice y los mismos sistemas de calidad**, con RAG y
  *query fan-out* (el modelo lanza varias búsquedas relacionadas en paralelo). Si no rankeas en lo
  clásico, no apareces en la IA.
- **Lo que no hace falta**: `llms.txt`, trocear el contenido en fragmentos, escribir "para la IA",
  cazar colas largas, fabricar menciones, obsesionarse con el schema.
- Contenido **no commodity**: perspectiva propia y experiencia que no esté ya en todas partes.

Medición: Search Console tiene informe de rendimiento de IA generativa desde el 3-jun-2026, global
desde el 31-ago-2026. **Solo impresiones**, sin clics ni consultas, con datos desde el 18-may-2026.
Hay además un interruptor para excluir el sitio de AI Overviews y AI Mode que, según Google, no se
usa como señal de ranking en el resto de la búsqueda
([SEJ, sep-2026](https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/)).

### llms.txt — grado X para Google

Illyes (jul-2025): Google no lo usa ni piensa usarlo. Mueller lo comparó con la meta keywords. La
guía de 2026 lo lista entre lo que no hace falta. Un análisis de 137.000 sitios encontró que el 97%
de los `llms.txt` publicados nunca los pidió ningún bot (dato de tercero, grado C)
([Search Engine Land](https://searchengineland.com/google-says-normal-seo-works-for-ranking-in-ai-overviews-and-llms-txt-wont-be-used-459422)).
No hace daño. No lo cobro.

### El paper de GEO — grado B en su banco de pruebas, C fuera de él

Aggarwal y otros (Princeton, IIT Delhi), KDD 2024 ([arXiv](https://arxiv.org/abs/2311.09735)).
Probaron nueve maneras de reescribir contenido y midieron cuánto aparecía en respuestas de un motor
generativo simulado:

- **Añadir estadísticas** y **añadir citas textuales de fuentes** fueron lo mejor: hasta **+41%**
  en visibilidad ajustada por posición.
- **Rellenar palabras clave no funcionó.** Lo que servía en el SEO de 2005 no sirve aquí.
- Combinar fluidez con estadísticas dio el máximo.
- Ganaron más las fuentes que partían de posiciones bajas: GEO iguala algo el terreno.

Límites: banco de pruebas propio con un modelo de 2023, no ChatGPT ni AI Overviews de hoy. Trabajo
posterior (2025-2026) aborda comercio electrónico y detección de contenido "optimizado para GEO",
señal de que los motores van a descontarlo igual que Google descontó el relleno.

### Qué citan los asistentes — grado C

- ChatGPT y Perplexity comparten solo el **5-8%** de dominios citados para las mismas preguntas
  ([Orbit Media, ago-2026](https://www.orbitmedia.com/blog/ai-citation-sources/)). No hay "una"
  optimización para IA.
- AI Overviews y AI Mode citan la misma URL solo el **13,7%** de las veces, aunque lleguen a
  conclusiones parecidas (Ahrefs, sep-2025; cifra tomada de resúmenes, no he leído el estudio
  original, así que grado D hasta verificarlo).
- La cuota de Reddit en citas de ChatGPT cayó de ~60% a ~10% entre agosto y septiembre de 2025
  ([Semrush](https://www.semrush.com/blog/most-cited-domains-ai/)). Una decisión de producto borra una
  "estrategia" en un mes.
- Un informe de 2026 encuentra que el **volumen de búsqueda de marca** correlaciona más con ser
  citado (0,334) que los enlaces ([Digital Bloom](https://thedigitalbloom.com/learn/2025-ai-citation-llm-visibility-report/)).
  Grado C-D: correlación moderada, método de vendedor.

### Lo que sale para IA

1. **El SEO clásico es condición necesaria.** Lo dicen Google y Bing por escrito.
2. **Datos propios y citas con fuente** en el texto: lo único con experimento detrás.
3. **Ser mencionado fuera** (directorios, prensa, comparativas de terceros) pesa más para los
   asistentes que para Google.
4. **HTML servido con el texto**, porque los bots de IA no ejecutan JS.
5. **No vender GEO como disciplina aparte con cifras.** Todo lo que circula es correlación de
   vendedor y caduca en meses.
