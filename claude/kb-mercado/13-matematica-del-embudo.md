# La matemática del embudo

Un embudo se diagnostica con números, no con opinión. Este fichero tiene las fórmulas que
importan, las trampas que hacen que una cuenta parezca sana cuando no lo está, y el orden en que
hay que mirar.

---

## Las cuatro cifras que mandan

| Métrica | Fórmula | Qué mide |
|---|---|---|
| **CAC** | Coste total de adquisición ÷ clientes nuevos | Cuánto cuesta entrar |
| **LTV** | Margen de contribución × vida del cliente | Cuánto deja |
| **Payback** | Meses hasta recuperar el CAC en caja | **Velocidad**, que es lo que mata negocios |
| **MER** | Ingresos totales ÷ gasto total de marketing | Si el motor entero es rentable |

**Ratio mide magnitud. Payback mide velocidad. Hay que llevar los dos.** Un 4:1 con 18 meses de
payback es buena economía a largo plazo y un problema de caja hoy. Un 2,5:1 con payback de 9 meses
y buena retención es mejor negocio que un 4:1 con payback de 36 meses.

## Las cuatro trampas — grado B

Salen una y otra vez en cuentas reales:

**1. El CAC de mentira.** El CAC real suele ser 2 o 3 veces el gasto en anuncios. El CAC completo
incluye sueldos, herramientas, agencias, producción de contenido y estructura. Quien solo mide
"CAC de performance" se está mintiendo.

**2. El promedio que tapa la cohorte.** Un LTV:CAC agregado de 3,2:1 puede esconder que la última
cohorte va por 1,8:1. La mayoría de las discusiones sobre CAC son sobre un número mezclado que
oculta el deterioro. **Siempre por cohorte de entrada.**

**3. El LTV fósil.** Calculado una vez, hace 18 meses, y arrastrado desde entonces.

**4. El ratio sin payback.** Ver arriba.

- [Referencia de unit economics 2026](https://www.digitalapplied.com/blog/saas-unit-economics-2026-cac-ltv-payback-reference)

## Punto de equilibrio del motor — grado A (es aritmética)

La fórmula más útil que existe para decidir si escalar o parar:

> **MER de equilibrio = 1 ÷ margen de contribución antes de marketing**

Un negocio con 45% de margen tiene un MER de equilibrio de **2,22**. Por debajo de eso, cada euro
extra de anuncios quema caja. Si además quieres un 20% de margen de contribución después de
marketing con un bruto del 55%, el objetivo de MER sube a ~1,57 como mínimo.

Esto se calcula en cinco minutos y cambia la conversación entera con un cliente. Deja de discutirse
si el ROAS "está bien" y pasa a discutirse si el negocio gana dinero.

## ROAS de plataforma contra MER — grado A

El ROAS que reporta la plataforma está **sistemáticamente inflado** desde iOS 14. Cuenta
conversiones por visualización, se solapa con el crédito de otras plataformas, incluye
conversiones modeladas y reporta **ingresos, no margen**. Todas las plataformas quieren atribuirse
todas las ventas.

El uso correcto de cada uno:

- **ROAS de plataforma** → decisiones tácticas dentro de una cuenta (qué anuncio pausar esta
  semana).
- **MER** → asignación de presupuesto entre canales.
- **CAC mezclado de cliente nuevo** → decisiones estratégicas y de escalado.
- **Margen de contribución después de marketing** → la única restricción que no se negocia.

Nunca los tres en el mismo gráfico sin decir qué es cada uno. Ver [14](14-medicion-e-incrementalidad.md).

---

## La curva de rendimientos decrecientes — grado A

La relación entre gasto y resultado **no es lineal**. Tiene tres tramos:

1. **Rendimientos crecientes** (gasto bajo): cada euro rinde más que el anterior. Estás llegando a
   la audiencia más receptiva.
2. **Tramo lineal**: subir presupuesto sube resultado en proporción.
3. **Rendimientos decrecientes**: el canal agotó su audiencia más barata y de más intención, y
   ahora puja por inventario progresivamente peor.

Se modela con función Hill o sigmoide, y es el output central de un MMM.

**Consecuencia operativa que casi nadie internaliza:** el CPA no sube porque "algo se rompió". Sube
porque estás más arriba en la curva. Duplicar presupuesto **nunca** duplica resultado, y el punto
donde deja de merecer la pena es calculable, no opinable.

Cuando un cliente pide "el doble de leads", la respuesta honesta no es sí o no. Es: en qué tramo de
la curva estamos y qué CPA sale al doble de gasto.

- [Curvas de saturación y decisiones de presupuesto](https://www.measured.com/faq/media-mix-modeling-diminishing-return-curves-mmm-budget-decision/)

## Embudos contra bucles — grado C (marco, no evidencia)

Brian Balfour (Reforge). Un embudo es lineal: metes más arriba, sacas más abajo, y para sacar más
hay que meter más. Un bucle es un sistema cerrado donde la salida se reinvierte en la entrada.

**Los embudos decaen. Los bucles componen.** El embudo tiene rendimientos decrecientes por
construcción (ver la curva de arriba). El bucle tiene rendimientos compuestos.

Tres bucles típicos:
- **Contenido**: creas contenido → posicionas → captas usuarios → que generan más contenido.
- **Viral**: usuario invita → el invitado se activa → invita a más.
- **De pago**: gastas → captas → retienes lo bastante para recuperar CAC → financias más gasto.

Es un marco, no un hallazgo con estudio detrás. Pero la aritmética que lo sostiene sí es real: el
bucle de pago solo compone si el payback es más corto que el ciclo de caja. Si tardas 9 meses en
recuperar el CAC y cobras mensual, el bucle no gira, lo financias tú.

- [Growth Loops are the New Funnels (Reforge)](https://www.reforge.com/blog/growth-loops)

---

## Retención: donde está el dinero de verdad

Bajar la fuga un 1% sube el LTV entre un 10% y un 15%. Es la palanca con más apalancamiento de
todas, y la que menos atención recibe porque no sale en el panel de anuncios.

Benchmarks de agencia, **grado C** (encuestas de sector, sin muestra publicada):

| | Churn anual | Permanencia media |
|---|---|---|
| Modelo de retainer | 18% | ~56 meses |
| Modelo por proyecto | 42% | ~24 meses |
| Híbrido | 28% | — |
| Agencias de 1-10 personas | 32% | — |
| Agencias de 51+ | 15% | — |

Retención media del sector en torno al 84% anual; las mejores pasan del 95%.

La lectura útil no son las cifras exactas, es la brecha: **el modelo de retainer retiene 2,3 veces
mejor que el de proyecto**, y las agencias pequeñas pierden el doble que las grandes. Eso último
suele ser dependencia de una sola persona y ausencia de proceso, no calidad del trabajo.

- [Churn medio en agencias de marketing](https://focus-digital.co/average-marketing-agency-churn/)

---

## Orden de diagnóstico

Cuando un embudo no funciona, mirar en este orden. Va de lo que más mueve a lo que menos, y no al
revés como suele hacerse:

1. **¿El negocio aguanta el CAC?** MER de equilibrio contra MER real. Si no aguanta, ninguna
   optimización de campaña lo arregla.
2. **¿Dónde está el agujero?** Descomponer el embudo por etapas y comparar cada una con su propia
   serie histórica, no con benchmarks de sector (ver [06](06-benchmarks.md)).
3. **¿Es el creativo?** 47% del efecto en ventas. Ver [16](16-creativo-como-motor.md).
4. **¿Es la oferta?** Ver [18](18-oferta-precio-y-escalado.md).
5. **¿Es la velocidad de respuesta?** Ver [17](17-conversion-y-captacion.md). Suele ser esto y
   nadie lo mira.
6. **¿Es la configuración de la cuenta?** El último sitio donde mirar, y el primero donde todo el
   mundo mira.
