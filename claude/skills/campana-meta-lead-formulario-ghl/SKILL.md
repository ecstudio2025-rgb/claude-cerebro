---
name: campana-meta-lead-formulario-ghl
description: Monta, prueba y revisa de principio a fin un embudo de captación por formulario para un cliente de servicios o formación con GoHighLevel y Meta Ads. El recorrido es anuncio, landing en GHL con formulario incrustado, evento Lead por la API de conversiones de GHL (servidor), aviso interno al cliente, oportunidad en el pipeline, secuencia de correos de nutrición, contacto manual o por WhatsApp y campaña de Meta optimizada a Cliente potencial. Incluye presupuesto, configuración de la campaña, pruebas de eventos con Test Events, búsqueda de errores, revisión psicológica de la oferta y entrega de instrucciones al cliente. Úsala cuando pidan «monta el embudo de formulario», «que les llamen ellos», «cambia el calendario por un formulario», «pasa a Lead», «monta la nutrición», «correos de seguimiento», «aviso a cliente cuando entra un lead», «revisa la campaña», «testea los eventos», «mira que no haya errores», «revisa la oferta», «activa la campaña» o «explícale el embudo al cliente». Para el embudo de llamada agendada (Schedule) usa campana-meta-schedule.
---

# Embudo de formulario con GHL y Meta (evento Lead por servidor)

```
Anuncio (Cliente potencial) → landing GHL (PageView) → formulario incrustado
   → página de gracias (PageView; botón WhatsApp = Contact)
   → servidor: flujo CAPI de GHL «Formulario enviado» → Lead a Meta
   → flujo de nutrición: oportunidad «Inscrita» → aviso interno → correos 1-4 (+ aviso final con fecha)
   → el cliente llama o escribe por WhatsApp → mueve etapas → «Reserva pagada» saca de la nutrición
```

Caso del que sale todo: Lucía García, curso de acrygel (14-nov-2026). Subcuenta GHL `vOXuP7SICDLsoNyQX6Km`, píxel `1497965162186833`, campaña `52655007867022`. Memoria: `lucia-campana-acrygel-nov2026.md`.

## Cuándo esta y no campana-meta-schedule

- Formulario y llama el cliente: cuando hay que maximizar volumen en poco tiempo, el cliente no puede atender un calendario fijo o trabaja con el móvil. Menos fricción, más volumen, menos intención (regla 19 de kb-mercado).
- Llamada agendada: cuando la agenda del cliente es estable y quieren menos leads y más cualificados. Ahí, `campana-meta-schedule`.
- Pasar de una a otra es reversible: el flujo CAPI se reutiliza cambiando disparador y evento.

## Cómo se usa

1. Sigue `playbook.md` fase a fase. Cada fase acaba en una puerta; si no se cumple, se para y se dice qué falta y quién lo hace.
2. Antes de tocar GHL o Meta, lee `references/ghl-trampas.md` y `references/meta-trampas.md`. Ahí está cada error que ya costó tiempo.
3. Pruebas: `references/pruebas-y-errores.md`. Nada se da por bueno sin el resultado esperado delante.
4. Textos: `references/copy-y-proceso-comercial.md` (correos, aviso, gracias, guion de llamada, objeciones, ráfaga de instrucciones al cliente). Se adaptan a la voz del cliente y pasan por `~/.claude/anti-patrones-ia-redaccion.md`.
5. Scripts:
   - `~/.claude/skills/campana-meta-schedule/scripts/verificar_pixel.py URL --pixel ID --espera PageView --prohibe Lead,Schedule,SubmitApplication` (qué dispara cada página).
   - `scripts/comprobar_landing.sh URL "texto1" "texto2"` (si lo publicado contiene lo que acabas de cambiar).
6. Al terminar: memoria del cliente con IDs (flujos, formulario, páginas, campaña), qué se probó y qué no.

## Reglas que no se saltan

- **Tokens, claves y contraseñas:** nunca los escribo. El token de la API de conversiones no se copia entre acciones de GHL: se reutiliza el flujo que ya lo tiene o lo pega Diego.
- **Compras y suscripciones** (WhatsApp de GHL, dominios, números): las hace Diego. El clasificador de permisos bloquea el clic de compra aunque Diego diga que sí.
- **Encender gasto:** solo con el sí de Diego y el presupuesto dicho. Cambios en campaña activa se publican con el botón Publicar, uno por tanda.
- **Nada al grupo del cliente** sin orden explícita («envíalo»). Los mensajes van primero a Diego en un bloque de código, en su voz.
- **Pruebas sin molestar al cliente:** durante una prueba real, el flujo de nutrición va en borrador para que no salga el aviso interno; después se republica.
- **Nunca prometer fechas nuestras ni dar más de lo pactado.** Las fechas del curso o servicio del cliente sí se dicen.
- **Precios intocables.** Si la oferta no convence, se toca el mensaje, la prueba o la urgencia real, no el precio.
- **Escasez solo si es verdad** (plazas reales, fecha real). Regla 5 de `~/.claude/kb-mercado/08-reglas-de-criterio.md`.
- Lo que no se ha podido probar se dice. En esta sesión quedó sin probar la entrega real de correos (pruebas con example.com).

## Ficheros

| Fichero | Para qué |
|---|---|
| `playbook.md` | Fases 0-11 con puertas |
| `references/ghl-trampas.md` | Errores reales de GHL y su arreglo |
| `references/meta-trampas.md` | Errores reales de Ads Manager y Events Manager |
| `references/pruebas-y-errores.md` | Checklist de pruebas y de configuración con resultados esperados |
| `references/copy-y-proceso-comercial.md` | Plantillas de textos y proceso de venta |
| `scripts/comprobar_landing.sh` | curl sin caché + conteo de textos |
