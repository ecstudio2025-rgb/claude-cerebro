# El Claude de Diego, para el equipo de ECS

Con esto tienes en tu ordenador el mismo Claude Code que usa Diego en su terminal. Trae sus más de 400 skills, los agentes, la base de criterio de mercado, las reglas para escribir sin que se note la IA, su voz de marca y la memoria de lo que se ha hecho con cada cliente y cada sistema.

Es lo que Diego enseñó en la reunión del 25 de septiembre. Vale igual para Mac que para Windows y se instala con una sola línea.

---

## Lo que necesitas

- **La cuenta de Claude del equipo.** Es compartida, así que no hace falta que te hagas una. Diego te pasa el acceso.
- **La clave del equipo.** Sirve para descargar la memoria de Diego. Te la da él por privado. Sin ella se instala todo menos la memoria y las skills que llevan casos de clientes.
- **Google Chrome.** Claude maneja el navegador a través de una extensión que solo existe para Chrome. Firefox no vale.
- 10 minutos.

## 1. Instalar

**Mac.** Abre la app **Terminal** (Cmd + espacio, escribe `terminal`, Enter) y pega esto:

```bash
curl -fsSL https://raw.githubusercontent.com/ecstudio2025-rgb/claude-cerebro/main/instalar.sh | bash
```

**Windows.** Abre **PowerShell** (tecla Windows, escribe `powershell`, Enter) y pega esto:

```powershell
irm https://raw.githubusercontent.com/ecstudio2025-rgb/claude-cerebro/main/instalar.ps1 | iex
```

Cuando te pida la **clave del equipo**, pégala y pulsa Enter. Mientras escribes no se ve nada, es normal.

## 2. Primer arranque

1. Cierra la terminal y abre una nueva.
2. Escribe `cd ~/Claude` y Enter. Luego `claude` y Enter.
3. Se abre el navegador para iniciar sesión. Entra con la **cuenta del equipo**.
4. Te pregunta por los plugins: di que sí a todo.
5. **Reinicia el ordenador.** Sin reiniciar no ve las conexiones.

## 3. Conectar Chrome

1. Instala la extensión **Claude in Chrome** desde la Chrome Web Store.
2. Inicia sesión en la extensión con la misma cuenta del equipo.
3. Dentro de Claude, en la terminal, escribe `/mcp`. Verás todo lo que tiene conectado: Notion, Gmail, Miro, Canva, Calendly, Chrome…

Con Chrome conectado, Claude puede hacer cosas en webs que no tienen conexión directa, como montar una automatización en GHL o configurar ManyChat para un cliente. Si algo no puede hacerlo, te lo dice, lo haces tú a mano, le contestas «ya está» y sigue.

## 4. Comprobar que tiene el cerebro

Pregúntale algo que solo sabría Diego, por ejemplo: *«¿qué contrato firmó el último cliente de Sprint 360?»*. Si te contesta con detalle, está bien instalado. Si no sabe nada, instalaste sin la clave: vuelve al paso 1.

---

## La terminal en 5 comandos

Si nunca la has usado, con esto te apañas:

| Escribes | Qué hace |
|---|---|
| `ls` | Enseña las carpetas y archivos de donde estás |
| `cd Claude` | Entra en la carpeta Claude |
| `cd ..` | Vuelve a la carpeta de arriba |
| `claude` | Arranca Claude en la carpeta donde estás |
| `/exit` (dentro de Claude) | Sale de Claude y vuelve a la terminal |

Trabaja siempre dentro de `~/Claude`. Si llevas varios clientes, crea una carpeta por cliente y abre una pestaña de terminal para cada uno (Cmd + T en Mac, Ctrl + Shift + T en Windows Terminal). Cada pestaña va a lo suyo y trabajan a la vez.

## Cómo pedirle las cosas

Cuanto más concreto, mejor sale. «Hazme una campaña» da un resultado mediocre. «Campaña de captación en Meta para una clínica dental de Madrid, 20 €/día, objetivo formularios, público mujeres de 35 a 55» da uno bueno. Dile el sector, el presupuesto, el objetivo y de dónde tiene que sacar la información.

Las skills se ven escribiendo `/` dentro de Claude. Algunas que se usan mucho:

- `/copywriting`, `/social-content`: textos, captions y guiones con la voz de Diego.
- `/carruseles-con-caricatura-diego`, `/carrusel-gemini`: carruseles.
- `/clips-cortos-de-videos-largos`, `/edicion-de-videos-ia`: cortar vídeos, quitar silencios y subtitular.
- `/ads-meta`, `/google-ads-360`, `/diagnostico-360`: publicidad.
- `/consejo`: para decidir si una idea tiene sentido.

**Editores:** para cortar, quitar silencios y subtítulos dinámicos funciona bien. Las animaciones todavía están verdes. Si ves que algo se puede mejorar, díselo a Diego y se mejora la skill entre todos.

## Lo que cuesta dinero

- **Imágenes.** No uses `/banana` salvo para una imagen concreta que haga falta de verdad: cada una cuesta unos 4 € y ya se han ido 700 € sin darnos cuenta. Pídele que busque en bancos de imágenes gratis o que genere con Gemini a través de Chrome. El cerebro ya trae esta regla, pero tenlo en la cabeza.
- **Modelo.** Opus 5.5 siempre. Si `/model` dice otro, cámbialo.
- **La cuenta es de todos.** No dejes agentes trabajando en bucle sin motivo. Si se agota, se para para el equipo entero.

---

## Qué trae y qué no

| Trae | No trae, nunca |
|---|---|
| Skills, agentes y comandos de Diego | Contraseñas y tokens (en la memoria están tachados) |
| Criterio de mercado con grado de evidencia | Acceso SSH a los servidores |
| Redacción sin huella de IA y voz de marca | Información financiera de la empresa |
| Banco de 10.000 ganchos | La sesión de Gmail o Meta de Diego |
| Memoria de clientes y sistemas (con la clave) | |
| Configuración Ruflo (swarm) y los mismos plugins | |

Si una tarea necesita algo de la columna derecha, Claude te avisará. Pídeselo a Diego. No intentes conseguirlo por otro lado.

La memoria de Diego es de solo lectura. Lo que Claude aprenda trabajando contigo se guarda en tu propia memoria, aparte.

## Actualizar

Diego añade skills y memoria casi a diario. Para traerte lo último, vuelve a lanzar **la misma línea del paso 1**. Tus cosas no se borran: si algo choca de nombre, lo guarda como `.bak-FECHA`.

Hazlo una vez por semana o cuando Diego avise en el grupo.

## Si algo falla

| Qué pasa | Qué hacer |
|---|---|
| `claude: command not found` | Cierra la terminal y abre otra. Si sigue, repite el paso 1. |
| «clave incorrecta o sin conexión» | Confirma la clave con Diego. El resto se instala igual. |
| No sabe nada de los clientes | Instalaste sin clave. Repite el paso 1 y pégala. |
| `/mcp` sale vacío o no ve Chrome | Reinicia el ordenador y comprueba que la extensión tiene la sesión iniciada. |
| Windows: «la ejecución de scripts está deshabilitada» | En PowerShell: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, acepta y repite. |
| «Sin Node.js: Ruflo queda para luego» | Opcional. Instala Node LTS desde nodejs.org y repite el paso 1. Claude funciona igual sin él. |
| Se queja de un plugin | Dentro de Claude escribe `/plugin` e instala el que falte. |

Para cualquier otra cosa, escribe a Diego. Mejor por texto que por audio.

## Confidencialidad

La memoria y las skills privadas llevan datos reales de clientes: nombres, contratos, cifras de campañas. Son para trabajar en ECS. No se copian a otro sitio, no salen del equipo y la clave no se reenvía a nadie. Si alguien sale del equipo, Diego cambia la clave.
