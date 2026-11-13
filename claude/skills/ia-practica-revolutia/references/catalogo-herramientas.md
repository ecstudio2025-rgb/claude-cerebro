# Catálogo de herramientas y técnicas (reels de @revolutia.ai)

Sacado de 217 reels (172 guiones distintos, del 14-ene al 14-sep-2026) transcritos el 13-nov-2026. 200 entradas con valor 2 o más sobre 5, ordenadas por valor y después por likes del reel.

- **Valor** es la utilidad para ECSSTUDIO y Custom Soft Lab, no la que vende el creador.
- **Ya lo tenemos** apunta a la skill o herramienta instalada que lo cubre.
- Las estrellas y la licencia de GitHub se comprobaron el 13-nov-2026. Los reels exageran las cifras y a veces se equivocan de nombre.
- Antes de instalar algo nuevo: estrellas, licencia, última actividad y qué scripts o hooks ejecuta. Un hook de SessionStart cambia todas las sesiones de todo el equipo.

## Ventas y prospección (22)

### Claude Cowork: prompt único de prospección con auditoría y demo  ·  valor 5  ·  prompt
Un prompt multi-paso: elegir ubicación y tipo de negocio, busca negocios con buenas reseñas y web mediocre, audita la web, monta landing y redacta email con los fallos.
- Cómo: Prompt de una sola vez con pasos: 1) investigar negocios del filtro, 2) elegir uno con buenas reseñas y web floja, 3) auditoría con informe de fallos (sin prueba social, CTA mal colocado), 4) landing de una página con datos reales, 5) email con problemas y demo.
- Para nosotros: Encaja con el módulo Comercial del OS de CSL (analizar web) y la oferta de rediseño de landing de ECS.
- Ojo: Uso de datos de negocios ajenos en una demo no solicitada; email en frío con RGPD/LSSI. Revisar el contenido antes de enviar.
- Reels: G69 · 277 likes

### Valor de Retorno (VR) en la primera línea de la propuesta  ·  valor 5  ·  tecnica
Poner arriba de la propuesta el beneficio económico cuantificado en vez de la descripción del servicio, para pasar de competir por precio a competir por valor.
- Cómo: Calcular: horas ahorradas por semana x coste hora x semanas = ahorro anual por empleado (ejemplo del guion: 10 h/semana x 20 euros = 2.400 euros al año por empleado). Poner esa cifra como primera línea de la propuesta en lugar de implementar un sistema automatizado y personalizado.
- Para nosotros: ECS: encabezar propuestas Sprint 360 con euros cobrados/ahorrados esperados por euro invertido (coherente con la regla x2). CSL: propuestas de ERP con horas ahorradas y coste de errores por empleado.
- Ojo: El ejemplo de 800 a 4.000 euros y el alumno Javi son anecdóticos sin verificación. Usar cifras reales del cliente, no promesas.
- Reels: G7 · 85 likes

### CRM open source alternativo a Salesforce  ·  valor 4  ·  repo-github
CRM open source autoalojado con las funciones de Salesforce, personalizable con Claude Code. El guion no da el nombre (probablemente Twenty, no confirmado).
- Cómo: Desplegarlo en servidor propio y customizarlo con Claude Code.
- Para nosotros: CSL: servicio vendible, montar CRM a medida para clientes (alineado con el OS CSL). ECS: alternativa a GHL para clientes.
- Ojo: Nombre no confirmado; comprobar licencia antes de revenderlo, mantenimiento y seguridad recaen en nosotros.
- Reels: G124 · 3512 likes

### Vibe Prospecting (conector de Explorium para Claude)  ·  valor 4  ·  mcp
Conector que convierte el chat en generador de leads: describes el perfil y devuelve lista verificada con emails directos (100 M de empresas).
- Cómo: Prompt literal: 'Encuéntrame 5 agencias inmobiliarias en Valencia con menos de 20 empleados y el email directo del dueño.'
- Para nosotros: Prospección de ECS (pymes locales) y CSL (empresas que necesitan ERP). Comparar con Apollo/Clay ya conectados.
- Ojo: Datos personales (RGPD, prospección en frío en España requiere base legítima). Posible coste por créditos. El guion lo llama 'ByProspecting'.
- Reels: G62 · 2664 likes

### Apify MCP para prospección con Claude  ·  valor 4  ·  mcp
Conecta Apify (scrapers/actors) con Claude para que busque leads y devuelva perfil, punto de dolor, oportunidad y ángulo de contacto.
- Cómo: Conectar Apify en Claude y escribir: encuentra 15 leads cualificados para mi servicio de automatización de IA de clínicas usando Apify.
- Para nosotros: ECS/CSL: listas por nicho (reformas, clínicas, concesionarios) con ángulo de contacto para la plantilla de primer mensaje.
- GitHub: apify/apify-mcp-server · 15.999 estrellas · licencia MIT
- Ojo: Repo deducido, verificar. Scraping de Google Maps/LinkedIn puede violar términos; tratamiento de datos personales. Pide token de Apify y consume créditos.
- Ya lo tenemos: viral-profile-scraper (Apify)
- Reels: G39 · 1067 likes

### Apify + Claude para prospección (Google Maps, LinkedIn, Instagram)  ·  valor 4  ·  mcp
Scrapers de Apify conectados a Claude generan listas de negocios con teléfonos, correos y contactos (ej.: 50 dentistas de Madrid en 5 minutos) y se puede enviar un correo a cada uno.
- Cómo: 1) Prueba gratuita de Apify. 2) Elegir fuente: LinkedIn para empresas, Google Maps para negocios locales, Instagram para marcas. 3) Conectarlo a Claude y pedir: «50 dentistas de Madrid con teléfonos, correos y contactos». 4) Contactar, o decir a Claude que envíe un correo a cada uno.
- Para nosotros: ECS: listas de leads locales por nicho (clínicas, reformas). CSL: prospección de pymes que necesitan ERP.
- Fuente: https://apify.com
- Ojo: Scraping de LinkedIn e Instagram viola términos; correo frío masivo automático choca con RGPD/LSSI y con la regla de Diego de no hacer masivos. Calidad de datos de contacto variable. Prueba gratuita limitada.
- Ya lo tenemos: viral-profile-scraper (Apify)
- Reels: G161 · 213 likes

### Agente de ventas por WhatsApp (audio, captura, texto)  ·  valor 4  ·  tecnica
Lead entra desde web, recibe WhatsApp de bienvenida, el bot clasifica audios, capturas y textos, responde, cualifica y agenda.
- Cómo: Botón de WhatsApp en la web, flujo que transcribe audio, analiza imagen y responde.
- Para nosotros: Mismo diseño que la IA Setter de ECS y demos de CSL; añadir transcripción de audio e imagen.
- Ojo: Audio e imagen de clientes: RGPD. Herramientas no nombradas.
- Reels: G67 · 83 likes

### Vender una sola solución replicable con propuesta de retorno  ·  valor 4  ·  tecnica
Posicionamiento comercial: dominar una única solución repetible (ej. automatización de WhatsApp a 3.000 euros) en lugar de vender muchas herramientas; menos propuestas (5 al mes) pero con cálculo de beneficio.
- Cómo: 1) Quitar testimonios sin números; documentar retorno concreto por caso. 2) Enviar pocas propuestas con cálculo de beneficio claro. 3) Elegir una solución y adaptarla a cada empresa del sector. Fuente de la biblioteca: comentar IA para recibir 12 soluciones.
- Para nosotros: ECS: encaja con Sprint 360 como oferta única con garantía x2 y casos con cifras. CSL: una demo/ERP vertical replicable por sector (ya hacen demos por nicho) en vez de catálogo suelto.
- Ojo: Cifras sin fuente primaria (conversión 5% a 40%, 80% de ingresos de una solución): folclore de sector, no citarlas en propuestas.
- Reels: G1 · 63 likes

### Prompts de LinkedIn y empleo con Claude Code  ·  valor 3  ·  prompt
Cuatro usos: optimizar perfil desde PDF de LinkedIn, buscar ofertas con Apify, optimizar CV para ATS, y analizar la exportacion de datos de LinkedIn para networking.
- Cómo: Perfil > Recursos > Guardar como PDF y subirlo con un prompt. Ajustes > Privacidad de datos > descargar copia (conexiones, mensajes) y pasarla a Claude Code para preguntar sobre la red. Prompts literales no revelados.
- Para nosotros: ECS: analizar la exportacion de LinkedIn de Diego para encontrar contactos y prospectos; optimizar perfil del cliente.
- Ojo: Exportacion de LinkedIn contiene datos personales de terceros: tratar con cuidado (RGPD). Prompts no incluidos.
- Reels: G121 · 1624 likes

### Skill de scraping de leads para Claude Code  ·  valor 3  ·  skill-claude
Skill de GitHub para Claude Code que scrapea leads de LinkedIn, Reddit, Indeed y cualquier web (500 fundadores SaaS en Madrid con email).
- Cómo: Instalar la skill y pedir a Claude Code a quien se busca en lenguaje natural.
- Para nosotros: ECS: listas de prospectos locales; ya existen lead-research-assistant, Clay y Apollo en el entorno.
- Ojo: Scraping de emails y LinkedIn: RGPD y terminos de plataforma; cold email sin base legal es riesgo. Nombre de la skill no dado.
- Reels: G125 · 507 likes

### Explorium MCP para generación de leads  ·  valor 3  ·  mcp
MCP de base de datos de empresas que devuelve empresas filtradas con emails verificados, LinkedIn y contexto de negocio.
- Cómo: Conectar el MCP de Explorium en Claude y escribir el prompt: dame 50 empresas de alto crecimiento en España con menos de 100 empleados.
- Para nosotros: CSL: prospección de pymes por sector para demos; ECS: listas de leads para outbound.
- Fuente: https://www.explorium.ai
- Ojo: Datos personales en frío: base legal RGPD/LOPDGDD y LSSI para email. Cobertura en España sin verificar; probablemente de pago.
- Reels: G38 · 426 likes

### Prospección de negocios sin web con Google Maps y landing por IA  ·  valor 3  ·  tecnica
Buscar negocios sin web en Google Maps, pasar sus datos a ChatGPT con un prompt, generar una landing con una herramienta de código IA y ofrecerla por 300 euros más 25 al mes.
- Cómo: 1) Google Maps, negocio sin web, copiar datos. 2) ChatGPT con el prompt (en el enlace del perfil). 3) AI Studio o similar: pegar el prompt y generar la landing. 4) Llamar y ofrecer 300 euros + 25 euros/mes. 5) Repetir 10 llamadas.
- Para nosotros: CSL: producto de entrada low-ticket (webs para micronegocios); la demo previa a la llamada ya es práctica de CSL. Mejor con precios propios.
- Ojo: Precio de 300 euros baja posicionamiento (regla: nunca bajar precio; CSL es estudio, no programa). Llamadas en frío: LSSI/RGPD. Promesa de ingreso extra sin experiencia es dudosa.
- Reels: G41 · 390 likes

### Caso Hugo: chatbot para su antiguo instituto (1.250 €)  ·  valor 3  ·  tecnica
Método de primer cliente de IA: sector que conoces, red cercana, solución simple de alto impacto.
- Cómo: 1) Elegir sector conocido. 2) Ir a tu red cercana. 3) Enseñar cómo un chatbot libera trabajo administrativo. 4) Cerrar solución simple (4 horas, 1.250 €).
- Para nosotros: Patrón de prospección para CSL y ECS: demo gratis en el sector del contacto y cierre de solución pequeña como entrada.
- Ojo: Caso anecdótico sin verificar; sirve para el CTA de lead (comenta 'Hugo').
- Reels: G49 · 261 likes

### Contratar 'chaval de IA' no es consultoría (diagnóstico antes que técnica)  ·  valor 3  ·  tecnica
Diferencia técnico vs consultor: diagnosticar qué automatizar primero, priorizar por retorno, decir 'esto no se automatiza'.
- Cómo: Preguntas: diagnostica o implementa, prioriza por retorno o por gusto.
- Para nosotros: Argumento para la propuesta de CSL: diagnóstico previo antes del desarrollo.
- Reels: G84 · 132 likes

### Sommelier digital para un local de vinos (caso de venta en frío)  ·  valor 3  ·  tecnica
Alumno cerró reunión en 10 min tras ver un problema en 30 s: asistente que recomienda vinos a extranjeros en 30 s.
- Cómo: Entrar al local, detectar fricción, ofrecer solución concreta, quedar para probarlo.
- Para nosotros: Patrón de venta presencial: demo mínima ligada a un dolor visible. Válido para CSL/ECS en negocios locales.
- Ojo: Caso sin verificar; transcripción pobre.
- Reels: G60 · 127 likes

### Caso Joan: asistente para clínicas de estética (300 €/hora)  ·  valor 3  ·  tecnica
Prototipo en 48 h para un bar, adaptado a clínicas para resolver dudas de pacientes en lista de espera.
- Cómo: 1) Taller práctico. 2) Prototipo de asistente. 3) Ofrecerlo a negocios locales cercanos. 4) Adaptar a cada cliente.
- Para nosotros: Demo reutilizable por vertical (clínicas, restauración) como la que CSL ya hace con kits por sector.
- Ojo: Caso sin verificar.
- Reels: G50 · 123 likes

### Sistema de primeros clientes de IA de Ester: problema real, validar, prospección directa  ·  valor 3  ·  tecnica
Método: detectar un problema real en tu propia empresa o conocidos, resolverlo con pocas herramientas, validar antes de invertir y prospectar directo sin anuncios.
- Cómo: 1) Usar ChatGPT para montar la solución sobre un problema conocido. 2) Validar con terceros; no invertir hasta que paga el primero. 3) Prospección directa a empresas que conoces: detectar problema, proponer solución clara y cobrar.
- Para nosotros: Guion de contenido de caso de cliente; método de prospección de CSL para demos a medida.
- Ojo: Testimonial de una alumna sin datos verificables; caso presentado como promesa de resultado.
- Reels: G27 · 102 likes

### Oferta de formación con devolución si no facturas lo que costó  ·  valor 3  ·  tecnica
Revolutia ofrece devolver el dinero si pasado un año el alumno no ha facturado más de lo que costó el curso; reduce el riesgo percibido.
- Cómo: Mecanismo descrito en G14: condición ligada al resultado (facturar mas que el precio) tras un año de trabajo completo. Ver captions G10, G13, G14.
- Para nosotros: ECS: refuerza el planteamiento de garantía x2 asumida como responsabilidad (bien de confianza). Comparar condiciones antes de copiarlo.
- Ojo: Garantía condicionada que hay que definir bien (gestión de reclamaciones, como ya pasa con devoluciones). Dato de 50.000 asistentes a clases gratuitas sin verificar.
- Reels: G10 · 51 likes

### Venta de flujos de automatización a empresas (500-3.000 €)  ·  valor 2  ·  tecnica
Modelo de negocio: construir flujos con IA y venderlos a empresas.
- Cómo: Sin pasos concretos en el guion; solo posicionamiento.
- Para nosotros: Referencia de precios de entrada para automatizaciones sueltas; ECS ya vende por resultados, no por flujo.
- Ojo: Cifra de ingresos no verificada.
- Reels: G48 · 2023 likes

### Servicio de scraping a agencias de lead gen  ·  valor 2  ·  tecnica
Idea de monetizacion: usar scraping con IA como servicio y cobrar por proyecto.
- Cómo: Montar listas de datos a medida para clientes usando ScrapeGraphAI. El guion afirma que se cobran 5.000 dolares por trabajo (sin fuente).
- Para nosotros: ECS: producto adicional de listas de prospectos B2B para clientes del Sprint 360.
- Ojo: Cifra de 5.000 dolares sin fuente; riesgo legal por RGPD y terminos de plataformas.
- Reels: G88 · 1149 likes

### Mercor (reclutamiento con IA y avatar entrevistador)  ·  valor 2  ·  saas
Plataforma que filtra CVs con IA y entrevista con avatar de IA, devolviendo ranking de candidatos. Valorada en 10.000 M$.
- Cómo: Empresa sube puesto, candidatos suben CV, la IA puntúa, agenda entrevista con avatar, resumen y lista final.
- Para nosotros: Idea de producto para CSL: módulo de preselección de candidatos con IA para pymes (ERP de RRHH).
- Ojo: Cifras de valoración y edad de fundadores sin verificar.
- Reels: G46 · 583 likes

### Checklist anti-gurú de IA (preguntas de validación)  ·  valor 2  ·  tecnica
Preguntas para evaluar a un vendedor de cursos: cuánto facturó, beneficio, qué habilidades necesito, para qué perfil tiene sentido.
- Cómo: Aplicar las 4 preguntas antes de comprar.
- Para nosotros: Posicionamiento: ECS vende bien de confianza con responsabilidad asumida; reforzar casos verificables.
- Ojo: Ironía: el propio creador capta con evento gratuito.
- Reels: G53 · 230 likes

## Marketing (6)

### Plugin SEO de Claude (18 agentes y 25 skills)  ·  valor 4  ·  plugin-claude-code
Plugin gratuito con agentes en paralelo (técnico, copywriter, SEO local, ecommerce, visibilidad en IAs) que auditan un dominio y devuelven un plan de acción.
- Cómo: Instalar el plugin, introducir el dominio más el comando; los agentes trabajan uno tras otro y entregan un plan a confirmar.
- Para nosotros: Diego ya tiene instaladas las seo-* (seo-audit, seo-local, seo-geo...); aplicable a auditorías gratis como gancho de captación de ECS y a webs de CSL.
- Ojo: Los «11.000 usuarios» no se verifican; lo que una agencia cobra es publicidad. Revisar el plan antes de enviarlo a un cliente.
- Ya lo tenemos: seo-* (más de 40 skills)
- Reels: G145 · 408 likes

### Pomelli (Google)  ·  valor 3  ·  saas
Escanea la web de una marca, extrae colores y tipografías y genera publicaciones de redes sociales con ese estilo.
- Cómo: Introducir la URL de la marca; genera posts con la identidad extraída.
- Para nosotros: ECS: borradores de posts de marca para clientes nuevos como punto de partida (hay que sustituir por voz propia y pasar filtro anti-IA).
- Ojo: Contenido genérico de IA; no sustituye guion con postura. Nombre transcrito Pomeli; verificar.
- Reels: G25, G158 · 81480 likes

### Skills de marketing (pack de 29 para Claude)  ·  valor 3  ·  repo-github
Pack de 29 skills (estrategia de contenido, copywriting, campañas, competencia) que se suben a Claude.
- Cómo: Entrar al enlace, abrir la skill, descargar el archivo RAW, Ajustes, Capacidades, Skills, arrastrar. Pedir estrategia de contenido.
- Para nosotros: Probablemente es el mismo pack del que ya vienen ab-test-setup, copywriting, page-cro; no instalar duplicado. Repo no nombrado en el guion.
- Ojo: Redundante con skills existentes; el guion no da enlace.
- Ya lo tenemos: copywriting, page-cro, email-sequence y resto del pack de marketing
- Reels: G81 · 3125 likes

### Foreplay (biblioteca de anuncios)  ·  valor 3  ·  saas
Guarda y descubre anuncios de Meta con mejor rendimiento para inspirarse.
- Cómo: Buscar en la biblioteca de anuncios y guardar referencias de formato y gancho.
- Para nosotros: ECS: biblioteca de referencias para anuncios de clientes y ganchos (alternativa a la Meta Ad Library).
- Fuente: https://www.foreplay.co
- Ojo: Nombre deducido de E4Play. Los anuncios con más gasto no prueban rendimiento causal.
- Reels: G31 · 1515 likes

### Cuatro skills de SEO con Claude (Auditor, AI Search Spy, Diagnoser, Fixer)  ·  valor 3  ·  skill-claude
Auditor (180 comprobaciones tecnicas conectado a Search Console), AI Search Spy (aparicion en ChatGPT, Perplexity y AI Overviews, puntuada sobre 100), Diagnoser (15 mejoras rapidas y preguntas que la gente hace a ChatGPT) y Fixer (escribe articulos y cambia copies).
- Cómo: Instalarlas y ejecutarlas en ese orden, con informe en vivo. No se da nombre del repo.
- Para nosotros: ECS: auditoria SEO y GEO de clientes; ya existen seo-*, seo-geo, seo-audit y seo-sem-360 en el entorno.
- Ojo: Dar acceso a Search Console del cliente. Puntuacion sobre 100 es heuristica, no prueba causal.
- Ya lo tenemos: seo-* (más de 40 skills)
- Reels: G120 · 579 likes

### Alta de producto/servicio para aparecer en ChatGPT (LLMO)  ·  valor 3  ·  tecnica
Formulario oficial de OpenAI para subir productos y servicios para que aparezcan en respuestas de ChatGPT; el creador lo enmarca como paso de SEO a LLMO.
- Cómo: Entrar en la web oficial de OpenAI, rellenar el formulario de productos (enlace por comentario NEGOCIO).
- Para nosotros: ECS/CSL: línea de servicio de visibilidad en IA (GEO) para clientes y para sus propias webs; ya existen skills seo-geo y ai-seo.
- Ojo: El formulario puede ser solo para comercio/feeds de producto y no para servicios; afirmación sin verificar. No prometer posicionamiento a clientes.
- Reels: G26 · 188 likes

## Contenido y vídeo (18)

### Skill Remotion para Claude Code  ·  valor 5  ·  skill-claude
Skill que permite a Claude Code generar vídeos animados con Remotion (React) y verlos en un editor en el navegador.
- Cómo: 1) Instalar la skill Remotion con el comando del repo. 2) Abrir Claude Code en un directorio limpio e invocar la skill. 3) Pedir un vídeo animado sobre el tema; se abre un editor en el navegador.
- Para nosotros: ECS: reels explicativos, motion 3D, vídeos de lanzamiento y demos de producto (ya existe la skill remotion-best-practices). CSL: vídeos demo de MVPs.
- GitHub: remotion-dev/remotion · 72.799 estrellas · licencia NOASSERTION
- Ojo: Licencia de Remotion exige licencia comercial para empresas con más de 3 empleados; revisar.
- Ya lo tenemos: remotion-best-practices
- Reels: G33 · 5183 likes

### HyperFrames (motion design con Claude)  ·  valor 4  ·  saas
Herramienta gratuita con biblioteca de plantillas de motion que se conecta a Claude; se copia el prompt, se personaliza y devuelve animación lista para el timeline.
- Cómo: Conectarla a Claude, elegir plantilla, copiar el prompt, pegarlo en Claude y pedir los cambios.
- Para nosotros: ECS: animaciones para reels, anuncios y YouTube de clientes (hoy se hace con motion 3D); sustituye animaciones de unos 300 € por pieza de 10 s, cifra del guion.
- Ojo: Nombre transcrito como «Hyperframe»: verificar. El precio de 300 € es referencia no verificada.
- Reels: G170 · 226 likes

### Sistema de 11 skills encadenadas para contenido (investigación, guion, carrusel, PDF lead, reel con voz clonada, vídeo, caption y miniatura)  ·  valor 4  ·  tecnica
Pipeline automático nocturno que investiga el nicho, escribe guion con hook validado, monta carrusel y PDF, graba reel con cara y voz clonada, edita vídeo y mide al día siguiente.
- Cómo: Encadenar skills en Claude Code; rechazar los vídeos flojos para que los rehaga. El propio guion admite que la primera semana rechazó más de lo que aprobó hasta enseñarle el criterio a mano.
- Para nosotros: ECS: es lo que ya construye Diego (carrusel-studio, stories-studio, impulso-cut, hook-vault); sirve como checklist de huecos (investigación diaria, medición al día siguiente).
- Ojo: Clonar cara y voz exige consentimiento y puede chocar con normas de plataformas. «Agencia de 3.000 €/mes» es promesa de marketing.
- Reels: G157 · 219 likes

### Remotion (plugin para editar vídeo con Claude)  ·  valor 4  ·  plugin-claude-code
Claude genera cortes, zooms, subtítulos, titulares y gráficos como código React/Remotion y renderiza el vídeo; los cambios se piden en lenguaje natural.
- Cómo: Instalar Claude, abrir complementos, añadir Remotion; subir el vídeo y describir la edición; para cambios, pedir a Claude qué actualizar y volver a renderizar.
- Para nosotros: ECS: reels y anuncios con subtítulos y gráficos animados sin timeline; ya existe skill remotion-best-practices e impulso-cut.
- GitHub: remotion-dev/remotion · 72.799 estrellas · licencia NOASSERTION
- Ojo: Remotion exige licencia de empresa de pago a partir de cierto tamaño de equipo; comprobar antes de usarlo para clientes.
- Ya lo tenemos: remotion-best-practices
- Reels: G134 · 150 likes

### Pilares invisibles de la IA (ASML, TSMC, NVIDIA)  ·  valor 3  ·  tecnica
Formato explicativo tipo glaciar: capas de la IA de arriba abajo (modelos, chips NVIDIA, fabricación TSMC, máquinas ASML).
- Cómo: Analogía visual del glaciar con niveles. Transcripción corrupta al final (bucle de Whisper).
- Para nosotros: Plantilla de reel explicativo 'lo invisible detrás de X' para sectores de clientes (ej. qué hay detrás de un ERP o de una campaña).
- Ojo: Sin riesgo; el guion termina con texto basura de Whisper.
- Reels: G45 · 41749 likes

### Infografia 3D con Gemini + Veo 3  ·  valor 3  ·  tecnica
Flujo de dos prompts: Gemini en modo imagen genera una infografia 3D y Veo 3 la anima.
- Cómo: 1) Gemini modo imagen: pegar el prompt cambiando 'tema'. 2) Descargar la imagen. 3) Subirla a Veo 3 con el segundo prompt (cambiando tema) y generar. Los prompts estan en la caption, no en el guion.
- Para nosotros: ECS: piezas visuales animadas de explicacion para reels (relacionado con motion 3D). Alternativa mas barata a producir motion.
- Ojo: Prompts no incluidos. Veo 3 es de pago/limitado.
- Reels: G105 · 887 likes

### Veo 3  ·  valor 3  ·  modelo-ia
Modelo de video de Google que anima imagenes.
- Cómo: Subir imagen y prompt para animarla.
- Para nosotros: ECS: clips cortos de anuncios y reels.
- Reels: G105 · 887 likes

### NotebookLM (Audio Overview / podcast automático)  ·  valor 3  ·  saas
Herramienta gratuita de Google que ingiere PDFs y genera resúmenes y un podcast con dos locutores debatiendo el contenido.
- Cómo: Subir PDFs (ej. una tesis de 120 páginas) y generar el podcast de audio; cambiar entre resumen y debate.
- Para nosotros: ECS: convertir briefings, propuestas y documentos de cliente en audio para repasar; investigar nicho y competencia subiendo fuentes. CSL: digerir documentación técnica y contratos de cliente.
- Fuente: https://notebooklm.google.com
- Ojo: No subir documentos confidenciales de clientes sin revisar condiciones de datos. Datos de 2 millones de usuarios y 30 euros sin fuente. Comparación con Otter/Descript es engañosa (herramientas distintas).
- Reels: G12 · 801 likes

### Blader Humanizer (skill de Claude)  ·  valor 3  ·  skill-claude
Skill gratuita que hace que Claude escriba más humano al activarse en cualquier tarea de escritura.
- Cómo: Buscar el nombre, descargar el zip, Personalizar, Skills, subir. Se activa sola.
- Para nosotros: Complemento a anti-patrones-ia-redaccion.md. Probar contra el filtro propio.
- Ojo: Skill de tercero: revisar el zip; su criterio puede no coincidir con la voz de Diego. Autor/repo no dados.
- Ya lo tenemos: humanizer (inglés; en español manda anti-patrones-ia-redaccion.md)
- Reels: G77 · 236 likes

### Skill personal de humanización de texto (Skill Creator + Wikipedia «Signs of AI writing»)  ·  valor 3  ·  tecnica
Se pide a Claude que lea la página de Wikipedia con señales de escritura de IA, liste los patrones y construya una skill propia que los evite al escribir.
- Cómo: 1) Decir a Claude: «quiero que humanices todos mis textos para que no suenen a IA». 2) «Ve a Wikipedia, busca la página de señales de escritura con IA, lista cada patrón y asegúrate de no hacer ninguno». 3) En el mismo chat, /skill-creator: «construyeme una skill personal de humanización basada en todo lo que acabamos de encontrar». 4) Instalarla y usar /human antes de escribir.
- Para nosotros: Diego ya tiene anti-patrones-ia-redaccion.md; sirve de contraste y para completar el checklist con la lista de Wikipedia. Aplicable a captions, emails y propuestas de ECS.
- Ojo: La promesa «0% detectado» es de marketing sin fuente; los detectores no son fiables. Quitar patrones no garantiza voz de marca.
- Reels: G131 · 177 likes

### Fish Audio (clonación de voz y texto a audio con Claude)  ·  valor 3  ·  saas
Se conecta Claude a la API gratuita de Fish Audio, se clona la voz y se convierte cualquier texto (guías, investigaciones, newsletters) en audio narrado.
- Cómo: Conectar Claude a la API de Fish Audio, clonar la voz y pasar el texto a convertir.
- Para nosotros: ECS: voz clonada de Diego para reels y audios de bienvenida; audiolibro de guías para clientes. Ya hay feedback sobre voz de reels v4.
- Fuente: https://fish.audio
- Ojo: Clonar voz exige consentimiento y puede no cumplir términos de plataformas; la API tiene límites gratis. Pide clave.
- Reels: G169 · 93 likes

### MoneyPrinterTurbo  ·  valor 2  ·  repo-github
Genera video faceless completo: tema > guion > clips Full HD/4K > subtitulos, musica y narracion; compatible con Claude, DeepSeek, ChatGPT y Gemini; lotes y vertical u horizontal; corre en local o en Google Colab.
- Cómo: Elegir tema, generar guion, seleccionar clips de stock, anadir subtitulos y narracion; opcion de ejecutar en Colab.
- Para nosotros: ECS: contenido de bajo coste para clientes sin cara o para nichos (stock). Probablemente inferior a lo que ya hace Impulso Cut.
- GitHub: harry0703/MoneyPrinterTurbo · 142.965 estrellas · licencia MIT
- Ojo: Videos de stock sin derechos claros, calidad generica; las cifras de ingresos (5-10 mil al mes) no tienen prueba.
- Reels: G117 · 12017 likes

### Estudio de exposición observada de Anthropic  ·  valor 2  ·  tecnica
Métrica 'exposición observada': teórico vs uso real (programación 94% vs 33%; programadores 74,5%, atención al cliente 70%).
- Cómo: Gráfico azul/rojo teórico vs real.
- Para nosotros: Argumento de venta de automatización de atención al cliente y entrada de datos para CSL.
- Ojo: Citar con el informe original, no el reel.
- Reels: G65 · 385 likes

### Ovi (vídeo + audio open source)  ·  valor 2  ·  modelo-ia
Modelo open source que genera vídeo con audio sincronizado (voz, efectos, música) desde texto o imagen en un solo paso.
- Cómo: El guion no da pasos; promete enlace por comentario IA. Se usa desde texto o imagen de entrada.
- Para nosotros: ECS: pruebas de clips con voz para anuncios o stories. En la práctica el equipo usa motion 3D y vídeo grabado, no UGC IA.
- GitHub: character-ai/Ovi · 1.763 estrellas · licencia Apache-2.0
- Ojo: Owner deducido, verificar. Requiere GPU potente para correrlo local; calidad inferior a Veo/Sora. Contradice la regla de no usar UGC IA.
- Reels: G16 · 353 likes

### Prompt anti-sonido-robot (humanizador de texto)  ·  valor 2  ·  prompt
Prompt con lista de palabras prohibidas, reglas de formato y autorrevisión de rayas antes de responder, para que ChatGPT no suene a IA.
- Cómo: Pegar el prompt en Ajustes, Personalización, Instrucciones personalizadas. El prompt completo se envía por DM, no sale en el guion.
- Para nosotros: Ya cubierto por el filtro anti-huella-IA de Diego (anti-patrones-ia-redaccion.md). Aplicable a copys de clientes.
- Ojo: El prompt no aparece en el guion; captación de lead.
- Reels: G51 · 348 likes

### Glyph (MCP de imagen y vídeo)  ·  valor 2  ·  mcp
Conecta Claude a cientos de herramientas de imagen y vídeo. Nombre dudoso en la transcripción.
- Cómo: Instalar el MCP en Claude Code. El guion no da pasos.
- Para nosotros: ECS: generación de creatividades; ya hay MCP de Higgsfield y Canva conectados.
- Ojo: Nombre sin verificar.
- Reels: G140 · 302 likes

### Tinder profesional + mapa de miembros de la comunidad  ·  valor 2  ·  tecnica
Función interna de la comunidad Revolutia para emparejar técnicos y comerciales y mapa de miembros cercanos.
- Cómo: Idea de producto comunitario.
- Para nosotros: Idea de producto para la Escuela de ECS: matching y mapa de alumnos.
- Reels: G74 · 141 likes

### Humano con IA vs sin IA (narrativa)  ·  valor 2  ·  tecnica
Argumento: la IA reemplaza tareas, no trabajos. Preguntas de auditoría: qué tareas acelerar, qué herramienta, cuántas horas ahorradas.
- Cómo: Cuestionario de 3 preguntas.
- Para nosotros: Argumento de venta de ECS/CSL para ahorro de horas.
- Reels: G83 · 85 likes

## Diseño (19)

### Google Stitch  ·  valor 4  ·  saas
Genera diseños de aplicaciones y pantallas con IA en minutos.
- Cómo: Describir la app, generar diseño y exportar a AI Studio Build.
- Para nosotros: CSL: maquetas rápidas de pantallas para demos de SaaS/ERP antes de construir. ECS: wireframes de landings.
- Fuente: https://stitch.withgoogle.com
- Ojo: URL deducida; verificar.
- Reels: G25, G87 · 81480 likes

### Nano Banana Pro (Gemini)  ·  valor 4  ·  modelo-ia
Modelo de generación de imágenes de Google de alta fidelidad.
- Cómo: Generar imágenes desde Gemini o AI Studio con prompt.
- Para nosotros: ECS: fondos y piezas estáticas de anuncios y carruseles. Ya hay skills (banana, carrusel-gemini) en el entorno.
- Ojo: Marcar contenido sintético cuando la plataforma lo exija.
- Reels: G25 · 81480 likes

### Awesome Design (sistemas de diseño de marcas en markdown)  ·  valor 4  ·  repo-github
Colección de sistemas de diseño de marcas reales (Apple, Notion, Stripe, Figma...) en markdown para que Claude los use como referencia; 38.000 estrellas en una semana según el guion.
- Cómo: Copiar el markdown de la marca de referencia al proyecto y pedir a Claude que construya con ese sistema.
- Para nosotros: CSL: webs y landings con base de diseño premium. ECS: referencia para estilo de cliente.
- GitHub: VoltAgent/awesome-design-md · 127.272 estrellas · licencia MIT
- Ojo: Imita sistemas de diseño de terceros: no copiar identidad de marca en trabajos de cliente.
- Ya lo tenemos: design-md-marcas
- Reels: G153 · 1322 likes

### Stitch (Google)  ·  valor 4  ·  saas
Convierte prompts en diseños de interfaz para apps y webs sin Figma.
- Cómo: Describir la pantalla en un prompt.
- Para nosotros: CSL: maquetas de demos de ERP y SaaS para enseñar al cliente antes de picar código.
- Fuente: https://stitch.withgoogle.com
- Reels: G158 · 578 likes

### Frontend Design (Anthropic)  ·  valor 4  ·  plugin-claude-code
Plugin oficial que evita el look generico de IA y produce UI de calidad de produccion.
- Cómo: Instalar el plugin frontend-design y pedir interfaces; ya esta disponible en el entorno de Diego.
- Para nosotros: CSL y ECS: webs y landings con aspecto no generico. Ya instalado.
- Ya lo tenemos: frontend-design
- Reels: G90 · 529 likes

### Taste Skill  ·  valor 4  ·  skill-claude
Da a Claude criterio estético con referencias visuales de sitios reales para que las interfaces no parezcan generadas por IA.
- Cómo: Instalar la skill y pedir interfaces; Claude usa referencias reales.
- Para nosotros: CSL: webs y demos de cliente con mejor acabado; ECS: landings y embudos.
- Ojo: Repo no identificado; revisar el contenido de la skill antes de instalar.
- Ya lo tenemos: design-taste-frontend
- Reels: G150 · 275 likes

### Impeccable (20 comandos de diseño, /polish)  ·  valor 4  ·  skill-claude
Sistema de 20 comandos sobre tipografía, color, espaciado y layout; /polish repasa la UI y ajusta detalles antes de publicar.
- Cómo: Instalar una vez; ejecutar /polish antes de publicar.
- Para nosotros: CSL: pase final de calidad en webs y SaaS antes de entregar. Ya está instalada (skill impeccable).
- GitHub: pbakaus/impeccable · 109.047 estrellas · licencia Apache-2.0
- Ya lo tenemos: impeccable
- Reels: G150 · 275 likes

### Kimi Agentic Slides (modo Adaptativo y Visual con Nano Banana Pro)  ·  valor 3  ·  saas
Generador de presentaciones de Kimi: modo Adaptativo con gráficos editables tipo consultora y datos de Yahoo Finance, FMI, Banco Mundial y Google Scholar; modo Visual con imágenes de Nano Banana Pro. Exporta a PPT, Google Slides o PNG.
- Cómo: En Kimi, pulsar Slides en la barra lateral, elegir modo Adaptativo o Visual, describir la presentación y descargar como PPT/Slides/PNG. Los prompts no se dan.
- Para nosotros: ECS: dosieres y decks para leads y webinars; CSL: presentación de demos. Alternativa a Gamma.
- Fuente: https://www.kimi.com
- Ojo: Subir datos de clientes a un servicio chino: no usar con información confidencial. Lo de «ilimitado» puede cambiar. Verificar cifras que cite.
- Reels: G135 · 3968 likes

### Skill de 50 estilos visuales y tipografias  ·  valor 3  ·  skill-claude
Skill con 50 estilos visuales y tipografias combinables para evitar el diseno generico de IA. El guion no da el nombre.
- Para nosotros: Parecida a theme-factory ya instalada.
- Ojo: Nombre no identificado.
- Reels: G118 · 2314 likes

### Mobbin  ·  valor 3  ·  saas
Biblioteca de capturas de pantalla de apps y webs reales para tomar de referencia de diseño de interfaces.
- Cómo: Buscar flujos de apps, tomar capturas y dárselas a Cursor para que construya la app.
- Para nosotros: CSL: referencias de UX para pantallas de ERP/SaaS antes de maquetar; usar como briefing visual para el agente de código.
- Fuente: https://mobbin.com
- Ojo: Transcrito Moblin; deducido. Plan de pago. No copiar diseños literalmente.
- Reels: G31 · 1515 likes

### Open Design  ·  valor 3  ·  repo-github
Alternativa open source a Claude Design: canvas interactivo para crear webs animadas, prototipos moviles, slides y motion graphics con cualquier modelo (suscripcion de ChatGPT, API, local).
- Cómo: Descargar el proyecto, conectar el modelo que se tenga y pedir diseno por prompt iterando en el canvas.
- Para nosotros: ECS: slides y prototipos para propuestas sin pagar Claude Design. CSL: prototipos de apps en demos.
- Ojo: Nombre exacto del repo no dado; verificar licencia y seguridad antes de conectar cuentas. Usar la suscripcion de ChatGPT por herramientas no oficiales puede incumplir terminos.
- Reels: G89 · 1327 likes

### Figma MCP  ·  valor 3  ·  mcp
Conecta Claude con Figma para leer y crear diseños.
- Cómo: Conectarlo como MCP en Claude Code.
- Para nosotros: CSL: pasar diseño del cliente a código.
- Ojo: Acceso a archivos de diseño del cliente.
- Reels: G159 · 266 likes

### Skills de UI para Claude + conexion a herramientas  ·  valor 3  ·  tecnica
Combinar skills de diseno UI con herramientas reales conectadas para que Claude genere sitios completos con animaciones y layouts de produccion.
- Cómo: 1) Anadir mejores skills de UI. 2) Conectar a herramientas reales para que entienda estructura y layout. No se nombran las herramientas concretas.
- Para nosotros: CSL y ECS: receta de webs y landings; ya se usan frontend-design, impeccable y similares.
- Ojo: Guion vago: no da nombres de skills ni herramientas.
- Reels: G91 · 234 likes

### Gemini Canvas  ·  valor 2  ·  saas
Convierte documentos en presentaciones con visuales dentro de Gemini.
- Cómo: Pegar o subir documento en Gemini y pedir presentación en modo Canvas.
- Para nosotros: Borradores de decks internos.
- Ya lo tenemos: Canva MCP
- Reels: G25 · 81480 likes

### Replicate  ·  valor 2  ·  saas
Plataforma con API a modelos de imagen y vídeo de código abierto.
- Cómo: Elegir modelo, llamar por API o web para generar imágenes de marca.
- Para nosotros: Generación de imágenes por API en automatizaciones.
- Fuente: https://replicate.com
- Ojo: Pago por uso.
- Reels: G31 · 1515 likes

### Herramienta web de visualización de Excel (no nombrada)  ·  valor 2  ·  saas
Convierte datos pegados o hojas de Excel en gráficos e infografías con estilos editables y exportación en alta calidad.
- Cómo: Pegar datos o subir la hoja, elegir estilo, editar y exportar. Enlace por comentario VISUAL.
- Para nosotros: ECS: infografías de resultados para informes de cliente.
- Ojo: El guion no da el nombre; no se puede identificar.
- Reels: G32 · 1042 likes

### Small PPT (generador de presentaciones por prompt)  ·  valor 2  ·  saas
Genera presentaciones completas con textos, imágenes y gráficos desde un prompt, y admite importar PDF, Excel, imágenes y URLs.
- Cómo: Buscar Small PPT en Google, escribir el prompt del tema, elegir tamaño, aceptar el esquema propuesto, generar y editar textos, gráficos y tipografía.
- Para nosotros: Borradores rápidos de decks para leads; para propuestas oficiales ya existe la skill de propuestas con maqueta de marca.
- Ojo: Nombre de producto dudoso en la transcripción (puede ser SmallPPT u otro); no se da URL. Calidad de marca inferior a la maqueta propia.
- Reels: G21 · 578 likes

### Mixboard (Google)  ·  valor 2  ·  saas
Tablero tipo Canva con Pinterest para generar y combinar imágenes con IA.
- Cómo: Generar varias imágenes y combinarlas. Nombre transcrito como «Mixport».
- Para nosotros: ECS: moodboards y conceptos de anuncio.
- Reels: G158 · 578 likes

### Design Arena  ·  valor 2  ·  saas
Enfrenta herramientas de IA de diseño (logos, webs, vídeo) con votación humana.
- Cómo: Ver resultados antes de pagar.
- Para nosotros: Elegir generador de webs/vídeo para ECS.
- Fuente: https://www.designarena.ai
- Reels: G85 · 269 likes

## Desarrollo web (16)

### Stitch MCP hacia Claude Code  ·  valor 5  ·  mcp
Conecta los disenos de Stitch con Claude Code para que lea las pantallas y las convierta en codigo.
- Cómo: En Stitch: Exportar > MCP > Setup MCP > elegir Claude Code > copiar el comando y pegarlo en la terminal. Luego un prompt para conectar pantallas, anadir animaciones y dejar la app lista (el prompt exacto se da en la boveda, no en el guion).
- Para nosotros: CSL: pipeline diseno a codigo para webs y fronts de demos de cliente; recorta horas de maquetacion.
- Fuente: https://stitch.withgoogle.com
- Ojo: El MCP da acceso a tus disenos de Stitch; usar con proyectos de cliente solo si el cliente lo permite. Prompt clave no incluido.
- Reels: G87 · 3401 likes

### Receta de 8 prompts para webs con Claude Code  ·  valor 5  ·  prompt
Receta: clonar layout con captura, CLAUDE.md de diseñador UI senior, librería de componentes, gradientes, animaciones y hover, gráficos 3D, dos fuentes de Google, correcciones con capturas.
- Cómo: 1) Captura de una web y pedir clonar layout. 2) CLAUDE.md 'diseña como UI senior'. 3) Librería de componentes. 4) Fondos con gradientes. 5) Animaciones y hover. 6) 3D. 7) Dos Google Fonts (títulos y cuerpo). 8) Iterar con capturas de lo que arreglar.
- Para nosotros: Webs y landings de ECS y demos de CSL: de 3,5 h a 10-30 min según el creador. Ya existen skills de diseño en el entorno.
- Ojo: Clonar el layout de una web ajena: cuidar copyright y no copiar assets ni textos. Tiempos de 10-30 min son del creador.
- Reels: G80 · 1356 likes

### Flujo de vibe coding: PRD, documento de diseño, tech stack y fichero de tareas  ·  valor 5  ·  tecnica
Método previo a programar con un agente de código: tres documentos y un fichero de tareas para que el agente trabaje una tarea cada vez.
- Cómo: 1) PRD: explicar la idea al LLM y que redacte el PRD. 2) Doc de diseño: tomar un diseño de Dribbble y pedir al LLM un documento de diseño. 3) Tech stack: investigar el mejor para el proyecto. 4) Pedir al agente que analice los tres y genere un fichero de tareas. 5) git init para poder volver atrás. 6) Subir a GitHub con CodeRabbit instalado.
- Para nosotros: CSL: plantilla estándar de arranque de proyectos (PRD, diseño, stack, tareas) para webs, SaaS y demos; encaja con las skills de plan existentes.
- Ojo: El guion dice ByteCoder/ByteCalling (error de transcripción, probablemente Claude Code u otro agente).
- Reels: G30 · 605 likes

### Flujo de diseño web: skills de diseño + Figma MCP + Playwright  ·  valor 5  ·  tecnica
Combina las skills de Emil Kowalski e Impeccable y Taste Skill con MCP de Figma y Playwright para diseñar, construir y testear webs con acabado profesional en minutos.
- Cómo: 1) Instalar skills de Emil Kowalski e Impeccable. 2) Añadir Taste Skill. 3) Conectar Figma MCP y Playwright. 4) Pedir la web; Claude diseña, construye y testea.
- Para nosotros: CSL: webs y demos de cliente más rápidas; ECS: landings de embudos.
- Ojo: Revisar siempre accesibilidad y rendimiento; Figma pide cuenta.
- Ya lo tenemos: webapp-testing
- Reels: G159 · 266 likes

### Skill de reglas de diseño de Apple (repo con 10 skills)  ·  valor 4  ·  skill-claude
Skill basada en charlas de diseño de Apple (respuesta inmediata al toque, arrastre pegado al dedo, animaciones interrumpibles); el repo trae 10 skills de animación, ingeniería y diseño. 28.000 estrellas.
- Cómo: Pegar el enlace del repo a Claude, pedir que instale la skill y que audite la interfaz de la app existente; después arreglar los problemas que reporte.
- Para nosotros: CSL: auditar SaaS y ERPs ya hechos contra criterios de interacción y acabado.
- Ojo: Repo no identificado; revisar contenido. Solo guía de diseño, no garantiza resultado.
- Ya lo tenemos: apple-design
- Reels: G172 · 2451 likes

### Reglas de diseno de Vercel (web interface guidelines)  ·  valor 4  ·  skill-claude
Mas de 100 reglas que auditan una pagina y dicen que arreglar. Whisper escribio 'Bersel' (Vercel).
- Para nosotros: CSL: auditoria rapida de calidad antes de entregar webs.
- Ojo: Atribucion a Vercel por inferencia del audio.
- Ya lo tenemos: web-design-guidelines y 5 más de Vercel
- Reels: G118 · 2314 likes

### Reglas de diseño de Vercel (Web Interface Guidelines)  ·  valor 4  ·  skill-claude
Audita el código frente a las normas de diseño de Vercel y marca puntos débiles antes de publicar.
- Cómo: Instalar la skill y pedir auditoría de la interfaz.
- Para nosotros: CSL: auditoría final de webs y SaaS antes de entregar.
- GitHub: vercel-labs/agent-skills · 33.965 estrellas · licencia null
- Ya lo tenemos: web-design-guidelines y 5 más de Vercel
- Reels: G165 · 183 likes

### Build de Google AI Studio  ·  valor 3  ·  saas
Crea aplicaciones web completas a partir de lenguaje natural; importa diseños de Stitch. Presentado como versión gratuita de Lovable.
- Cómo: Ir a AI Studio > Build, escribir qué app quieres o importar el diseño de Stitch.
- Para nosotros: CSL: prototipos de demo de bajo coste para leads; ECS: landings de pruebas.
- Fuente: https://aistudio.google.com
- Ojo: Prototipos, no producción; datos de cliente no deberían cargarse.
- Reels: G25 · 81480 likes

### Prompt de produccion tras exportar diseno  ·  valor 3  ·  prompt
Prompt especifico que convierte los disenos de Stitch en codigo listo para produccion con pantallas conectadas y animaciones.
- Cómo: Tras conectar el MCP, pedir a Claude Code: conecta las pantallas, anade animaciones fluidas y deja la app lista para lanzar. Prompt literal no revelado.
- Para nosotros: Plantilla propia en CSL para pasar de diseno aprobado a front.
- Ojo: Prompt no incluido en el guion (se vende como boveda).
- Reels: G87 · 3401 likes

### Antigravity (IDE de Google) para dashboards sobre n8n  ·  valor 3  ·  saas
IDE agéntico para crear interfaces visuales conectadas a flujos de n8n y convertir automatizaciones en producto.
- Cómo: Crear dashboard en Antigravity que lea datos de los flujos de n8n.
- Para nosotros: CSL: paneles de cliente rápidos sobre automatizaciones.
- Fuente: https://antigravity.google
- Ojo: Dependencia de producto de Google en preview.
- Reels: G61 · 338 likes

### Skill de animación de Emil Kowalski  ·  valor 3  ·  skill-claude
Añade movimiento real a las interfaces: easing intencionado, animaciones con sentido.
- Cómo: Instalar la skill y ejecutar su comando sobre la interfaz.
- Para nosotros: CSL: pulir micro-interacciones en webs y SaaS (ya hay skills ui-animation y userinterface-wiki).
- Ya lo tenemos: emil-design-eng y 18 más de Emil Kowalski
- Reels: G150 · 275 likes

### Image to Code  ·  valor 3  ·  plugin-claude-code
Convierte una referencia visual en código usable sin perder detalle.
- Cómo: Pasar la imagen de referencia y pedir el código.
- Para nosotros: CSL: de la maqueta del cliente a HTML en demos.
- Ojo: Repo no identificado.
- Reels: G165 · 183 likes

### Dominios gratuitos open source  ·  valor 2  ·  saas
Proyecto open source para registrar dominios gratis en varias extensiones, conectables a Cloudflare.
- Cómo: Registrar el dominio, conectarlo a Cloudflare y apuntar el DNS. Pensado para demos y pruebas.
- Para nosotros: CSL: dominio para demos sin coste. Ya se usa sslip.io en el VPS.
- Ojo: Nombre del proyecto no dado. Extensiones gratuitas suelen ser inestables o pueden retirarse; no usar en produccion de cliente ni en landings de anuncios (Meta penaliza dominios de baja reputacion).
- Reels: G98 · 496 likes

### Animaster Lib (250+ componentes animados)  ·  valor 2  ·  saas
Librería de más de 250 componentes con efectos de scroll, heros e interacciones de ratón, para copiar y pegar. Nombre dudoso.
- Cómo: Copiar el componente y pegarlo en la web.
- Para nosotros: CSL: acelerar webs y demos de cliente.
- Ojo: Revisar licencias antes de uso comercial.
- Reels: G154 · 365 likes

### Skipper UI  ·  valor 2  ·  saas
Componentes listos (heros, tarjetas, precios) con acabado premium.
- Cómo: Copiar y pegar componentes.
- Para nosotros: ECS: landings y páginas de precios de embudos.
- Ojo: Nombre sin verificar; comprobar licencia.
- Reels: G154 · 365 likes

### Vengeance UI  ·  valor 2  ·  saas
Bloques de diseño y componentes animados para webs.
- Cómo: Copiar y pegar componentes.
- Para nosotros: CSL: webs corporativas con aspecto premium.
- Ojo: Nombre sin verificar.
- Reels: G154 · 365 likes

## Desarrollo (29)

### Traspaso limpio con handoff.md en Claude Code  ·  valor 5  ·  prompt
Antes de cerrar la sesión, crear handoff.md con objetivo, estado, archivos, cambios, intentos fallidos y siguiente paso; luego /clear y leerlo.
- Cómo: Pedir a Claude: 'crea handoff.md con objetivo, estado actual, archivos, qué cambió, qué intentaste, qué falló y qué planeas'. Después /clear y 'lee handoff.md y continúa'.
- Para nosotros: Estándar para proyectos CSL largos; compatible con las notas de memoria de Diego.
- Reels: G86 · 4085 likes

### Plugin de seguridad de Anthropic (100 agentes y 3 jueces)  ·  valor 5  ·  plugin-claude-code
Parte el proyecto en trozos, lanza unos 100 agentes de ataque y cada hallazgo debe confirmarlo un panel de 3 jueces (alcanzable, daño real, mitigación) con archivo y línea exactos; genera el parche en una copia, corre tests y entrega un archivo para aplicar.
- Cómo: Instalar el plugin oficial y lanzarlo en la terminal sobre el proyecto; pedir arreglos cuando termine. Ejemplo: app de citas médicas en 27 min con 7 fallos, el peor un IDOR por número en la URL.
- Para nosotros: CSL: auditoría de seguridad previa a entrega de SaaS y ERPs a medida y argumento de venta; comprobar IDOR en las demos con datos de cliente.
- Ojo: Consume muchos tokens; el ahorro de 3.000 a 10.000 € es promesa de marketing. No sustituye pentest formal. Nombre exacto del plugin no dado.
- Reels: G168 · 3073 likes

### GitHub Spec Kit  ·  valor 5  ·  repo-github
Kit de GitHub para desarrollo guiado por especificaciones: la IA define requisitos, arquitectura, plan tecnico y tareas antes de escribir codigo.
- Cómo: Instalar el repo y seguir el flujo spec > plan > tareas > implementar.
- Para nosotros: CSL: plantilla de arranque para ERPs y SaaS a medida; mejora presupuestos y alcance con cliente al dejar el spec por escrito.
- GitHub: github/spec-kit · 149.552 estrellas · licencia MIT
- Ya lo tenemos: skill spec-kit + comando specify
- Reels: G106 · 1213 likes

### Awesome Claude Code Subagents  ·  valor 4  ·  repo-github
Colección comunitaria de más de 100 subagentes para Claude Code.
- Cómo: Copiar los subagentes deseados a .claude/agents.
- Para nosotros: CSL: subagentes de revisión, seguridad, tests y arquitectura para proyectos de cliente.
- GitHub: VoltAgent/awesome-claude-code-subagents · 26.510 estrellas · licencia MIT
- Ojo: Prompts de terceros: revisar antes de usar con código de clientes.
- Reels: G52 · 2654 likes

### /rewind (doble Escape) en Claude Code  ·  valor 4  ·  tecnica
Volver al mensaje previo al error en vez de corregir encima, para no contaminar el contexto.
- Cómo: Doble Escape o /rewind, elegir el mensaje y replantear con lo aprendido.
- Para nosotros: Hábito para sesiones largas de CSL.
- Ojo: Atribuye el consejo a 'el desarrollador principal' (Boris/Tariq, transcripción dudosa).
- Reels: G82 · 634 likes

### gstack  ·  valor 4  ·  repo-github
Repo de Garry Tan (CEO de Y Combinator) que convierte Claude Code en un equipo: planificador, CEO que afina la idea, jefe de ingenieria, disenador, programador, revisor de bugs y tester que abre el navegador y hace clics.
- Cómo: Copiar la URL del repo y pedir a Claude que ayude a instalarlo.
- Para nosotros: CSL: QA automatico con navegador real antes de entregar demos; revision de idea como CEO antes de presupuestar.
- GitHub: garrytan/gstack · 141.385 estrellas · licencia MIT
- Ojo: Revisar lo que instala. Estrellas segun el guion.
- Reels: G113 · 626 likes

### Superpowers  ·  valor 4  ·  plugin-claude-code
Plugin que obliga a Claude a planificar y testear antes de programar.
- Cómo: Instalar el plugin desde su repo de GitHub y trabajar con sus flujos de planificacion y TDD.
- Para nosotros: CSL: disciplina de calidad en proyectos a medida (spec, plan, tests) con menos reescrituras.
- GitHub: obra/superpowers · 316.809 estrellas · licencia MIT
- Ya lo tenemos: 15 skills de superpowers (sin el plugin)
- Reels: G90 · 529 likes

### Security Review (plugin)  ·  valor 4  ·  plugin-claude-code
Escanea el codigo base buscando vulnerabilidades antes de desplegar.
- Cómo: Ejecutar security-review sobre el repo antes de produccion.
- Para nosotros: CSL: auditoria de seguridad antes de entregar ERPs y SaaS con datos de clientes. Ya disponible.
- Ya lo tenemos: security-review
- Reels: G90 · 529 likes

### Playwright MCP  ·  valor 4  ·  mcp
Claude controla un navegador: clics, formularios y test de la app.
- Cómo: Instalar el MCP de Playwright en Claude Code y pedir que pruebe la app o la web.
- Para nosotros: CSL: pruebas end-to-end de demos y ERPs; ECS: revisar landings y embudos antes de lanzar campañas.
- GitHub: microsoft/playwright-mcp · 39.570 estrellas · licencia Apache-2.0
- Ojo: Las 34k estrellas pueden corresponder al repo principal de Playwright; verificar.
- Ya lo tenemos: webapp-testing
- Reels: G140 · 302 likes

### /goal (objetivo persistente)  ·  valor 4  ·  tecnica
Se fija la meta final y Claude sigue trabajando turno tras turno, hasta días, hasta que esté terminada.
- Cómo: /goal con la meta final y criterios de terminado.
- Para nosotros: CSL: tareas largas (migraciones, módulos) sin supervisión; ECS: lotes de entregables.
- Ojo: Sin supervisión puede consumir mucho límite y tocar archivos; acotar permisos y alcance.
- Reels: G139 · 224 likes

### Playwright CLI  ·  valor 4  ·  plugin-claude-code
Claude abre un navegador, captura lo construido y detecta errores visuales antes de que lo veas.
- Cómo: Instalar y pedir verificación visual tras construir.
- Para nosotros: CSL: QA visual automático de demos y landings.
- GitHub: microsoft/playwright · 100.023 estrellas · licencia Apache-2.0
- Ya lo tenemos: webapp-testing
- Reels: G165 · 183 likes

### Plugin Code Review de Claude Code (5 agentes en paralelo)  ·  valor 4  ·  plugin-claude-code
Cinco agentes revisan el código en paralelo y detectan bugs antes de producción.
- Cómo: Instalar el plugin code-review y lanzar /code-review sobre el diff o PR.
- Para nosotros: CSL: revisión de PRs de ERPs y SaaS a medida antes de entregar al cliente.
- GitHub: anthropics/claude-code · 155.461 estrellas · licencia null
- Ya lo tenemos: code-review
- Reels: G132 · 90 likes

### Ruflo (antes Claude Flow)  ·  valor 3  ·  repo-github
Framework multiagente para Claude Code: unos 60 agentes en paralelo, memoria compartida, aprendizaje y enrutado de tareas simples a modelos baratos.
- Cómo: Instalar el CLI y lanzar swarm; comentando 'Ruflo' se capta lead.
- Para nosotros: Ya configurado en CLAUDE.md del proyecto de Diego. Para CSL: swarms de revisión y tests.
- GitHub: ruvnet/ruflo · 81.579 estrellas · licencia MIT
- Ojo: Afirmación de '2,5x de potencia' sin verificar; coste real de tokens puede subir.
- Ya lo tenemos: claude-flow (Ruflo)
- Reels: G68 · 4431 likes

### Claude Code dentro de Antigravity (extensión) con /init y modo plan  ·  valor 3  ·  plugin-claude-code
Instalar la extensión de Claude Code en el editor Antigravity de Google para usarlo sin terminal.
- Cómo: 1) Buscar y descargar Antigravity. 2) Abrir una carpeta nueva. 3) Extensiones > Claude Code > instalar. 4) Pulsar el icono de Claude. 5) Escribir /init para crear el archivo de memoria del proyecto (CLAUDE.md). 6) Activar modo plan y describir lo que se quiere construir.
- Para nosotros: Onboarding de becarios y programadores de CSL sin terminal; el equipo ya usa Claude Code. Pasos /init y modo plan útiles como estándar.
- Fuente: https://antigravity.google
- Ojo: Claude Code requiere cuenta o API de pago. Datos del cliente en un editor de Google: revisar ajustes de privacidad.
- Reels: G43 · 3035 likes

### Everything Claude Code  ·  valor 3  ·  repo-github
Setup completo del ganador de un hackathon de Anthropic: 181 habilidades, 47 subagentes, 79 comandos; funciona en Claude Code, Cursor, Codex, OpenCode y Gemini.
- Cómo: Clonar el repo e instalar las skills y agentes que interesen.
- Para nosotros: CSL: cantera de skills (seguridad, memoria, aprendizaje) para adaptar; no instalarlo entero.
- GitHub: affaan-m/ECC · 302.055 estrellas · licencia MIT
- Ojo: Instalar solo lo revisado: skills y hooks pueden ejecutar comandos. Ya hay muchos skills en el entorno; riesgo de conflictos.
- Reels: G112 · 2434 likes

### Resend  ·  valor 3  ·  saas
API para enviar emails transaccionales desde aplicaciones.
- Cómo: Crear cuenta, verificar dominio, usar la API desde el backend.
- Para nosotros: CSL: envío de correos en SaaS y ERPs a medida.
- Fuente: https://resend.com
- Ojo: Transcrito Recent. Pide clave API: una por cliente.
- Reels: G31 · 1515 likes

### Plugin de Codex para Claude Code  ·  valor 3  ·  plugin-claude-code
Conecta Claude con OpenAI Codex para que ambos se revisen mutuamente.
- Cómo: Instalar el plugin y pedir revisión cruzada.
- Para nosotros: CSL: segunda opinión en código crítico (facturación, pagos, ERPs).
- GitHub: openai/codex-plugin-cc · 35.097 estrellas · licencia Apache-2.0
- Ojo: Envía código a OpenAI; requiere cuenta de OpenAI.
- Reels: G153 · 1322 likes

### CodeRabbit  ·  valor 3  ·  saas
Revisor automático de pull requests en GitHub que escanea código en busca de bugs y vulnerabilidades.
- Cómo: Instalar la app de CodeRabbit en el repositorio de GitHub; revisa cada PR.
- Para nosotros: CSL: segunda revisión automática en repos de clientes y de producto antes de desplegar.
- Fuente: https://coderabbit.ai
- Ojo: Da acceso al código del cliente a un tercero; pedir permiso y revisar contrato. Plan gratis limitado.
- Reels: G30 · 605 likes

### Code Review (plugin)  ·  valor 3  ·  plugin-claude-code
Cinco agentes revisan el codigo en paralelo: bugs, reglas, historial de git.
- Cómo: Ejecutar el comando de code review sobre el diff o PR.
- Para nosotros: CSL: revision automatica antes de entregar a cliente. Ya existe como skill en el entorno.
- Ya lo tenemos: code-review
- Reels: G90 · 529 likes

### gstack (plugin)  ·  valor 3  ·  plugin-claude-code
Pack de 23 skills de Garry Tan (Y Combinator) con roles CEO, jefe de ingenieria, QA, etc.
- Cómo: Instalar plugin gstack desde GitHub.
- Para nosotros: CSL: revision de producto y QA antes de demos. Ver entrada del G113.
- GitHub: garrytan/gstack · 141.385 estrellas · licencia MIT
- Reels: G90 · 529 likes

### Sistemas completos con Claude Code (backend + frontend, multiagentes)  ·  valor 3  ·  tecnica
Tercera recomendación: montar desde asistentes multiagente hasta procesos de negocio con Claude Code y metodología.
- Cómo: Método, orden y claridad; sin necesitar n8n.
- Para nosotros: Es el núcleo de lo que ya hace CSL.
- Reels: G61 · 338 likes

### Codebase Memory (índice de código para Claude)  ·  valor 3  ·  repo-github
Indexa el repositorio en un mapa de funciones y archivos para que Claude no explore todo en cada chat; afirma ~10 veces menos tokens en consultas grandes.
- Cómo: Ir al repo en GitHub, copiar el enlace, pegarlo en Claude y decirle que indexe; después pedir cambios y Claude va directo al archivo. Nombre del owner no dado.
- Para nosotros: CSL: repos grandes de ERP; Diego ya tiene graphify para lo mismo.
- Ojo: Cifra del 10x es del propio proyecto. Indexa código de cliente en local; revisar que no envíe nada fuera.
- Reels: G136 · 294 likes

### /ultraplan  ·  valor 3  ·  tecnica
Comando de Claude Code que lanza un enjambre de agentes en la nube para diseñar un plan completo; el truco es reconstruir el plan en local para no gastar créditos.
- Cómo: Ejecutar /ultraplan con el objetivo; luego rehacer el plan en local.
- Para nosotros: CSL: planificar módulos de ERP o SaaS grandes antes de picar código.
- Ojo: Gasta créditos en la nube. El «80% del código de Anthropic» no tiene fuente.
- Reels: G139 · 224 likes

### /agent (tarea en segundo plano) y /ultrareview  ·  valor 3  ·  tecnica
/agent manda una tarea al segundo plano para lanzar otra en paralelo; /ultrareview lanza otro enjambre que revisa el trabajo producido (ejecutable en local para ahorrar créditos).
- Cómo: Encadenar: /ultraplan, /goal, /agent y /ultrareview; definir objetivo, irse y volver con el trabajo hecho y revisado.
- Para nosotros: CSL: revisión previa a entregar. ECS: paralelizar varias piezas (guiones, landings).
- Ojo: Revisar siempre el resultado final a mano antes de entregar a cliente.
- Reels: G139 · 224 likes

### Repo de system prompts filtrados de herramientas de IA  ·  valor 3  ·  repo-github
Colección pública de system prompts de Cursor, Manus, Lovable, v0 y otras herramientas para estudiar cómo estructuran sus agentes.
- Cómo: Leer los prompts, extraer estructura de instrucciones, herramientas y reglas, y reutilizar patrones en agentes y skills propios.
- Para nosotros: CSL: copiar patrones de prompt de agente de código (planificación, reglas de edición) para skills y para el Setter IA. ECS: ver cómo estructuran agentes de ventas.
- GitHub: x1xhlol/system-prompts-and-models-of-ai-tools · 144.639 estrellas · licencia GPL-3.0
- Ojo: Owner/repo deducido de memoria, verificar. Material filtrado, posible problema de propiedad intelectual; no incluir tal cual en productos. Cifra de miles de millones no verificable.
- Reels: G19 · 166 likes

### Los cuatro niveles de ingeniería de IA (wrapper, RAG, agentes, orquestador)  ·  valor 3  ·  tecnica
Marco para clasificar la madurez de un producto IA: 1 wrapper de prompts, 2 RAG, 3 agentes con herramientas y evals, 4 orquestación multiagente con humano en el loop.
- Cómo: Usarlo como escalera para decidir qué ofrecer o aprender.
- Para nosotros: CSL: argumento de venta para diferenciar un SaaS con agentes de un simple wrapper; ECS: explicar el setter IA como nivel 3.
- Ojo: Marco opinativo del creador, no estándar.
- Reels: G152 · 102 likes

### AirLLM  ·  valor 2  ·  repo-github
Ejecuta modelos de 70B parámetros en GPUs de 4 GB cargando una capa a la vez; compatible con Llama, Qwen, Mistral. Funciona en Mac, Linux y Colab.
- Cómo: pip install airllm y cargar el modelo con la clase AutoModel del paquete.
- Para nosotros: CSL: pruebas locales con datos sensibles de clientes sin nube. Muy lento (segundos por token), no apto para producción.
- GitHub: lyogavin/airllm · 42.267 estrellas · licencia Apache-2.0
- Ojo: El propio caption admite que no siempre funciona. Rendimiento muy bajo; 'comando filtrado' es gancho exagerado.
- Reels: G54 · 1663 likes

### Antigravity (editor de código de Google)  ·  valor 2  ·  saas
Editor con IA competidor de Claude Code y Cursor, orientado a vibe coding.
- Cómo: Instalar el editor y trabajar en proyectos.
- Para nosotros: CSL: alternativa gratis para prototipos.
- Ojo: El código sube a Google.
- Reels: G158 · 578 likes

### Pixel Agents (visualizador de agentes de Claude Code)  ·  valor 2  ·  plugin-claude-code
Extensión que lee los logs de actividad de Claude Code y muestra en interfaz visual cuántos agentes hay activos, subagentes y esperas de permiso.
- Cómo: Instalar la extensión y dejarla leer el registro.
- Para nosotros: Útil si se lanzan varias sesiones/swarm en CSL. Valor menor.
- Ojo: Repo no confirmado. Lee logs locales.
- Reels: G58 · 324 likes

## Apps móviles (1)

### Flujo de app móvil con React Native + Expo y publicación en App Store  ·  valor 4  ·  tecnica
Construir una app iOS/Android desde Claude Code con React Native y Expo, de MVP a publicación.
- Cómo: 1) Pedir a Claude que instale React Native y Expo. 2) Construir MVP. 3) Añadir funciones pequeñas que hagan volver (bucle de reactivación). 4) Probar en Chrome y con QR de Expo en el móvil. 5) Pedir título, descripción, certificados y capturas con una skill de capturas. 6) Enviar a aprobación de Apple.
- Para nosotros: CSL: oferta de apps móviles a medida; prototipar rápido para demos de cliente.
- Fuente: https://expo.dev
- Ojo: «Sin saber programar» es exagerado para producción; la cuenta de Apple Developer cuesta 99 USD al año y la revisión puede rechazar. La skill de capturas no se nombra.
- Reels: G144 · 388 likes

## Entrega (1)

### Forward a Port de VS Code  ·  valor 3  ·  tecnica
Comparte un localhost con una URL publica sin instalar nada.
- Cómo: Levantar el servicio local, copiar el puerto, en VS Code abrir la pestana Ports, Forward a Port, introducir el puerto y compartir la URL publica.
- Para nosotros: CSL: ensenar una demo en curso a un cliente sin desplegar. Util en reuniones tecnicas.
- Ojo: Expone el servicio local a Internet: usar datos ficticios y cerrar el puerto al acabar. En VS Code los puertos pueden ser privados por defecto; hay que marcarlos publicos.
- Reels: G101 · 5476 likes

## Datos y automatización (20)

### MarkItDown (Microsoft)  ·  valor 5  ·  repo-github
Convierte PDF, Word, Excel, PowerPoint y hasta vídeos de YouTube a Markdown limpio; reduce hasta un 70% los tokens. Trae servidor MCP para Claude Desktop.
- Cómo: Instalar MarkItDown, conectar su servidor MCP a Claude Desktop; los archivos enviados se convierten solos a Markdown.
- Para nosotros: CSL: leer contratos, briefings y especificaciones del cliente en PDF y Excel; ECS: ingerir dosieres y facturas para análisis. Pieza clave para cargar documentación de clientes.
- GitHub: microsoft/markitdown · 195.131 estrellas · licencia MIT
- Ojo: Cifras de tokens por página sin fuente primaria; correr en local para no enviar documentos de cliente a terceros.
- Ya lo tenemos: skill markitdown + comando markitdown
- Reels: G167 · 223 likes

### MCP Builder (skill)  ·  valor 4  ·  skill-claude
Claude se conecta a cualquier herramienta describiendola y pasando las conexiones, sin escribir codigo.
- Cómo: Describir la herramienta y dar credenciales; la skill genera el MCP.
- Para nosotros: CSL: conectores MCP propios de clientes y OS. Ya instalada (mcp-builder).
- Ojo: Pide claves de la herramienta objetivo: no pegar claves de clientes en chats compartidos.
- Ya lo tenemos: mcp-builder
- Reels: G118 · 2314 likes

### n8n-MCP + Claude Code en Cursor para generar flujos de n8n  ·  valor 4  ·  mcp
Un repo de GitHub con MCP de n8n permite a Claude Code construir flujos completos de n8n desde un prompt (leads, onboarding, facturas).
- Cómo: 1) Instalar Cursor. 2) Extensión Claude Code. 3) Clonar el repo de GitHub (no se nombra) en Cursor. 4) Abrir n8n, copiar API key y pegarla en Claude Code. 5) Comprobar MCP con marca verde. 6) Pedir el flujo por prompt.
- Para nosotros: ECSSTUDIO: flujos de captación de leads, avisos, onboarding de cliente. CSL: integraciones rápidas entre ERP y herramientas del cliente. Probable repo: czlonkowski/n8n-mcp (no confirmado en el guion).
- Ojo: Pide la API key de n8n del cliente: usar instancia propia o clave con permisos mínimos. Promesa de venta de flujos a 500-3.000 € es de marketing del creador.
- Reels: G48 · 2023 likes

### Agent-Reach (lectura de Twitter, LinkedIn, Reddit y YouTube)  ·  valor 4  ·  repo-github
Herramienta open source que da a Claude Code acceso a transcripciones de YouTube, hilos de Reddit, búsquedas en Twitter y perfiles de LinkedIn sin APIs de pago.
- Cómo: Pegar un comando en la terminal e incorporarlo a Claude Code.
- Para nosotros: ECS: transcripciones de YouTube para clips y guiones, ideas de Reddit y X para contenido, investigación de competidores.
- Ojo: Acceso a LinkedIn y X por vías no oficiales puede violar términos y bloquear cuentas; usar cuentas desechables. El nombre exacto del repo no se da.
- Reels: G162 · 1752 likes

### ScrapeGraphAI  ·  valor 4  ·  repo-github
Libreria open source (MIT) que scrapea webs con lenguaje natural: das una URL y describes que quieres extraer, sin selectores ni codigo.
- Cómo: Dar una URL, escribir en lenguaje normal lo que se quiere (perfiles, emails, precios, listados, reviews) y la IA lo extrae, incluso multipagina.
- Para nosotros: ECS: listas de leads, analisis de competencia y de precios, recopilar anuncios o reviews para propuestas. CSL: extraccion de datos de webs de cliente en migraciones.
- GitHub: ScrapeGraphAI/Scrapegraph-ai · 32.751 estrellas · licencia MIT
- Ojo: Scraping de LinkedIn, Twitter, Amazon y Glassdoor suele violar sus terminos y puede dar problemas legales y de RGPD con emails personales. Las afirmaciones 'sin baneos' y 'cobrar 5.000 dolares por scraping' son marketing sin prueba. Necesita un LLM (coste de API o modelo local).
- Reels: G88 · 1149 likes

### n8n-mcp (servidor MCP de n8n) con Claude Desktop  ·  valor 4  ·  mcp
Servidor MCP que da a Claude conocimiento de los nodos de n8n para que cree flujos completos desde una descripción en lenguaje natural y devuelva el enlace al flujo.
- Cómo: 1) Descargar Claude Desktop e iniciar sesión. 2) Abrir el repo de n8n MCP en GitHub, copiar el primer comando y ejecutarlo en terminal (deja el servidor corriendo). 3) Claude Desktop > Ajustes > Desarrollador > Editar configuración y pegar el bloque JSON del repo. 4) Pedir la automatización en lenguaje natural; el prompt es la clave (guía y prompt exacto prometidos por comentario IA).
- Para nosotros: ECS: montar automatizaciones de seguimiento de leads, avisos y reporting en n8n más rápido. CSL: acelerar integraciones de clientes (WhatsApp, CRM, facturas) como entregable.
- GitHub: czlonkowski/n8n-mcp · 23.253 estrellas · licencia MIT
- Ojo: Repo deducido del nombre (no se cita owner en el guion), verificar. Requiere clave API de n8n y acceso a la instancia; no pasar credenciales de clientes. Cada cliente con su clave.
- Reels: G4 · 1043 likes

### Automatización de gastos: WhatsApp a Drive, extracción con IA a Google Sheets  ·  valor 4  ·  tecnica
Flujo que recibe una foto de recibo por WhatsApp, la guarda en Drive, extrae datos con un LLM, los registra en Sheets y responde con resumen y enlace.
- Cómo: 1) Disparador: mensaje entrante de WhatsApp. 2) Descargar la imagen y subirla a Drive, compartir con enlace. 3) Enviar la imagen al LLM para extraer tienda y total. 4) Limpiar y escribir fila en Sheets. 5) El agente responde por WhatsApp con el resumen y el enlace.
- Para nosotros: ECS/CSL: facturas de proveedores recibidas por WhatsApp o correo a la hoja y al OS de facturas; alta mensual como servicio a clientes.
- Ojo: Enlace compartido a cualquiera con el enlace expone documentos fiscales; usar permisos restringidos. Datos de terceros: RGPD.
- Reels: G36 · 498 likes

### Chatbots de WhatsApp con n8n + YCloud  ·  valor 4  ·  tecnica
Agente en n8n conectado a WhatsApp Business vía YCloud (proveedor oficial, coexistencia con app).
- Cómo: Montar agente en n8n con herramientas y enlazar YCloud como canal.
- Para nosotros: ECS/CSL: IA Setter ya existe en WhatsApp; YCloud como alternativa al canal bloqueado por Meta (ver WhatsApp API OS).
- Fuente: https://www.ycloud.com
- Ojo: Coste por conversación del proveedor; cumplir políticas de WhatsApp. Guion dice 'White Cloud', se deduce YCloud por el caption.
- Reels: G61 · 338 likes

### Firecrawl (MCP)  ·  valor 4  ·  mcp
Lee webs enteras y vuelca el contenido limpio en la conversación.
- Cómo: Instalar el MCP de Firecrawl con API key y pedir a Claude que lea una URL.
- Para nosotros: ECS: analizar la web y los competidores de un lead antes de la propuesta; CSL: migración y auditoría de webs.
- GitHub: firecrawl/firecrawl · 201.302 estrellas · licencia AGPL-3.0
- Ojo: Pide API key (capa gratis limitada). Respetar términos de las webs que se rastrean.
- Reels: G140 · 302 likes

### Contable personal por Telegram (ticket a Google Sheets y Drive)  ·  valor 4  ·  tecnica
Foto de ticket por Telegram, extrae importe, fecha, IVA, lo vuelca en Google Sheets y guarda el archivo en la carpeta del mes en Drive.
- Cómo: Bot de Telegram, OCR/IA, hoja de cálculo y carpeta por mes; herramientas no nombradas (probablemente n8n).
- Para nosotros: Directo para Facturas/Buzones de gastos de ECS y CSL; servicio a vender a clientes.
- Ojo: Datos fiscales de clientes pasan por servicios externos.
- Reels: G71 · 69 likes

### Rowboat (copilot que construye sistemas multiagente)  ·  valor 3  ·  repo-github
Herramienta open source respaldada por Y Combinator: describes lo que quieres en lenguaje natural y construye un sistema multiagente conectado a herramientas.
- Cómo: Describir el agente en lenguaje normal; el copilot genera los agentes y conexiones.
- Para nosotros: CSL: prototipar agentes de atención/ventas para demos de cliente. Alternativa a n8n para agentes.
- GitHub: rowboatlabs/rowboat · 18.187 estrellas · licencia Apache-2.0
- Ojo: Autoría 'vendieron startup a Coinbase' y 'hace irrelevantes las agencias' son de gancho. Repo deducido, comprobar.
- Reels: G56 · 5452 likes

### OpenWA  ·  valor 3  ·  repo-github
API de WhatsApp open source autoalojada con dashboard, multisesion, envio de mensajes y archivos, eventos en tiempo real, control de accesos, despliegue con Docker.
- Cómo: Desplegar con Docker en servidor propio, escanear sesion y usar la API para enviar mensajes y recibir eventos.
- Para nosotros: ECS/CSL: automatizar WhatsApp sin API oficial (CSL tiene la API oficial bloqueada por Meta). Ya existe whatsapp-bridge propio.
- Ojo: API no oficial de WhatsApp: riesgo de baneo del numero y de incumplir terminos de Meta. No usar con numeros de cliente sin avisar.
- Reels: G95 · 3639 likes

### Apify  ·  valor 3  ·  saas
Plataforma de scrapers (actores) para sacar datos de LinkedIn, ofertas y mas.
- Cómo: Se usa desde Claude con un prompt para sacar ofertas recientes.
- Para nosotros: ECS: leads y datos de competencia; alternativa de pago a ScrapeGraphAI.
- Fuente: https://apify.com
- Ojo: Scraping de LinkedIn contra terminos de la plataforma.
- Ya lo tenemos: viral-profile-scraper (Apify)
- Reels: G121 · 1624 likes

### PostHog  ·  valor 3  ·  saas
Analítica de producto con grabaciones de sesiones de usuarios.
- Cómo: Instalar el snippet en la app o web y ver sesiones y eventos.
- Para nosotros: ECS: grabaciones de sesión en landings para detectar fricción. CSL: analítica de uso en SaaS entregados.
- Fuente: https://posthog.com
- Ojo: Consentimiento de cookies/RGPD para grabar sesiones.
- Reels: G31 · 1515 likes

### Google Sheets Canvas (dashboards con Gemini)  ·  valor 3  ·  saas
Dashboard funcional conectado a la hoja en tiempo real; los cambios van en ambos sentidos.
- Cómo: Abrir Google Sheets, ir a Gemini, activar Canvas y describir qué quieres ver.
- Para nosotros: ECS: dashboards rápidos de resultados de campañas para clientes con datos en Sheets (informes semanales, MER, CPA).
- Ojo: Subir datos de cliente a Gemini; disponibilidad según plan de Workspace.
- Ya lo tenemos: Canva MCP
- Reels: G160 · 1351 likes

### Firecrawl como plugin de scraping  ·  valor 3  ·  plugin-claude-code
Scrapea cualquier web, incluso con protección anti-bot, según el guion.
- Cómo: Instalar el plugin de Firecrawl.
- Para nosotros: Análisis de competencia y webs de leads.
- GitHub: firecrawl/firecrawl · 201.302 estrellas · licencia AGPL-3.0
- Ojo: Saltarse protecciones anti-scraping puede violar términos de servicio y leyes de datos; legal sobre datos personales (RGPD).
- Reels: G153 · 1322 likes

### OpenRouter con modelos gratuitos en n8n  ·  valor 3  ·  saas
API unificada para muchos LLMs; sus modelos gratuitos se enchufan al nodo OpenRouter Chat Model de n8n.
- Cómo: Ir a openrouter.ai, crear cuenta, obtener clave API, en n8n añadir el nodo OpenRouter Chat Model, conectar la credencial y escribir free en el selector de modelos.
- Para nosotros: Pruebas y automatizaciones de bajo coste; cambiar de modelo sin reescribir el agente. Regla: cada cliente con su propia clave.
- Fuente: https://openrouter.ai
- Ojo: Los modelos gratis tienen límites y pueden usar tus datos para entrenar; no enviar datos de cliente ni personales. Clave de IA: cada cliente la suya.
- Reels: G37 · 283 likes

### Opal (Google)  ·  valor 2  ·  saas
Constructor visual de flujos que se convierten en mini apps; el creador hizo un generador de títulos virales en menos de 20 segundos.
- Cómo: Unir nodos de prompt y herramientas y publicar como mini app.
- Para nosotros: Mini apps internas (generador de ganchos, títulos) para el equipo de orgánico.
- Reels: G25 · 81480 likes

### Manus Cloud Computer  ·  valor 2  ·  saas
Servidor en la nube (Ubuntu) configurado por Manus a partir de lenguaje natural, que mantiene bots corriendo 24/7 aunque el portatil este apagado.
- Cómo: Describir lo que se quiere (bot de WhatsApp, bot de Telegram con scraping y reportes, base de datos self-hosted) y Manus monta la maquina y el codigo.
- Para nosotros: CSL: hosting rapido de prototipos y bots para demos. ECS: bots de reportes diarios.
- Fuente: https://manus.im
- Ojo: El guion dice 'Zuckerberg lo ha resuelto' (Manus fue adquirida por Meta segun el guion; no verificado). Datos de clientes en servidor de terceros. Ya tenemos VPS propio, preferible. Chatbot de WhatsApp via no oficial puede violar terminos.
- Reels: G93 · 1223 likes

### Google Opal  ·  valor 2  ·  saas
Constructor de flujos de automatización con modelos de Google, tipo n8n o Make.
- Cómo: Describir el flujo y encadenar pasos.
- Para nosotros: ECS: automatizaciones ligeras de contenido; ya hay n8n/ghl.
- Reels: G158 · 578 likes

## Productividad con IA (66)

### MarkItDown  ·  valor 5  ·  repo-github
Herramienta de Microsoft que convierte PDF, Word, Excel, PowerPoint y videos de YouTube a Markdown limpio; reduce tokens (hasta 70% segun el guion) y trae servidor MCP.
- Cómo: Instalar markitdown y convertir archivos antes de pasarlos a Claude, o conectar su MCP a Claude Desktop para conversion automatica.
- Para nosotros: CSL: pasar documentacion y briefings de clientes a Markdown para ficha tecnica y propuestas. ECS: leer PDFs de clientes, contratos y dossieres sin gastar tokens.
- GitHub: microsoft/markitdown · 195.131 estrellas · licencia MIT
- Ojo: Cifras de tokens del guion (1.500-3.000 por pagina) son orientativas. Convierte documentos de clientes: mantener en local.
- Ya lo tenemos: skill markitdown + comando markitdown
- Reels: G111 · 13776 likes

### Claude Skills: qué son y cómo funcionan (explicador)  ·  valor 5  ·  tecnica
Una skill es carpeta con SKILL.md (nombre, descripción de activación, instrucciones) más scripts/plantillas opcionales; se carga progresivamente. No es MCP, ni plugin, ni custom instructions.
- Cómo: Crear carpeta con SKILL.md, subirla en Ajustes, Capacidades, Skills. Claude decide cuándo cargarla y puede combinarlas.
- Para nosotros: Ya aplicado en ECS: skills propuestas-sprint360, guiones-sprint, stories. Más skills: guía de marca por cliente, formato de notas de reunión, análisis de datos.
- Reels: G57 · 768 likes

### Crear una skill propia paso a paso (SKILL.md)  ·  valor 5  ·  tecnica
Crear carpeta y archivo con nombre, descripción e instrucciones; pedir a Claude Code que la genere; se invoca con / o se activa sola.
- Cómo: 1) Editor de texto. 2) Nombre, descripción, instrucciones. 3) Guardar como SKILL.md en carpeta. 4) Invocar con /nombre o dejar activación automática.
- Para nosotros: Skill por cliente (voz de marca, formato de reuniones) en ECS; skills de convenciones de código en CSL.
- Reels: G79 · 389 likes

### Claude for Excel (barra lateral)  ·  valor 4  ·  plugin-claude-code
Extensión de Claude en Microsoft Excel que lee, analiza y construye hojas desde lenguaje natural, con conexión a datos financieros.
- Cómo: Instalar la barra lateral en Excel y pedir: resume gastos por departamento, encuentra el mayor pico de beneficios, crea un libro de trabajo para el cuarto trimestre.
- Para nosotros: ECS: análisis de exportaciones de Meta/CRM, cuotas pendientes y P&G en Excel. CSL: auditoría de datos y migraciones de ERP desde Excel de cliente.
- Ojo: Cifra de 300.000 clientes empresariales sin fuente. Subir datos de clientes a Excel con IA: revisar RGPD y cláusulas.
- Reels: G29 · 30861 likes

### Graphify  ·  valor 4  ·  repo-github
Construye un grafo de conocimiento de toda la base de codigo una vez; Claude navega el grafo en vez de releer archivos, con la reduccion de tokens que afirma el guion (70x, no verificada).
- Cómo: Ejecutar graphify una vez sobre el repo; en sesiones posteriores Claude consulta el grafo. En el entorno de Diego ya instalado como /graphify con graphify query/path/explain.
- Para nosotros: CSL: ahorro de tokens en proyectos grandes (OS, plataforma). Ya adoptado; seguir usandolo y ejecutar graphify update tras cambios.
- Ojo: La cifra de 70 veces menos tokens es de marketing; medir en proyecto propio.
- Ya lo tenemos: graphify
- Reels: G97 · 17315 likes

### MarkItDown MCP  ·  valor 4  ·  mcp
Servidor MCP de MarkItDown que convierte automaticamente cada archivo subido en Claude Desktop.
- Cómo: Conectarlo a Claude Desktop en la configuracion de MCP.
- Para nosotros: Mismo uso que MarkItDown sin pasos manuales.
- GitHub: microsoft/markitdown · 195.131 estrellas · licencia MIT
- Ya lo tenemos: skill markitdown + comando markitdown
- Reels: G111 · 13776 likes

### Claude en Chrome (extensión) con grabación de flujos  ·  valor 4  ·  plugin-claude-code
Extensión gratuita de Chrome que ve la página, responde y actúa; permite grabar un flujo de trabajo (clics y textos) y repetirlo solo.
- Cómo: Instalar desde Chrome Web Store (60 s). Grabar un flujo una vez (ej. investigar noticias del sector cada mañana) y lanzarlo cuando se quiera.
- Para nosotros: ECSSTUDIO: automatizar investigación diaria de competencia, revisión de Biblioteca de Anuncios de Meta, extracción de métricas de paneles sin API. CSL: pruebas manuales repetitivas de demos.
- Fuente: https://claude.ai/chrome
- Ojo: Da control del navegador con sesiones logueadas: riesgo de inyección de prompts y de acciones en cuentas de clientes (Meta, GHL). Usar perfil aislado. Comentando 'extensión' captan lead del evento.
- Ya lo tenemos: Claude in Chrome (MCP)
- Reels: G47 · 4681 likes

### Biblioteca oficial de Skills de Anthropic  ·  valor 4  ·  repo-github
Repositorio oficial con skills listas para Claude.
- Cómo: Descargar la skill y subirla a Claude o a Claude Code.
- Para nosotros: Base para skills propias de ECS (propuestas, guiones) y CSL (documentos, hojas).
- GitHub: anthropics/skills · 193.730 estrellas · licencia null
- Ojo: Revisar el contenido de cualquier skill antes de instalar.
- Ya lo tenemos: pdf, docx, xlsx, pptx, mcp-builder, frontend-design…
- Reels: G52 · 2654 likes

### Agent Browser (skill)  ·  valor 4  ·  skill-claude
Da a Claude un navegador real para clicar, entrar a paginas, extraer informacion y probar el proyecto como un usuario.
- Cómo: Instalar la skill agent-browser.
- Para nosotros: CSL: test de demos y webs de cliente; ECS: revisar landings en vivo. Ya disponible (compound-engineering:agent-browser).
- Ojo: Puede ejecutar acciones reales en webs: usar entornos de prueba.
- Ya lo tenemos: compound-engineering:agent-browser
- Reels: G118 · 2314 likes

### Prompt anti-complaciente para ChatGPT  ·  valor 4  ·  prompt
Instrucciones personalizadas que convierten al modelo en mentor crítico que pone a prueba las ideas en vez de darte la razón.
- Cómo: ChatGPT > Ajustes > Personalización > Instrucciones personalizadas. Texto literal del guion: Sé mi mentor sin flores ni colores rosas. Si mis ideas son malas, dime por qué. Tienes que poner a prueba todo y llevar las cosas hasta el punto en que estén super blindadas. El prompt completo se envía por comentario BLINDADO.
- Para nosotros: Usarlo para revisar propuestas, ofertas y guiones antes de enviarlos (red team de la oferta). Aplicable igual en Claude con una instruccion de proyecto.
- Reels: G24 · 871 likes

### Claude for Small Business (plugin de Cowork)  ·  valor 4  ·  plugin-claude-code
Pack de 15 workflows y 15 habilidades para pymes dentro de Claude Desktop (Cowork): seguimientos, informes financieros, etc.
- Cómo: Claude Desktop > Cowork > Customize > + junto a Personal Plugin > buscar Small > Small Business > Install. Ejemplos: revisar emails de la semana, detectar propuestas sin respuesta y redactar seguimientos; conectar facturas y generar el informe mensual de ingresos, gastos y margenes.
- Para nosotros: ECS: seguimiento automatico de propuestas sin respuesta (alinea con el problema de seguimiento); informe financiero mensual de apoyo. Probar con borradores, no envio automatico.
- Ojo: Requiere dar acceso a email y facturas: datos de clientes y fiscales. Regla de Diego: borradores, nada se envia sin revisar. Incluye mini curso gratuito segun el guion.
- Reels: G92 · 830 likes

### Loops de IA (spec, build y correccion)  ·  valor 4  ·  tecnica
Patron de bucle: la IA evalua su salida contra una checklist y se corrige hasta que no hay margen; se monta con tres prompts que crean Spec Skill, Build Skill y una de correccion.
- Cómo: Copiar tres prompts de una pagina (no dada) a Claude Code; abrir un proyecto y pedir que use las tres skills.
- Para nosotros: CSL/ECS: bucle de calidad para guiones, anuncios y codigo con checklist de marca. Se puede hacer con /loop y skills propias.
- Ojo: Pueden consumir muchos tokens si no hay limite de iteraciones (ver G100).
- Reels: G123 · 774 likes

### Exportar fuentes de NotebookLM a Markdown y montar un cerebro en Obsidian con Claude Code  ·  valor 4  ·  tecnica
Extensión de Chrome que exporta todas las fuentes de un cuaderno a Markdown; se pasan a una carpeta de proyecto y Claude Code las organiza como un vault de Obsidian enlazado.
- Cómo: 1) Instalar la extensión de exportación (nombre no dado). 2) Abrir el cuaderno, ejecutarla y descargar la carpeta. 3) Pegarla en un proyecto nuevo. 4) Claude Code apuntado a la carpeta con un prompt que organice todo como cerebro digital en Obsidian. 5) Trabajar con ese contexto.
- Para nosotros: ECS: base de conocimiento por cliente (entrevistas, competencia, documentos) consultable por Claude. CSL: documentación de proyecto.
- Ojo: Las extensiones de Chrome de terceros leen tu sesión de Google; revisar permisos.
- Reels: G138 · 755 likes

### anthropics/skills (repo oficial de skills)  ·  valor 4  ·  repo-github
Repositorio oficial de Anthropic con mas de 30 skills: PDF, Excel, Word, brand kits, frontend.
- Cómo: Descargar el repo e instalar las skills.
- Para nosotros: ECS: generar propuestas y contratos en docx/pdf, informes en Excel. Muchas ya instaladas (docx, pdf, xlsx, pptx, brand-guidelines).
- GitHub: anthropics/skills · 193.730 estrellas · licencia null
- Ojo: La cifra de 143.000 descargas es del guion.
- Ya lo tenemos: pdf, docx, xlsx, pptx, mcp-builder…
- Reels: G116 · 348 likes

### Claude Code Setup (plugin oficial de Anthropic)  ·  valor 4  ·  plugin-claude-code
Escanea la base de código y recomienda hooks, skills, subagentes y MCPs que encajan con el proyecto, en menos de 30 segundos.
- Cómo: Instalar el plugin una vez, ejecutar su comando y revisar las recomendaciones; si detecta fallos de seguridad sugiere un subagente revisor.
- Para nosotros: CSL: arrancar cada repo de cliente con la configuración de Claude Code adecuada; evita instalar plugins al azar.
- GitHub: anthropics/claude-plugins-official · 47.063 estrellas · licencia Apache-2.0
- Reels: G133 · 105 likes

### Configuración global vs de proyecto en Claude Code (CLAUDE.md, skills y agentes)  ·  valor 4  ·  tecnica
Separar CLAUDE.md global (comportamiento en todos los proyectos) de CLAUDE.md de proyecto (stack, carpetas, despliegue); skills y agentes globales ocupan contexto en todos, así que solo lo universal.
- Cómo: CLAUDE.md global con estilo y preferencias; skills y agentes globales solo universales; por proyecto, stack, estructura, despliegue y skills propios (no disponibles en otros proyectos).
- Para nosotros: Diego ya lo hace; revisar que no haya demasiadas skills globales (el listado actual es enorme y consume contexto).
- Reels: G142 · 103 likes

### Skills que dejar escritas antes de perder el plan superior  ·  valor 4  ·  tecnica
Pedir al modelo bueno que escriba cinco skills para que los modelos inferiores las sigan: auditoria de seguridad, setup de proyecto, planificador, asesor honesto (sin modo pelota) y cazador de bugs.
- Cómo: Preguntar: te vas, que manuales quieres dejar? Guardar las cinco como skills.
- Para nosotros: CSL: skills propias de seguridad, plan y bugs para que el equipo y los modelos baratos mantengan el estandar.
- Reels: G129 · 40 likes

### Kimi Claw (agente 24/7 en la nube de Moonshot/Kimi)  ·  valor 3  ·  saas
Agente gestionado en la nube con un clic, precio fijo, contexto de 1 M tokens, 40 GB y 5.000 skills; modelo K2.5 a 0,58 $ por M de tokens.
- Cómo: Activarlo desde Kimi; sin código ni VPS.
- Para nosotros: Alternativa barata a agentes propios; mirar K2.5 como modelo barato para tareas masivas.
- Fuente: https://www.kimi.com
- Ojo: Datos de clientes en servidor chino: no usar con datos personales. Afirmaciones de superioridad y 'mejor que Claude Code' sin prueba.
- Reels: G66 · 5061 likes

### Cursos gratuitos de Anthropic (Anthropic Academy)  ·  valor 3  ·  saas
Biblioteca oficial de cursos gratis para aprender Claude.
- Cómo: Entrar en la web de cursos de Anthropic.
- Para nosotros: Formación del equipo ECS y becarios de CSL.
- Fuente: https://www.anthropic.com/learn
- Reels: G52 · 2654 likes

### Stack de 7 días para lanzar una empresa (orquestación de herramientas)  ·  valor 3  ·  tecnica
Lista de herramientas por fase: investigación, branding, diseño, desarrollo, cobro, email, hoja de ruta, analítica y creativos.
- Cómo: Perplexity para investigación; Replicate para imágenes de marca; Claude para branding y go-to-market; Mobbin para referencias; Cursor para construir; Stripe y RevenueCat para cobrar; Resend para email; Linear para hoja de ruta con Cursor; PostHog para analítica; Foreplay para creativos de Meta. Biblioteca por comentario KIT.
- Para nosotros: CSL: checklist de stack para MVPs en 7 días con demo. Cada pieza abajo como entrada propia.
- Ojo: Promesa de montar una empresa en 7 días: hipérbole. Nombres transcritos con errores (Moblin, Recent, PostHoc, E4Play).
- Reels: G31 · 1515 likes

### Auto-Research (optimización de skills en bucle)  ·  valor 3  ·  plugin-claude-code
Toma skills existentes, las testea y las optimiza en bucle hasta mejorar de forma medible.
- Cómo: Instalar y apuntar a las skills a optimizar. Sin detalle.
- Para nosotros: ECS: afinar las skills propias (guiones-sprint, propuestas-sprint360) con métricas.
- Ojo: Puede gastar muchos tokens; repo no identificado.
- Reels: G153 · 1322 likes

### OpenClaw (agente autónomo con Telegram)  ·  valor 3  ·  repo-github
Agente open source con memoria persistente que ejecuta código y tareas en tu ordenador a través de Telegram y puede crear sus propias skills.
- Cómo: Enviarle un mensaje por Telegram (ej. hazme una app de tareas); abre herramientas, corrige errores, sube a GitHub y devuelve el enlace. Cowork se contrapone como privado y en navegador.
- Para nosotros: El entorno del equipo ya incluye un workspace openclaw. Uso: tareas de desarrollo desde el móvil, borradores y vigilancia.
- GitHub: openclaw/openclaw · 394.403 estrellas · licencia MIT
- Ojo: Owner deducido, verificar. Acceso total a la máquina, skills autocreadas y memoria: riesgo de seguridad y fuga de datos de clientes; aislar en VPS.
- Reels: G40 · 1023 likes

### Claude Council (skill del consejo)  ·  valor 3  ·  skill-claude
Skill con 5 asesores de IA (contrarian, primeros principios, expansionista, outsider, ejecutor) que se revisan entre pares y devuelven un veredicto con plan, para evitar el servilismo del modelo.
- Cómo: Decir 'pregunta al consejo' ante una decision; 5 respuestas, 5 revisiones cruzadas y un veredicto.
- Para nosotros: Ya cubierto: Diego tiene agentes consejo-* y la skill consejo. Puede mejorar presidente de decisiones de oferta.
- Ojo: Autor mencionado como Ali Limon (nombre dudoso por Whisper).
- Ya lo tenemos: consejo
- Reels: G114 · 792 likes

### Directorio de skills oficiales de Anthropic  ·  valor 3  ·  repo-github
Directorio curado con skills de seguridad, productividad, desarrollo y diseño.
- Cómo: Descargar y subir a Claude.
- Para nosotros: Ver G52.
- GitHub: anthropics/skills · 193.730 estrellas · licencia null
- Reels: G57 · 768 likes

### Claude Code Remote Control (comando rc)  ·  valor 3  ·  tecnica
Control remoto de Claude Code desde el móvil: se escribe rc, sale un QR y se maneja la sesión del portátil desde el teléfono.
- Cómo: Abrir terminal con Claude Code, comando rc, escanear QR con el móvil.
- Para nosotros: Diego ya usa VPS y chat; permite dirigir sesiones largas de desarrollo CSL desde fuera. Verificar el comando exacto en la documentación actual.
- Ojo: Sesión del portátil expuesta al móvil: cuidar el acceso. Comando exacto no confirmado.
- Reels: G55 · 614 likes

### Comando /compact de Claude  ·  valor 3  ·  tecnica
Resume la conversación para seguir sin quemar límite de uso.
- Cómo: Escribir /compact en el chat.
- Para nosotros: Ahorro de tokens en sesiones largas de CSL.
- Ojo: El guion lo mezcla con abrir un chat nuevo; en Claude Code compacta in situ.
- Reels: G78 · 602 likes

### LLM Council de Karpathy  ·  valor 3  ·  repo-github
Proyecto que hace debatir a varios LLMs y sintetiza la respuesta más precisa; alternativa gratuita al Model Council de Perplexity.
- Cómo: Clonar el repo, poner claves de OpenRouter o similares; también hay Space de Hugging Face.
- Para nosotros: Decisiones difíciles (precios, ofertas); similar al Consejo propio de Diego.
- GitHub: karpathy/llm-council · 26.456 estrellas · licencia null
- Ojo: Pide claves de API de varios proveedores.
- Ya lo tenemos: consejo
- Reels: G70 · 500 likes

### Lista de proveedores de API de IA gratuitos (repo GitHub)  ·  valor 3  ·  repo-github
Repo con ~22.000 estrellas que lista proveedores de APIs de modelos de IA con capa o créditos gratis para proyectos, agentes y pruebas.
- Cómo: Abrir el repo, elegir proveedor, sacar API key gratuita y conectarla al proyecto. El guion no da el nombre del repo.
- Para nosotros: CSL: prototipos y demos con modelos gratis antes de pagar OpenAI/Anthropic; ECS: automatizaciones internas de bajo coste (clasificar leads, resumir llamadas).
- Ojo: Los límites de las capas gratis cambian y pueden usar tus datos para entrenar: no pasar datos de clientes. No usar en producción de cliente sin plan de pago.
- Reels: G130 · 482 likes

### Headroom  ·  valor 3  ·  repo-github
Proxy que se coloca delante de Claude y elimina de logs, archivos y volcados el ruido antes de llegar al modelo; el guion afirma 60-90% menos de tokens. Creado segun el guion por un ingeniero de Netflix.
- Cómo: Ir al repo, copiar el boton de instalacion y pegarlo en Claude Code; una linea de configuracion.
- Para nosotros: CSL: bajar coste de tokens en sesiones largas con logs y salidas de comandos.
- Ojo: Se interpone entre tu contenido y el modelo: revisar que no envia nada a un tercero. El ahorro de 700.000 dolares es afirmacion no verificada.
- Reels: G122 · 464 likes

### Prompt Master (skill)  ·  valor 3  ·  skill-claude
Convierte una frase desordenada en un prompt completo (resultado esperado, archivos permitidos, cuándo parar); revisa contra 35 formas conocidas de desperdiciar créditos y recuerda decisiones pasadas. 11.000 estrellas, licencia MIT.
- Cómo: Descargar el repo; en Claude, Personalizar > Añadir skills; describir lo que quieres en una frase. Funciona también con ChatGPT.
- Para nosotros: ECS: que el equipo y becarios saquen prompts mejores y gasten menos cuota.
- Ojo: Auditar el contenido de la skill antes de instalar; repo no identificado.
- Ya lo tenemos: prompt-master
- Reels: G166 · 334 likes

### Composio como conector personalizado de Claude (1000+ apps, Canva)  ·  valor 3  ·  mcp
Una cuenta de Composio da un enlace MCP que conecta Claude a más de mil apps, incluido Canva, para diseñar con un prompt.
- Cómo: Claude > Personalizar > Conectores > Añadir personalizado; crear cuenta en Composio, buscar Claude, copiar el enlace, pegarlo, ponerle nombre y añadir.
- Para nosotros: ECS: acceso a muchas apps desde un solo conector (CRM, redes, Sheets). Diego ya tiene Canva directo.
- Fuente: https://composio.dev
- Ojo: Da a un intermediario tokens OAuth de todas tus cuentas conectadas; limitar apps y permisos. La capa gratis puede tener límites.
- Ya lo tenemos: Canva MCP
- Reels: G164 · 304 likes

### Perplexity (MCP de búsqueda web)  ·  valor 3  ·  mcp
Da a Claude Code búsqueda web en tiempo real.
- Cómo: Instalar el MCP de Perplexity en Claude Code con su API key.
- Para nosotros: ECS: investigación de competencia y tendencias de nicho con fuentes actuales.
- Ojo: Pide API key de pago.
- Reels: G140 · 302 likes

### Claude in Chrome (lectura de pestañas)  ·  valor 3  ·  mcp
Claude lee lo que tengas abierto en el navegador, con contexto de páginas en vivo.
- Cómo: Instalar la extensión de Claude en Chrome y conectarla.
- Para nosotros: Ya usado por Diego (claude-in-chrome) para GHL y Meta Ads.
- Ojo: Acceso a sesiones abiertas (banca, CRM): limitar sitios permitidos.
- Ya lo tenemos: Claude in Chrome (MCP)
- Reels: G140 · 302 likes

### The Agency (equipo de agentes open source)  ·  valor 3  ·  repo-github
Equipo completo de agentes especializados (frontend, redactores de anuncios, comunidades de Reddit...) que se instala en Claude Code, con app de escritorio para instalación en un clic. 124.000 estrellas según el guion.
- Cómo: Instalar el repo en Claude Code o con la app de escritorio.
- Para nosotros: ECS: agentes de copy de anuncios, SEO y comunidad; CSL: agentes de frontend y QA. Sirve como catálogo de roles para el equipo de IA de la agencia.
- Ojo: Muchos agentes ocupan contexto; revisar prompts de agentes de terceros antes de instalarlos. Las 124k estrellas deben verificarse.
- Reels: G171 · 288 likes

### Pinokio (llamado 'Pinocchio')  ·  valor 3  ·  saas
Lanzador de un clic para ejecutar localmente herramientas de IA de texto, voz, imagen y vídeo.
- Cómo: Instalar y elegir app.
- Para nosotros: Vídeo/voz local sin suscripción.
- Fuente: https://pinokio.computer
- Ojo: Ejecuta scripts de terceros en el equipo; revisar cada app.
- Reels: G85 · 269 likes

### Claude para Excel  ·  valor 3  ·  saas
Barra lateral de Claude dentro de Excel: lee, analiza y construye hojas con lenguaje natural, con datos financieros en vivo.
- Cómo: Instalar el complemento en Excel y pedir resumen, previsiones o libros nuevos.
- Para nosotros: ECS: informes de gastos de anuncios, MER y presupuestos desde las hojas de cliente.
- Ojo: Datos financieros del cliente en la nube; cifra de 300.000 empresas del guion sin fuente.
- Reels: G127 · 265 likes

### NotebookLM: investigación por objetivos y prompt estructurado  ·  valor 3  ·  tecnica
Mejora la calidad de las fuentes que busca NotebookLM: dar el objetivo de la investigación en vez del tema y usar un prompt muy estructurado en la caja de búsqueda.
- Cómo: 1) Empezar la instrucción con lo que quieres conseguir, no con el tema. 2) Usar prompt estructurado (la caja es pequeña). Los tres prompts literales no se dan.
- Para nosotros: ECS: investigación de nicho y competencia de un cliente antes de propuesta u orgánico.
- Fuente: https://notebooklm.google.com
- Reels: G137 · 264 likes

### Skill de investigación propia creada con Claude (Personalizar > Skills > Crear con Claude)  ·  valor 3  ·  tecnica
Se crea una skill con el criterio de investigación del usuario (tipo de investigación, fuentes preferidas, enfoque) y se pega como instrucción en NotebookLM.
- Cómo: En Claude: Personalizar > Skills > Crear con Claude; explicar qué investigación haces, qué fuentes prefieres y qué enfoque; responder sus preguntas; copiar el resultado a NotebookLM.
- Para nosotros: ECS: skill de investigación de mercado por cliente con criterio de la kb-mercado de Diego.
- Reels: G137 · 264 likes

### Checklist de configuración inicial de Claude (app de escritorio, instrucciones, conectores, modelos, proyectos)  ·  valor 3  ·  tecnica
Cinco ajustes: app de escritorio con acceso a archivos; instrucciones personalizadas (incluyendo lo que no quieres); conectores (Gmail, Drive, Notion); cambiar de modelo según tarea; proyectos con instrucciones y documentos por área.
- Cómo: Descargar la app; Ajustes > instrucciones (ej.: «corrígeme cuando me equivoque, nada de guiones largos, respuestas en menos de 150 palabras»); conectar herramientas; elegir modelo en el desplegable; crear proyecto y subir documentos.
- Para nosotros: ECS: un proyecto de Claude por cliente con brief, voz de marca y documentos; para onboarding del equipo y becarios.
- Ojo: Los conectores dan acceso a datos de clientes: usar cuentas con mínimo privilegio.
- Reels: G149 · 136 likes

### Understand Anything  ·  valor 3  ·  plugin-claude-code
Plugin que convierte codigo o documentos en un grafo de conocimiento interactivo con comandos /understand, /understand-dashboard, /understand-chat, /understand-diff y /understand-domain.
- Cómo: Instalar el marketplace de plugins y luego el plugin; /understand crea el grafo, dashboard lo visualiza, chat conversa, diff muestra impacto de un cambio, domain analiza flujos de datos del negocio.
- Para nosotros: CSL: /understand-diff antes de subir cambios al OS; /understand-domain para documentos de negocio de clientes ERP. Complementa Graphify.
- Ojo: Los documentos de clientes pasan por el agente: mantener en local.
- Reels: G119 · 121 likes

### Pack oficial de skills de Anthropic  ·  valor 3  ·  skill-claude
Conjunto curado de skills oficiales (programación, frontend, calidad de vida) instalable en Claude Code.
- Cómo: Añadir el marketplace oficial de Anthropic e instalar las skills que interesen.
- Para nosotros: Ya instalado en parte (anthropic-skills:docx, pptx, pdf, xlsx). Útil para propuestas en pdf/docx.
- GitHub: anthropics/skills · 193.730 estrellas · licencia null
- Ya lo tenemos: pdf, docx, xlsx, pptx, mcp-builder, frontend-design…
- Reels: G132 · 90 likes

### Claude.md de tres niveles  ·  valor 3  ·  tecnica
Archivo de instrucciones permanentes con tres niveles (global del ordenador, proyecto, carpeta). Idea: que el modelo bueno escriba las reglas para que los modelos inferiores las sigan.
- Cómo: Pedir al plan bueno que escriba los tres archivos: global, de proyecto y de carpeta.
- Para nosotros: Ya aplicado en Diego (CLAUDE.md global y de proyecto). Revisar que el de carpeta exista donde hace falta.
- Ojo: No sustituye la capacidad del modelo bueno.
- Reels: G128 · 63 likes

### Learn Your Way (Google)  ·  valor 2  ·  saas
Tutor personalizado de Google que crea un currículum con vídeos, cuestionarios y proyectos y adapta las lecciones según tus puntos débiles.
- Cómo: Pegar qué quieres aprender; sigue el currículum generado.
- Para nosotros: Formación interna de becarios y equipo en temas concretos.
- Reels: G34 · 33689 likes

### Sistema de 4 pasos para optimizar el CV con Claude  ·  valor 2  ·  prompt
Prompts encadenados en el mismo chat: reclutador senior puntua el match, reescribe con formula XYZ de Google, simula filtro ATS y propone 10 ofertas.
- Cómo: 1) Subir CV y oferta: actua como reclutador senior de esa empresa, puntuacion de match sobre 100, 5 palabras clave que faltan y 3 red flags en menos de 10 segundos. 2) Reescribe mi experiencia con esas palabras y la formula XYZ (logre X medido por Y haciendo Z). 3) Actua como filtro ATS y como responsable que lee 200 CV, dime que secciones saltaria y reescribelas. 4) Busca 10 ofertas y personaliza la candidatura.
- Para nosotros: ECS: el patron 'actua como el comprador y puntua sobre 100' sirve para revisar propuestas y landings antes de enviarlas. No aplica el CV.
- Ojo: Enviar candidaturas automaticas es poco fiable; el propio creador dice que no fue a las entrevistas.
- Reels: G99 · 8369 likes

### Proxy gratuito para Claude Code (modelos alternativos)  ·  valor 2  ·  repo-github
Repo que engana a Claude Code para que hable con modelos gratuitos (NVIDIA NIM, OpenRouter, Ollama local con DeepSeek, Kimi, GLM) en vez de Claude.
- Cómo: Ir al repo en GitHub, ejecutar dos comandos y elegir proveedor: clave gratuita de NVIDIA NIM u OpenRouter, o Ollama en local.
- Para nosotros: Bajo para trabajo de cliente. Util para tareas masivas de bajo riesgo (clasificar, resumir) con coste cero.
- Ojo: Calidad inferior (el guion dice 80-90% sin prueba). Envia codigo y contexto a proveedores terceros: nada de datos de clientes. Posible incumplimiento de terminos de Anthropic.
- Reels: G94 · 4594 likes

### Find Skills (skill)  ·  valor 2  ·  skill-claude
Busca en el catalogo la skill adecuada para el proyecto descrito y la instala.
- Cómo: Decir que proyecto se quiere construir.
- Para nosotros: Ya instalada (find-skills).
- Ojo: Instala codigo de terceros: revisar antes.
- Reels: G118 · 2314 likes

### Cortex Notebook LM / WebSync (extensiones para volcar fuentes)  ·  valor 2  ·  plugin-claude-code
Extensión de Chrome que vuelca artículos, documentos, vídeos y chats de IA a NotebookLM en un clic.
- Cómo: Instalar la extensión y mandar fuentes al notebook.
- Para nosotros: Investigación de nichos y base de conocimiento para propuestas.
- Ojo: No es de Claude pese al tipo; extensión de terceros con acceso a navegación.
- Reels: G75 · 2278 likes

### Borrado de huella digital con Claude  ·  valor 2  ·  tecnica
Flujo: Claude lista data brokers con enlaces de baja, redacta solicitudes, las envia con su navegador y repite semanalmente con una tarea programada.
- Cómo: 1) Busca todo lo que haya sobre mi y lista data brokers con enlace de baja. 2) Redacta la solicitud exacta para cada uno. 3) Envia cada solicitud con el navegador. 4) Revisa cada semana y reenvia las ignoradas.
- Para nosotros: ECS: servicio de privacidad para clientes o para Diego; plantilla de solicitudes RGPD (arco).
- Ojo: Dar datos personales al agente y que actue en webs en tu nombre; 'eliminó cientos de webs' no verificado. Los data brokers de EE.UU. aplican poco en Espana.
- Reels: G126 · 1956 likes

### Gemini Gems con pasos y editor avanzado  ·  valor 2  ·  saas
Los Gems de Gemini ahora ejecutan pasos y se conectan a Opal para crear mini apps con Nano Banana y Veo.
- Cómo: Crear un Gem, abrir el editor avanzado, conectarlo a Opal y encadenar nodos; ejemplo: pedir nombre de producto y generar estrategia e ideas de contenido en HTML.
- Para nosotros: ECS: Gems de ideación de contenido o ganchos con nombre de producto del cliente. Equivalente a las skills propias.
- Fuente: https://gemini.google.com/gems
- Ojo: Quedan en el ecosistema Google; los Gems no sustituyen skills versionadas.
- Reels: G23 · 1607 likes

### Linear + Cursor (hoja de ruta con despliegue automático)  ·  valor 2  ·  saas
Gestión de tareas que se conecta con Cursor para que el agente implemente y despliegue actualizaciones.
- Cómo: Crear tareas en Linear, conectar Cursor, dejar que implemente.
- Para nosotros: CSL: asignar tickets a agentes de código; el OS propio ya tiene tickets.
- Fuente: https://linear.app
- Reels: G31 · 1515 likes

### Claude Desktop (app de escritorio) con servidores MCP  ·  valor 2  ·  saas
Aplicación de escritorio de Claude que carga servidores MCP desde un fichero de configuración para ejecutar acciones en otras herramientas.
- Cómo: Ajustes > Desarrollador > Editar configuración, pegar el bloque mcpServers del repo del MCP, reiniciar.
- Para nosotros: Base para conectar MCPs (n8n, Apify, Explorium) sin terminal. El equipo ya trabaja con MCPs propios.
- Reels: G4 · 1043 likes

### Odysseus (PewDiePie)  ·  valor 2  ·  repo-github
Workspace de IA open source local: deep research, memoria persistente, agentes de OpenCode, bandeja de email organizada por IA, analisis de hardware y clon de Photoshop.
- Cómo: Instalarlo en local y conectar un modelo.
- Para nosotros: Poco: Diego ya tiene su stack. Vigilar como idea de producto privado.
- Ojo: Atribucion a PewDiePie sin confirmar; revisar antes de conectar email.
- Reels: G109 · 964 likes

### claude-mem  ·  valor 2  ·  plugin-claude-code
Da memoria persistente a Claude entre sesiones para no reexplicar el proyecto.
- Cómo: Instalar el plugin y trabajar; guarda contexto de sesiones previas.
- Para nosotros: Poco necesario: Diego ya tiene memoria propia y graphify.
- Ojo: Guarda historial de sesiones, posibles datos de clientes en local.
- Reels: G90 · 529 likes

### OmniRoute (router de modelos gratuitos para Claude Code)  ·  valor 2  ·  repo-github
Conecta Claude Code a más de 200 proveedores gratuitos, cambia de modelo al agotar el límite y comprime prompts (hasta 90% menos tokens, según el guion).
- Cómo: Instalar el repo y apuntar Claude Code a su endpoint.
- Para nosotros: CSL: seguir trabajando cuando se agota el límite en tareas sin datos sensibles.
- Ojo: Proxy intermedio: ve código y prompts; modelos gratis pueden registrarlos. Los 1.600 millones de tokens y el 90% no tienen fuente. No usar con código de clientes.
- Reels: G156 · 410 likes

### Agentes en la nube (Black Box)  ·  valor 2  ·  saas
Plataforma para ejecutar agentes de IA en la nube, un entorno por agente, en paralelo, desde el navegador, sin depender del portatil abierto.
- Cómo: Crear entornos en la nube, clonarlos y lanzar agentes en paralelo.
- Para nosotros: CSL: agentes largos sin dejar el Mac encendido; ya hay VPS propio y claude-flow.
- Ojo: Codigo y datos en nube de terceros. Equivalentes propios: VPS.
- Reels: G103 · 333 likes

### Codigos secretos de ChatGPT  ·  valor 2  ·  prompt
Cinco atajos: /human, L10, X10 Think, Kill Critic, Alt 3.
- Cómo: /human antes del prompt para tono natural; L10 explica como a un nino de 10 anos; X10 Think al final fuerza razonar mas; Kill Critic evita avisos de consulta a un profesional; Alt 3 al final devuelve 3 versiones (copia, estructura y plan de accion).
- Para nosotros: ECS: Alt 3 para sacar variantes de copy; /human para evitar tono corporativo (ya cubierto por anti-patrones de redaccion).
- Ojo: No son comandos oficiales, solo patrones de prompt que cambian segun modelo. Kill Critic desactiva cautelas: no usar para consejo legal o fiscal de clientes.
- Reels: G110 · 258 likes

### SciBot  ·  valor 2  ·  saas
Asistente de IA conectado a una gran base de datos de articulos cientificos que responde con enlace directo al articulo original.
- Cómo: Hacer una pregunta; analiza millones de estudios y devuelve respuesta con fuentes.
- Para nosotros: ECS: respaldo con fuentes para contenido educativo, con cautela. Util en la kb de mercado.
- Ojo: Sin enlace ni detalles verificables; comprobar que cita fuentes reales.
- Reels: G104 · 256 likes

### Escepticismo ante benchmarks de modelos  ·  valor 2  ·  tecnica
Aviso de que los benchmarks de lanzamiento no prueban calidad; ejemplo de modelo que parecía conocer canary strings.
- Cómo: Probar los modelos en tareas propias antes de cambiar de proveedor.
- Para nosotros: Criterio para elegir modelo del Setter IA: probar con conversaciones reales.
- Ojo: Afirmación sobre Karpathy y Gemini 3 sin verificar; guion contradictorio.
- Reels: G35 · 248 likes

### Free Claude Code (FCC) con OpenRouter o NVIDIA NIM  ·  valor 2  ·  repo-github
Repo que permite usar el CLI de Claude Code con modelos gratuitos de proveedores como OpenRouter o NVIDIA NIM.
- Cómo: Pegar el comando de instalación; ejecutar fcc-server (abre web de configuración); elegir modelo, pegar API key gratuita y validar; en otra terminal ejecutar fcc-claude.
- Para nosotros: CSL: tareas rutinarias de bajo riesgo sin gastar cuota de Claude.
- Ojo: Es un proxy de terceros: las claves y el código pasan por él y por el proveedor gratis. Calidad del modelo inferior. Posible incumplimiento de términos de Anthropic; no usar con código de clientes.
- Reels: G143 · 227 likes

### Plugin Human Resources de Claude Cowork (/hr comp-analysis)  ·  valor 2  ·  plugin-claude-code
Analiza una nómina contra el mercado y da percentil, diferencia con la media y qué decir en negociación; también cartas de oferta, onboarding, organización de equipos y evaluaciones.
- Cómo: Cowork > Personalizar > Explorar plugins > Human Resources; en el chat /hr comp-analysis, subir la nómina y responder preguntas.
- Para nosotros: Diego ya tiene human-resources:comp-analysis, draft-offer y onboarding: contratos de equipo, bandas de comisión del closer, becarios.
- Ojo: Datos salariales sensibles; los datos de mercado pueden no ser fiables para España.
- Reels: G146 · 175 likes

### Claude vende tus cosas en Wallapop (fotos a anuncio y publicación con navegador)  ·  valor 2  ·  tecnica
Sube fotos, Claude identifica, tasa con datos de mercado, redacta anuncio y, con navegador, lo publica y negocia con compradores.
- Cómo: Subir fotos, pedir identificación y precio, pedir anuncio (título, descripción, precio), pedir que abra el navegador y publique, programar revisión diaria para responder compradores.
- Para nosotros: Casi nulo; la mecánica foto a ficha y publicación sirve para clientes con catálogo (coches, inmobiliaria, ecommerce), p. ej. concesionarios de Jacobo.
- Ojo: Automatizar publicación y respuestas en Wallapop puede violar sus términos; negociar solo sin revisión es arriesgado.
- Reels: G147 · 119 likes

### Inkling (Thinking Machines, open weights)  ·  valor 2  ·  modelo-ia
Primer modelo del laboratorio de Mira Murati, open weights, pensado para personalizarse con datos propios; incluye dial de esfuerzo de razonamiento y se autoentrenó para no usar la letra E.
- Cómo: Acceder a la plataforma pública y entrenar la base con datos, flujo o producto propios.
- Para nosotros: CSL: vigilar como base para modelos afinados por cliente (ERP con asistente propio).
- Fuente: https://thinkingmachines.ai
- Ojo: Noticia; afirmaciones del lanzamiento sin verificar. No prometer a clientes modelos propios sin probar.
- Reels: G151 · 95 likes

### Ponytail (plugin de optimización de output)  ·  valor 2  ·  plugin-claude-code
Plugin que dice reducir el consumo de tokens más de un 50% optimizando el output de Claude Code. Nombre dudoso en la transcripción (PonyTech/Ponytail).
- Cómo: Instalar desde el marketplace de plugins de Claude Code. El guion no da pasos.
- Para nosotros: CSL: abaratar sesiones largas de desarrollo.
- Ojo: Cifra del 50% sin fuente; verificar el nombre real y el código antes de instalar (plugin de terceros con acceso al proyecto).
- Reels: G132 · 90 likes

### claude-mem (memoria entre sesiones)  ·  valor 2  ·  plugin-claude-code
Da memoria persistente a Claude Code entre sesiones sobre el proyecto y los archivos.
- Cómo: Instalar el plugin y trabajar con normalidad; recupera contexto de sesiones anteriores.
- Para nosotros: CSL: proyectos largos de cliente sin reexplicar contexto. Diego ya usa memoria propia (MEMORY.md, agentdb).
- GitHub: thedotmack/claude-mem · 116.605 estrellas · licencia Apache-2.0
- Ojo: Guarda contenido de sesiones: puede almacenar datos de clientes; revisar dónde se guarda.
- Reels: G132 · 90 likes

### Skill de Obsidian para Claude Code  ·  valor 2  ·  skill-claude
Conecta Claude Code con un vault de Obsidian para usarlo como segundo cerebro de código y notas.
- Cómo: Instalar la skill y apuntar Claude al vault.
- Para nosotros: Diego ya tiene MCP de Obsidian conectado; unir documentación de clientes y repos.
- Reels: G132 · 90 likes

### Análisis de 900 ofertas de empleo en IA (RAG, LangChain, LangGraph)  ·  valor 2  ·  tecnica
Dato de mercado: piden sobre todo Python, AWS/Docker/Kubernetes, RAG y prompt engineering; LangChain y LangGraph top 2; 93% pide más que IA generativa.
- Cómo: Informativo, sin pasos.
- Para nosotros: CSL: orientar a los programadores becarios en qué formarse (RAG, despliegue) y posicionar oferta de agentes con RAG.
- Ojo: Estudio sin fuente nombrada; no citarlo en propuestas.
- Reels: G141 · 88 likes

## Modelos de IA (2)

### NVIDIA build.nvidia.com (modelos gratis via API)  ·  valor 3  ·  saas
API gratuita de NVIDIA con unos 80 modelos (Minimax, GLM, Kimi, DeepSeek, GPT-OSS) compatible con el formato OpenAI.
- Cómo: Ir a build.nvidia.com, obtener API key gratuita, base URL integrate.api.nvidia.com, pegar la clave y elegir modelo (Minimax M2.7, Kimi 2.5, DeepSeek 3.2) en Cursor, OpenCode o agentes.
- Para nosotros: ECS/CSL: tareas masivas de bajo riesgo (clasificar leads, resumir) sin gastar API. No para datos de clientes.
- Fuente: https://build.nvidia.com
- Ojo: Limites de uso y condiciones no explicados; 'sin limite de tiempo' no verificado. Los datos salen a NVIDIA: no enviar informacion de clientes.
- Reels: G115 · 24442 likes

### LMArena (llamado 'Elemarina' en el guion)  ·  valor 2  ·  saas
Sitio gratuito que da la respuesta de varios modelos a un mismo prompt y permite compararlos.
- Cómo: Escribir prompt y comparar lado a lado.
- Para nosotros: Elegir modelo para cada tarea.
- Fuente: https://lmarena.ai
- Ojo: Nombre deducido por la transcripción; prompts públicos: no subir datos de clientes.
- Reels: G85 · 269 likes
