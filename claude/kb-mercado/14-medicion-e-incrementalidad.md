# Medición: atribución, incrementalidad y lo que de verdad se puede afirmar

El fichero que separa "esto correlaciona" de "esto lo causamos nosotros". Es la diferencia entre un
informe que aguanta que el cliente lo discuta y uno que no.

---

## Los tres métodos y para qué sirve cada uno

| Método | Qué responde | Qué NO responde |
|---|---|---|
| **Atribución** (MTA, último clic, plataforma) | Qué tocó el cliente antes de convertir | Si habría convertido igual |
| **MMM** (modelo de mezcla de medios) | Cómo repartir el presupuesto del trimestre | Qué anuncio pausar hoy |
| **Incrementalidad** (experimento) | **Si lo causamos nosotros** | Poco, pero cuesta y tarda |

La atribución es una herramienta táctica de dirección: te dice qué ajustar esta semana. El MMM es
la herramienta estratégica de asignación: te dice cómo repartir el trimestre, incluyendo canales
offline e imposibles de trackear. El experimento es el árbitro que prueba causalidad.

Tres de cada cuatro responsables de marketing dicen que su medición no les da ni velocidad ni
precisión ni confianza. Casi la mitad va a invertir más en MMM.

- [Árbol de decisión: incrementalidad, atribución o MMM](https://www.measured.com/faq/incrementality-attribution-mmm-decision-tree/)

## El experimento que todo el sector debería conocer — grado A

Blake, Nosko y Tadelis, **Econometrica** (2015). eBay apagó la publicidad de búsqueda de marca (las
consultas con la palabra "eBay") en Yahoo y Microsoft, manteniéndola en Google como control.

Resultado:

> **La publicidad de marca en búsqueda no tuvo beneficio medible a corto plazo.** Casi todo el
> tráfico de clic perdido y las ventas atribuidas los recogió la búsqueda orgánica. La sustitución
> entre pago y orgánico fue **casi completa**.

Y para palabras no-marca: los usuarios nuevos e infrecuentes sí se influyen, pero **los usuarios
frecuentes, cuya compra no depende del anuncio, se llevan la mayor parte del gasto**. El retorno
medio resultó negativo.

Esto es un experimento de campo a gran escala publicado en la mejor revista de economía. Es de lo
más sólido que existe en toda esta base, y contradice de frente lo que muestra cualquier panel de
plataforma.

- [Consumer Heterogeneity and Paid Search Effectiveness (NBER, PDF)](https://www.nber.org/system/files/working_papers/w20171/w20171.pdf)

## Retargeting: el caso más inflado — grado A en la dirección, C en la magnitud

El mismo mecanismo. El retargeting aparece justo antes de gente que iba a convertir de todas
formas, así que **captura demanda en vez de crearla**. Cuando se retiene el anuncio a un grupo de
control, buena parte de esos usuarios de alta intención convierte igual: vuelven directamente o
buscan la marca.

Los múltiplos que se citan (ROAS atribuido 8x contra incremental 2x, atribución de último clic
inflando 2-5x) son de proveedores de medición, así que grado C. La dirección viene de la misma
lógica de sesgo de selección de Lewis y Rao del fichero [03](03-persuasion-evidencia.md) y es
sólida.

**Regla:** ningún canal de retargeting se defiende con su ROAS. Se defiende con un holdout.

## Cómo se mide de verdad

**Geo lift.** Se apagan (o encienden) regiones y se comparan contra regiones control. No depende de
cookies y evita el sesgo de atribución. Necesita una ventana de **14 a 30+ días** y solo evalúa un
canal cada vez, así que se programa por rotación, no en continuo.

**Holdout de audiencia.** 80% expuesto, 20% retenido, 2 a 4 semanas. Lift incremental = (conversión
expuestos − conversión holdout) ÷ conversión holdout.

**Google Meridian GeoX** (mayo 2026): solución open source de geo-incrementalidad que se integra en
el MMM y permite experimentos agnósticos de publisher.

Los tests de geo también sirven para **validar el MMM**: cuando el MMM y la atribución cuentan
historias distintas sobre un canal, el experimento desempata.

- [Guía de incrementalidad con geo](https://lifesight.io/blog/geo-based-incrementality-testing/)

---

## Pérdida de señal: qué está roto y qué se recupera

### Consent Mode v2 y conversiones modeladas — grado C

- Google infiere conversiones de quien rechazó cookies analizando patrones de quien aceptó. El
  uplift reportado por el modelado suele ser del **15-25%**.
- El modelado **solo se activa por encima de umbrales**: en torno a 1.000 usuarios diarios con
  consentimiento concedido durante 7 de los últimos 28 días, y 1.000 eventos diarios con
  consentimiento denegado en el mismo periodo. **Por debajo, no se modela nada.**

Esto último es crítico para clientes pequeños, que es todo el ICP de Diego: **no llegan al umbral,
así que no tienen modelado y su pérdida de señal es real y completa**. Las cifras de recuperación
que venden las agencias no les aplican.

### CAPI y servidor — grado C

El servidor mejora la cobertura sin garantizarla: si la etiqueta del navegador nunca dispara (por
consentimiento denegado o bloqueador), el servidor no recibe nada. Lo que sí sube de forma medible
es la **calidad de emparejamiento de eventos** (EMQ) al pasar identificadores hasheados limpios
(email, teléfono) junto al ID de clic.

Ojo con el orden: implementar CAPI sin consentimiento válido no es una mejora técnica, es un
problema legal en la UE.

- [Meta y TikTok CAPI: guía de servidor 2026](https://www.digitalapplied.com/blog/meta-tiktok-conversions-api-capi-server-side-tracking-2026)

---

## Cómo reporto a un cliente

Esto es posición, no solo técnica. Y es diferenciación en un sector donde casi nadie lo hace.

1. **La cifra de plataforma, nombrada como lo que es.** "ROAS reportado por Meta: 4,2. Es
   atribución de la propia plataforma, incluye conversiones modeladas y por visualización, y no
   prueba causalidad."
2. **La cifra de negocio al lado.** Ingresos reales del CRM o de la contabilidad en el mismo
   periodo. MER. CAC de cliente nuevo.
3. **Lo que sí sabemos y lo que no.** Explícito. "Sabemos que el volumen de leads subió un X.
   No sabemos cuántos de esos habrían llegado igual sin campaña. Para saberlo hay que hacer un
   holdout, que cuesta esto y tarda esto."
4. **Una recomendación, no un menú.**

El intervalo de confianza mediano sobre el ROI publicitario en experimentos serios supera los 100
puntos porcentuales. Cualquiera que reporte un ROAS con dos decimales como si fuera verdad está
reportando precisión falsa.

## Banderas rojas de medición

| Lo que se ve | Lo que significa |
|---|---|
| Conversiones de plataforma > ventas reales | Solapamiento entre plataformas, modelado y view-through |
| Retargeting con el mejor ROAS de la cuenta | Casi seguro captura de demanda, no creación |
| Campaña de marca con ROAS altísimo | Canibalización del orgánico (eBay) |
| ROAS que sube justo cuando bajas presupuesto | Estás bajando por la curva, no mejorando |
| Cliente pequeño citando recuperación por modelado | No llega al umbral. No tiene modelado |
