# Fase 0 — Contexto del negocio · Fase 1 — Auditoría inicial

Fuente principal: Peter Raventós (bloques 1 y 4 de su curso). Complementos de Surfer (Screaming Frog, local SEO).

## Fase 0: contexto del negocio (la base de todo)

La regla fundamental del SEO en Google, Bing y la IA es la misma: contenido relevante y ORIGINAL que resuelva lo que busca el usuario. La IA no puede generar contenido original de un negocio que no conoce. Por eso el primer paso no es tocar la web: es capturar el conocimiento que solo tiene el dueño.

### Procedimiento

1. **Grabar un audio largo** (el dueño del negocio, con la grabadora del móvil; Peter lo hizo en un trayecto de coche de 3 horas) contestando, como mínimo:
   - Qué es el negocio y cómo funciona; historia y origen.
   - Quién participa; quién es el cliente ideal y potencial.
   - Qué busca un usuario en este negocio y CÓMO lo buscaría (con sus palabras).
   - Qué experiencia tiene un cliente; qué dicen los clientes de bueno.
   - Quién es la competencia; por qué contratarle a él y no a otro; qué competencia no está a la altura.
   - Decisiones internas que hacen el producto/servicio exclusivo; diferenciales reales.
2. **Transcribir** el audio. (Peter usa TurboScribe; en el entorno de Diego la transcripción va SIEMPRE en local con Whisper — norma propia, no del curso.)
3. **Crear un proyecto de IA** (Claude Projects o equivalente) con:
   - Instrucciones: "asistente experto en SEO moderno, GEO y marketing de contenidos" + el guion metodológico (esta skill cumple ese papel).
   - Archivos: la transcripción del negocio + cualquier documentación del negocio.
4. **Conectores si existen** (Ahrefs, SE Ranking, DataForSEO, Apify…): dárselos al proyecto para que tire de datos reales. Sin ellos también funciona.
5. Cada tarea SEO posterior (contenidos, análisis de keywords, resolver errores de auditoría) se pide en un chat nuevo dentro de ese proyecto, que ya tiene el contexto.

**Por qué importa**: de esta transcripción salen las *hidden gems* (gemas ocultas) — información que solo tiene este negocio — que son lo que diferencia el contenido en las fases 5-6 y lo que la IA y Google premian frente al contenido genérico.

## Fase 1: auditoría inicial

Objetivo: foto del punto de partida y corrección de errores estructurales ANTES de invertir en contenidos. Arreglar errores muchas veces mejora la indexación por sí solo. Con clientes: primero auditar y corregir, luego contenidos.

### Herramientas

- **Katapulta** (la que usa Peter; gratuita): se le da la URL, define proyecto (descripción, industria, nicho, servicios, ubicación, modalidad) — REVISAR y editar lo que autodetecta, porque se equivoca con servicios que no son core (ej.: detectaba "foodtruck" como servicio cuando solo es un cruzado de las bodas). Devuelve errores clasificados (rojo = ya, naranja = cuando se pueda) y, a diferencia de otras herramientas, explica CÓMO arreglar cada uno. Incluye apartado específico de IA (robots, acceso de bots).
- **Screaming Frog SEO Spider** (la que usa Surfer; gratis hasta 500 URLs): rastrea el sitio y devuelve lista priorizada de problemas técnicos.

### Qué revisar (checklist de la auditoría)

- **Códigos de respuesta / errores 404**: páginas internas que devuelven 404 pierden autoridad y bloquean a usuarios y a Google → redirección 301 (ver fase 10, Rank Math).
- **Enlaces rotos** internos.
- **Titles**: longitud incorrecta, duplicados. Solo prioridad en páginas estratégicas; el resto puede esperar.
- **Meta descriptions** ausentes o duplicadas.
- **Páginas noindex**: no es error per se — verificar que lo que está fuera del índice debe estarlo (una página legal noindex está bien) y que lo importante SÍ está indexado.
- **Encabezados**: varios H1, jerarquías rotas, duplicados entre idiomas.
- **Idiomas**: discrepancias hreflang/estructura si hay multi-idioma.
- **robots.txt**: comprobar que no se bloquea a bots necesarios (Googlebot, bots de herramientas SEO, bots de IA). Algunos hostings traen bloqueos por defecto.
- **Imágenes**: peso y alt (se ejecuta en fases 6 y 10).

### Cómo trabajar los errores

Pegar los errores de la auditoría en el proyecto de IA de la fase 0 y pedir el plan de corrección uno a uno. La auditoría NO impide avanzar con el resto de fases; lo grave (rojo) se arregla ya, el resto en paralelo.

### Nota de SEO local (Surfer)

Si el negocio tiene ubicación física: reclamar el **Google Business Profile**, rellenar todos los campos, conseguir el máximo de reseñas y responderlas todas. Solo eso ya mete al negocio en el map pack de las búsquedas "cerca de mí". El mapa también es SEO: Google Maps es un buscador de ubicaciones (The BIG).
