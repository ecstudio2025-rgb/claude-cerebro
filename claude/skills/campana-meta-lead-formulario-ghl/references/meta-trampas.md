# Trampas de Ads Manager y Events Manager comprobadas (14-nov-2026)

## Edición de anuncios

- **Triple clic sobre una etiqueta marca su casilla.** Un triple clic mal situado cayó en el texto de «El anuncio incluye contenido multimedia creado o editado con IA» y la dejó marcada en V3 (vídeo real de la clienta). Después de editar cualquier anuncio, comprueba:
  ```js
  [...document.querySelectorAll('input[type=checkbox]')].find(c=>/creado o editado con IA/.test(c.closest('label')?.innerText||'')).checked
  ```
  Si sale `true` y no es contenido de IA, clic en la casilla y vuelve a comprobar.
- **Editar una línea del texto principal sin coordenadas** (editor Draft.js):
  ```js
  const ed=[...document.querySelectorAll('[contenteditable=true]')][0]; ed.focus();
  const s=[...ed.querySelectorAll('span[data-text=true]')].find(x=>/TEXTO VIEJO/.test(x.textContent));
  const r=document.createRange(); r.selectNodeContents(s);
  const sel=getSelection(); sel.removeAllRanges(); sel.addRange(r);
  document.dispatchEvent(new Event('selectionchange'));
  ```
  Luego `computer type` con el texto nuevo y relee `ed.innerText`.
- «Texto principal (1 de 5)» indica cuántas variantes caben, no cuántas hay. Revisa si hay más con capturas.
- **CTA:** abre el combobox y haz clic por JS en la opción: `[...document.querySelectorAll('[role=option]')].find(e=>e.innerText.trim()==='Más información').click()`.
- Tras cada cambio espera «Se han guardado todos los cambios».

## Coordenadas

- En este Mac la captura no coincide con los píxeles CSS: viewport 1837×996 frente a captura 1498×812, factor ≈ 0,8155. Si calculas coordenadas con `getBoundingClientRect`, multiplícalas por ese factor (o calcúlalo con `innerWidth` y el ancho de la captura).

## Leer la página

- Ads Manager virtualiza: `get_page_text` y `body.innerText` no traen secciones fuera de pantalla. Recorre los contenedores con scroll y acumula:
  ```js
  const sc=[...document.querySelectorAll('*')].filter(e=>e.scrollHeight>e.clientHeight+200&&getComputedStyle(e).overflowY.match(/auto|scroll/));
  const acc=new Set(); for(const s of sc){for(let y=0;y<=s.scrollHeight;y+=300){s.scrollTop=y;await new Promise(r=>setTimeout(r,250));document.body.innerText.split('\n').forEach(l=>acc.add(l.trim()))}}
  ```
- Leer valores con URL y parámetros devuelve «[BLOCKED: Cookie/query string data]». Devuelve solo `new URL(v).origin + pathname`.
- Las secciones «Presupuesto y programación», «Sugiere una audiencia» y la fecha de fin aparecen al hacer scroll en el formulario del conjunto; usa `scroll_to` sobre una referencia cercana.

## Programación

- La hora de fin tecleada (`2359`) no se guardó como se esperaba. Poner la fecha del día siguiente funciona; Meta propuso las 09:00. Revisa con zoom el valor final.
- La fecha de inicio pasada no es problema: arranca al publicar.

## Audiencia y ubicaciones

- Advantage+ con sugerencias: «Mostrar sugerencias» → Edad (selects mínimo y máximo) y Género (radio). El nombre del conjunto no configura nada: el de Lucía decía «Mujeres 18-55» y no tenía sugerencia puesta.
- La exclusión de ubicaciones ya no está en el conjunto: aviso «Pronto habrá cambios en la configuración de la ubicación». Solo queda en **Controles de cuenta** y afecta a toda la cuenta, incluidas otras campañas del cliente.
- Meta no tiene «Mallorca» como región: radio desde un municipio central (Inca +55 km).

## Publicar

- Campaña activa: cada edición deja «Cambios sin publicar» hasta pulsar **Publicar** abajo a la derecha. Luego la tabla muestra «Publicando N de M».
- Tras publicar por primera vez: «En proceso» = en revisión. Los anuncios pasan a «Activa» al aprobarse (en el caso real, en menos de una hora).
- Al cerrar con Escape puede salir «¿Publicar borradores?»: Cerrar si no tienes el sí de Diego.

## Events Manager / Test Events

- Pestaña «Probar eventos» → elegir canal **«Sitio web»** (el combobox «Selecciona un canal»). Por JS: `[...document.querySelectorAll('[role=option]')].find(e=>e.innerText.trim()==='Sitio web').click()`.
- La lista solo añade eventos que llegan **con la página abierta** y el canal elegido. Ábrela antes de hacer la prueba y no la recargues.
- El código de prueba (ej. `TEST79854`) se mantiene en el tiempo; se pone en la acción de GHL y se quita al acabar.
- Las horas de Test Events salen en la zona horaria del Mac (Canarias, una hora menos que GHL en CET).
- Para ver las claves de datos de usuario: clic en la fila del evento y leer «Claves de datos de usuario».
- Un evento puede tardar 1-2 minutos en aparecer.

## Compras y cuenta

- El clic de compra (suscripción de WhatsApp en GHL) lo bloquea el clasificador aunque Diego haya dicho que sí. Lo hace él.
- Cambios en «Controles de cuenta» son ajustes de cuenta: piden OK explícito.
