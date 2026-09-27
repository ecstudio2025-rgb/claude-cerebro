# Fases 2-4 — Keyword research · Intención de búsqueda · Arquitectura SEO

Fuente principal: The BIG (el bloque más fuerte de su curso). Marcos de priorización de Surfer. Complementos de Peter (Katapulta, SE Ranking).

## Fase 2: keyword research

Una keyword es la conexión con el cliente potencial y delata su intención. Todo lo que se haga en la web se trabaja contra keywords con demanda demostrada — nunca contra ideas de keywords que sugiera una IA sin histórico de búsquedas.

### El método del planificador de Google Ads (gratis, The BIG)

1. **Semilla**: preguntar al cliente en la reunión de arranque: «¿cuáles crees que son tus webs de competencia?» y «si tuvieras que elegir UNA búsqueda para salir el primero, ¿cuál?». La respuesta rara vez es la keyword buena, pero da la palabra core desde la que ramificar. Otras fuentes de semillas: web de la competencia, ChatGPT/Gemini para brainstorming (solo ideas, no volúmenes).
2. Google Ads → Herramientas → **Planificador de palabras clave** → «empezar con una palabra clave». Configurar idioma y país reales del proyecto.
3. **Dos filtros que cambian el trabajo**:
   - *Excluir palabras clave del plan*: cada keyword que añades al plan desaparece de la lista — no revisas dos veces lo mismo.
   - *Palabra clave no contiene*: lista de negativas separadas por comas (ej. «verdura, verduras, merca, patatas», marcas de competencia). Limpia la lista de ruido no cualificado.
4. Revisar el listado y **añadir al plan solo tráfico cualificado** (el que puede convertir para ESTE negocio). Posicionar «mayorista de verdura» vendiendo fruta es tráfico que no compra.
5. **Iterar**: re-sembrar con las keywords buenas que aparezcan (ej. «fresas al por mayor» genera sus propias sugerencias). El research termina cuando ya no salen sugerencias nuevas que añadir.
6. **Descargar** desde "palabras clave guardadas" eligiendo las opciones de abajo (Excel o Google Sheets) que incluyen los 12 meses — no la media suelta: se necesita la **estacionalidad**.
7. Maquetar: columna keyword, media mensual ordenada desc., 12 columnas de meses con gradiente de color (verde el mes pico), y columna de variación interanual (qué keywords crecen o caen).

**Aviso sobre volúmenes**: sin campañas activas en la cuenta, Google da rangos (10-100) en vez de números exactos. Da igual: lo que importa es que la keyword TENGA demanda, no el número exacto.

**Estacionalidad**: ningún sector es lineal. Conocer los meses pico y valle evita diagnosticar como problema una caída de agosto que es estacional.

### El marco de evaluación (keyword sweet spot, Surfer)

Cada keyword se puntúa en cuatro atributos:
1. **Demanda** — ¿la busca alguien? Sin búsquedas, rankear #1 no aporta.
2. **Fit** — ¿en qué punto del funnel cae y qué relación tiene con lo que vendes?
3. **Intención** — ¿qué quiere el que busca y puedes dárselo? (si la SERP la dominan vídeos, toca hacer vídeo).
4. **Dificultad** — ¿puedes rankearla con tu autoridad actual? Una web nueva no le gana a Amazon «zapatillas running», pero sí «zapatillas running pies planos invierno».

Regla para sitios nuevos: **empezar por long tail** (menos volumen, intención clarísima, competencia manejable) y escalar a las short tail cuando haya autoridad. Mil long tails valen más que dos short tails, aunque la visibilidad de una short tail no es despreciable.

Tipos de intención (nomenclatura Surfer): **informacional** (aprender), **comercial** (comparando opciones, dispuesto a gastar), **transaccional** (listo para comprar), **navegacional/marca** (busca una web concreta).

### Herramientas alternativas de research

- Google Search Console (si la web ya existe): la mejor fuente — qué buscan de verdad para encontrarte.
- Autocompletar de Google, «Preguntas frecuentes» (People Also Ask), «Búsquedas relacionadas» al pie.
- Subreddits/foros del sector: el lenguaje literal del cliente.
- Pegar el sitemap propio (o del competidor) a una IA y pedir huecos de contenido.
- Katapulta (Peter): sección keywords → propone estructura con intención clasificada por página.
- SE Ranking / Ahrefs: volumen, dificultad, keywords similares — usar la que ya se pague.

## Fase 3: intención de búsqueda (la piedra filosofal)

Sin identificar intenciones no hay proyecto: el listado de keywords se convierte en arquitectura AGRUPANDO por intención, y cada página trabaja UNA intención de búsqueda. No se agrupa por sinónimos ni por "entidades semánticas": solo por intención.

### El test de la SERP (manual, no delegable a la IA)

1. Abrir **ventana** de incógnito nueva (ventanas, no pestañas: una pestaña reutilizada ya arrastra cookies e historial de la sesión).
2. Buscar la keyword tal cual. Mirar el top 10: qué webs y QUÉ PÁGINA de cada web sale.
3. Cerrar la ventana. Abrir OTRA ventana de incógnito y buscar la segunda keyword.
4. Comparar: si los dos top 10 se parecen (mismas páginas aunque cambie el orden) → **misma intención → una sola página**. Si no se parecen → intenciones distintas → páginas distintas.

Con el mismo test se clasifica informacional vs transaccional: SERP de blogs, guías y AI Overview → informacional; SERP de fichas, listados de empresas, formularios y map pack → transaccional. Los anuncios se ignoran (los puso una persona que puede equivocarse). Si 9 de 10 resultados son de un tipo, la keyword es de ese tipo.

**No pedirle esta clasificación a una IA**: no está viendo los resultados reales de Google. Muchas veces el sentido común basta y no hace falta el test; ante la duda, un minuto de incógnito la resuelve.

## Fase 4: arquitectura SEO

La arquitectura es el organigrama de páginas de la web, y **no se define por sentido común ni por el catálogo: se define por la demanda**. El SEO conecta oferta con demanda.

- **Home** = la intención más genérica del negocio (todas las variantes de «mayorista de fruta», «proveedor de frutas», «frutas al por mayor»… suman su volumen en una sola página).
- **Categorías de primer nivel** = cada intención transaccional con demanda propia (cerezas al por mayor, naranjas al por mayor…), enlazadas desde el menú.
- **Subcategorías** cuando una intención hija tiene demanda propia (plátano macho al por mayor cuelga de plátanos al por mayor).
- Error típico: una página "servicios" con todos los servicios listados = varias intenciones en una página = no posiciona ninguna. Cada servicio, su página.
- Error inverso: 98 keywords ≠ 98 páginas. Agrupadas por intención pueden quedar en 15-20 páginas.
- El usuario no navega catálogos: busca «chaqueta mujer invierno» y entra DIRECTO a esa página de categoría. Si no existe, entra en la de la competencia.
- Sectores grandes (moda: research de 10.000 keywords) generan arquitecturas gigantes — el trabajo de agrupar toma horas y se hace UNA vez, al inicio. Es elegir los ladrillos de la casa.
- **Transaccional en páginas / informacional en el blog.** El contenido informativo alimenta el funnel y enlaza hacia las páginas de venta (ver fase 5).

Entregable de la fase: diagrama/árbol con todas las páginas, su intención agrupada, el volumen sumado de cada grupo y la jerarquía de enlazado. Después (fases 5-6) se ejecuta: «el Excel no consigue resultados».
