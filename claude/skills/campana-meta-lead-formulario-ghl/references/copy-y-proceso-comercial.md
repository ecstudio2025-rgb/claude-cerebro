# Textos y proceso comercial (plantillas con huecos)

Origen: caso Lucía García, curso de acrygel con molde (14-nov-2026). Textos completos reales en `~/Claude/proyectos-clientes/lucia-biel/campana-acrygel/nutricion-formulario-correos.md`.

Huecos: `<CLIENTE>` (quien firma), `<SEGUNDO>` (quien también llama), `<TEL>`, `<PRODUCTO>`, `<FECHAS>`, `<LUGAR>`, `<PRECIO>`, `<RESERVA>`, `<PAGO>` (Bizum o transferencia), `<INCLUYE>`, `<PLAZAS>`, `<MECANISMO>` (lo que lo diferencia), `<OBJECION>`.

Antes de usar: adapta a la voz del cliente, pásalo por `~/.claude/anti-patrones-ia-redaccion.md`, no prometas nada que el cliente no haya dicho, y la escasez solo si es real.

## Aviso interno (cliente y segundo, al instante)

Asunto: `Nueva solicitud <PRODUCTO>: {{contact.name}} {{contact.phone}}`

```
Ha pedido que la llaméis:
Nombre: {{contact.name}}
Teléfono: {{contact.phone}}
Correo: {{contact.email}}
(Su respuesta de cualificación está en su ficha de contacto.)

Llamadla ahora. Si no contesta, mandadle un WhatsApp desde el <TEL> y volved a probar por la tarde.
Cuando hayáis hablado, movedla de etapa en Clientes potenciales: Contactada por WhatsApp, En conversación o Reserva pagada.
```

## Correo 1 · al momento

Asunto: `Recibido, te contactamos desde el <TEL>`

```
Hola {{contact.first_name}},

Soy <CLIENTE>. Me ha llegado tu solicitud para <PRODUCTO>.

<SEGUNDO> o yo te contactamos desde el <TEL>, por llamada o por WhatsApp, como prefieras. Guárdalo en tus contactos para saber que somos nosotros. Si quieres adelantarte, contesta a este correo o mándame un WhatsApp a ese número.

Te dejo lo básico a mano:
· <FECHAS>, en <LUGAR>.
· <PRECIO> con <INCLUYE>. Reservas la plaza con <RESERVA> por <PAGO> y el resto lo pagas al empezar.
· <ESTRUCTURA en una línea por día o fase>.
· <MECANISMO>.
· <PLAZAS> plazas como máximo.

<CLIENTE>
```

## Correo 2 · al día siguiente (el mecanismo y la historia)

Asunto: `Lo que pasa al cuarto día` (o el equivalente del producto)

```
Hola {{contact.first_name}},

<El problema que aparece justo después de comprar algo parecido. Concreto y reconocible.>

<Cómo lo resuelve el MECANISMO, en dos pasos.>

<Historia personal breve del cliente: por qué hace esto. Calidez antes que competencia.>

Si todavía no hemos hablado, contesta a este correo con la hora que te va mejor y te llamamos.

<CLIENTE>
```

## Correo 3 · a los 2 días (inoculación de la objeción principal)

Asunto: `¿<OBJECION formulada como pregunta>?`

```
Hola {{contact.first_name}},

Es lo que más me preguntan. Y no: <reconocer el límite con honestidad>, y desconfía de quien te lo prometa.

Lo que sí te llevas es <resultado real y concreto>.

<Cómo se cubre lo que falta: el MECANISMO.>

<Segunda objeción frecuente y su respuesta en una frase (ej. «Si nunca has hecho uñas, puedes venir»).>

¿Te llamamos? Contesta a este correo o escríbeme al <TEL>.

<CLIENTE>
```

## Correo 4 · a los 3 días (cierre de la secuencia)

Asunto: `Para reservar tu plaza`

```
Hola {{contact.first_name}},

Te escribo por <PRODUCTO> del <FECHAS>.

Somos <PLAZAS> plazas como máximo, para <razón real del límite>. La plaza se reserva con <RESERVA> por <PAGO> y el resto se paga al empezar.

Si te interesa, contesta a este correo o mándame un WhatsApp al <TEL> y te paso los datos para hacer la reserva.

Si no es el momento, no pasa nada.

<CLIENTE>
```
OJO: si existe el correo 5 (aviso final con fecha), el 4 NO puede decir «te escribo por última vez» ni «no te escribo más». Fue un fallo real (Lucía, 14-nov): se corrigió antes de que saliera ningún correo.

## Correo 5 · aviso final con fecha (flujo aparte, «esperar hasta» la fecha)

Asunto: `El curso es este <DÍA DE LA SEMANA> <DÍA>`

```
Hola {{contact.first_name}},

Te escribo porque <PRODUCTO> empieza este <DÍA DE LA SEMANA> <DÍA> en <LUGAR>, y quería avisarte antes de cerrar las plazas.

Si todavía te lo estás pensando, contéstame a este correo o mándame un WhatsApp al <TEL> hoy o mañana y lo hablamos. La plaza se reserva con <RESERVA> por <PAGO> y el resto se paga al empezar.

Si esta vez no puede ser, no pasa nada.

<CLIENTE>
```
Flujo: Formulario enviado → Esperar «hasta una fecha/hora específica» (ej. martes 24-nov 09:00) con «Si esta fecha ya ha pasado: Eliminar contacto de la automatización» (así quien entra tarde no recibe dos correos a la vez) → Correo 5. Añade este flujo a la lista del flujo «sacar de nutrición al pagar reserva». Comprueba el día de la semana antes de escribirlo (Lucía: 28-nov fue sábado, no viernes). Si se conoce el número real de plazas libres, «quedan X de <PLAZAS>»; si no, no se pone.

## Página de gracias

```
Recibido
<SEGUNDO> o yo te contactamos desde el <TEL>, por llamada o por WhatsApp. Guárdalo en tus contactos para reconocernos.
Si quieres adelantarte, mándame un WhatsApp ahora y empezamos por ahí.
[Escribir a <CLIENTE> por WhatsApp]  → wa.me/<TEL_INTERNACIONAL>?text=Hola <CLIENTE>, acabo de pedir información de <PRODUCTO>
También te hemos mandado un correo con todos los detalles. La plaza se reserva con <RESERVA> por <PAGO>.
```

## WhatsApp cuando no contesta la llamada

```
Hola X, soy <CLIENTE>, te acabo de llamar por <PRODUCTO>. ¿Cuándo te va bien que te llame? Son 10 minutos
```

## Guion de llamada (10-15 min)

1. Saludo: «Hola X, soy <CLIENTE>, has pedido info de <PRODUCTO>, ¿tienes 10 minutos?»
2. Preguntar antes de contar: experiencia y qué quiere conseguir (trabajar de esto, añadir el servicio, para sí).
3. Conectar con lo que dice: si empieza de cero, qué parte le sirve; si ya trabaja, qué problema concreto le corrige.
4. Lo que diferencia: <MECANISMO>.
5. Precio claro: <PRECIO>, <INCLUYE>, reserva <RESERVA> y resto al empezar.
6. Cerrar en la llamada: «Te mando ahora por WhatsApp cómo hacer la reserva y te guardo la plaza». Mandarlo con la llamada abierta si se puede.

## Objeciones (respuesta en una frase)

| Objeción | Respuesta |
|---|---|
| «En X días no se aprende» | Tienes razón; por eso después está <MECANISMO> |
| «No tengo experiencia» | Empezamos desde <el principio concreto>, no hace falta nada |
| «Es caro» | Lleva <INCLUYE> y <MECANISMO>. Un tutorial no te ve las manos |
| «Me lo pienso» | Vale, ¿qué te hace dudar? (y responder a eso). ¿Te guardo la plaza hasta mañana? Somos <PLAZAS> |
| <logística, ej. «No tengo modelo»> | <solución concreta> |

## Etapas del pipeline (las que se explican al cliente)

Inscrita (acaba de dejar sus datos) → Contactada por WhatsApp (no cogió y se le escribió) → En conversación (se lo piensa) → Reserva pagada (sale de los correos) → Pago completo → Asistió. Lista de espera si se llenan.

## Ráfaga de instrucciones al cliente (voz de Diego, chat corto, un mensaje por bloque)

```
<cliente> <segundo> os explico como queda todo el sistema, leedlo con calma que de esto depende llenar las <PLAZAS> plazas

1. QUE HACE LA CLIENTA
ve un anuncio en instagram o facebook, solo en <ZONA>
entra en <DOMINIO>, ve el curso y abajo deja nombre, whatsapp, correo y <pregunta de cualificación>
al enviarlo le sale una pagina que dice que la contactais desde el <TEL> y un boton para escribiros por whatsapp

2. QUE OS LLEGA A VOSOTROS
al momento os llega un correo "Nueva solicitud <PRODUCTO>" con su nombre y telefono
a ella le llega un correo vuestro con todos los datos y luego 3 correos mas, uno al dia
y entra sola en GHL, en clientes potenciales, pipeline <PIPELINE>, etapa Inscrita

3. LO MAS IMPORTANTE: LLAMAR RAPIDO
la que deja sus datos esta pensando en el curso en ese momento, a las pocas horas ya esta en otra cosa
llamadla en cuanto os llegue el correo
si no coge, whatsapp al momento desde el <TEL> y otro intento esa tarde y al dia siguiente. despues de 3 intentos se deja
decidid entre vosotros quien llama y en que horas

4. LA LLAMADA, 10-15 MIN
<guion en guiones cortos>

5. LO QUE OS VAN A DECIR
<objeciones en guiones cortos>

6. MOVED LAS ETAPAS EN GHL, ESTO ES CLAVE
<etapas una por línea>
asi vemos cuantas piden info, cuantas cogen el telefono y cuantas pagan, y ajustamos los anuncios con datos reales

7. WHATSAPP AUTOMATICO
<estado: activado / falta conectar / quién lo hace y cómo>

8. NECESITO QUE ME DIGAIS
- quien llama y en que horas
- como cobrais la reserva
```

Respuesta tipo a «¿dónde veo los contactos?»: correo «Nueva solicitud» al momento; en GHL, Clientes potenciales → pipeline (tarjetas por etapa) y Contactos; en el móvil, app «LeadConnector» con su correo de GHL.

## Peticiones al cliente que suben la conversión (pedir en un solo mensaje)

- 3-5 fotos de trabajos de alumnos o clientes (antes y después) con permiso y una o dos frases reales.
- Número real de plazas libres, actualizado.
- Método de cobro de la reserva.
