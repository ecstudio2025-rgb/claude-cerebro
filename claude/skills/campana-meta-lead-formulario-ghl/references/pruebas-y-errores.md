# Pruebas, búsqueda de errores y checklist de configuración

Nada se da por bueno sin el resultado esperado delante. Lo que no se pueda probar se dice.

## 1. Píxel por página (fuera del navegador de Diego)

```bash
cd ~/.claude/skills/campana-meta-schedule/scripts
for u in "https://DOMINIO/?nc=1" "https://DOMINIO/solicitud-recibida?nc=1" "https://DOMINIO/<ruta-privacidad>"; do
  python3 verificar_pixel.py "$u" --pixel <PIXEL_ID> --espera PageView --prohibe Lead,Schedule,SubmitApplication,CompleteRegistration --segundos 8 | tail -6
done
```
Esperado en las tres: una llamada, `PageView pixel=<PIXEL_ID>`, «OK». Headless no ensucia: Meta descarta esos eventos.

## 2. Contenido publicado

```bash
~/.claude/skills/campana-meta-lead-formulario-ghl/scripts/comprobar_landing.sh https://DOMINIO/ "Quiero información" "Bizum" "widget/form/<FORM_ID>" "widget/booking" "Quiero que me llam"
```
Lo nuevo > 0; lo retirado (calendario, copy viejo) = 0. Repite para `/solicitud-recibida` y para la ruta vieja (debe dar 404 con `curl -o /dev/null -w "%{http_code}"`).

## 3. Recorrido real (Chrome de Diego)

Preparación:
1. Flujo de nutrición → **Borrador** (no avisar al cliente).
2. Flujo CAPI → acción Meta → Código de prueba = `TESTxxxxx` → Guardar acción → Guardar flujo.
3. Pestaña A: Events Manager → Probar eventos → canal «Sitio web». No recargar.

Recorrido en la pestaña B:
1. `https://DOMINIO/?fbclid=PRUEBAclaude<N>&utm_source=prueba`.
2. Enlace de WhatsApp de la landing sin salir de la página:
   ```js
   const a=document.getElementById('lg-wa'); a.addEventListener('click',e=>e.preventDefault(),{once:true}); a.click();
   ```
3. Formulario: nombre «Prueba Claude <N>», teléfono 60000000N, correo `prueba-leadN-<producto>@example.com`, experiencia, casilla. Enviar.
4. En `/solicitud-recibida`, lo mismo con el botón `cf-wa`.

Esperado en Test Events, en este orden y **una vez cada uno**:

| Evento | Recibido de |
|---|---|
| PageView | Navegador |
| Contactar | Navegador |
| Cliente potencial | **Servidor** |
| PageView | Navegador |
| Contactar | Navegador |

Error si aparece: Lead o SubmitApplication desde Navegador (formulario con píxel o `fbq` en la página), dos Leads, o ningún Lead (flujo CAPI sin publicar, filtro de formulario mal, código de prueba no guardado).

Claves de datos de usuario del Lead (clic en la fila): país, correo, identificador de clic (fbc), nombre, IP, teléfono, agente de usuario. **Sin fbp** porque el formulario va en un iframe: aceptable.

Registro en GHL: flujo CAPI → «Registros de ejecución» → acción «Meta Conversion API» en «Ejecutado» → Ver detalles → «Success».

## 4. Limpieza (obligatoria)

1. Flujo CAPI: borrar el código de prueba → Guardar acción → Guardar.
2. Flujo de nutrición: **Publicar** (zoom al interruptor y mensaje «publicado y activo»).
3. Contactos: borrar los de prueba (BORRAR, recuperables 2 meses).
4. Anotar en memoria la hora de la prueba y el resultado.

## 5. Checklist de configuración de Meta

| Punto | Correcto si |
|---|---|
| Objetivo | Clientes potenciales |
| Presupuesto | El de la fase 0, en la campaña (CBO). «Gastaremos un promedio de X € al día» |
| Lugar de la conversión | Sitio web |
| Conjunto de datos | El píxel del cliente |
| Evento | Cliente potencial |
| Objetivo de rendimiento | Maximizar el número de clientes potenciales |
| Atribución | Estándar (7 días clic) |
| Ubicación | La zona real del cliente (radio que cubra la isla/región) |
| Sugerencia de audiencia | Coherente con el nombre del conjunto (edad, género) |
| Fechas | Inicio y fin marcados; fin con margen antes del servicio |
| Ubicaciones | Advantage+; Audience Network revisada a las 48 h |
| Anunciante UE | Rellenado, check verde |
| Anuncios | Todos «Activa»; texto y CTA coherentes con el formulario; casilla IA desmarcada si no es IA |
| URL de destino | `https://DOMINIO/` (leer solo origin+pathname) |
| Estado | Sin «Cambios sin publicar» |

## 6. Checklist de GHL

| Punto | Correcto si |
|---|---|
| Formulario | Consentimiento obligatorio, redirige a gracias, píxel vacío, botón con copy y color de marca |
| Flujo CAPI | Disparador formulario, evento Lead, sin valor, sin código de prueba, Publicado |
| Flujo nutrición | Oportunidad → aviso (destinatario + Cc) → correos 1-4 → Detener en respuesta, Publicado |
| Flujo sacar | Fase Reserva pagada → quitar de nutrición y aviso final, Publicado |
| Flujo aviso final | Espera hasta fecha → correo 5, Publicado |
| Correo saliente | Al menos un envío real recibido en una bandeja de verdad (si no, decirlo) |
| Contactos | Sin contactos de prueba |

## 7. Errores típicos y causa

| Síntoma | Causa | Arreglo |
|---|---|---|
| La landing no cambia tras «publicado» | No se guardó la página antes de publicar | Guardar página, publicar, `comprobar_landing.sh` |
| Texto raro dentro del código | cmd+F escribió en el editor | Borrar y comprobar el final del código |
| No llega Lead a Test Events | Página de Test Events abierta después, o canal sin elegir | Abrirla antes y repetir el envío |
| Aviso interno no se guarda | Dos correos con coma, o nombre de remitente sin correo | Segundo en Cc; vaciar «Desde el nombre» |
| Se abre otra acción en el flujo | Lista de recientes reordenada | Buscar por nombre |
| Casilla «creado con IA» marcada | Triple clic sobre su etiqueta | Desmarcar y comprobar con JS |
| Audiencia a toda la región | Sugerencia sin poner | Mostrar sugerencias → edad/género |
