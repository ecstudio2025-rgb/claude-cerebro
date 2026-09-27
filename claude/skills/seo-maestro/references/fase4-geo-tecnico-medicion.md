# Fases 9-11 — GEO / SEO en IA · Técnico y velocidad · Medición

Fuentes: Peter (el bloque de IA más detallado y el stack WordPress), Surfer (AI search, tracking de visibilidad), The BIG (customer journey con LLMs).

## Fase 9: GEO / SEO en IA (ChatGPT, Perplexity, Gemini, AI Overviews)

### El marco (en lo que los TRES cursos coinciden)

- **El SEO tradicional es la base del posicionamiento en IA.** ChatGPT usa el índice de Bing cuando busca; Perplexity rastrea pero se apoya en índices existentes; la mayoría de URLs citadas en AI Overviews ya están en primera página de Google. Si no apareces en Google/Bing, eres invisible también para la IA.
- Google publicó que "el GEO no existe": es el SEO de siempre. Matiz real: hay pequeñas prácticas que mejoran visibilidad en LLMs sin mover nada en Google.
- La IA se come sobre todo tráfico **informacional** (AI Overviews resuelven la consulta sin clic). El transaccional apenas se solapa: la IA informa y compara, pero la compra/contratación acaba en Google o en la web. El viaje típico hoy: conversar con ChatGPT para decidir → ir a Google → convertir. Ese clic llega mucho más convencido, por eso el tráfico procedente de LLMs convierte más.
- Zero-click: los AI Overviews ya salen en gran parte de las búsquedas y recortan el CTR del #1 orgánico. La respuesta no es huir: es ser la fuente citada y hacer contenido más profundo que el resumen de la IA para ganarse el clic.

### Prácticas que sí mueven en LLMs

1. **Answer capsules**: bajo cada H2 tipo pregunta, responder PRIMERO en 25-30 palabras, directo y citable, y luego desarrollar. Colocar lo importante en el primer tercio del texto (las citas de los LLMs salen desproporcionadamente del principio y de estos formatos de respuesta).
2. **Contenido verificable**: citar fuentes externas con nombre, estadísticas propias, citas de expertos. «El SEO es importante» no es citable; «solo un pequeño porcentaje de usuarios pasa a la segunda página, según [fuente]» sí.
3. **Frescura**: el contenido actualizado se cita mucho más. Un artículo «mejores agencias 2022» se actualiza al año en curso o muere.
4. **Entidad de marca** (EEAT ampliado): trabajar la marca como entidad con contexto (quién, certificaciones, relaciones), no solo keywords sueltas.
5. **Esquemas** (fase 7) y estructura clara de encabezados: los LLMs parsean mejor lo bien estructurado.
6. **llms.txt** en la raíz del hosting (Rank Math lo genera): evidencia discutida — hay quien demuestra que no sirve y Google lo ignora, pero Perplexity parece consultarlo. Cuesta un minuto: ponerlo "por si acaso".
7. **Roundups y comparativas**: los LLMs favorecen artículos "mejores X" — salir en ellos (o escribirlos) multiplica las menciones. Buscar en qué consultas citan a la competencia y a ti no, y convertir eso en lista de outreach.
8. **Topical authority** (fase 5): cubrir el tema desde todos los ángulos hace que el modelo te reconozca como autoridad.

### Cómo medir la parte de IA

- No existe un "Search Console de ChatGPT": nadie fuera de OpenAI/Perplexity ve los prompts reales. Las herramientas de visibilidad IA (AI tracker de Surfer y equivalentes) monitorizan PROMPTS concretos que tú defines y te dicen si tu marca aparece y cómo evoluciona frente a competidores. Es referencia, no exposición real.
- Comprobación manual gratuita: ventana de incógnito, preguntar a ChatGPT/Perplexity las preguntas de compra de tu sector y ver qué marcas salen. Esa es tu competencia en IA.
- **GA4** (ver fase 11): con fuente/medio de sesión se ve el tráfico que llega desde chatgpt.com, gemini, perplexity, copilot…

## Fase 10: SEO técnico y velocidad

Para pymes en WordPress/Shopify/Webflow, el 90% del técnico ya viene resuelto; lo que frena a un principiante no es el técnico, es no haber publicado nada. Lo esencial:

### Errores de URL y redirecciones (Rank Math → módulo Redirections)

- **404** → redirección **301** (permanente) hacia la página equivalente o más parecida (producto descatalogado → producto similar). La 302 (temporal) solo para ausencias temporales; en la práctica casi siempre 301.
- **Cadenas de redirección** (A → B → C): Google lo marca como error; apuntar A → C directamente.
- Rank Math permite redirecciones una a una o importadas en dos columnas (origen, destino), con reglas exactas o por patrón.

### Rastreo e indexación

- **robots.txt** editable desde Rank Math (sin tocar hosting): verificar que no bloquea bots necesarios.
- **Sitemap** generado por Rank Math → enviarlo a Google Search Console.
- htaccess y llms.txt también editables desde Rank Math si hacen falta.

### Velocidad / Core Web Vitals (afectan al ranking y a la experiencia)

Stack recomendado en WordPress (Peter):
- **WP Rocket**: minificar CSS, minificar JS, carga diferida de JS, retrasar ejecución JS, lazy load de imágenes, precarga de caché; integración con Cloudflare/CDN si existe. Método seguro: activar opción → borrar y precargar caché → mirar la web → si algo se rompe, desactivar y borrar caché. No hay riesgo permanente.
- **Imagify** (misma casa): optimiza todas las imágenes existentes (3-4× menos peso o más), las convierte a WebP y optimiza automáticamente cada imagen nueva que se suba.
- **Medir con GTmetrix** (o el informe integrado en WP Rocket): objetivo, todo en verde; los sospechosos habituales son CSS, JS e imágenes.

## Fase 11: medición

### Google Search Console (obligatoria, gratis)

- Alta de propiedad por dominio → verificación con registro TXT en el DNS (pedirle a la IA el paso a paso para el proveedor concreto es más rápido que pelearse con paneles).
- A los pocos días: clics, impresiones, CTR medio, consultas que activan la web, páginas más vistas, países, estado de indexación, Core Web Vitals. Son datos internos REALES — la fuente de verdad.

### Rank tracker (SE Ranking o equivalente)

Solo sigue las keywords que le declares (si no se la das, no existe para él). Útil como vista externa e intuitiva de posiciones, y para ver keywords que aún no asoman en GSC.

### Google Analytics 4

- Alta de cuenta y propiedad web → instalar el código (Rank Math permite vincular Analytics o pegar el código de seguimiento sin plugins extra).
- Informes → Adquisición → Adquisición de tráfico → cambiar dimensión a **fuente/medio de la sesión** y ampliar filas: ahí aparecen chatgpt, gemini, bing, copilot, perplexity… — la forma real de ver cuánta gente llega desde las IAs.
- Recordar: organic search = SEO; el ratio de conversión por canal vale más que el volumen. Y antes de diagnosticar una caída, comprobar la estacionalidad del research (fase 2).

### Ritmo de evaluación

El SEO tarda meses (a veces un año). Señales tempranas de que la dirección es buena: impresiones subiendo aunque los clics no, keywords nuevas apareciendo en GSC, posiciones migrando de página 5 a página 3. Enlaces comprados: medir efecto a ~2 semanas (fase 8).
