# Design System — Carrusel ECSSTUDIO

Sistema visual completo para generar el HTML del carrusel. Contiene tokens de diseño, funciones de slide y el boilerplate completo.

---

## Tokens de diseño

```
Color fondo:       #ffffff (blanco puro)
Color principal:   #0d0d0d (negro marca)
Color acento:      #b03035 (rojo ECSSTUDIO)
Color cuerpo:      #555555 (gris medio)
Color muted:       #aaaaaa (gris claro — handle, numeración)

Fuente:            'Montserrat', system-ui, -apple-system, sans-serif
Peso títulos:      900 (black)
Peso cuerpo:       400 (regular)

Tamaño frame:      420px × 540px
Escala Playwright: 1080 / 420 = 2.571× (para PNG a 1080px)
Padding lateral:   24-26px cada lado
```

---

## Anatomía de cada slide

```
┌─────────────────────────────────┐  ← frame 420×540
│ DIEGO ÁLVAREZ          0X / 0Y │  ← header: 18px top, 26px lateral
│                                 │
│  [contenido principal]          │  ← sc (flex:1, padding 0 26px)
│                                 │
│ ● @thediegoalvarez  DESLIZA → │  ← footer: 0 26px 22px
└─────────────────────────────────┘
```

**Header:** siempre presente. `DIEGO ÁLVAREZ` izquierda en negro 900, 10px, tracking 0.12em. Numeración `0X / 0Y` derecha en #aaa, 10px.
En la portada: sin numeración a la derecha.

**Footer:** siempre presente. Punto rojo (9px) + `@thediegoalvarez` izquierda en #aaa. `DESLIZA →` en píldora negra derecha.
En el último slide (CTA): sin `DESLIZA →`.

---

## Template HTML completo

Copiar este boilerplate y reemplazar `[SLIDES_AQUÍ]` con el array de funciones de slide.

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Carrusel ECSSTUDIO</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;900&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{background:#f0efec;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;font-family:'Montserrat',system-ui,-apple-system,sans-serif;padding:40px 20px;gap:24px;}
#frame{width:420px;height:540px;background:#fff;overflow:hidden;position:relative;box-shadow:0 4px 32px rgba(0,0,0,.13);}
.slide{width:100%;height:100%;display:flex;flex-direction:column;}
.sh{display:flex;justify-content:space-between;align-items:center;padding:18px 26px 0;font-weight:900;font-size:10px;letter-spacing:.12em;color:#0d0d0d;}
.sh .sn{color:#bbb;font-weight:700;font-size:10px;}
.sc{flex:1;padding:0 26px;display:flex;flex-direction:column;justify-content:center;}
.sf{display:flex;justify-content:space-between;align-items:center;padding:0 26px 22px;}
.handle{display:flex;align-items:center;gap:7px;font-size:10px;color:#aaa;font-weight:700;letter-spacing:.03em;}
.dot{width:9px;height:9px;background:#b03035;border-radius:50%;}
.desliza{background:#0d0d0d;color:#fff;font-size:9px;font-weight:900;letter-spacing:.12em;padding:6px 14px;border-radius:20px;}
.nav{display:flex;align-items:center;gap:20px;}
.nb{width:40px;height:40px;border-radius:50%;border:0.5px solid #ccc;background:#fff;color:#111;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .15s;}
.nb:hover{background:#f4f4f4;}
.nb:disabled{opacity:.22;cursor:default;}
.nc{font-size:12px;color:#999;min-width:44px;text-align:center;font-weight:700;letter-spacing:.05em;}
.hint{font-size:11px;color:#bbb;font-weight:400;letter-spacing:.03em;}
</style>
</head>
<body>
<div id="frame"></div>
<div class="nav">
  <button class="nb" id="pb" disabled>←</button>
  <span class="nc" id="nc">1 / N</span>
  <button class="nb" id="nb2">→</button>
</div>
<p class="hint">← → para navegar entre slides</p>
<script>
(function(){
const R='#b03035',B='#0d0d0d',G='#555';
const F="'Montserrat',system-ui,-apple-system,sans-serif";
const TOTAL = N_SLIDES; /* reemplazar con número total de slides */

function hdr(num){
  return `<div class="sh"><span>DIEGO ÁLVAREZ</span>${num?`<span class="sn">${num}</span>`:''}</div>`;
}
function ftr(desliza){
  return `<div class="sf"><div class="handle"><div class="dot"></div><span>@thediegoalvarez</span></div>${desliza?`<div class="desliza">DESLIZA →</div>`:'<div></div>'}</div>`;
}

/* ── FUNCIONES DE SLIDE (ver abajo) ── */

const slides = [
  [SLIDES_AQUÍ]
];

let cur=0;
const frame=document.getElementById('frame');
const nc=document.getElementById('nc');
const pb=document.getElementById('pb');
const nb2=document.getElementById('nb2');
function show(i){
  frame.innerHTML=slides[i]();
  nc.textContent=`${i+1} / ${slides.length}`;
  pb.disabled=i===0;
  nb2.disabled=i===slides.length-1;
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

## Funciones de slide — copiar y adaptar

### portada(titleLines, accentLine)

```javascript
function portada(titleLines, accentLine){
  /* titleLines: array de strings, una por línea
     accentLine: string — la última línea en rojo */
  return `<div class="slide">
    ${hdr('')}
    <div class="sc" style="padding-top:8px;padding-bottom:8px;">
      <div style="font-family:${F};font-weight:900;font-size:54px;line-height:.90;letter-spacing:-.025em;color:${B};">
        ${titleLines.join('<br>')}${accentLine?`<br><span style="color:${R};">${accentLine}</span>`:''}
      </div>
    </div>
    ${ftr(true)}
  </div>`;
}
```

**Guía de font-size para portada según longitud de línea más larga:**

| Chars en línea más larga | Font-size |
|---|---|
| ≤ 6 | 72px |
| 7-9 | 60px |
| 10-12 | 52px |
| 13-15 | 44px |
| 16+ | 38px |

---

### contexto(slideNum, totalSlides, label, titleLines, bodyHTML)

```javascript
function contexto(slideNum, totalSlides, label, titleLines, bodyHTML){
  return `<div class="slide">
    ${hdr(`${String(slideNum).padStart(2,'0')} / ${String(totalSlides-1).padStart(2,'0')}`)}
    <div class="sc">
      <div style="font-family:${F};font-size:10px;font-weight:900;letter-spacing:.15em;color:${R};margin-bottom:16px;">${label}</div>
      <div style="font-family:${F};font-weight:900;font-size:52px;line-height:.90;letter-spacing:-.025em;color:${B};margin-bottom:20px;">
        ${titleLines.join('<br>')}
      </div>
      <div style="font-family:${F};font-size:13px;font-weight:400;color:${G};line-height:1.68;">${bodyHTML}</div>
    </div>
    ${ftr(true)}
  </div>`;
}
```

**Guía de font-size para título contexto:**

| Chars en línea más larga | Font-size |
|---|---|
| ≤ 6 | 60px |
| 7-10 | 50px |
| 11-14 | 42px |
| 15+ | 34px |

---

### hackSlide(slideNum, totalSlides, hackNum, titleLines, bodyHTML)

```javascript
function hackSlide(slideNum, totalSlides, hackNum, titleLines, bodyHTML){
  return `<div class="slide">
    ${hdr(`${String(slideNum).padStart(2,'0')} / ${String(totalSlides-1).padStart(2,'0')}`)}
    <div class="sc" style="justify-content:flex-start;padding-top:6px;">
      <div style="font-family:${F};font-weight:900;font-size:88px;line-height:.80;letter-spacing:-.035em;color:${R};margin-bottom:8px;">${hackNum}</div>
      <div style="font-family:${F};font-weight:900;font-size:29px;line-height:.96;letter-spacing:-.02em;color:${B};margin-bottom:16px;">${titleLines.join('<br>')}</div>
      <div style="font-family:${F};font-size:12.5px;font-weight:400;color:${G};line-height:1.70;">${bodyHTML}</div>
    </div>
    ${ftr(true)}
  </div>`;
}
```

**Regla de font-size para título hack:**

| Chars en línea más larga | Font-size |
|---|---|
| ≤ 8 | 34px |
| 9-12 | 29px |
| 13-16 | 24px |
| 17+ | 20px |

**Regla de font-size para número hack (hackNum):**
- Si hay 4+ líneas de título + cuerpo largo → reducir a 72px
- Si el cuerpo es muy largo → reducir número a 64px y título a 26px

---

### ctaSlide(totalSlides, keyword, postText)

```javascript
function ctaSlide(totalSlides, keyword, postText){
  /* keyword: string en mayúsculas ej: "GUION"
     postText: string ej: "Y TE MANDO EL DOCUMENTO." */
  
  /* font-size de la keyword según longitud */
  const kLen = keyword.length;
  const kSize = kLen <= 5 ? 104 : kLen <= 7 ? 88 : kLen <= 9 ? 72 : 60;
  
  return `<div class="slide">
    ${hdr(`${String(totalSlides-1).padStart(2,'0')} / ${String(totalSlides-1).padStart(2,'0')}`)}
    <div class="sc" style="justify-content:center;">
      <div style="font-family:${F};font-weight:900;font-size:30px;letter-spacing:-.015em;color:${B};line-height:1;">COMENTA</div>
      <div style="font-family:${F};font-weight:900;font-size:${kSize}px;line-height:.82;letter-spacing:-.035em;color:${R};">${keyword}</div>
      <div style="font-family:${F};font-weight:900;font-size:28px;letter-spacing:-.015em;color:${B};line-height:1.18;margin-top:10px;">${postText}</div>
    </div>
    ${ftr(false)}
  </div>`;
}
```

---

## Ejemplo de uso — array slides completo (8 slides)

```javascript
const slides = [
  () => portada(
    ['5 HACKS', 'PARA CAPTAR', 'CLIENTES EN', 'INSTAGRAM'],
    'SIN ADS.'
  ),
  () => contexto(1, 8, 'EL PROBLEMA',
    ['NO ES', 'PUBLICAR', 'POCO.'],
    'Muchos negocios tienen cuenta activa y buenos vídeos.<br><br>Pero no les llegan clientes.<br><br>Publicar no es captar. La diferencia está en la estructura.'
  ),
  () => hackSlide(2, 8, '01',
    ['ESCRIBE EL', 'BENEFICIO EN', 'PANTALLA DESDE', 'EL FRAME 0.'],
    'El primer fotograma. No en el segundo 2.<br><br>Cuando el texto aparece antes de que abras la boca, el ojo lo ve y la persona se queda.'
  ),
  /* ... más slides de hack ... */
  () => ctaSlide(8, 'GUION', 'Y TE MANDO EL DOCUMENTO.')
];
```

---

## Ajustes frecuentes

**El cuerpo de texto no cabe en el slide:**
→ Reducir `font-size` del cuerpo de 12.5px a 11.5px
→ Reducir `line-height` de 1.70 a 1.55
→ Recortar el copy hasta máx 45 palabras

**El número hack corta con el título:**
→ Reducir número de 88px a 72px
→ Añadir `margin-bottom:4px` al número

**La portada tiene texto muy corto (queda espacio vacío):**
→ Aumentar font-size en +8px
→ O añadir un subtítulo pequeño debajo en #aaa, 13px, font-weight 400

**La keyword del CTA es muy larga (> 9 chars):**
→ La función `ctaSlide` ya ajusta automáticamente
→ Si aún no cabe, usar `overflow:hidden` en el contenedor de la keyword
