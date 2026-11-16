# Playbook: embudo de formulario GHL + Meta (Lead por servidor)

Cada fase acaba en una **puerta**. Si no se cumple, no se pasa a la siguiente.

---

## Fase 0. Aritmética y presupuesto

1. Presupuesto diario = presupuesto total ÷ días que quedan hasta la fecha de fin. Ejemplo real: 500 € entre el 14 y el 26-nov (≈12 días) = 40 €/día ≈ 470 € gastados. Con 25 €/día se habrían quedado 200 € sin usar.
2. Techo de ingresos: plazas × precio (9 × 597 € = 5.373 €). Cuántas ventas cubren la publicidad (aquí, una).
3. Fecha de fin: deja margen para llamar y cobrar antes del servicio (curso el 28 → anuncios hasta el 26 a las 09:00).
4. Comprueba qué día de la semana cae cada fecha antes de escribir «este viernes/sábado». El 14-nov-2026 es sábado; el 28 también.

**Puerta:** presupuesto diario, fecha de fin y techo calculados y dichos a Diego.

## Fase 1. Landing en GHL con formulario

1. La landing es un bloque «HTML/Javascript personalizado» en el page builder. La fuente local va en `campana-…/landing/landing-ghl-pegar.html`. Copia de seguridad antes de tocar: `cp X X.antes-<cambio>-<fecha>.html`.
2. Sustituye el iframe del calendario por el formulario:
   ```html
   <iframe src="https://api.leadconnectorhq.com/widget/form/<FORM_ID>" style="width:100%;height:560px;border:none;border-radius:10px;display:block" id="inline-<FORM_ID>" data-layout="{'id':'INLINE'}" data-trigger-type="alwaysShow" data-trigger-value="" data-activation-type="alwaysActivated" data-activation-value="" data-deactivation-type="neverDeactivate" data-deactivation-value="" data-form-name="<NOMBRE>" data-height="560" data-layout-iframe-id="inline-<FORM_ID>" data-form-id="<FORM_ID>" title="Quiero información"></iframe>
   <script src="https://link.msgsndr.com/js/form_embed.js"></script>
   ```
3. Copy de baja fricción, aplicado en todos los sitios:
   - CTA del hero y botón: «Quiero información» (no «Reservar llamada» ni «Quiero que me llaméis»).
   - Sección del formulario: «Te contactamos nosotros… por llamada o por WhatsApp, como prefieras».
   - Método de pago visible donde salga el precio: «reservas con 100 € por Bizum o transferencia».
   - «Pedir información no te obliga a nada».
4. Edición con Python (`str.replace` con `assert s.count(a)==1`) para que un texto que no existe pare el script en vez de pasar en silencio.
5. Pegar en GHL y publicar siguiendo `references/ghl-trampas.md` (pbcopy, cmd+A, cmd+V, Guardar código, Guardar página, Publicar).
6. Verifica en vivo: `scripts/comprobar_landing.sh https://dominio/ "Quiero información" "Bizum" "widget/form/<FORM_ID>" "widget/booking"`. Lo nuevo > 0, lo viejo = 0.

**Puerta:** la landing publicada muestra el formulario y el copy nuevo, y no contiene el calendario.

## Fase 2. Formulario de GHL

1. Campos mínimos: nombre, WhatsApp, correo, una pregunta de cualificación con desplegable (ej. «Tu experiencia»: Nunca he hecho uñas / Me hago las mías / Trabajo o he trabajado de manicurista) y la casilla de privacidad.
2. Casilla de privacidad: comprueba en sus ajustes que «Obligatorio» está marcado (por defecto puede no estarlo).
3. Botón: texto «Quiero información» y tema oscuro (Ajustes del botón → Seleccionar tema → Rellenado negro) para que no salga el azul de GHL.
4. Configuración → Al enviar → «Redirigir a la URL» → `https://dominio/solicitud-recibida`.
5. Configuración → ID de píxel de Facebook: **vacío**. El Lead va por servidor; si se rellena, el formulario podría disparar eventos de navegador duplicados.
6. Guardar.

**Puerta:** al enviar redirige a la página de gracias y el formulario no dispara Lead ni SubmitApplication en el navegador (lo confirma la fase 8).

## Fase 3. Página de gracias

1. Reutiliza el paso del embudo que había (antes /llamada-confirmada). En el paso → Publicación: nombre «Solicitud recibida», ruta `/solicitud-recibida`. La ruta vieja queda en 404: comprueba que nada la enlace.
2. El contenido vive en el **código de seguimiento del pie de página** de esa página, no en un bloque. Fuente: `landing/gracias-solicitud-ghl.html`.
3. Contenido: «Recibido», quién contacta y desde qué número («por llamada o por WhatsApp»), botón «Escribir a <nombre> por WhatsApp» (wa.me con texto prellenado) que dispara solo `fbq('track','Contact')`, aviso de que ha llegado un correo y método de pago.
4. Nada de Lead en esta página.

**Puerta:** `comprobar_landing.sh …/solicitud-recibida "Recibido" "Bizum"` cuenta > 0 y `verificar_pixel.py` solo ve PageView.

## Fase 4. API de conversiones (Lead por servidor)

1. Si ya existe un flujo con la acción «API de conversión de Meta» y el token pegado, **reutilízalo**: el token no se hereda en acciones nuevas y yo no lo escribo.
2. Disparador: «Formulario enviado», filtro «El formulario está» = el formulario de la fase 2. Borra el disparador viejo (ej. «Cita reservada por el cliente»).
3. Acción: Integración, Funnel Event, conjunto de datos = ID del píxel, evento **Lead**, valor vacío, moneda EUR, mapeo personalizado apagado.
4. Nombre del flujo: «Meta CAPI Lead - formulario <producto>». Guardar. Publicado.
5. Código de prueba solo mientras pruebas (fase 8); después se borra y se guarda.
6. GHL no deja fijar event_id: el Lead va **solo** por servidor. No pongas `fbq('track','Lead')` en ninguna página.

**Puerta:** registro de ejecución del flujo en «Success» tras un envío real y «Cliente potencial · Servidor» en Test Events.

## Fase 5. Flujos de GHL: pipeline, aviso y nutrición

Flujo principal (ej. «Inscripción Curso Acrygel: pipeline y aviso», `dc66b0d3`), disparado por el mismo formulario:

1. Crear o actualizar oportunidad → pipeline del producto, etapa «Inscrita».
2. Notificación interna → Email → «Correo electrónico personalizado» = cliente principal; segundo destinatario en **Cc** (comas en el mismo campo dan error). Deja «Desde el nombre» vacío o rellena también el correo remitente. Asunto con `{{contact.name}} {{contact.phone}}`. Cuerpo: datos + «llamadla ahora; si no coge, WhatsApp y otro intento por la tarde» + qué etapa mover.
3. Correo 1 (al momento) → Esperar 1 día → Correo 2 → Esperar 1 día → Correo 3 → Esperar 1 día → Correo 4. Remitente: nombre y correo del cliente.
4. Configuración del flujo: «Detener en respuesta» ON. «Permitir reentrada» ON. Sin ventana horaria (retrasaría el aviso).
5. Flujo «<producto>: sacar de nutrición al pagar reserva»: disparador «Cambio de fase de la secuencia» con filtros pipeline = el del producto y fase = «Reserva pagada» → acción «Elimine del flujo de trabajo» → «Otro flujo de trabajo» → el principal (y el de aviso final). Ojo: al elegir «Otro flujo» GHL preselecciona el propio flujo; quítalo.
6. Flujo de aviso final con fecha real (caso real: «Acrygel: último aviso mar 24-nov», `3dc90e9c`): disparador formulario → «Esperar hasta una fecha/hora específica» (martes 24-nov 09:00) → Correo 5. Quien entra después de esa hora tiene que salir del flujo sin recibirlo (si no, le llegan el correo 1 y el 5 a la vez): pon esa condición y compruébala. Detener en respuesta ON. Añádelo también al flujo de sacar.

**Puerta:** los tres flujos publicados, nombres claros, y la lista de flujos muestra «Publicado» en todos.

## Fase 6. WhatsApp en GHL

1. Ajustes → WhatsApp. Si pide suscripción (10 $/mes a cargo de la agencia), la activa Diego.
2. Conexión: opción «Conecte su WhatsApp» (coexistencia: el cliente sigue usando WhatsApp Business en el móvil). La hace el dueño del número: inicia sesión con su Facebook, elige su negocio y su número y escanea el código con la app. Necesita ordenador y móvil a la vez.
3. Requisito: el número tiene que estar en **WhatsApp Business**, no en el WhatsApp normal. Pregúntalo antes.
4. Mensajes iniciados por la empresa = plantilla aprobada por Meta. Hasta que esté, contacto manual.

**Puerta:** o conectado con plantilla aprobada, o acordado por escrito el contacto manual.

## Fase 7. Meta Ads

1. Conjunto: Sitio web, conjunto de datos = píxel, evento **Cliente potencial**, atribución estándar.
2. Anuncios: el texto y el botón tienen que decir lo mismo que el embudo. Se cambió «Reserva una llamada de 15 minutos» por «Déjame tu nombre y tu WhatsApp y te llamo para contarte si el curso es para ti» y CTA «Reservar» por «Más información» en los 4 anuncios.
3. Audiencia: si el nombre del conjunto dice «Mujeres 18-55» comprueba que la sugerencia lo diga (Mostrar sugerencias → Edad 18-55, Género Mujeres). Con Advantage+ es orientación, no límite.
4. Fechas: fecha de fin marcada (fase 0). Presupuesto de campaña (fase 0).
5. Anunciante UE: obligatorio; comprueba el check verde.
6. Audience Network: la exclusión ya solo está en «Controles de cuenta», que afecta a todas las campañas de la cuenta (Lucía tenía otra activa). No se toca sin OK; se revisa el reparto a las 48 h.
7. Publicar: en campaña activa, cada cambio deja «Cambios sin publicar» hasta pulsar Publicar. Comprueba después que vuelve a «Activa / En proceso».

**Puerta:** checklist de configuración de `references/pruebas-y-errores.md` completa.

## Fase 8. Pruebas de punta a punta

Sigue `references/pruebas-y-errores.md`: script de píxel, recorrido real con Test Events abierto, registro de ejecución, limpieza.

**Puerta:** los cinco eventos esperados, cada uno una vez, y la limpieza hecha.

## Fase 9. Revisión de la oferta y la comunicación

Lee `~/.claude/kb-mercado/08-reglas-de-criterio.md` y `29-oferta-trafico-frio.md`. Revisa con grado de evidencia:
- Escasez y plazo reales (B). Promesa concreta con mecanismo corto (C). Objeción planteada y refutada en landing y correo (inoculación, B). Calidez antes que competencia (B). Bonus pocos y ligados al núcleo (B-C).
- Lo que faltó en el caso real: prueba de alumnos o clientes (fotos antes/después, frases reales), número de plazas restantes real, correo final con fecha, fricción de la llamada, método de pago visible.
- No toques anuncios recién lanzados: esperar 72 h para no reiniciar el aprendizaje.

**Puerta:** lista priorizada entregada a Diego; lo que depende del cliente, pedido en un mensaje.

## Fase 10. Entrega al cliente

1. Ráfaga de instrucciones (plantilla en `references/copy-y-proceso-comercial.md`): qué hace la clienta, qué les llega, llamar rápido, guion, objeciones, etapas de GHL, WhatsApp, qué necesito que me digáis.
2. Antes de redactar: lee el chat reciente del grupo (base SQLite de WhatsApp del Mac, ver memoria `reference-whatsapp-base-local-mac.md`).
3. Se envía solo con orden explícita. Envío con computer-use en la app de WhatsApp: buscar grupo, abrir, por mensaje `write_clipboard` → clic en el campo → cmd+V → zoom para verificar → Return. Verifica después en ZWAMESSAGE (ZISFROMME=1).

**Puerta:** mensajes enviados y verificados en la base, o entregados a Diego en bloque si no hubo orden.

## Fase 11. Seguimiento

- +48 h: reparto por ubicaciones (Audience Network), coste por Lead, ¿están contactando? (etapas en GHL).
- +72 h: qué anuncio trae Leads; solo entonces se tocan creativos.
- Antes de culpar a la campaña: ¿contestan a los leads en minutos? (regla 17).
- Parar antes de la fecha si se llenan las plazas.
