---
name: spec-kit
description: Desarrollo guiado por especificación con GitHub Spec Kit (comando specify): antes de programar un SaaS, ERP o demo a medida se escribe la especificación, el plan técnico y la lista de tareas, y Claude Code las ejecuta por fases. Úsala al arrancar un proyecto nuevo de Custom Soft Lab o una funcionalidad grande, cuando el cliente ha pasado requisitos y hay riesgo de que la IA improvise.
---

# Spec Kit (github/spec-kit, MIT)

Instalado el 13-nov-2026 con `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`. Si falta `specify` en este equipo, repite ese comando.

## Flujo (comprobado el 13-nov-2026 con la versión instalada)

1. `specify init <proyecto> --integration claude --non-interactive` (o `specify init --here --integration claude --non-interactive` dentro de un repo existente). Crea `.specify/` y 9 skills `speckit-*` en `.claude/skills/` del proyecto.
2. Dentro de Claude Code, en el proyecto, por orden:
   - `/speckit-constitution`: reglas del proyecto (stack, estilo, tests, lo que nunca se hace).
   - `/speckit-specify`: qué hay que construir y por qué, en lenguaje de negocio. Aquí van los requisitos del cliente (briefing, reunión transcrita).
   - `/speckit-clarify`: preguntas para cerrar huecos de la spec (opcional, recomendable con clientes).
   - `/speckit-plan`: cómo, con el stack elegido.
   - `/speckit-tasks`: lista de tareas pequeñas y verificables.
   - `/speckit-analyze` y `/speckit-checklist`: coherencia y requisitos completos (opcionales).
   - `/speckit-implement`: ejecutar las tareas.
3. La especificación se le puede enseñar al cliente antes de programar: es el documento de alcance que evita el «yo pensaba que incluía…».

Encaja con el contrato de Custom Soft Lab: la spec firmada es el alcance; lo que no está en la spec es ampliación.
