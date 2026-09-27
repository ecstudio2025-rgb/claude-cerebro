# Contenido, autoridad temática y arquitectura

Qué contenido rankea, cómo se organiza un sitio para que Google entienda de qué va, y qué enseñan
los cursos que se venden sobre esto. Grados como en [21](21-seo-como-rankea-google.md): en SEO,
**B** es "lo dice Google por escrito o se confirmó en el juicio", **C** es "estudio de industria
con método publicado pero sin control causal", **D** es "lo dice quien vende el curso o la
herramienta".

Compilado el 24-sep-2026.

---

## 1. Lo que Google pide al contenido, dicho por Google

### Las directrices de evaluadores — grado B como descripción del objetivo

Última versión: **11-sep-2025**, 182 páginas
([PDF](https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf)). La de enero de 2025
reorganizó "Lowest" y "Low" para calcar las políticas de spam y definió por primera vez la IA
generativa; la de septiembre añadió ejemplos de AI Overviews y precisó YMYL
([Search Engine Land, sep-2025](https://searchengineland.com/google-updates-search-quality-raters-guidelines-adding-ai-overview-examples-ymyl-definitions-461908)).

Por qué importa aunque los evaluadores no toquen tu web: sus notas entrenan los modelos de ranking
(RankEmbed, ver [21](21-seo-como-rankea-google.md)). Leerlas es leer la función objetivo.

Lo que casi nadie extrae de ellas:

- **La nota más baja va a contenido hecho con poco esfuerzo y en mucha cantidad**, incluido el
  generado con IA sin añadir nada. No castigan la IA; castigan la ausencia de esfuerzo, originalidad
  y valor añadido.
- **"Needs Met" y "Page Quality" son dos escalas distintas.** Una página excelente puede no
  satisfacer la búsqueda concreta. La mayoría de páginas de servicio fallan en lo primero, no en lo
  segundo: responden a una pregunta que el usuario no hizo.
- **La reputación se busca fuera del sitio.** El evaluador busca qué dicen otros de la empresa. Lo
  que la web dice de sí misma pesa menos. Encaja con la regla de bien de confianza de
  [10](10-bienes-de-confianza.md): la autoevaluación no convence, tampoco a Google.
- **La experiencia de primera mano** (la primera E de E-E-A-T) se demuestra con detalle que solo
  tiene quien lo hizo: fotos propias, cifras de un proyecto, errores cometidos.

### Autoevaluación de contenido útil — grado B

Las preguntas oficiales ([creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content))
se resumen en tres filtros que uso al revisar una pieza:

1. ¿Aporta información, investigación o análisis **original**, o reescribe lo que ya hay?
2. ¿Alguien que llega por la búsqueda sale sabiendo lo suficiente como para no volver a Google?
3. ¿Se habría escrito si Google no existiera?

La tercera es la que tumba la mayoría de blogs de agencia.

---

## 2. Autoridad temática: qué hay de real

### El concepto

Un sitio que cubre un tema con profundidad y coherencia rankea mejor en ese tema que uno que lo
toca de pasada. Grado **C**: consistente con la puntuación de calidad por sitio, con la topicalidad
(T\*) y con cómo funcionan los modelos de lenguaje, pero **el único sistema que Google ha llamado
"topic authority" es para noticias** ([Search Central, may-2023](https://developers.google.com/search/blog/2023/05/understanding-news-topic-authority)).
Para webs de negocio no hay confirmación de un sistema con ese nombre.

La trampa del concepto: se usa para justificar publicar 200 artículos. Cobertura no es volumen. La
política de contenido a escala castiga exactamente eso cuando no hay valor detrás, y la puntuación
de calidad por sitio hace que los artículos flojos arrastren a los buenos.

### Mapa temático (topical map) — método útil, evidencia D sobre resultados

Lo que enseña la escuela de Koray Tuğberk Gübür (Holistic SEO), en resumen propio:

- **Entidad central y contexto de fuente**: define de qué va el sitio (la entidad) y desde qué
  ángulo comercial lo cubre (el contexto). Una empresa de software a medida no cubre "software" en
  general; cubre software a medida visto desde quien lo paga.
- **Sección núcleo y sección externa**: el núcleo monetiza y recibe los enlaces internos; la
  externa aporta cobertura y los manda hacia el núcleo.
- **Red de contenido semántica**: cada página responde a una pregunta con su propio vocabulario y
  enlaza a las vecinas por relación de atributos, no por "artículos relacionados".
- **Ritmo de publicación** como señal: publicar el mapa en bloque en vez de a goteo. Esto es
  afirmación del autor, grado D.

Qué me quedo: la disciplina de definir el tema y el ángulo antes de escribir, y la jerarquía
núcleo-externa. Qué no me creo: que sus casos de "ranking sin enlaces" sean generalizables. Son
estudios de caso propios sin grupo de control.

---

## 3. Arquitectura de enlaces internos

### Lo que está confirmado — grado B

Google recomienda la estructura de enlaces internos también para aparecer en las funciones de IA
([AI features, act. 10-dic-2025](https://developers.google.com/search/docs/appearance/ai-features)).
El texto de ancla es parte de la topicalidad (la A del ABC del juicio).

### Lo que está medido — grado C

Estudio de Zyppy (Cyrus Shepard): **23 millones de enlaces internos, 1.800 sitios, ~520.000 URLs**,
cruzado con clics de Search Console ([Zyppy](https://zyppy.com/seo/seo-study/)). Hallazgos:

- Más **variedad** de textos de ancla hacia una URL correlaciona con más tráfico, y la relación
  aguantó al quitar la mitad de las URLs como valores atípicos.
- Las páginas con al menos un ancla interna de concordancia exacta tenían unas **5 veces** más
  tráfico que las que no.

Es correlación: las páginas importantes reciben más enlaces porque son importantes. Pero la
dirección coincide con el juicio, y el coste de hacerlo bien es cero.

### Reglas que aplico

1. Cada página de dinero recibe enlaces desde todas las piezas que tratan su tema, con anclas
   variadas y al menos una exacta.
2. Enlaces en el cuerpo del texto, no solo en menú y pie.
3. Ninguna página importante a más de tres clics de la portada.
4. Ninguna página huérfana. Una URL en el sitemap sin enlaces internos es una señal contradictoria.

---

## 4. SEO programático sin que acabe en spam

Programático = generar muchas páginas desde una base de datos con una plantilla. Funciona cuando
cada combinación responde a una búsqueda real y tiene datos distintos. Se convierte en spam cuando
cambia solo el nombre de la ciudad.

Las dos políticas que lo alcanzan ([spam policies](https://developers.google.com/search/docs/essentials/spam-policies), grado B):
**contenido a escala** y **páginas puerta**. Ejemplo textual de puerta en la política: varias
páginas dirigidas a ciudades o regiones que embudan a una sola.

Prueba que hago antes de aprobar un proyecto programático:

| Pregunta | Si la respuesta es no |
|---|---|
| ¿Cada página tiene datos que no están en ninguna otra (precios, stock, horarios, casos, cifras)? | Es plantilla con relleno. No |
| ¿Existe búsqueda real para cada combinación, o solo para la genérica? | Sobran páginas |
| ¿Un humano elegiría llegar a esa página y no a la genérica? | Puerta |
| ¿Se puede retirar de golpe sin perder nada? | Entonces no aporta |

Para un negocio local con una sola sede: páginas por ciudad sin presencia real en esa ciudad son
el ejemplo de manual de página puerta. Para un B2B: páginas por sector solo si hay caso o
funcionalidad distinta por sector.

---

## 5. Lo que enseñan los cursos (temario, no contenido)

Extraigo solo lo que cada uno enseña que no es obvio. Grado de lo que prometen entre paréntesis.

| Curso | Qué enseña que no es obvio | Cuidado con |
|---|---|---|
| **Guía de inicio de Google** (gratis) | Una sección entera de cosas en las que no gastar tiempo: meta keywords, recuento de palabras, orden de encabezados, dominio con palabra clave, E-E-A-T como factor ([act. 10-dic-2025](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)) (B) | Es básica a propósito. Lo que calla importa tanto como lo que dice |
| **Ahrefs Academy** (gratis) | Elegir temas por potencial de tráfico del tema entero, no del volumen de una palabra; "business potential" (puntuar cada tema por lo cerca que está del producto) (C) | Todo acaba en su herramienta y en DR, que no es de Google |
| **Semrush Academy** (gratis, con certificados) | Investigación de intención y agrupación de palabras por SERP compartida; auditoría técnica con checklist (C) | Mismo sesgo hacia su métrica (Authority Score) |
| **Moz** (Beginner's Guide, Whiteboard Friday) | Buena base conceptual; la historia de cómo se llegó a cada práctica (C) | Inventó el DA. Moz dice que no es de Google; la industria lo olvida |
| **Kyle Roof** (Internet Marketing Gold, PageOptimizer Pro) | Pruebas de una sola variable en dominios de ensayo; patentó el método en 2020. El caso famoso: rankear "rhinoplasty Plano" con una web en lorem ipsum y la palabra clave en las posiciones justas (D sobre generalización) | Demuestra que la on-page mueve la aguja en consultas con poca competencia. No demuestra que funcione en SERPs disputadas ni que dure. Sus "términos a incluir" son densidad con otro nombre |
| **Matt Diggity** (Affiliate Lab) | SEO para afiliación basado en pruebas, rediseño de páginas por conversión, auditorías de enlaces (D) | Históricamente ha enseñado redes privadas de blogs (PBN), que violan la política de enlaces. Nicho afiliación, no servicios |
| **Koray Tuğberk Gübür** (Topical Authority, Semantic SEO) | Mapa temático, entidad central, contexto de fuente, red semántica (ver §2). El marco más útil de los de pago para decidir qué escribir y en qué orden (D sobre resultados) | Jerga propia densa; casos sin control; la parte de "frecuencia de publicación" no tiene soporte |
| **Sterling Sky / Joy Hawkins** (SEO local) | Pruebas publicadas campo a campo del Perfil de Empresa; cuál mueve ranking y cuál no. El mejor corpus de pruebas de local que hay (C, con método visible). Ver [23](23-seo-tecnico-local-y-ia.md) | EE. UU. y Canadá; el mercado español tiene menos competencia en reseñas y los umbrales cambian |

Lo que tienen en común los de pago: venden certeza sobre un sistema que ni Google describe con
pesos. Uso el método (cómo decidir, cómo probar) y descarto las cifras.

---

## 6. Qué contenido escribir, en orden

Para un sitio de servicios con presupuesto limitado:

1. **Páginas de dinero**: una por servicio, que respondan a la búsqueda comercial. En local es el
   factor número uno de ranking orgánico según Whitespark 2026 (ver [23](23-seo-tecnico-local-y-ia.md)).
2. **Páginas de decisión**: precio, comparativas con alternativas, "cómo elegir", objeciones. Son
   las que lee alguien a punto de comprar y las que casi nadie escribe con cifras reales.
   Conecta con la inoculación de [19](19-nutricion-y-secuencias.md): plantear la objeción y
   responderla también funciona en una página.
3. **Casos con datos**: la prueba de experiencia de primera mano. Detalle verificable, nombre del
   cliente si lo permite.
4. **Contenido informativo**: solo si alimenta a 1-3 con enlaces internos, y sabiendo que es donde
   más muerden los AI Overviews (ver [23](23-seo-tecnico-local-y-ia.md)).

Orden inverso al que sigue casi toda agencia, que empieza por el blog.

---

## 7. Lo que sale de todo esto

1. **Menos páginas, mejores.** La calidad por sitio hace que el relleno reste.
2. **Autoridad temática es profundidad y coherencia, no volumen.** Grado C como sistema.
3. **Enlazar por dentro con anclas variadas** es la palanca más barata del SEO.
4. **Programático solo con datos únicos por página.** Ciudades sin presencia real, no.
5. **De los cursos, el método sí, las cifras no.**
6. **Empezar por páginas de dinero y de decisión**, no por el blog.
