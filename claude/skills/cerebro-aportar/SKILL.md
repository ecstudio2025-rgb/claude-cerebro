---
name: cerebro-aportar
description: Sube al cerebro común del equipo de ECS una nota con algo aprendido en esta sesión (un procedimiento que funcionó, un fallo y su arreglo, un criterio de cliente o de venta, una herramienta o repo que vale la pena). Úsala cuando el usuario diga «apórtalo al cerebro», «guárdalo para el equipo», «que lo sepa todo el mundo», o cuando cierres una tarea que otro miembro del equipo tendrá que repetir. Por la noche se junta con la memoria de Diego y al día siguiente lo tiene el Claude de todo el equipo.
---

# Aportar al cerebro del equipo

El cerebro tiene dos capas: la pública (GitHub `ecstudio2025-rgb/claude-cerebro`, skills y guías) y la privada (memoria de Diego, en el VPS con la clave del equipo). Los aportes van a la privada, a un buzón en el VPS. Su dirección la deja el instalador en `~/.config/claude-cerebro-equipo/buzon`.

Cada noche el Mac de Diego recoge el buzón, revisa que no haya claves, lo mete en el paquete privado y a las 09:00 cada equipo se actualiza solo. Lo que subas hoy lo ve el Claude de todos mañana.

## Qué merece una nota

Sí:
- Un procedimiento que costó dar con él y que se va a repetir (configurar X en GHL, montar un embudo, exportar Y).
- Un fallo con su causa y su arreglo.
- Una regla de un cliente o de ventas que no está escrita en otro sitio.
- Una herramienta, skill o repo probado, con para qué sirve y cómo se instala.

No:
- Contraseñas, tokens, claves API, códigos. Nunca. Si hacen falta, escribe «pedir a Diego».
- Datos de salud, vida personal o familia de nadie.
- Teléfonos, correos o DNI de leads y clientes.
- Lo que ya está en la memoria de Diego o en una skill: busca antes en `~/.claude/cerebro-privado/` y en `~/.claude/skills/`.

## Formato

Un fichero Markdown corto (máximo 60 líneas):

```markdown
---
titulo: <frase corta>
autor: <nombre de quien usa este Claude>
fecha: <AAAA-MM-DD>
tipo: procedimiento | fallo | cliente | venta | herramienta | criterio
cliente: <nombre o "general">
---

<Qué pasó o qué se hace, en pasos si es un procedimiento.>

**Por qué importa:** <una línea>
**Cómo aplicarlo:** <una línea: cuándo debe usarlo el Claude del resto>
```

## Cómo subirlo

1. Escribe la nota en un fichero temporal.
2. Comprueba que no lleva claves: `grep -n -i -E "(sk-|ghp_|xox|AIza|eyJ|password|contraseña|token)\S*" nota.md` no debe devolver nada con valores.
3. Súbela con un nombre único (fecha, autor, tema en minúsculas y guiones, sin tildes):

```bash
CLAVE="$(cat ~/.config/claude-cerebro-equipo/clave)"
NOMBRE="$(date +%Y%m%d-%H%M)-<autor>-<tema>.md"
BUZON="$(cat ~/.config/claude-cerebro-equipo/buzon)"
curl -fsS -u "equipo:$CLAVE" -T nota.md "$BUZON$NOMBRE" && echo subido
```

Si no existen `~/.config/claude-cerebro-equipo/clave` y `buzon` es que el equipo se instaló sin clave: dile al usuario que repita la instalación con la clave del equipo (`curl -fsSL https://raw.githubusercontent.com/ecstudio2025-rgb/claude-cerebro/main/instalar.sh | bash`).

4. Di en una línea qué has subido y con qué nombre.

En el Mac de Diego (donde existe `~/.config/claude-cerebro/`) no hace falta el buzón: guarda la nota directamente como memoria normal; ya entra en la capa privada cada noche.

## Ver lo que ha aportado el resto

`~/.claude/cerebro-privado/aportes/INDICE.md`, ordenado del más nuevo al más viejo.
