# SEM: la subasta, las concordancias y las pujas

Cómo decide Google quién sale y cuánto paga, qué quedó de las concordancias después de cinco años
de cambios, y qué pide la puja inteligente para funcionar. Lo que aquí es mecánica de plataforma
lleva la marca **caduca: revisar trimestral**. Lo que es aritmética o experimento publicado aguanta.

Compilado el 24-sep-2026. Las URL de `support.google.com/google-ads/answer/...` se citan abreviadas
como `/answer/NNNN`. La tabla de umbrales verificados uno a uno, con fecha de comprobación, vive en
`~/.claude/skills/google-ads-360/referencias/00-como-leer-esta-skill.md`: este fichero es la capa de
criterio, la skill es el manual de operación.

---

## 1. La subasta (grado B, caduca: revisar trimestral)

Cada búsqueda lanza una subasta nueva. Google ordena los anuncios por **Ad Rank**, que según su
propia ayuda sale de seis cosas: la puja, la calidad del anuncio y de la landing, los umbrales
mínimos de Ad Rank, la competitividad de la subasta, el contexto de la búsqueda (términos,
ubicación, dispositivo, hora) y el efecto esperado de los recursos y formatos.

Lo que se paga es menos que la puja. Literal de Google: pagas lo mínimo necesario *"to clear the Ad
Rank thresholds and beat the Ad Rank of the competitor immediately below you"*. Y la calidad baja
el precio: *"Higher quality ads can often lead to lower CPCs"*.

- [Ad Rank, `/answer/1722122`](https://support.google.com/google-ads/answer/1722122?hl=en), consultado 24-sep-2026
- [CPC real, `/answer/6297`](https://support.google.com/google-ads/answer/6297?hl=en), consultado 24-sep-2026

Dos consecuencias que casi nadie saca:

1. **Los umbrales dependen del contexto.** Un mismo anuncio puede no salir en una búsqueda y salir
   en otra con la misma puja. Por eso "subir la puja" no arregla un problema de relevancia.
2. **Los recursos cuentan en el ranking.** Enlaces de sitio, llamada, logo y nombre del negocio
   entran en Ad Rank, así que dejarlos vacíos cuesta posición, no solo CTR.

## 2. El Nivel de Calidad no entra en la subasta (grado B)

Literal de la ayuda de Google: *"Quality Score is not an input in the ad auction. It's a diagnostic
tool"*. Va de 1 a 10 y se compone de tres lecturas relativas a la competencia: CTR esperado,
relevancia del anuncio y experiencia en la página de destino.

- [Nivel de Calidad, `/answer/6167118`](https://support.google.com/google-ads/answer/6167118?hl=en), consultado 24-sep-2026

Lo que la subasta usa es una estimación de calidad **en el momento de cada búsqueda**, que no se
ve. El número del 1 al 10 es un resumen agregado por palabra clave. Optimizar para subir ese número
es trabajar sobre el termómetro.

Sirve para una cosa: localizar **cuál de los tres componentes** está en "Por debajo de la media".
Si es la landing, el problema es la landing, y ahí sí hay dinero.

**Lo que circula y no se usa.** "El CTR esperado pesa un 39%, la landing un 39% y la relevancia un
22%" viene de Adalysis, que dice haber hecho ingeniería inversa de la fórmula. La página no publica
muestra, método ni fecha. **Grado D.** Tampoco se usa "un QS de 10 te da un 50% de descuento en el
CPC": no tiene fuente primaria.

- [Adalysis, fórmula del Quality Score](https://adalysis.com/quality-score/), consultado 24-sep-2026

---

## 3. Concordancias: qué queda después de los cambios (caduca: revisar trimestral)

### La cronología (grado B)

- **Julio de 2021**: desaparece la amplia modificada (BMM) y su comportamiento pasa a la de frase.
  La frase ya no exige el orden de las palabras si el significado se mantiene.
- **Variantes cercanas** en las tres concordancias: errores, plurales, abreviaturas, reordenaciones
  y, en exacta, búsquedas con el mismo significado.
- **2024**: la amplia pasa a ser la concordancia por defecto al crear campañas de Search con puja
  inteligente.
- **3-ago-2026**: ya no se puede crear amplia a nivel de campaña ni activos creados automáticamente
  antiguos, en interfaz, Editor ni API.
- **1 al 30 de septiembre de 2026**: automigración a **AI Max** de las campañas de Search que tengan
  amplia a nivel de campaña o activos automáticos antiguos. Basta una de las dos. Sin opt-out
  documentado. Los DSA migran del 1 al 28 de febrero de 2027.

Fuentes:
- [Opciones de concordancia, `/answer/7478529`](https://support.google.com/google-ads/answer/7478529?hl=en)
- [Google Ads Developer Blog, migración a AI Max, 12-ago-2026](https://ads-developers.googleblog.com/2026/08/migrate-campaign-level-broad-match-and.html), verificado el 6-sep-2026 en la skill google-ads-360

### Qué dicen los datos independientes (grado C, observacional)

Google publica que pasar de frase a amplia con puja inteligente da en torno a un 25% más de
conversiones con tCPA. Es dato de parte, sin contrafactual publicado.

Optmyzr publicó el 11-may-2026 un análisis de **30.000 cuentas** de Search (febrero de 2026),
separando marca de no-marca y ecommerce de captación de leads:

- La amplia ya es la concordancia con más gasto. La exacta ha perdido casi 10 puntos de cuota de
  gasto desde 2022.
- **En eficiencia gana la exacta**: mejor CPA, mejor ROAS y mejor tasa de conversión en no-marca.
- **En captación de leads domina la frase**, en gasto y en cuota de conversiones. La amplia "pierde
  pie" de forma más visible cuando no hay valor de conversión que guíe a la puja inteligente.
- En marca, la exacta gana casi todas las métricas.

Un estudio anterior de Optmyzr (nov-2024, 992.028 palabras clave en 15.491 cuentas) daba ROAS de
415% en exacta, 314% en frase y 278% en amplia, con la amplia a la cabeza solo en tasa de
conversión (8,52%).

- [Optmyzr, Broad Match is Winning the Budget War, 11-may-2026](https://www.optmyzr.com/blog/google-ads-match-type-performance/)
- [Optmyzr State of PPC](https://www.optmyzr.com/blog/optmyzr-state-of-ppc-study/)

Es observacional: las cuentas que usan exacta no son las mismas que usan amplia, y la exacta suele
cargar con los términos de más intención. Aun así, la dirección coincide entre estudios y
contradice el discurso de Google.

**Corrige al fichero [15](15-plataformas-mecanica-real.md)**, que da la frase "en retirada" con un
23% más de CPA. Con los datos de 2026 eso no se sostiene para captación de leads, que es justo el
negocio de Diego.

### Lo que sale para una cuenta de leads pequeña

1. **Exacta y frase primero**, sobre los términos de más intención.
2. **Amplia solo cuando haya señal de valor**: importación offline del lead cualificado o de la
   venta, con suficiente volumen. Sin eso, la amplia optimiza hacia el formulario más barato.
3. **Marca en exacta y en campaña propia.**

### Los términos que no ves (grado C)

Desde septiembre de 2020 el informe de términos de búsqueda solo enseña los que busca "un número
significativo" de usuarios. Seer Interactive midió sobre 30+ empresas que la parte oculta suponía
el **28% del presupuesto**. Muestra pequeña y de 2020, pero dice algo útil: en cuentas de cola
larga una parte grande del gasto no se puede revisar ni negativizar término a término.

PMax ya tiene informe de términos de búsqueda propio, con columna de origen.

- [Seer Interactive, 28% del presupuesto sin términos](https://www.seerinteractive.com/insights/google-ads-removes-search-terms-for-28-percent-of-paid-search-budgets)
- [Términos de búsqueda en PMax, `/answer/16327396`](https://support.google.com/google-ads/answer/16327396)

---

## 4. Puja inteligente: lo que pide de verdad (grado B, caduca: revisar trimestral)

| Qué | Dato | Fuente |
|---|---|---|
| tCPA sin histórico | Se puede arrancar sin conversiones previas. No hay umbral de entrada | [`/answer/6268632`](https://support.google.com/google-ads/answer/6268632) |
| tROAS en Search | 15 conversiones con valor en 30 días | [`/answer/6268637`](https://support.google.com/google-ads/answer/6268637) |
| Duración del aprendizaje | Hasta 3 semanas o 1-2 ciclos de conversión | [`/answer/13020501`](https://support.google.com/google-ads/answer/13020501) |
| Qué lo reinicia | Crear o reactivar la estrategia, cambiar su ajuste, añadir o quitar campañas, grupos o palabras clave | misma |
| Ajustes manuales bajo puja inteligente | Se ignoran los de ubicación, calendario, audiencias, llamadas y demografía. Con tCPA el de dispositivo modifica el objetivo, no la puja | [`/answer/2732132`](https://support.google.com/google-ads/answer/2732132) |
| Gasto diario | Puede llegar al doble del presupuesto diario medio, sin pasar del límite mensual | `/6268632` |
| Cambio del 17-ago-2026 | Las campañas **limitadas por presupuesto** con objetivo entregan más cerca del objetivo escrito. Con tCPA de 10 € y CPA real de 5 €, el real sube hacia 10 | [`/answer/17125145`](https://support.google.com/google-ads/answer/17125145) |
| Presupuesto sobre el objetivo | Demand Gen: al menos 10× el tCPA. Documentación de Scripts: más de 15× el CPA | `/answer/16797388` y [Scripts, Demand Gen](https://developers.google.com/google-ads/scripts/docs/campaigns/demand-gen/required-components) |

Verificado todo el 22-ago y el 6-sep-2026 en la skill google-ads-360.

El cambio del 17 de agosto merece una línea aparte: si tienes una campaña ahogada de presupuesto
con un tCPA generoso "para que no se frene", desde esa fecha Google gasta hasta tu objetivo. El
objetivo pasa a ser un precio, no un techo teórico. Se escribe el CPA que de verdad aguantas.

### Maximizar clics es una fase, no un destino

---

## 5. El presupuesto mínimo de aprendizaje en Google

La regla de la casa (fichero [08](08-reglas-de-criterio.md), regla 13) es **CPA × 50 ÷ 7** al día.
Viene de Meta, donde el umbral de 50 eventos en 7 días sí está en la documentación. **Google no
publica ningún presupuesto mínimo de aprendizaje.** Aplicar el ×50÷7 a Google es una convención
propia, no una regla de la plataforma. Lo digo así cuando lo uso.

Cómo lo leo en Google:

- **CPA × 50 ÷ 7 al día** es el presupuesto cómodo: el sistema tiene señal de sobra y la lectura
  semanal significa algo.
- **CPA × 30 al mes** es el suelo operativo: 30 conversiones en 30 días es la ventana que Google
  recomienda para evaluar tCPA, y el doble del umbral de tROAS. Por debajo, la puja inteligente
  trabaja casi a ciegas y ningún informe semanal dice nada.
- **Por debajo del suelo**: pocas palabras clave en exacta y frase, Maximizar conversiones sin
  objetivo o CPC manual, y lectura mensual. O no hacer Google.

### Por qué el suelo no es un capricho (grado A, aritmética)

Con n conversiones, el ruido relativo del recuento es aproximadamente 1/√n.

| Conversiones en el periodo | Ruido (±) | Qué se puede afirmar |
|---|---|---|
| 10 | ~32% | Nada. Ni una caída a la mitad es concluyente |
| 30 | ~18% | Solo cambios grandes |
| 50 | ~14% | Un cambio de un tercio |
| 100 | ~10% | Un cambio del 20-25% |

Una cuenta con 12 leads al mes no tiene lectura semanal. Se agrega a cuatro semanas y se dice.

### El coste que no sale en el panel (grado B la tarifa, A la aritmética)

Google añade un **3% de recargo por normativa** a lo servido en España desde el 1-jul-2024, en
factura y fuera de la columna Coste. El MER de equilibrio deja de ser 1 ÷ margen y pasa a
**1,03 ÷ margen**. Con margen del 30%, de 3,33 a 3,43.

- [Recargo por normativa, `/answer/9750227`](https://support.google.com/google-ads/answer/9750227), verificado 6-sep-2026

---

## 6. Búsqueda de marca: la versión completa del caso eBay (grado A)

El experimento de eBay (fichero [14](14-medicion-e-incrementalidad.md)) dice que la marca en
búsqueda no aporta casi nada. Es verdad **para eBay**. El trabajo que lo completa es de Simonov,
Nosko y Rao en *Marketing Science* (2018): experimentos aleatorizados en Bing con miles de marcas,
limitando al azar el número de anuncios por página.

- Sin competidores pujando por tu marca, tu anuncio de marca sube los clics totales a tu web un
  **2-3% de media**, más en marcas pequeñas y casi nada en las fuertes. El anuncio canibaliza cerca
  de la mitad de los clics que habrías tenido gratis en orgánico, así que el coste por clic
  **incremental** es más de diez veces el aparente.
- Si hay competidores y tú pujas, te quedas arriba y ellos solo roban un 1-5% de tus clics.
- Si hay competidores y tú **no** pujas, se llevan el **18-42% de los clics**. Un solo competidor
  en la primera posición capta el 15-20% de quien buscaba tu marca.

- [Simonov, Nosko y Rao (2018), Marketing Science 37(2)](https://pubsonline.informs.org/doi/10.1287/mksc.2017.1065) · [PDF](https://business.columbia.edu/sites/default/files-efs/pubfiles/26238/competition_crowdout.pdf)

**Regla:** la campaña de marca se defiende mirando las Estadísticas de subasta, no el ROAS. Si
nadie puja por tu marca, es gasto casi puro. Si alguien puja, es seguro barato. Y en marcas
pequeñas, que es todo lo que toca Diego, el efecto incremental es mayor que en eBay.

---

## 7. Microsoft Advertising: cuándo merece la pena (grado C la cuota, B la mecánica)

Bing tiene el **5,64%** de las búsquedas de escritorio en España en agosto de 2026, y Yahoo, que
sirve anuncios de Microsoft, otro 3,44%. En móvil es residual. StatCounter mide páginas vistas, no
búsquedas, así que es orden de magnitud.

- [StatCounter, buscadores en escritorio, España](https://gs.statcounter.com/search-engine-market-share/desktop/spain), consultado 24-sep-2026

Tiene sentido en B2B con comprador de oficina, **después** de que Google funcione, importando las
campañas. Conversiones offline con el MSCLKID: ventana de 90 días, esperar 2 horas tras crear el
objetivo, y Microsoft recomienda subir a diario porque la puja automática se resiente si no.

- [Microsoft Advertising, conversiones offline](https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_uetv2offlineconversion), actualizada 27-jul-2026

---

## 8. Scripts: para qué sirven en una cuenta pequeña (grado B, caduca: revisar trimestral)

Límites oficiales: 30 minutos por ejecución en cuenta de anunciante (lo hecho hasta el corte se
aplica), iteradores de 50.000 resultados por defecto, 50 cuentas en paralelo desde administradora.

- [Google Ads Scripts, límites](https://developers.google.com/google-ads/scripts/docs/limits)

Los tres que pagan su coste en cuentas de leads: **alerta de conversiones a cero** (la etiqueta se
cae cuando alguien republica la web, y pasó en ECSSTUDIO el 7-ago-2026), **ritmo de gasto** contra
el mes, y **n-gramas de términos de búsqueda** para sacar negativas. Código y GAQL en
`google-ads-360/referencias/15-gaql-scripts-y-automatizacion.md`.

---

## Banderas rojas

| Lo que se dice | Qué pasa |
|---|---|
| "Hay que subir el Quality Score" | No entra en la subasta. Mira qué componente falla y arregla eso |
| "El QS pesa 39/39/22" | Ingeniería inversa sin método publicado. Grado D |
| "La amplia con Smart Bidding siempre gana" | Dato de Google. En 30.000 cuentas la exacta gana en eficiencia y en leads domina la frase |
| "Ponemos tCPA alto para que no se frene" | Desde el 17-ago-2026 Google gasta hasta el objetivo si vas limitado de presupuesto |
| "Con 500 €/mes montamos Smart Bidding" | Calcula CPA × 30. Si no llega, no hay puja inteligente, hay ruido |
| "La marca tiene ROAS de 20" | Mira si alguien puja por ella. Sin competidores, es casi todo orgánico pagado |
| "Maximizar clics para arrancar y ya veremos" | Es una fase. Sin fecha de salida, trae clics baratos que no compran |
| "Google recomienda 50 conversiones a la semana" | No publica ese umbral. El 50 es de Meta |
