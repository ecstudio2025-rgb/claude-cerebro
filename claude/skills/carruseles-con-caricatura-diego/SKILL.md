---
name: carruseles-con-caricatura-diego
description: >-
  Genera carruseles de Instagram con Diego caricaturizado de protagonista sobre
  escenas ilustradas a pantalla completa. Cada slide es una escena que dibuja el
  mensaje (fondo incluido), con Diego grande, título enorme arriba y una palabra
  clave en rojo. Estilo negro/rojo/crema, layout fijo. Úsala cuando Diego pida
  "carruseles", "carrusel con mi caricatura", "carrusel caricatura Diego" o quiera
  convertir guiones/copys en carruseles ilustrados con su personaje. La cara sale
  siempre parecida porque se pasa su foto de referencia en cada generación.
---

# Carruseles con caricatura de Diego

Convierte copy (frases por slide) en carruseles ilustrados de Instagram 4:5.
Cada slide: **escena completa que ilustra la frase + Diego grande de protagonista
+ título arriba con una palabra en rojo**. Motor: Gemini image (`gemini-3-pro-image`)
para el dibujo, PIL para el texto (así el copy se corrige sin regenerar la imagen).

## El preset visual (lo que hace inconfundible al estilo)

- **Layout único** en todas las slides: fondo negro, escena a sangre que llena el
  marco, degradado oscuro arriba, título Montserrat Black enorme, una palabra clave
  en rojo #b03035.
- **Diego siempre presente y grande**, de pecho hacia arriba, en primer plano.
- **El fondo ilustra el mensaje**, no es plano: si la frase habla de comparar, hay
  una balanza; si habla de un dato, una escena que lo representa.
- **Paleta cerrada**: negro #141414, rojo carmín #b03035, crema #f2e8dc, grises.
  La piel va en tono carne (nunca roja).
- **Parecido**: se pasa `assets/diego-ref.png` como referencia en CADA llamada.
  Rasgos fijos: cara delgada, pómulos marcados, pelo oscuro rizado bajo gorra beige
  lisa, perilla fina, aros en las orejas, piercing en la nariz, collar de cuentas,
  camisa oscura con ribete rojo.
- **Formato**: 1080×1350. Tipografía Montserrat (Black para títulos).

## Cómo usarla

1. Escribe/consigue el copy por slide (frase corta + qué palabra va en rojo).
2. Para cada slide, redacta una **escena** que dibuje esa frase con Diego dentro
   (con props y fondo ambientado; nunca "Diego sobre negro liso").
3. Vuelca todo en un JSON con el formato de `carruseles.example.json`.
4. Genera:
   ```bash
   cd <carpeta-de-la-skill>
   python3 generar.py <mi-carruseles.json> <carpeta-salida>
   # o solo algunos:  python3 generar.py mi.json salida RITMO VENTA
   ```
5. Cada carrusel sale en `<salida>/<carpeta>/slide-01.png…`. Las slides ya hechas
   no se regeneran (borra el png para rehacer uno).

## Reglas de redacción de escenas (para que salgan bien)

- **Pide siempre una escena ambientada**, con fondo que ilustra: "detrás, a
  pantalla completa, …". No dejes a Diego flotando sobre negro.
- **Diego grande**: el preset ya lo fuerza; describe su pose/gesto y expresión.
- **Datos**: intégralos en la escena (una pantalla, dos paneles con flecha, lluvia
  de billetes) y además ponlos en el título; no pidas a Gemini que escriba números,
  los escribe mal — el texto lo pone PIL.
- **Una palabra roja por slide** como mucho (la clave o el dato).
- **Títulos**: 4–5 palabras/línea, máx 4 líneas. Si es muy largo pisa la escena.
- **CTA**: última slide con "Comenta KEYWORD" y la keyword en rojo.

## Config

- Clave Gemini: se lee de `~/.config/ecsstudio/gemini.env` (línea con `AIza…`).
- Referencia de cara: `assets/diego-ref.png`. Para cambiar el look base, sustituye
  esa foto por otra de frente con buena luz.
- Motor de layout y helpers: `compose.py` (funciones `hero_full`, `dato`,
  `antes_despues`, `cierre`, `_tok`, `gemini`).

## Otros layouts disponibles en compose.py

Aunque el estándar es `hero_full` (escena completa), el motor también trae:
- `dato(num, etiqueta, …)` — número gigante centrado (para prueba/estadística).
- `antes_despues(a,b,…)` — comparación con flecha roja (estilo dato-prueba).
- `cierre(texto, keyword, promesa, …)` — CTA con botón de keyword.

Se usan directamente desde Python si un carrusel pide una slide de dato puro.

## Notas

- Las cifras de ejemplo (500K, 25K, 40.000€…) son ilustrativas del concepto; si
  Diego da cifras reales, se cambian en el JSON (texto), sin regenerar imágenes.
- La skill NO escribe song lyrics ni texto en la imagen vía IA: el texto es siempre
  PIL, para control total y correcciones baratas.
- Copys base de referencia: el proyecto `carruseles-virales-master5` en
  Documents/Claude tiene 30 guiones (`MASTER-30-valor.md`) y su dirección visual.
