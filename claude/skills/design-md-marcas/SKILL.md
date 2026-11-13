---
name: design-md-marcas
description: Biblioteca de 84 DESIGN.md (sistemas de diseño destilados de Apple, Stripe, Linear, Notion, Airbnb, Tesla, Vercel, Revolut, Nike, Spotify, Uber, Supabase, Shopify y otras) para que una web, landing, demo o panel salga con un lenguaje visual coherente y no con pinta de "hecho con IA". Úsala cuando haya que diseñar o rediseñar la interfaz de una demo de Custom Soft Lab, una landing de ECSSTUDIO o de un cliente, y el usuario diga «que parezca de Apple/Stripe/Linear», «más premium», «más limpio», o no haya marca definida y haga falta una base seria.
---

# DESIGN.md de marcas

Origen: VoltAgent/awesome-design-md (MIT), copiado el 13-nov-2026. Cada fichero de `marcas/` es el DESIGN.md de una marca: colores con tokens, tipografía, espaciado, radios, sombras, componentes y reglas de uso.

## Cómo usarla

1. Elige la referencia según el cliente, no por moda:
   - Software de gestión, ERP, CRM, paneles (Custom Soft Lab): `linear.app`, `notion`, `stripe`, `supabase`, `sentry`, `posthog`, `airtable`, `sap`.
   - Servicios profesionales y agencia (ECSSTUDIO, landings de captación): `stripe`, `apple`, `framer`, `webflow`, `superhuman`, `mercury`.
   - Consumo, retail, restauración, estética: `airbnb`, `nike`, `starbucks`, `spotify`, `shopify`, `pinterest`.
   - Automoción, lujo, alto ticket: `tesla`, `bmw`, `ferrari`, `lamborghini`, `bugatti`, `apple`.
   - Finanzas y trading: `revolut`, `stripe`, `mercury`, `coinbase`, `kraken`.
2. Lee el fichero entero antes de escribir CSS. Copia los tokens tal cual a variables (`:root { --color-... }`).
3. Si el cliente tiene marca propia (logo, colores), quédate con la estructura de la referencia (escala tipográfica, espaciado, componentes) y sustituye solo la paleta y la tipografía de marca.
4. Para el acabado, combina con `apple-design` (interacción y movimiento), `web-design-guidelines` (Vercel) e `impeccable`.

No copies logotipos, nombres ni textos de la marca de referencia: solo el sistema visual. Una demo para un cliente nunca debe parecer una web de Stripe con otro nombre.

Lista completa: `ls ~/.claude/skills/design-md-marcas/marcas/`.
