# Instalado el 13-nov-2026

Origen de cada skill y herramienta añadida a raíz de los reels. Para actualizar una: volver a clonar el repo, revisar el diff (sobre todo scripts y hooks) y copiar la carpeta de la skill encima.

| Repo | Commit | Licencia | Skills |
|---|---|---|---|
| emilkowalski/skills | f7ce8c0 | MIT | animate-expo, animate, animation-performance, animation-vocabulary, apple-design, ask-sonner, break-ui, choreograph, emil-design-eng, find-animation-opportunities, gestures, improve-animations, learn-taste, mobile-native, pick-ui-library, prototype, remove-animations, review-animations, write-swift |
| obra/superpowers | 22f0b46 | MIT | brainstorming, diagnosing-superpowers, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills |
| vercel-labs/agent-skills | 1a2c79d | sin-licencia | react-best-practices, web-design-guidelines, composition-patterns, react-view-transitions, react-native-skills, writing-guidelines |
| nidhinjs/prompt-master | 49b3a72 | MIT | prompt-master |
| blader/humanizer | b48c832 | MIT | humanizer |
| VoltAgent/awesome-design-md | fcc7028 | MIT | design-md-marcas |
| microsoft/markitdown | uv-tool | MIT | markitdown |
| github/spec-kit | uv-tool | MIT | spec-kit |

## Cambios locales sobre el original

- `brainstorming` (superpowers): descripción reescrita para que solo salte cuando se pide; la original obligaba a usarla antes de cualquier trabajo creativo.
- Quitadas `using-superpowers` y `diagnosing-superpowers`: la primera forzaba usar skills en cada conversación y la segunda solo sirve con el plugin.
- De vercel-labs/agent-skills no se copiaron `deploy-to-vercel`, `vercel-cli-with-tokens` ni `vercel-optimize` (no usamos Vercel y manejan tokens). Ese repo no declara licencia: sus skills van solo a la capa privada del cerebro, no al GitHub público.
- `design-md-marcas`: skill nuestra hecha con los 84 DESIGN.md de VoltAgent/awesome-design-md.

## Descartado

- Plugin `obra/superpowers` completo (hook de SessionStart en todas las sesiones).
- `garrytan/gstack` (120 MB, ~2.900 scripts, reconfigura Claude).
- `VoltAgent/awesome-claude-code-subagents` (100+ agentes más sobre los 150 que ya hay; inflan el contexto).
- `thedotmack/claude-mem` (duplica la memoria y añade hooks).
- `czlonkowski/n8n-mcp` (no usamos n8n; la automatización va por GHL y el OS). Si algún cliente usa n8n, es el primero que instalar.
- `microsoft/playwright-mcp` (lo cubren Claude in Chrome y webapp-testing).
- `firecrawl` (necesita clave de pago; ya está seo-firecrawl), `ScrapeGraphAI` y Agent-Reach (scraping de redes contra sus términos).
- `x1xhlol/system-prompts-and-models-of-ai-tools` (prompts filtrados, GPL, zona gris).
- `harry0703/MoneyPrinterTurbo` (vídeos de stock con voz sintética: choca con la regla de motion 3D y corte limpio, nunca UGC genérico).
