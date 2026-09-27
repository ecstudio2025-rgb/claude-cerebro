# Fases 5-7 — Estrategia de contenidos · On-page · Datos estructurados

Fuente principal: Surfer (priorización, checklist on-page) y Peter (EEAT, hidden gems, schema, flujo con IA). The BIG aporta la separación transaccional/informacional.

## Fase 5: estrategia y creación de contenidos

### Priorización: de abajo arriba en el funnel (Surfer)

1. **Money pages primero.** Las páginas que convierten directamente: producto, servicio, precios, features. Keywords transaccionales o comerciales. Son el cimiento; sin ellas, todo el tráfico del mundo no vale nada. Error clásico: empezar por 10 posts informacionales «porque tienen volumen» y preguntarse por qué nadie compra — no había dónde convertir.
2. **Un cluster temático cada vez.** Elegir UN cluster conectado a una money page y construir su funnel completo: la money page (transaccional) → contenido comercial de comparación que enlaza hacia ella («mejor X», «X vs Y») → contenido educativo top-of-funnel. Cada pieza enlaza a la de abajo y a sus hermanas: eso es un **topic cluster**.
3. **Repetir cluster a cluster.** Terminar uno antes de empezar el siguiente. Saltar de tema en tema (ordenar el research por volumen/dificultad y tirar de lista) reparte el esfuerzo entre demasiados temas y retrasa resultados.

**Topical authority**: Google no evalúa páginas aisladas. Ante «cómo prevenir X», comprueba si el sitio también cubre «qué es X», «señales de X», «checklist de respuesta a X»… — el mismo usuario en fases distintas del mismo problema. Cubrir el viaje completo hace más fácil rankear TODO el cluster, incluidas las keywords duras. También es señal de autoridad para los LLMs (ver fase 9).

**Keyword top-of-funnel con plan** (caso PandaDoc): una keyword informacional masiva puede alimentar el negocio si hay camino de conversión detrás (descarga → email → nurture → alta). Una keyword sin camino de conversión es tráfico de vanidad. Caso Counter Culture: autoridad construida con guías de preparación de café → la venta llega después. Decidir SIEMPRE qué pasa después de que alguien aterrice.

### Separación de formatos (The BIG + Peter)

- **Transaccional → página** orientada a venta: explicar el servicio + CTA claro (formulario/contacto).
- **Informacional → blog** orientado a informar: tráfico frío en fase temprana de decisión.
- Cada cosa en su sitio; el blog enlaza hacia las páginas de venta («te explico los precios de una boda… y por cierto, aquí puedes casarte: enlace»).

### Cómo se crea una pieza (4 pasos, Surfer)

1. **Investigar**: abrir los 5 primeros resultados de la keyword y leerlos ENTEROS. Anotar: qué temas cubren todos (imprescindibles), qué les falta (tu hueco), longitud media (benchmark de exhaustividad), ángulos únicos. Hacerlo a mano las primeras veces para entender qué se automatiza después.
2. **Estructurar**: outline que responda a la intención antes de escribir una línea. Se puede pedir a la IA a partir de las notas de investigación.
3. **Escribir**: la IA como andamio (estructura, definiciones, fluidez) + **capa humana obligatoria**:
   - Experiencia propia: qué pasó cuando lo hiciste.
   - Opinión: qué está sobrevalorado o mal.
   - Datos propios: resultados, experimentos, casos, conversaciones con clientes.
   - Citas de expertos (pueden venir de podcasts, libros, papers — no hace falta que sean tuyas).
   - Ejemplos concretos: negocios reales, números reales.
4. **Optimizar**: contra datos, no intuición (cobertura de temas y términos vs el top de la SERP; herramientas tipo Surfer lo puntúan, pero el criterio es replicable a mano).

**Sobre la IA y las penalizaciones** (Peter): usar IA no penaliza; penaliza el contenido pobre copiado y pegado sin capa propia. La mayoría del contenido fracasa no por malo sino por IGUAL al resto. El listón no es «bueno»: es claramente mejor que lo que ya existe para esa búsqueda. El conocimiento único del negocio (hidden gems de la fase 0) es el foso defensivo.

### EEAT (Experience, Expertise, Authority, Trustworthiness)

Validar el contenido con señales de identidad y experiencia:
- **Autor real con página de autor** en la web: quién es, trayectoria, certificaciones, fotos, enlaces a perfiles (LinkedIn/redes). Los artículos enlazan a esa página.
- **Fecha visible** en cada artículo y contenido actualizado (la frescura pesa, sobre todo en IA — fase 9).
- **Transparencia comercial**: precios publicados, tablas comparativas «por qué yo y no otro», reseñas de clientes, equipo visible. Peter: publicar precios hace que la IA te recomiende cuando alguien pregunta por alternativas más baratas.
- Tablas, citas y referencias externas verificables en el contenido informativo.

### Flujo práctico con el proyecto de IA (Peter)

Con el proyecto de la fase 0 cargado de contexto, pedir por página: metas (title + description) → encabezados → redacción del contenido transaccional → propuesta visual por bloques (hero, secciones, CTA final, enlazados internos sugeridos, checklist on-page). Si la IA vaguea o alucina con todo junto, pedirlo por fases. Implementación en WordPress: Rank Math para metas/schema + el builder que use el proyecto (Elementor u otro), marcando explícitamente qué texto es H1, cuál H2, etc. Shopify/PrestaShop tienen funciones equivalentes nativas o por app. Ignorar los semáforos de colores de Rank Math si la implementación sigue esta checklist.

## Fase 6: on-page (checklist por página)

- **Title**: keyword al principio, < 60 caracteres, que apetezca clicar. En money pages puede ser keyword + beneficio (vende, no solo describe). Único por página.
- **Meta description**: 150-160 caracteres, redactada como copy de anuncio, con la keyword y lo que el usuario va a encontrar. No es factor de ranking directo, pero mueve el CTR. Única por página.
- **H1**: uno solo por página, único en el sitio (que no se repita entre páginas), normalmente espejo del title.
- **Jerarquía de encabezados**: H2 para secciones, H3 anidados bajo su H2. Errores a evitar: varios H1; H3 colgando directo de H1; marcar como heading bloques decorativos («Contacta») que no aportan estructura — eso es párrafo.
- **URL**: corta, descriptiva, con la keyword, categorizada (`/categoria/keyword`). Nada de cadenas aleatorias del CMS.
- **Enlazado interno**: enlaces contextuales dentro del cuerpo hacia páginas relacionadas y hacia las money pages. Es como se conectan los clusters y una de las tácticas con mejor ratio esfuerzo/valor de todo el SEO. No publicar sin enlazar.
- **Imágenes**: nombre de archivo descriptivo, alt que describa la imagen como a quien no puede verla (accesibilidad real + contexto para Google), comprimidas, formato WebP. No repetir el mismo alt en todas (error visto incluso en sitios bien optimizados). Nota: Peter matiza que el alt hoy pesa menos que antes; se pone igual porque es barato y correcto.

## Fase 7: datos estructurados (schema)

Información estructurada que ayuda a Google Y a los LLMs a entender la página. Implementación sin código con **Rank Math** (WordPress); validación con un Schema Validator pegando la URL.

Esquemas que suman:
- **Organization**: datos de la empresa.
- **WebPage / Service / Product** con precio y **reviews** → opción de rich snippet con estrellas en la SERP (más CTR y más confianza; a menudo eres el único del top 10 que las tiene).
- **FAQ**: preguntas frecuentes — especialmente relevante para la IA.
- **Author / Person**: enlaza con la estrategia EEAT.
- Tablas y comparativas marcadas.

Cuantos más datos estructurados correctos, mejor; todo suma. Matiz honesto (Peter): quien dice que «el schema ahora posiciona en ChatGPT» suele ser quien nunca lo tuvo hecho — el schema tocaba desde siempre; hacerlo ahora simplemente corrige un atraso.
