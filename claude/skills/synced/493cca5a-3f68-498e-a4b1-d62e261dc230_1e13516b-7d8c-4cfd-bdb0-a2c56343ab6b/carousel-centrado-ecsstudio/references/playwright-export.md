# Playwright Export — Carrusel Centrado ECSSTUDIO

Script Python para exportar cada slide del carrusel como PNG a 1080px.

---

## Script completo (pegar en bash_tool)

```bash
python3 << 'EOF'
from playwright.sync_api import sync_playwright
import time, os

# ── CONFIGURAR AQUÍ ─────────────────────────────────
HTML_FILE = "/mnt/user-data/outputs/carousel_[TEMA].html"
OUT_DIR   = "/mnt/user-data/outputs/carousel_[TEMA]_slides"
TOTAL     = [N]          # número total de slides
SCALE     = 1080 / 420   # siempre este valor para PNG a 1080px
WAIT      = 2.0          # esperar Google Fonts — aumentar a 3.5 si salen mal
# ────────────────────────────────────────────────────

os.makedirs(OUT_DIR, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 420, "height": 540},
        device_scale_factor=SCALE
    )
    page.goto(f"file://{HTML_FILE}", wait_until="networkidle")
    time.sleep(WAIT)

    for i in range(TOTAL):
        # Limpiar UI de navegación y sombra
        page.evaluate("""() => {
            document.body.style.cssText =
              'background:#fff;padding:0;margin:0;min-height:unset;gap:0;display:block;';
            ['nav','hint'].forEach(c => {
              const el = document.querySelector('.' + c);
              if (el) el.style.display = 'none';
            });
            const f = document.getElementById('frame');
            if (f) f.style.boxShadow = 'none';
        }""")

        out = f"{OUT_DIR}/slide_{i+1:02d}.png"
        page.locator("#frame").screenshot(path=out)
        print(f"  ✓ slide_{i+1:02d}.png")

        if i < TOTAL - 1:
            page.evaluate("""() => {
              const n = document.querySelector('.nav');
              if (n) n.style.display = 'flex';
            }""")
            page.locator("#nb2").click()
            time.sleep(0.3)

    browser.close()
    print(f"\n✓ {TOTAL} slides exportados en {OUT_DIR}")
EOF
```

---

## Verificar Playwright

```bash
python3 -c "from playwright.sync_api import sync_playwright; print('OK')"
```

---

## Troubleshooting

**Fuentes en fallback (no aparece Montserrat):**
→ Aumentar `WAIT` de 2.0 a 3.5

**Slide en blanco:**
→ El botón `#nb2` no reaccionó — aumentar el `time.sleep(0.3)` a `0.6`

**PNG con sombra alrededor:**
→ Verificar que el `evaluate` elimina el `boxShadow` del frame antes del screenshot

**Emojis no se renderizan:**
→ Normal en algunos entornos Linux. Instalar Noto Emoji o reemplazar emojis por SVG inline

---

## Naming convention

```
HTML:    /mnt/user-data/outputs/carousel_[tema].html
Slides:  /mnt/user-data/outputs/carousel_[tema]_slides/slide_01.png ... slide_0N.png
```
