---
name: viral-profile-scraper
description: >
  Rastrea y descarga guiones completos de videos virales de TikTok (1M+ vistas, últimos 90 días) en cualquier nicho y mercado, y los exporta como XLSX listo para análisis de contenido. Activar siempre que el usuario pida: "scrapea videos virales del sector X", "dame los guiones virales del nicho Y", "bájame los videos más vistos de la competencia", "analiza qué contenido funciona en el mercado Z", "quiero ver qué está viralizando en [nicho]", "extrae transcripciones de videos virales", o cualquier variación de inteligencia competitiva de contenido en redes sociales. Funciona con cualquier cliente y cualquier nicho — no requiere configuración previa ni información específica del cliente.
---

# Viral Profile Scraper — Inteligencia de Contenido para Cualquier Nicho

Skill para extraer guiones completos de videos virales (TikTok, extensible a Instagram) de cualquier nicho y mercado. Usa la API de Apify + el sistema ASR nativo de TikTok para obtener transcripciones reales sin necesitar Whisper local.

---

## Cuándo usar esta skill

Activar cuando el usuario quiera:
- Saber qué contenido viral está funcionando en su nicho
- Extraer guiones/transcripciones de videos con muchas vistas
- Hacer inteligencia competitiva de contenido
- Alimentar la metodología del Máster 5.0 con referencias virales reales
- Encontrar ideas para reframear en guiones propios

---

## Inputs que necesitas recopilar

| # | Input | Descripción | Default |
|---|---|---|---|
| 1 | **API token de Apify** | Token personal del usuario — **siempre preguntar, nunca asumir** | (obligatorio) |
| 2 | **Nicho del cliente** | Descripción breve del sector/tema | (obligatorio) |
| 3 | **Mercados a rastrear** | Lista de códigos: ES, EN, PT, RU, FR, DE… | ES + EN |
| 4 | **Umbral de vistas** | Mínimo de views para incluir un video | 1.000.000 |
| 5 | **Ventana temporal** | Días hacia atrás | 90 días |

**Opcional:** nombre del cliente (para nombrar el archivo de salida), idioma de salida para las traducciones (default: español).

---

## Proceso paso a paso

### Paso 0 — Solicitar el API token de Apify ⚠️ OBLIGATORIO EN CADA USO

**Esta es la primera acción siempre, sin excepción.**

Pedir el token al usuario con este mensaje exacto:

> *"Para ejecutar el scraper necesito tu API token de Apify. Lo encontrás en console.apify.com → Settings → Integrations → API token. Tiene el formato `apify_api_XXXX…`"*

**Reglas estrictas:**
- **Nunca usar un token que aparezca en el historial de conversación.** Los tokens son credenciales sensibles y pueden haber cambiado o sido revocados.
- **Nunca asumir que el token de una ejecución anterior sigue siendo válido.**
- **No continuar al Paso 1 hasta recibir el token en el mensaje actual.**
- Si el usuario dice "usa el mismo de antes" o "ya lo diste antes", responder: *"Por seguridad solicito el token de nuevo en cada ejecución. Por favor pegalo aquí."*

### Paso 1 — Generar hashtags por mercado

Para cada mercado solicitado, generar 3–5 hashtags relevantes al nicho del cliente. Seguir las plantillas de `references/hashtag-generation.md`. Mostrar los hashtags propuestos al usuario y esperar confirmación antes de continuar. El usuario puede modificarlos.

Los inputs de nicho, mercados, umbral y ventana temporal sí se pueden extraer del contexto si ya fueron mencionados en la conversación. **Solo el token se pide siempre de nuevo.**

**Reglas de generación de hashtags:**
- Sin tildes ni caracteres especiales (TikTok no los indexa bien)
- En el idioma del mercado correspondiente
- Mix de: keyword principal del nicho + problema/dolor del cliente ideal + término más amplio del sector
- 3 hashtags mínimo, 5 máximo por mercado

### Paso 2 — Confirmar hashtags y recopilar el resto de inputs

Confirmar con el usuario:
1. Los hashtags propuestos (puede añadir, quitar o modificar)
2. Nombre del cliente para el archivo de salida
3. Idioma de salida (default: español)

### Paso 3 — Crear el archivo de configuración

Crear un JSON con el esquema siguiente y guardarlo en `/home/claude/scrape_config.json`.

**Esquema del config:**

```json
{
  "apify_token": "apify_api_...",
  "client_name": "Nombre del cliente",
  "client_niche": "Descripción del nicho",
  "output_language": "es",
  "output_path": "/mnt/user-data/outputs/",
  "min_views": 1000000,
  "fallback_views": 500000,
  "date_range_days": 90,
  "results_per_hashtag": 100,
  "markets": [
    {
      "id": "ES",
      "name": "Español",
      "flag": "🇪🇸",
      "lang_code": "es",
      "color": "20C4B8",
      "hashtags": ["hashtag1", "hashtag2", "hashtag3"]
    }
  ]
}
```

**Colores sugeridos por mercado:**
- ES `20C4B8` · EN `4ECB71` · PT `F4A261` · RU `E05A5A` · FR `7B61FF` · DE `64B5F6` · IT `FF7043` · Otros `9E9E9E`

### Paso 4 — Ejecutar el scraper

```bash
cd /home/claude
pip install openai-whisper deep-translator openpyxl langdetect requests --break-system-packages -q
python3 /home/claude/viral-profile-scraper/scripts/viral_scraper.py --config /home/claude/scrape_config.json
```

El script imprime progreso en tiempo real. Tiempo estimado: 2–5 minutos por mercado (depende del número de hashtags y créditos Apify disponibles).

### Paso 5 — Presentar el archivo

Cuando el script termine, llamar a `present_files` con la ruta del XLSX generado.

---

## Output: estructura del XLSX

El XLSX tiene 4 hojas:

| Hoja | Contenido |
|---|---|
| **Guiones Virales** | Tabla completa: mercado, handle, seguidores, views, likes, fecha, idioma original, caption, guion original, guion en español, URL |
| **Ganchos** | Solo la primera frase de cada guion — para extraer patrones de hook |
| **Dashboard** | KPIs + top 10 por views con primera frase |
| **Metodología** | Parámetros del scraping, nota sobre créditos, hashtags usados |

---

## Manejo de errores comunes

| Error | Causa | Solución |
|---|---|---|
| `402 Payment Required` | Sin créditos Apify | Recargar cuenta en console.apify.com. Plan Free = $5/mes |
| `0 items returned` | Hashtag sin resultados | Cambiar hashtags por términos más populares |
| `No videos with X+ views` | Umbral muy alto para el nicho | El script activa fallback automático a `fallback_views` |
| Transcripciones vacías | Video sin subtítulos ASR | Se usa el caption como fallback |
| Error de traducción | Rate limit de GoogleTranslator | El script reintenta con delay. Si falla, mantiene el original |

---

## Limitaciones conocidas

- **Solo TikTok**: Instagram requiere créditos adicionales y tiene protecciones anti-scraping más agresivas.
- **Créditos Apify**: El plan Free ($5/mes) permite ~8–12 runs del scraper gratuito de TikTok. Para 4 mercados × 3 hashtags = 12 runs → consume el plan mensual completo. Plan Starter ($49/mes) recomendado para uso regular.
- **Transcripciones ASR**: Solo disponibles para videos que TikTok procesó con su sistema automático (≈70% de los videos virales). Los demás usan el caption como fallback.
- **Videos de más de 6 meses**: TikTok puede haber eliminado las URLs de subtítulos. Filtro de fecha es importante.

---

## Referencias bundled

- `references/hashtag-generation.md` — Plantillas de hashtags para 20+ nichos comunes. **Leer siempre en el Paso 1.**
- `references/apify-integration.md` — Documentación de actores, esquema de respuesta, troubleshooting. Leer si hay errores o para entender los datos.
- `scripts/viral_scraper.py` — Script Python completo, niche-agnostic. Leer si necesitas modificar el comportamiento.
- `scripts/requirements.txt` — Dependencias Python.
