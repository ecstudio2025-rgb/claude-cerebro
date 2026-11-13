---
name: markitdown
description: Convierte PDF, Word, Excel, PowerPoint, HTML, CSV, JSON, imágenes (OCR de metadatos), audio y vídeos de YouTube a Markdown con MarkItDown de Microsoft antes de leerlos. Úsala siempre que haya que leer o analizar un PDF o un documento de Office largo (contratos, briefings, propuestas, facturas, presentaciones de cliente, exportaciones): gasta muchos menos tokens que leer el fichero en bruto y las tablas salen bien.
---

# MarkItDown

Herramienta de Microsoft (microsoft/markitdown, MIT). Instalada en el Mac de Diego el 13-nov-2026 con `uv tool install 'markitdown[all]'`.

Si `markitdown` no existe en este equipo: `uv tool install 'markitdown[all]'` (sin uv: `pip install 'markitdown[all]'`).

## Uso

```bash
markitdown fichero.pdf -o fichero.md        # un fichero
markitdown presentacion.pptx > pres.md      # a salida estándar
for f in carpeta/*.pdf; do markitdown "$f" -o "${f%.pdf}.md"; done
```

Después lee el `.md`, no el original. Si es muy largo, búscalo con grep antes de leerlo entero.

Cuándo NO: PDFs escaneados sin capa de texto (sale vacío: usa OCR o la skill `pdf`), y cuando hay que conservar el maquetado exacto (firmar, rellenar formularios: skill `pdf` o `docx`).
