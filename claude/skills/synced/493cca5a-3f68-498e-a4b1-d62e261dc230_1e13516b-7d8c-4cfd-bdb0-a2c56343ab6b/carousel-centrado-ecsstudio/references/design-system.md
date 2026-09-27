# Design System — Carrusel Centrado ECSSTUDIO

Sistema visual completo. CSS, funciones de slide y boilerplate HTML listo para usar.

---

## HTML Boilerplate completo

Copiar íntegro. Reemplazar `[SLIDES_JS]` con el array de funciones y `[TOTAL]` con el número total.

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Carrusel ECSSTUDIO</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{background:#f0efec;display:flex;flex-direction:column;align-items:center;min-height:100vh;font-family:'Montserrat',system-ui,sans-serif;padding:40px 20px;gap:24px;}
#frame{width:420px;height:540px;background:#fff;overflow:hidden;box-shadow:0 4px 32px rgba(0,0,0,.12);}
.slide{width:100%;height:100%;display:flex;flex-direction:column;}
.sh{display:flex;justify-content:space-between;align-items:center;padding:16px 24px 0;font-weight:900;font-size:10px;letter-spacing:.12em;color:#0d0d0d;flex-shrink:0;}
.sn{color:#bbb;font-weight:700;}
.sf{display:flex;justify-content:space-between;align-items:center;padding:0 24px 18px;flex-shrink:0;}
.hndl{display:flex;align-items:center;gap:7px;font-size:10px;color:#aaa;font-weight:700;}
.dot{width:9px;height:9px;background:#b03035;border-radius:50%;}
.pill{background:#0d0d0d;color:#fff;font-size:9px;font-weight:900;letter-spacing:.12em;padding:6px 14px;border-radius:20px;}
.sc{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 26px;}
.nav{display:flex;align-items:center;gap:20px;}
.nb{width:40px;height:40px;border-radius:50%;border:0.5px solid #ddd;background:#fff;color:#111;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;}
.nb:hover{background:#f0f0f0;}
.nb:disabled{opacity:.2;cursor:default;}
.nc{font-size:12px;color:#999;min-width:44px;text-align:center;font-weight:700;}
.hint{font-size:11px;color:#bbb;}
</style>
</head>
<body>
<div id="frame"></div>
<div class="nav">
  <button class="nb" id="pb" disabled>←</button>
  <span class="nc" id="nc">1 / [TOTAL]</span>
  <button class="nb" id="nb2">→</button>
</div>
<p class="hint">← → para navegar</p>
<script>
(function(){
const R='#b03035', B='#0d0d0d', G='#555', MUT='#aaa';
const F="'Montserrat',system-ui,sans-serif";
const TOTAL=[TOTAL];

function hdr(n){ return `<div class="sh"><span>DIEGO ÁLVAREZ</span>${n?`<span class="sn">${n}</span>`:''}</div>`; }
function ftr(d){ return `<div class="sf"><div class="hndl"><div class="dot"></div><span>@thediegoalvarez</span></div>${d?`<div class="pill">DESLIZA →</div>`:'<div></div>'}</div>`; }

[SLIDES_JS]

let cur=0;
const frame=document.getElementById('frame');
const nc=document.getElementById('nc');
const pb=document.getElementById('pb');
const nb2=document.getElementById('nb2');
function show(i){
  frame.innerHTML=slides[i]();
  nc.textContent=`${i+1} / ${slides.length}`;
  pb.disabled=i===0; nb2.disabled=i===slides.length-1;
}
pb.onclick=()=>{if(cur>0)show(--cur);};
nb2.onclick=()=>{if(cur<slides.length-1)show(++cur);};
document.addEventListener('keydown',e=>{
  if(e.key==='ArrowLeft'&&cur>0)show(--cur);
  if(e.key==='ArrowRight'&&cur<slides.length-1)show(++cur);
});
show(0);
})();
</script>
</body>
</html>
```

---

## Funciones de slide

### 1. portada_numero — Hook con cifra grande

Usar cuando el gancho es una cantidad, porcentaje o número impactante.

```javascript
function portada_numero(){
  return `<div class="slide" style="background:#fff;">
    ${hdr('')}
    <div class="sc" style="padding:0 28px;gap:0;justify-content:center;">

      <!-- CONTEXTO ARRIBA (muted, pequeño) -->
      <div style="font-family:${F};font-size:11px;font-weight:700;letter-spacing:.14em;color:${MUT};text-transform:uppercase;text-align:center;margin-bottom:8px;">
        [TEXTO CONTEXTO ARRIBA, EJ: SI NO USAS UN EMBUDO ORGÁNICO TIMELAPSE]
      </div>

      <!-- SEPARADOR -->
      <div style="width:32px;height:2px;background:#e0e0e0;margin:0 auto 10px;"></div>

      <!-- ACCIÓN / CONSECUENCIA -->
      <div style="font-family:${F};font-weight:900;font-size:20px;letter-spacing:-.01em;color:${B};text-align:center;line-height:1;margin-bottom:2px;">
        [ESTÁS PERDIENDO / DEJAS DE FACTURAR / SON]
      </div>

      <!-- NÚMERO — ancla visual, siempre rojo -->
      <div style="font-family:${F};font-weight:900;font-size:118px;line-height:.85;letter-spacing:-.04em;color:${R};text-align:center;">
        [50K / 3X / 90%]
      </div>

      <!-- UNIDAD / PERIODO -->
      <div style="font-family:${F};font-weight:900;font-size:32px;letter-spacing:-.015em;color:${B};text-align:center;line-height:1;margin-top:4px;">
        [AL MES. / AL AÑO. / MÁS.]
      </div>

      <!-- CALIFICADOR (opcional, en muted) -->
      <div style="font-family:${F};font-weight:900;font-size:14px;letter-spacing:.12em;color:${MUT};text-align:center;margin-top:8px;">
        [MÍNIMO. / EN MEDIA. / COMO MÍNIMO.]
      </div>

    </div>
    ${ftr(true)}
  </div>`;
}
```

**Guía de tamaño del número según longitud:**
| Chars | Font-size |
|---|---|
| 2-3 (50K, 3X) | 118px |
| 4 (100K, 50%) | 96px |
| 5+ | 76px |

---

### 2. portada_texto — Hook con texto impactante

Usar cuando el gancho es una frase, no un número.

```javascript
function portada_texto(){
  return `<div class="slide" style="background:#fff;">
    ${hdr('')}
    <div class="sc" style="padding:0 28px;gap:0;justify-content:center;">

      <!-- STICKER (opcional en portada_texto) -->
      <div style="font-size:56px;margin-bottom:14px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.12));">[EMOJI]</div>

      <!-- CONTEXTO PEQUEÑO (opcional) -->
      <div style="font-family:${F};font-size:11px;font-weight:700;letter-spacing:.14em;color:${MUT};text-align:center;margin-bottom:10px;">
        [TEXTO PEQUEÑO OPCIONAL]
      </div>

      <!-- TÍTULO PRINCIPAL -->
      <div style="font-family:${F};font-weight:900;letter-spacing:-.02em;line-height:.93;color:${B};text-align:center;font-size:[VER GUÍA]px;">
        [LÍNEA 1]<br>[LÍNEA 2]<br>
        <span style="color:${R};">[ÚLTIMA LÍNEA EN ROJO]</span>
      </div>

      <!-- SEPARADOR -->
      <div style="width:36px;height:2.5px;background:${R};margin:16px auto 14px;"></div>

      <!-- SUBTÍTULO (opcional, muted) -->
      <div style="font-family:${F};font-size:12px;font-weight:400;color:${MUT};line-height:1.6;text-align:center;">
        [Subtítulo de contexto breve.]
      </div>

    </div>
    ${ftr(true)}
  </div>`;
}
```

**Guía de font-size para portada_texto:**
| Chars en línea más larga | Font-size |
|---|---|
| ≤ 6 | 60px |
| 7-9 | 52px |
| 10-12 | 44px |
| 13-15 | 36px |
| 16+ | 30px |

---

### 3. step — Slide de contenido estándar

El tipo más frecuente. Un paso, un concepto, un hack.

```javascript
// num = número del slide (1, 2, 3...)
// totalContent = total de slides de contenido (no cuenta portada ni CTA)
// emoji = sticker representativo
// label = "PASO 01", "HACK 02", "EL PROBLEMA", etc.
// title = texto del título (puede incluir <span style="color:${R};">texto rojo</span>)
// titleSize = font-size del título en px (ver guía abajo)
// titleColor = color del título: B (negro) o R (rojo)
// body = HTML del cuerpo (máx 3 líneas de ~35 chars)

function step(num, totalContent, emoji, label, title, titleSize, titleColor, body){
  return `<div class="slide">
    ${hdr(`${String(num).padStart(2,'0')} / ${String(totalContent).padStart(2,'0')}`)}
    <div class="sc" style="gap:0;">

      <!-- STICKER -->
      <div style="font-size:52px;margin-bottom:10px;filter:drop-shadow(0 2px 6px rgba(0,0,0,.1));">${emoji}</div>

      <!-- LABEL -->
      <div style="font-family:${F};font-size:9px;font-weight:900;letter-spacing:.2em;color:${R};text-transform:uppercase;margin-bottom:8px;">${label}</div>

      <!-- TÍTULO -->
      <div style="font-family:${F};font-weight:900;font-size:${titleSize}px;line-height:.90;letter-spacing:-.025em;color:${titleColor};text-align:center;margin-bottom:14px;">${title}</div>

      <!-- SEPARADOR -->
      <div style="width:32px;height:2px;background:#e8e8e8;margin:0 auto 13px;"></div>

      <!-- CUERPO -->
      <div style="font-family:${F};font-size:12.5px;font-weight:400;color:${G};line-height:1.65;text-align:center;max-width:316px;">${body}</div>

    </div>
    ${ftr(true)}
  </div>`;
}
```

**Guía font-size para título de step:**
| Chars en línea más larga | Font-size |
|---|---|
| ≤ 5 | 60px |
| 6-8 | 52px |
| 9-10 | 44px |
| 11-13 | 36px |
| 14+ | 28px |

**Para título en rojo:** pasar `R` como titleColor.
**Para título mixto (negro + rojo):** pasar el HTML directamente en `title`:
```javascript
`TRIAL<br><span style="color:${R};">CAPTURA.</span>`
```

---

### 4. moraleja — Slide de conclusión / insight

Penúltimo slide. Mensaje contundente con acento rojo en la parte crítica.

```javascript
function moraleja(totalContent, emoji, label, titleHTML, body){
  return `<div class="slide">
    ${hdr(`${String(totalContent).padStart(2,'0')} / ${String(totalContent).padStart(2,'0')}`)}
    <div class="sc" style="gap:0;">

      <div style="font-size:52px;margin-bottom:10px;filter:drop-shadow(0 2px 6px rgba(0,0,0,.1));">${emoji}</div>
      <div style="font-family:${F};font-size:9px;font-weight:900;letter-spacing:.2em;color:${R};text-transform:uppercase;margin-bottom:10px;">${label}</div>

      <!-- TÍTULO MULTI-LÍNEA CON ACENTO ROJO -->
      <div style="font-family:${F};font-weight:900;font-size:36px;line-height:.93;letter-spacing:-.02em;color:${B};text-align:center;margin-bottom:14px;">
        ${titleHTML}
      </div>

      <div style="font-family:${F};font-size:12px;font-weight:400;color:${G};line-height:1.65;text-align:center;max-width:300px;">${body}</div>

    </div>
    ${ftr(true)}
  </div>`;
}
```

**Ejemplo de titleHTML con acento:**
```javascript
`SIN ESTO<br>CADA VÍDEO<br><span style="color:${R};">EMPIEZA<br>DESDE CERO.</span>`
```

---

### 5. cta — Último slide

Siempre el mismo patrón: COMENTA + KEYWORD en rojo + Y TE MANDO EL DOCUMENTO.

```javascript
// keyword: string en mayúsculas, ej: "EMBUDO", "SPRINT", "DIAGNÓSTICO"
function cta(emoji, keyword){
  // font-size keyword según longitud
  const kLen = keyword.length;
  const kSize = kLen <= 5 ? 80 : kLen <= 7 ? 68 : kLen <= 9 ? 58 : 46;

  return `<div class="slide">
    ${hdr('')}
    <div class="sc" style="gap:0;">

      <div style="font-size:52px;margin-bottom:14px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.12));">${emoji}</div>
      <div style="font-family:${F};font-weight:900;font-size:26px;letter-spacing:-.01em;color:${B};text-align:center;line-height:1;margin-bottom:4px;">COMENTA</div>
      <div style="font-family:${F};font-weight:900;font-size:${kSize}px;line-height:.82;letter-spacing:-.035em;color:${R};text-align:center;">${keyword}</div>
      <div style="font-family:${F};font-weight:900;font-size:22px;letter-spacing:-.01em;color:${B};text-align:center;line-height:1.2;margin-top:10px;">Y TE MANDO<br>EL DOCUMENTO.</div>

    </div>
    ${ftr(false)}
  </div>`;
}
```

**Tabla de keyword font-size:**
| Chars | Font-size | Ejemplo |
|---|---|---|
| ≤ 5 | 80px | GUION |
| 6-7 | 68px | EMBUDO, SPRINT |
| 8-9 | 58px | CONTROL |
| 10+ | 46px | DIAGNÓSTICO |

---

## Ejemplo completo — array slides

```javascript
const slides = [
  () => portada_numero(),   // Hook con cifra

  () => step(1, 6, '📡', 'PASO 01', 'TRIAL', 52, B,
    'Captura atención fría en masa.<br>15-30 segundos. Sin keyword.<br>Solo capta.'),

  () => step(2, 6, '🎬', 'PASO 02', 'REEL', 52, B,
    'Filtra al cliente ideal.<br>Hook específico. Keyword al final<br>que abre la conversación.'),

  () => step(3, 6, '🔁', 'PASO 03', 'STORY', 52, B,
    'Convierte confianza en acción.<br>5 historias en secuencia.<br>Problema → prueba → CTA.'),

  () => step(4, 6, '⚡', 'PASO 04', 'MANYCHAT', 44, B,
    'Cualifica sin que estés tú delante.<br>Keyword → recurso → pregunta<br>→ segmentación automática.'),

  () => step(5, 6, '🎯', 'PASO 05', 'RESERVA', 52, R,
    'El lead llega ya convencido.<br>No es tráfico frío. Es alguien<br>que ya recorrió todo el funnel.'),

  () => moraleja(6, '💡', 'LA DIFERENCIA',
    `SIN ESTO<br>CADA VÍDEO<br><span style="color:${R};">EMPIEZA<br>DESDE CERO.</span>`,
    'El contenido solo funciona cuando hay recorrido.<br>Sin embudo, publicas en el vacío.'),

  () => cta('💬', 'EMBUDO'),
];
```

---

## Ajustes frecuentes

**El título del step es muy largo y se corta:**
→ Reducir font-size 4-8px
→ O partir en más líneas con `<br>`

**El cuerpo no cabe en el slide:**
→ Reducir a 2 líneas. Si sigue sin caber, reducir `font-size` de 12.5px a 11px
→ Nunca sacrificar legibilidad por meter más texto

**El número de la portada_numero es muy pequeño:**
→ Aumentar font-size en +8px
→ Reducir el padding lateral de 28px a 22px

**Quiero título en negro con una palabra en rojo:**
→ Usar HTML en el parámetro title:
```javascript
`ESTO ES<br>LO QUE<br><span style="color:${R};">FALTA.</span>`
```

**Sticker se ve muy pequeño:**
→ Cambiar de 52px a 60px
→ No pasar de 64px o ocupa demasiado espacio vertical
