# SEM: estructura, Performance Max y medición

Cómo montar una cuenta de Google Ads que la puja inteligente pueda leer, qué se ve y qué no dentro
de Performance Max, y el bloque que más dinero mueve en captación de leads: devolverle a Google
**qué lead acabó siendo cliente**. Para Diego esto es el fichero importante del trío, porque sus
leads entran por calendarios de GHL y por WhatsApp, y ninguno de los dos cuenta nada a Google por
sí solo.

Compilado el 24-sep-2026. Mecánica de plataforma con la marca **caduca: revisar trimestral**. URL de
ayuda abreviadas como `/answer/NNNN` = `support.google.com/google-ads/answer/NNNN`. Umbrales
verificados uno a uno en `~/.claude/skills/google-ads-360/referencias/00-como-leer-esta-skill.md`.

---

## 1. Estructura: densidad de datos antes que orden

La puja inteligente aprende por estrategia. Cada campaña o grupo que partes le quita
conversiones a los demás. La regla de [15](15-plataformas-mecanica-real.md) ("consolida también en
Google") se aplica, con dos excepciones que no se negocian:

1. **Marca aparte.** Es la única forma de saber cuánto aporta lo genérico. Una cuenta que mezcla
   marca y genérico tiene un CPA precioso y ninguna información.
2. **Separar lo que tiene economía distinta**, no lo que tiene temática distinta. Dos servicios con
   el mismo ticket van juntos aunque "parezcan" distintos. Dos países con márgenes distintos, no.

### Configuración que cuesta dinero y nadie mira (grado B y casos propios)

- **Ubicación por defecto "Presencia o interés"**: sirve anuncios a quien busca *sobre* España sin
  estar en España. Se cambia a "Presencia". Pasó en la campaña de ECSSTUDIO, corregido el 8-ago-2026.
- **Negativas con y sin tilde**: `guia` y `guía` son dos negativas distintas. Las negativas a nivel
  de cuenta (máximo 1.000) **no cubren variantes cercanas**: singular y plural van por separado.
  [`/answer/11396330`](https://support.google.com/google-ads/answer/11396330)
- **Red de búsqueda de socios y Display** dentro de campañas de Search: se revisan al crear.
  Display dentro de Search casi nunca aporta en captación de leads.

Casos en `google-ads-360/referencias/99-trampas.md`, A5 y A6.

---

## 2. Performance Max (caduca: revisar trimestral)

Una sola campaña que sirve en Search, Shopping, YouTube, Display, Discover, Gmail y Maps, sin
palabras clave. Se alimenta de grupos de activos, señales de audiencia y **search themes**.

### Lo que ya se ve (grado B)

| Qué | Dato | Fuente |
|---|---|---|
| Informe por canal | Search, Display, YouTube, Discover, Maps, Gmail y socios de búsqueda, con conversiones y coste por canal | [`/answer/16260130`](https://support.google.com/google-ads/answer/16260130?hl=en) |
| Términos de búsqueda | Informe completo, con columna de origen y negativas desde el propio informe | [`/answer/16327396`](https://support.google.com/google-ads/answer/16327396) |
| Negativas de campaña | Hasta 10.000 por campaña, solo sobre inventario de Search y Shopping | `/answer/15726455` |
| Exclusiones de marca | Solo en Search y Shopping. Cogen erratas y variantes | `/answer/13721847` |
| Search themes | Hasta 50 por grupo de activos desde el 7-ago-2025. Misma prioridad que frase y amplia | `/answer/14767319` |
| Prioridad de la exacta | Si la búsqueda coincide con una exacta de Search, Search va antes que PMax. **No es absoluto**: con Search corta de presupuesto, PMax puede salir en tu marca | `/answer/10724817` |

### Lo que el informe por canal no dice

Literal: el informe *"supports whatever attribution model the advertiser uses"*. Reparte las
conversiones con el modelo de atribución de la cuenta. Te dice **dónde cayó el crédito**, no qué
canal lo causó. El Display de PMax con buen CPA puede ser remarketing a gente que iba a convertir
igual, que es el caso inflado del fichero [14](14-medicion-e-incrementalidad.md).

### PMax en captación de leads (grado C, es mecanismo)

El sistema optimiza el evento que le das. Si el evento es "formulario enviado", el inventario donde
los formularios salen más baratos gana, y ahí caben bots, clics accidentales en Display y gente
que rellena por rellenar. No hace falta un estudio para saberlo: es la misma lógica de Maximizar
clics un escalón más abajo.

**Regla:** PMax para leads solo cuando el objetivo principal sea una etapa importada del CRM (lead
cualificado, cita realizada o venta) y llegue a unas 30 al mes. Antes, Search.

### Demand Gen y AI Max, en dos líneas

- **Demand Gen**: YouTube, Discover y Gmail, y desde junio de 2026 absorbe Display. Arrancar en
  Maximizar conversiones, pasar a objetivo con al menos 50 conversiones, presupuesto de al menos
  10× el tCPA (`/answer/14509385`, `/answer/16797388`). Es creación de demanda, se mide como tal.
- **AI Max for Search**: concordancia por términos, personalización de texto y expansión de URL
  final sobre una campaña de Search. Exige puja inteligente basada en conversiones. Google publica
  +14% de conversiones en beta y +7% fuera de beta: el salto de 14 a 7 al ampliar la población es
  lo que se espera de un dato sin control. **Grado C.**
  [`/answer/15910187`](https://support.google.com/google-ads/answer/15910187?hl=en)

---

## 3. Atribución y ventanas (grado B, caduca: revisar trimestral)

- Desde septiembre de 2023 solo quedan dos modelos: **basado en datos** (por defecto) y **último
  clic**. Primer clic, lineal, decaimiento temporal y basado en la posición desaparecieron.
  [Search Engine Journal](https://www.searchenginejournal.com/google-is-removing-4-attribution-models-for-advertisers/484264/)
- Ventanas por defecto: 30 días post-clic, 3 días de vista con interacción, 1 día post-impresión.
  Los cambios no son retroactivos. `/answer/3123169`
- El modelo basado en datos reparte crédito entre anuncios de Google. **No es incrementalidad**:
  no sabe qué habría pasado sin anuncios.

---

## 4. Pérdida de señal en la UE (grado B, caduca: revisar trimestral)

### Consent Mode v2

Cuatro parámetros: `ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`.

- **Modo básico**: la etiqueta no carga hasta que el usuario toca el banner. Modelado genérico.
- **Modo avanzado**: la etiqueta carga siempre y, con consentimiento denegado, manda pings sin
  cookies. Modelado específico del anunciante.

**Umbral de modelado de conversiones de Google Ads: 700 clics en anuncios en total en 7 días**, por
dominio y país, y 7 días completos con el modo implementado. Unos 100 clics al día. Ojo: la
traducción española de la ayuda dice "700 al día", y está mal. Manda la página de verificación.

- [`/answer/14218557`](https://support.google.com/google-ads/answer/14218557), verificado 6-sep-2026

**Matiz al fichero [14](14-medicion-e-incrementalidad.md):** el umbral de "1.000 usuarios diarios"
que da ese fichero es el del modelado de comportamiento de GA4, no el de conversiones de Google
Ads. La conclusión no cambia: una cuenta local con 20 clics al día no tiene modelado, y su pérdida
de señal es real. No se afirma de memoria: se abre Objetivos, Conversiones, la acción, pestaña
Diagnóstico.

### Conversiones mejoradas

Datos del usuario (email, teléfono en E.164, dirección) normalizados y hasheados con SHA-256, que
Google cruza con cuentas con sesión iniciada. Desde junio de 2026 las de web y las de leads
comparten un solo interruptor. Hasta que no se aceptan las condiciones de datos de cliente en la
cuenta, no se recoge nada.

- [`/answer/9888656`](https://support.google.com/google-ads/answer/9888656) · [`/answer/16884284`](https://support.google.com/google-ads/answer/16884284)

---

## 5. Conversiones offline: el lead que se vuelve cliente

Esto es lo que separa una cuenta de leads que aprende de una que se llena de basura. Google solo
sabe que alguien rellenó un formulario. **No sabe cuál de esos leads contestó el teléfono, cuál fue
a la cita y cuál firmó.** Si no se lo dices, puja por más formularios, no por más clientes.

### La mecánica (grado B, caduca: revisar trimestral)

| Qué | Dato | Fuente |
|---|---|---|
| Identificadores | `gclid` (web), `gbraid` (clic en web que acaba en app iOS), `wbraid` (clic en app iOS que acaba en web). Se capturan y guardan los tres. Distinguen mayúsculas | [API, upload-offline](https://developers.google.com/google-ads/api/docs/conversions/upload-offline) |
| Ventana con gclid | 90 días desde el clic | [`/answer/15081888`](https://support.google.com/google-ads/answer/15081888?hl=en) |
| Ventana con datos personales (conversiones mejoradas para leads) | 63 días | misma |
| Espera mínima clic a subida | 6 horas | `/answer/13321563` |
| Procesamiento | Menos de 12 horas normalmente, hasta 72 con gbraid o wbraid | misma |
| Duplicados | Mismo identificador, nombre de conversión y hora: no se importa dos veces. Con `order_id` se deduplica por pedido | `/answer/6386790` |
| API desde el 15-jun-2026 | La Google Ads API no acepta nuevos adoptantes de importación offline. La ruta nueva es la **Data Manager API**. Quien ya subía, sigue | [Ads Developer Blog, 15-may-2026](https://ads-developers.googleblog.com/2026/05/changes-to-offline-click-conversion.html) |
| Reglas de valor | Multiplicador de 0,5 a 10 | `/answer/10520348` |

### Qué etapas subir y cuál manda

Se suben **varias etapas** del embudo como acciones de conversión distintas, cada una con su valor:

1. Lead cualificado (contestó y encaja).
2. Cita realizada.
3. Propuesta enviada.
4. Venta, con el importe.

Una sola va como **principal** (la que puja). Las demás, secundarias, para leer el embudo. La
principal es **la etapa más profunda que llegue a unas 30 al mes**. Si la venta llega a 3 al mes,
la venta no puede mandar: manda el lead cualificado, y la venta se sube igual para que el valor
exista cuando haya volumen.

Si hay puja por valor, el valor de cada etapa es su probabilidad de acabar en venta por el margen
de la venta. Un lead cualificado que cierra una de cada cinco veces en un servicio de 8.000 € con
50% de margen vale 800 €, no 8.000 €.

### GHL: dónde se rompe (casos propios verificados, más ayuda de GHL)

**El calendario pierde el gclid.** El widget de reserva de GHL se inserta con el `src` pelado. Probado
con `?gclid=TEST`: el parámetro no llega al iframe, y el script `form_embed.js` solo copia a
`sessionStorage` los parámetros que empiezan por `utm_`. Solución: guardar `gclid`, `gbraid` y `wbraid`
en la landing y añadirlos al `src` del iframe al crearlo, más una página de gracias en el dominio
propio. Caso A4 en `google-ads-360/referencias/99-trampas.md`.

**La acción nativa "Add to Google Ads" no cubre el embudo.** Según la ayuda de GHL, solo funciona
con cinco disparadores: envío de formulario, compra, llamada de number pool, encuesta y chat widget.
**No** con cita reservada ni con cambio de etapa del pipeline. No se puede probar antes de ir en
vivo. Además, con gbraid o wbraid solo admite recuento "cada conversión".

- [HighLevel, acción Add to Google Ads](https://help.gohighlevel.com/support/solutions/articles/155000003368-workflow-action-add-to-google-ads), consultado 24-sep-2026

Para las etapas del pipeline: disparador "cambio de etapa de oportunidad" en un workflow, webhook
saliente con el gclid del contacto, la hora, el valor y el nombre exacto de la conversión, y de ahí
a la Data Manager API o a una hoja de Google con **importación programada** desde Google Ads. La
hoja programada es lo más barato y lo que menos se rompe en una cuenta pequeña.

### WhatsApp: el lead sin clic (grado C, procedimiento)

Un lead que escribe por WhatsApp desde un anuncio no deja gclid en ningún sitio. Tres salidas, de
mejor a peor:

1. **Pasar por la landing antes de WhatsApp.** El botón de la landing guarda el gclid y abre
   `wa.me` con un mensaje prellenado que lleva un código corto. El código se casa en GHL con el
   gclid guardado. Se pierde algo de volumen por el paso extra y se gana saber de dónde viene.
2. **Pedir nombre y teléfono antes de abrir WhatsApp.** Un formulario de dos campos crea el contacto
   en GHL con gclid y teléfono. Las conversiones mejoradas para leads casan luego por teléfono
   hasheado.
3. **Recurso de mensaje de Google con la conversión "conversación iniciada".** Está en beta y la
   disponibilidad en España no está confirmada. Solo cuenta que la conversación empezó, no que
   sirviera. [`/answer/14888522`](https://support.google.com/google-ads/answer/14888522?hl=en)

Sin ninguna de las tres, la campaña que lleva a WhatsApp puja a ciegas. Es mejor saberlo antes
de lanzar.

### Customer Match: el umbral que deja fuera a las cuentas pequeñas (grado B)

Para **segmentar** con Customer Match la cuenta necesita 90 días de historial y más de 50.000 USD de
gasto acumulado, además de buen historial de políticas y de pagos. Sin eso, solo observación y
exclusión. Para servir, 100 usuarios activos en 30 días.

- [Política de Customer Match](https://support.google.com/adspolicy/answer/6299717) · [`/answer/7476585`](https://support.google.com/google-ads/answer/7476585)

Traducción: en una cuenta nueva de un cliente pequeño, subir la base de clientes sirve para
**excluirlos** y como señal, no para apuntar a ellos.

---

## 6. Incrementalidad en Google (caduca: revisar trimestral)

**Desde el 11-nov-2025 Google permite experimentos de incrementalidad desde unos 5.000 USD**, antes
del orden de 100.000. Lo consigue con estadística bayesiana. (Grado B el dato.)

- [`/answer/16719772`](https://support.google.com/google-ads/answer/16719772?hl=en)

Lo que eso implica (grado C, es razonamiento): un modelo bayesiano con poco dato se apoya más en
lo que supone de partida. Con 5.000 USD el resultado se parece más a la suposición de Google que
con 100.000. Sirve como dirección, y se lee con el intervalo, no con el punto.

Para cuentas de Diego lo que funciona mejor y cuesta menos:

- **Pausa de marca en semanas alternas** o por provincias, mirando clics totales a la web (pago más
  orgánico) y leads en el CRM.
- **Geo on/off** para genérico: provincias con y sin campaña, de 3 a 4 semanas, leads del CRM como
  métrica. Método en [14](14-medicion-e-incrementalidad.md).

**Meridian (el MMM de Google) no es para clientes pequeños.** Su propia documentación dice que dos
años de datos semanales, 104 puntos, dan unos 4 puntos por parámetro y *"too low to estimate the
model reliably"*, y apunta a unos 15 por parámetro. Grado B.

- [Meridian, cantidad de datos necesaria](https://developers.google.com/meridian/docs/pre-modeling/amount-data-needed)

---

## Banderas rojas

| Lo que se ve o se dice | Qué pasa |
|---|---|
| La conversión principal es "formulario enviado" y el CRM dice que la mitad es basura | La cuenta puja por basura. Importar la etapa cualificada y hacerla principal |
| PMax de leads con el mejor CPA de la cuenta | Mira dónde sirve en el informe por canal y cuántos de esos leads contestan |
| "El informe por canal dice que YouTube convierte" | Es reparto de crédito con el modelo de la cuenta, no causalidad |
| "Tenemos modelado de Consent Mode" en una cuenta local | Por debajo de 700 clics en 7 días no hay. Abrir Diagnóstico antes de afirmarlo |
| Reservas del calendario de GHL que no aparecen en Google Ads | El gclid no llega al iframe. Probar con `?gclid=TEST` |
| "La acción de GHL ya sube las citas" | No tiene disparador de cita ni de etapa. Webhook o importación programada |
| Campaña a WhatsApp sin paso intermedio | Puja a ciegas. Ningún clic se casa con ningún cliente |
| "Subimos la base de clientes y apuntamos a lookalikes" | Sin 90 días y 50.000 USD, Customer Match solo observa y excluye |
| "Vamos a montar un MMM" con un año de datos | Meridian dice que ni con dos años alcanza en modelo nacional |
