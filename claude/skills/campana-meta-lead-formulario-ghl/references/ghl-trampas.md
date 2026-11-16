# Trampas de GHL comprobadas (14-nov-2026, subcuenta de Lucía)

Navegador: Chrome real de Diego por el Chrome MCP. Usa la pestaña visible; en pestañas ocultas las capturas dan timeout (CDP «renderer frozen»).

## Iframes y lectura de páginas

- **El page builder** carga en un iframe de `page-builder.leadconnectorhq.com` y **los ajustes de correo** en `ghl-isv-app-prod.leadconnectorhq.com`. Son cross-origin: `javascript_tool` y `get_page_text` no ven su contenido. Se trabaja con capturas y clics.
- **Workflows y formularios** sí funcionan con clics; los desplegables de los paneles de acción no aparecen en `find`. Haz captura y clic por coordenadas.
- Una encuesta «How has your experience been…» puede tapar la página de ajustes: botón «Skip for Now».

## Pegar código en el editor (landing y pie de página)

1. `pbcopy < fichero.html` en Bash.
2. Clic dentro del editor CodeMirror → `cmd+a` → `cmd+v`.
3. Haz zoom al final del código para comprobar que termina donde debe.
4. **No uses cmd+F**: no abre la búsqueda, escribe el texto dentro del código. Si pasa, bórralo con BackSpace (cuenta caracteres + salto de línea) y vuelve a comprobar.
5. Bloque de código: botón «Guardar» del diálogo → **Guardar página** (icono de disco) → **Publicar**. Si publicas sin guardar la página, sale «publicado» y la web no cambia. Compruébalo siempre con `scripts/comprobar_landing.sh`.

## Página de gracias

- El contenido está en **Código de seguimiento → Seguimiento de pie de página** (icono `</>` de la barra), no en un bloque. La sección visible del editor sale vacía y es normal.
- Renombrar la ruta del paso (Publicación → URL del paso) deja la ruta vieja en **404**. Revisa que el formulario o el calendario no redirijan a la vieja.

## Formularios

- La casilla de privacidad puede no ser obligatoria por defecto: ajustes de la casilla → «Obligatorio».
- El texto del botón se edita en línea: triple clic, cmd+A, escribir.
- «ID de píxel de Facebook» del formulario vacío cuando el Lead va por servidor.
- Al guardar sale el modal «Su formulario está listo»: es informativo, ciérralo.

## Workflows

- **Lista de acciones recientes:** cambia de orden según lo último usado. Un clic «a ciegas» en la misma posición abrió «Correo» en vez de «Esperar». Busca siempre la acción escribiendo su nombre («Esperar», «Enviar correo», «flujo de trabajo») y haz clic en el resultado.
- Si se abre una acción equivocada: Cancelar → «Cambios no guardados» → Confirmar.
- **Notificación interna por email:** «Para Correo Electrónico Personalizado» no acepta dos direcciones separadas por coma («Please check the fields for valid inputs»). El segundo va en **Cc**. Si rellenas «Desde el nombre», exige «Desde el correo electrónico»; si no lo tienes, déjalo vacío.
- Los paneles de ajustes tapan el lienzo; para seguir añadiendo pasos, haz scroll en el lienzo (no en el panel) y busca el «+» bajo el último nodo.
- Cada acción se guarda con «Guardar acción» y después el flujo con «Guardar» arriba.
- **Merge tags tecleados** (`{{contact.first_name}}`) a veces quedan como texto plano en vez de etiqueta. GHL los sustituye igual, pero compruébalo en el primer correo real.
- Para reescribir un correo: clic en el cuerpo → cmd+A → escribir el texto entero. Más fiable que editar una frase.
- **«Probar flujo de trabajo» se salta la acción de la API de conversiones** («sin datos de atribución»). La CAPI solo se prueba con un envío real del formulario.
- **Durante las pruebas reales,** pon el flujo de nutrición en **Borrador** (interruptor Borrador/Publicar) para que no llegue el aviso «Nueva solicitud» al cliente. Al acabar, Publicar. Comprueba el interruptor con zoom.
- Flujo «Elimine del flujo de trabajo» → «Otro flujo de trabajo»: GHL preselecciona el propio flujo. Quita esa etiqueta y elige el correcto.
- Etapas de pipeline: el filtro de «Fase de la secuencia» es de selección única; con la primera etapa de pago basta.

## API de conversiones de Meta en GHL

- El token **no se hereda** al crear una acción nueva: el campo sale vacío. Reutiliza el flujo que ya lo tiene cambiando disparador y evento.
- Al pegar el token puede resetear conjunto de datos, evento (vuelve a Lead) y moneda (USD). Revisa todos los campos después.
- GHL no deja fijar `event_id`: un evento por servidor no se puede deduplicar con el navegador. Elige una sola vía.

## Contactos

- Borrado en lote: seleccionar → Borrar → escribir BORRAR → confirmar. Se puede restaurar durante 2 meses. Se ejecuta en segundo plano.
- Borra solo contactos de prueba que hayas creado tú (nombres «Prueba Claude…», correos example.com).

## Correo saliente

- Sin dominio dedicado, GHL envía desde su dominio compartido (`amail.msgsndrls.com`, 1.000/día). El remitente puede ser el Gmail del cliente, con riesgo de spam. Prueba con un correo real antes de lanzar.

## Usuarios y permisos

- El segundo responsable del cliente (Biel) no tenía usuario en GHL: solo recibe avisos por correo en Cc. Crear usuarios es un paso de Diego.
- App móvil para el cliente: «LeadConnector», con su correo de usuario de GHL.
