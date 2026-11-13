# Playwright Export — Carrusel ECSSTUDIO

Script Python para exportar cada slide del carrusel como PNG a 1080px de ancho.
Requiere Playwright instalado (`pip install playwright --break-system-packages && playwright install chromium`).

---

## Script completo de exportación

Copiar este script, ajustar las variables en la sección `CONFIGURACIÓN` y ejecutar.

```python
from playwright.sync_api import sync_playwright
import time, os

# ── CONFIGURACIÓN ──────────────────────────────────────────
HTML_FILE  = "/mnt/user-data/outputs/carousel_CONCEPTO.html"   # ruta al HTML generado
OUT_DIR    = "/mnt/user-data/outputs/carousel_slides"           # carpeta de salida
TOTAL      = 8          # número total de slides
FRAME_W    = 420        # ancho del frame en CSS px (no cambiar)
FRAME_H    = 540        # alto del frame en CSS px (no cambiar)
TARGET_W   = 1080       # ancho del PNG de salida en px
SCALE      = TARGET_W / FRAME_W   # = 2.571...
WAIT_FONTS = 2.0        # segundos de espera para carga de fuentes
WAIT_NAV   = 0.3        # segundos de espera tras cambiar slide
# ──────────────────────────────────────────────────────────

os.makedirs(OUT_DIR, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": FRAME_W, "height": FRAME_H},
        device_scale_factor=SCALE
    )

    page.goto(f"file://{HTML_FILE}", wait_until="networkidle")
    time.sleep(WAIT_FONTS)

    for i in range(TOTAL):
        # Ocultar UI de navegación, quitar sombra y ajustar body para flush con el frame
        page.evaluate("""() => {
            document.body.style.background  = '#ffffff';
            document.body.style.padding     = '0';
            document.body.style.margin      = '0';
            document.body.style.minHeight   = 'unset';
            document.body.style.gap         = '0';
            document.body.style.display     = 'block';
            const nav  = document.querySelector('.nav');
            const hint = document.querySelector('.hint');
            if (nav)  nav.style.display  = 'none';
            if (hint) hint.style.display = 'none';
            const frame = document.getElementById('frame');
            if (frame) frame.style.boxShadow = 'none';
        }""")

        frame = page.locator("#frame")
        out_path = os.path.join(OUT_DIR, f"slide_{i+1:02d}.png")
        frame.screenshot(path=out_path)
        print(f"  ✓ slide_{i+1:02d}.png guardado")

        # Avanzar al siguiente slide si no es el último
        if i < TOTAL - 1:
            page.evaluate("""() => {
                const nav = document.querySelector('.nav');
                if (nav) nav.style.display = 'flex';
            }""")
            page.locator("#nb2").click()
            time.sleep(WAIT_NAV)
            page.evaluate("""() => {
                const nav = document.querySelector('.nav');
                if (nav) nav.style.display = 'none';
            }""")

    browser.close()
    print(f"\nExportación completa: {TOTAL} slides en {OUT_DIR}")
```

---

## Cómo ejecutarlo desde bash_tool

```python
# En bash_tool, ejecutar directamente:
exec(open('/tmp/export_carousel.py').read())

# O inline completo:
import subprocess
subprocess.run(['python3', '/tmp/export_carousel.py'])
```

O pegar el script directamente en un bloque de Python dentro de `bash_tool`:

```bash
python3 << 'EOF'
from playwright.sync_api import sync_playwright
import time, os

HTML_FILE = "/mnt/user-data/outputs/carousel_CONCEPTO.html"
OUT_DIR   = "/mnt/user-data/outputs/carousel_slides"
TOTAL     = 8
SCALE     = 1080 / 420

os.makedirs(OUT_DIR, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 420, "height": 540},
        device_scale_factor=SCALE
    )
    page.goto(f"file://{HTML_FILE}", wait_until="networkidle")
    time.sleep(2.0)

    for i in range(TOTAL):
        page.evaluate("""() => {
            document.body.style.cssText = 'background:#fff;padding:0;margin:0;min-height:unset;gap:0;display:block;';
            ['nav','hint'].forEach(c => { const el = document.querySelector('.'+c); if(el) el.style.display='none'; });
            const f = document.getElementById('frame'); if(f) f.style.boxShadow='none';
        }""")
        page.locator("#frame").screenshot(path=f"{OUT_DIR}/slide_{i+1:02d}.png")
        print(f"  ✓ slide_{i+1:02d}.png")
        if i < TOTAL - 1:
            page.evaluate("() => { const n=document.querySelector('.nav'); if(n) n.style.display='flex'; }")
            page.locator("#nb2").click()
            time.sleep(0.3)

    browser.close()
    print("Done.")
EOF
```

---

## Verificar Playwright disponible

```python
python3 -c "from playwright.sync_api import sync_playwright; print('Playwright OK')"
```

Si falla:
```bash
pip install playwright --break-system-packages
playwright install chromium
```

---

## Convención de nombres de output

| Variable | Patrón | Ejemplo |
|---|---|---|
| HTML | `carousel_[concepto].html` | `carousel_5hacks_instagram.html` |
| Carpeta PNGs | `carousel_slides/` | `carousel_slides/` |
| Slides | `slide_01.png` … `slide_0N.png` | `slide_01.png` … `slide_08.png` |

Si se generan múltiples carruseles en la misma sesión, usar subcarpetas:
`/mnt/user-data/outputs/carousel_slides_5hacks/`
`/mnt/user-data/outputs/carousel_slides_errores/`

---

## Tamaños de salida

| Config | Ancho CSS | Scale | PNG output |
|---|---|---|---|
| **Estándar (default)** | 420px | ×2.571 | 1080px |
| Alta resolución | 420px | ×3.333 | 1400px |
| Vista previa rápida | 420px | ×1.0 | 420px |

Para Instagram, usar siempre **1080px** (estándar).

---

## Troubleshooting

**El texto sale borroso:**
→ Verificar que `device_scale_factor = 1080 / 420` (no redondeado)

**Las fuentes no cargan (texto en fallback):**
→ Aumentar `WAIT_FONTS` de 2.0 a 3.5
→ Verificar que el HTML apunta a `fonts.googleapis.com` y tiene conexión

**El slide N sale en blanco:**
→ El botón `#nb2` no responde — aumentar `WAIT_NAV` de 0.3 a 0.6
→ Verificar que `TOTAL` coincide con el número real de slides en el HTML

**El frame sale con sombra en el PNG:**
→ Verificar que el `evaluate` borra el `boxShadow` antes del screenshot

**Error `Element not found: #nb2`:**
→ El selector puede haber cambiado — verificar que el HTML usa `id="nb2"` para el botón siguiente
