# El Claude de Diego, para el equipo de ECS

Con esto tienes en tu ordenador el mismo Claude Code que usa Diego en su terminal: sus 400 y pico skills, los agentes, la base de criterio de mercado (`kb-mercado`), las reglas de redacción sin huella de IA, su voz de marca y la memoria de todo lo que ha hecho con cada cliente y cada sistema.

Tarda unos 5 minutos. Se instala con una línea y se actualiza con la misma línea.

---

## Antes de empezar

1. **Una cuenta de Claude con Claude Code.** Plan Pro, Max o un puesto del plan Team. Sin eso no arranca. Si no la tienes, pídela a Diego.
2. **La clave del equipo.** Te la da Diego por privado. Sin ella se instala todo menos la memoria y las skills con casos de clientes.
3. **Git.** En Mac, si no lo tienes, el instalador te lo dirá (`xcode-select --install`). En Windows se instala solo.

## Instalar

### Mac o Linux

Abre la app **Terminal** y pega:

```bash
curl -fsSL https://raw.githubusercontent.com/ecstudio2025-rgb/claude-cerebro/main/instalar.sh | bash
```

### Windows

Abre **PowerShell** (botón de inicio, escribe `powershell`, Enter) y pega:

```powershell
irm https://raw.githubusercontent.com/ecstudio2025-rgb/claude-cerebro/main/instalar.ps1 | iex
```

En los dos casos te pedirá la **clave del equipo**. Pégala y pulsa Enter (no se ve mientras escribes, es normal). Si la dejas en blanco, instala la parte pública y sigue.

## Primer arranque

Cierra la terminal, abre una nueva y escribe:

```bash
cd ~/Claude
claude
```

La primera vez te pide iniciar sesión en el navegador con tu cuenta de Claude y aceptar los plugins. Di que sí a todo.

Para comprobar que tiene el cerebro, pregúntale algo que solo sabría Diego, por ejemplo: *«¿qué contrato tiene el último cliente de Sprint 360?»*. Si responde con detalle, está bien instalado.

## Actualizar

Diego va añadiendo skills y memoria cada día. Para traerte lo último, vuelve a lanzar **la misma línea de instalación**. No borra nada tuyo: lo que ya tuvieras con el mismo nombre lo renombra a `.bak-FECHA`.

Recomendado: una vez por semana, o cuando Diego avise en el grupo.

---

## Qué trae y qué no

| Trae | No trae, nunca |
|---|---|
| Skills, agentes y comandos de Diego | Contraseñas y tokens (están tachados en la memoria) |
| `kb-mercado`: reglas de criterio con grado de evidencia | Acceso SSH a los VPS |
| Redacción sin huella de IA y voz de marca | Los MCP con token (facturas, CRM, WhatsApp, Instagram) |
| Banco de 10.000 ganchos | Su sesión de Gmail, Notion o Meta |
| Memoria de clientes y sistemas (con la clave) | |
| Los mismos plugins y ajustes (Opus, modo auto) | |

Si una tarea necesita algo de la columna derecha, Claude te dirá que falta. **Pídeselo a Diego**, no intentes sacarlo por tu cuenta.

## Cómo trabajar con él

- **Trabaja siempre desde `~/Claude`.** Crea una carpeta por cliente o proyecto ahí dentro.
- **La memoria de Diego es de solo lectura.** Claude la consulta, pero lo que aprenda contigo lo guarda en tu propia memoria. Al actualizar, la de Diego se sustituye entera.
- **Pídele las cosas como se las pedirías a Diego.** «Hazme un guion de reel para X con su voz», «revisa esta propuesta con el criterio de mercado», «¿qué pasó con la campaña de tal cliente en septiembre?».
- **Las skills se invocan con `/`.** Escribe `/` en Claude y verás la lista. Las más usadas: `/copywriting`, `/social-content`, `/ads-meta`, `/google-ads-360`, `/diagnostico-360`, `/consejo`.
- **Lo que va a un cliente, revísalo tú antes.** Claude redacta con la voz de Diego, pero la responsabilidad del envío es tuya.

## Si algo falla

| Síntoma | Qué hacer |
|---|---|
| `claude: command not found` | Cierra la terminal y abre otra. Si sigue, vuelve a lanzar la línea de instalación. |
| «clave incorrecta o sin conexión» | Revisa la clave con Diego. El resto se instala igual. |
| No sabe nada de los clientes | Instalaste sin clave. Vuelve a lanzar la línea y pégala. |
| Windows: «la ejecución de scripts está deshabilitada» | En PowerShell: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, acepta y repite. |
| Se queja de un plugin | Dentro de Claude: `/plugin` y dale a instalar el que falte. |

## Confidencialidad

La memoria y las skills privadas llevan datos de clientes reales: nombres, cifras, contratos. Son para trabajar en ECS. No se copian a otro sitio, no se comparten fuera del equipo y la clave no se reenvía. Si sales del equipo, Diego cambia la clave y deja de actualizarse.
