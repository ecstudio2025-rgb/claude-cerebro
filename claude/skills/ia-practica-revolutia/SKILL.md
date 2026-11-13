---
name: ia-practica-revolutia
description: Lo útil de 217 reels de @revolutia.ai (IA práctica en español, ene-sep 2026) destilado para ECSSTUDIO y Custom Soft Lab. Catálogo de 200 herramientas, repos, skills, MCPs y técnicas por área (ventas, marketing, contenido, diseño, web, desarrollo, apps, automatización), qué tenemos ya instalado y cómo se usa, más el análisis de su fórmula de contenido (ganchos, CTA de palabra clave, republicar ganadores). Úsala cuando alguien pregunte «¿hay alguna herramienta o skill para X?», «¿qué repo de GitHub sirve para…?», antes de buscar o instalar una herramienta de IA nueva, o al preparar reels y carruseles sobre IA y herramientas.
---

# IA práctica: lo que sirve de @revolutia.ai

Fuente: 217 reels de la Comunidad Revolutia (@revolutia.ai), del 14-ene al 14-sep-2026. Son 172 guiones distintos, porque los que funcionan los republica hasta 7 veces. Se transcribieron con Whisper el 13-nov-2026 y se analizaron uno a uno. Vídeos, transcripciones y datos en bruto: `~/Claude/docs/revolutia/` (solo en el Mac de Diego).

Todo lo que dicen los reels es grado C (lo afirma un creador que vende comunidad) hasta que lo probemos. Las estrellas de GitHub sí están comprobadas el 13-nov-2026.

## Ficheros

- `references/catalogo-herramientas.md`: las 200 entradas por área, con qué hacen, cómo se usan, para qué nos sirven, riesgos y si ya lo tenemos. Búscalo con grep, no lo leas entero (117 KB).
- `references/contenido-revolutia.md`: cómo construye los reels, qué le da likes y qué copiar para el contenido de ECS.
- `references/instalado-13nov.md`: qué se instaló, de dónde y qué se descartó y por qué.

## Instalado el 13-nov a raíz de esto

| Para | Skill o comando |
|---|---|
| Leer PDF y Office gastando menos tokens | `markitdown` (comando y skill) |
| Arrancar un SaaS o ERP con alcance cerrado | `spec-kit` (comando `specify`) |
| Webs y demos que no parezcan hechas con IA | `apple-design`, `emil-design-eng` y 17 más de Emil Kowalski; `web-design-guidelines`; `design-md-marcas` (84 sistemas de diseño de marcas) |
| React, Next, React Native | `react-best-practices`, `composition-patterns`, `react-view-transitions`, `react-native-skills` |
| Método de desarrollo | `systematic-debugging`, `test-driven-development`, `writing-plans`, `executing-plans`, `verification-before-completion` y el resto de Superpowers |
| Prompts para otras IAs (Midjourney, Veo, Cursor…) | `prompt-master` |
| Texto en inglés sin pinta de IA | `humanizer` (en español mandan `anti-patrones-ia-redaccion.md` y `voz-diego-marca.md`) |

Ya lo teníamos antes: Remotion, Graphify, Impeccable, Taste, las skills oficiales de Anthropic, SEO, marketing, consejo, code review, security review, Chrome.

## Prácticas que vale la pena adoptar

Ordenadas por lo que mueven en caja, no por likes.

1. **El retorno en la primera línea de la propuesta.** Calcula horas ahorradas por semana × coste hora × semanas de trabajo, o euros que entran de más, y ponlo arriba del todo. Cuadra con la regla de ×2 de las propuestas Sprint 360 y con el bien de confianza (`kb-mercado/10`). Cuidado: el reel lo calcula mal (10 h × 20 € no son 2.400 € al año, son unos 9.600 € con 48 semanas). Rehaz siempre la cuenta.
2. **Una sola solución replicable por sector.** Una oferta, casos con números, la misma demo adaptada a cada empresa del sector. Es lo que ya hacen las demos de Custom Soft Lab. Sirve de argumento para no abrir más líneas.
3. **Prospección con auditoría y demo hecha.** Busca negocios con buenas reseñas y web floja, audita la web (sin prueba social, CTA mal puesto), monta una landing con sus datos reales y manda el correo con los fallos y la demo. Encaja con el módulo Comercial del OS de Custom Soft Lab. Respeta RGPD: datos de empresa públicos sí, emails personales no.
4. **Spec antes de código** (`spec-kit`). La spec que aprueba el cliente es el alcance del contrato, y lo que no esté ahí es ampliación.
5. **handoff.md en sesiones largas.** Pide un handoff.md con objetivo, estado, ficheros, qué cambió, qué se intentó, qué falló y qué sigue; luego /clear y «lee handoff.md y continúa». Abarata las sesiones de programación largas.
6. **Diseño web en 4 capas.** Referencia (`design-md-marcas` o una captura), skill de diseño (`apple-design`, `impeccable`), dos Google Fonts (títulos y cuerpo), e iterar con capturas de lo que falla (Chrome o `webapp-testing`).
7. **Pasar los documentos a Markdown antes de dárselos a Claude** (`markitdown`). Los briefings, contratos y PDFs de cliente gastan muchos menos tokens.
8. **Red team de la oferta.** Antes de mandar una propuesta o un guion, pide una crítica sin complacencia: dónde se cae, qué objeción no está respondida. Lo cubre la skill `consejo`.

## Lo que se descartó (y por qué)

- **Plugin Superpowers completo:** su hook de arranque se mete en todas las sesiones de todo el equipo. Instaladas sus skills sueltas, que solo se usan cuando hace falta.
- **gstack (Garry Tan):** 120 MB y casi 3.000 scripts que reconfiguran Claude entero.
- **Scraping de LinkedIn, Instagram y Twitter con cookies** (Agent-Reach, ScrapeGraphAI sobre redes): viola los términos y es un riesgo para la cuenta. Apify con actores oficiales y datos de empresa, sí.
- **Repos de system prompts filtrados:** zona gris legal y no aporta.
- **claude-mem y similares:** duplican la memoria que ya tenemos y añaden hooks en cada sesión.

## Antes de instalar algo nuevo que salga en un reel

Mira las estrellas, la licencia, la última actividad, y qué scripts y hooks ejecuta (`hooks/hooks.json`, `scripts/`, `curl … | bash`). Si añade un hook de SessionStart o toca `settings.json`, no lo actives sin que lo vea Diego. Apúntalo en `references/instalado-13nov.md` y súbelo al cerebro con `cerebro-aportar`.
