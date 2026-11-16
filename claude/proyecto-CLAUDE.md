# Claude Code Configuration - RuFlo V3

## Alcance de este fichero (manda sobre todo lo de abajo)
- Este es el ordenador de trabajo de una agencia de marketing y un estudio de software: la mayoría de encargos son contenido, campañas, propuestas, clientes y operaciones, no programación.
- Las reglas de abajo (DDD, TDD London, event sourcing, `/src` `/tests` `/docs`, límite de 500 líneas) se aplican **solo cuando se programa un proyecto de software**. Para lo demás manda `~/.claude/CLAUDE.md`.
- Enjambres y agentes en paralelo: solo cuando hay trabajo independiente que lo justifique, nunca por defecto. Una tarea que se resuelve con unas pocas llamadas se hace directamente.
- «No crear .md» no aplica a entregables que se piden (guiones, propuestas, informes, notas de memoria, aportes al cerebro), que van en `~/Claude/deliverables/` o `~/Claude/docs/`.
- Comandos `npx @claude-flow/cli` (swarm, hooks, memory): opcionales. Si fallan o no aportan, se sigue sin ellos. Referencia completa de Ruflo (CLI, agentes, routing, swarm) en `docs/CLAUDE.ruflo-completo.bak.md`.

## Reglas
- Hacer lo que se pide; ni más ni menos.
- No crear ficheros salvo que hagan falta; preferir editar uno existente. Leer antes de editar.
- Nada de ficheros de trabajo en la raíz: `/src` código, `/tests` tests, `/docs` documentación, `/config` configuración, `/scripts` utilidades, `/examples` ejemplos.
- Nunca commitear secretos, credenciales ni `.env`; nunca claves en el código.
- Validar entradas en los límites del sistema y sanear rutas (directory traversal).
- Operaciones independientes en paralelo en un solo mensaje. Tras lanzar agentes en segundo plano, esperar el resultado sin sondear.

## Al programar
- Domain-Driven Design con bounded contexts; ficheros de menos de 500 líneas; interfaces tipadas en las APIs públicas.
- TDD London School (mock-first) para código nuevo; event sourcing para cambios de estado.
- `npm run build`, `npm test`, `npm run lint`: tests siempre tras cambiar código y build verde antes de commitear.
- Tras cambios de seguridad: `npx @claude-flow/cli@latest security scan`.
- Enjambre de código, si de verdad hace falta: topología jerárquica, 6-8 agentes, estrategia especializada.
