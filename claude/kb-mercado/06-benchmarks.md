# Benchmarks de embudo

Este es el fichero **menos fiable** de la base y hay que usarlo sabiéndolo.

Casi todas las cifras de conversión que circulan vienen de blogs de herramientas que se copian
entre sí, sin muestra publicada, sin mediana frente a media, sin decir de qué año son ni de qué
mercado. Muchas se citan en cadena hasta que nadie sabe el origen.

Regla de uso: **estas cifras sirven para detectar un número absurdo, no para poner un objetivo**.
Si un cliente convierte al 0,2% donde la horquilla dice 5-15%, hay algo roto. Si convierte al 4%,
no digo "estás por debajo de la media", digo "veamos tu propia serie".

---

## Landing y captación — grado C

| Métrica | Horquilla citada | Comentario |
|---|---|---|
| Mediana general de landing | ~6,6% | De un análisis de Q4 2024, muestra no publicada |
| Buen resultado (cuartil superior) | ≥10% | |
| Servicios profesionales / consultoría | 1,7–6% | Rango enorme según si compite por especialización o por precio |
| Generación de leads con consulta gratuita | 5–15% | La consulta gratis infla el número y baja la calidad |
| Registro a webinar (coaches) | 15–25% | Página de registro, no del total de tráfico |
| Aplicación a programa de ticket alto | 3–5% | |
| SaaS | ~3,8% | |

## Embudo de ticket alto (webinar/VSL → llamada → cierre) — grado C/D

Horquillas que circulan para coaching de 1.000 €+:

| Etapa | Mínimo viable | Bueno | Excelente |
|---|---|---|---|
| Registro a webinar/VSL | 20% | 35% | 50%+ |
| Asistencia | 30% | 45% | 60%+ |
| Envío de aplicación | 5% | 10% | 15%+ |
| Aplicación → asiste a llamada | 60% | 75% | 85%+ |
| Llamada → cierre | 15% | 25% | 40%+ |
| **Conversión total del embudo** | **0,3%** | **1%** | **2%+** |

Conversión de webinar de oferta 1.000 €+: 5–10%.

**Grado D en el detalle, C en la estructura.** Ninguna de estas tablas publica muestra. Lo que sí
es útil es la **estructura**: descomponer el embudo en esas seis etapas y medir cada una es lo que
permite saber dónde está el agujero. Una conversión total del 0,5% puede venir de un registro
malo o de un cierre malo, y son problemas opuestos.

El número que más se manipula es **llamada → cierre**, porque depende enteramente de a quién
dejaste pasar a la llamada. Un 40% de cierre con 5 llamadas al mes no es mejor que un 20% con 40.

---

## Lo que sí es fiable y hay que usar en su lugar

1. **La serie histórica del propio cliente.** Su mediana de los últimos 6 meses vale más que
   cualquier benchmark de sector.
2. **Test A/B con potencia suficiente.** Ojo: la mayoría de los tests que se corren en cuentas
   pequeñas no tienen muestra para detectar el efecto que buscan. Un test de 200 visitas no
   distingue 4% de 6%.
3. **Experimentos con grupo de control**, cuando se pueden hacer. Ver el problema de sesgo de
   selección en [03-persuasion-evidencia.md](03-persuasion-evidencia.md): sin control, el ROAS de
   plataforma no prueba causalidad.

## Fuentes de benchmark que sí tienen metodología

Cuando necesite una cifra defendible, ir a la fuente primaria, no a un blog:

- Informe de benchmarks de conversión de Unbounce (publica muestra y mediana por sector).
- Benchmarks de Google Ads de LOCALiQ / WordStream (muestra grande, dice el periodo).
- Datos propios de la plataforma (Meta, Google), sabiendo que son parte interesada.
- Ehrenberg-Bass y WARC para efectividad, no para conversión.

- [Recopilación de benchmarks por sector (usar con la cautela de arriba)](https://landerlab.io/blog/landing-page-conversion-rate)
- [Benchmarks de webinar por punto de precio](https://scaleforimpact.co/webinar-conversion-rate-benchmarks-what-to-expect-at-every-price-point/)
