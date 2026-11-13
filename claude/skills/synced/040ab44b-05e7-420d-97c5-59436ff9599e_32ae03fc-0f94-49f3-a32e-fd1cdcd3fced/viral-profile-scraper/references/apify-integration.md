# Integración con Apify — Actores, Datos y Troubleshooting

## Actores disponibles

### TikTok (principal)

**Actor:** `clockworks~free-tiktok-scraper`
**Coste:** Gratuito (no consume compute units, solo el actor en sí)
**Nota:** A pesar del nombre "free", en cuentas nuevas puede requerir créditos mínimos. Si da 402, probar con `clockworks~tiktok-scraper` (versión de pago).

**Input:**
```json
{
  "hashtags": ["#dependenciaemocional"],
  "resultsPerPage": 100,
  "maxResultsPerQuery": 100
}
```

**Nota:** El hashtag siempre con `#` al inicio.

**Output (campos clave):**

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | string | ID único del video |
| `text` | string | Caption del video |
| `createTime` | int | Timestamp Unix de publicación |
| `createTimeISO` | string | Fecha ISO del video |
| `textLanguage` | string | Idioma detectado por TikTok |
| `playCount` | int | Número de views |
| `diggCount` | int | Número de likes |
| `commentCount` | int | Número de comentarios |
| `shareCount` | int | Número de compartidos |
| `webVideoUrl` | string | URL del video en TikTok |
| `authorMeta.name` | string | Handle del creador |
| `authorMeta.nickName` | string | Nombre display del creador |
| `authorMeta.fans` | int | Seguidores del creador |
| `videoMeta.subtitleLinks` | array | Subtítulos ASR disponibles |

**Estructura de subtitleLinks:**
```json
[
  {
    "source": "ASR",
    "language": "spa-ES",
    "downloadLink": "https://v16m-webapp.tiktokcdn-us.com/..."
  }
]
```
`source` puede ser: `"ASR"` (automático, el mejor), `"LC"` (manual), `"MT"` (traducción automática)

**Los subtítulos son archivos WebVTT** servidos como `Content-Type: video/mp4` (engañoso). El contenido es texto plano con timestamps.

---

### Instagram (limitado)

**Actor:** `apify~instagram-scraper`
**Input para hashtag:**
```json
{
  "directUrls": ["https://www.instagram.com/explore/tags/hashtag/"],
  "resultsType": "posts",
  "resultsLimit": 100
}
```

**Limitaciones Instagram:**
- No tiene sistema de subtítulos accesible via API
- Consume más créditos que TikTok
- Rate limiting más agresivo
- Transcripciones no disponibles → solo caption

---

## API REST de Apify

**Base URL:** `https://api.apify.com/v2`

### Iniciar un run
```
POST /acts/{actorId}/runs?token={token}
Content-Type: application/json
Body: {input}
```
Devuelve `{ data: { id: "runId" } }`

### Consultar estado del run
```
GET /actor-runs/{runId}?token={token}
```
Devuelve `{ data: { status: "RUNNING" | "SUCCEEDED" | "FAILED" | "TIMED-OUT" | "ABORTED" } }`

### Obtener los items del dataset
```
GET /actor-runs/{runId}/dataset/items?token={token}&limit=500&clean=true
```
Devuelve un array de objetos.

### Consultar cuenta y créditos
```
GET /users/me?token={token}
```
Devuelve info de usuario, plan y uso mensual.

---

## Gestión de créditos

| Plan | Precio | Créditos/mes | Runs TikTok aprox. |
|---|---|---|---|
| Free | $0 | $5 equiv. | ~8–12 runs |
| Starter | $49/mes | $49 equiv. | ~80–120 runs |
| Scale | $499/mes | $499 equiv. | ~800–1200 runs |

**Para 4 mercados × 3 hashtags = 12 runs → consume el plan Free completo.**

Si da `402 Payment Required`:
1. Ir a console.apify.com
2. Settings → Billing → Add credits
3. O cambiar al plan Starter

---

## Retención de datos

Los datasets de Apify tienen retención limitada:
- **Plan Free:** ~7 días
- **Plan Starter:** 30 días
- **Plan Scale:** 90 días

**Implicación:** los datasets se pueden perder. El script descarga los datos inmediatamente al completarse cada run y los guarda en memoria/disco. No depender del re-fetch posterior.

---

## Errores comunes y soluciones

| Error HTTP | Mensaje | Causa | Solución |
|---|---|---|---|
| 401 | Unauthorized | Token inválido o expirado | Verificar token en console.apify.com |
| 402 | Payment Required | Sin créditos | Recargar cuenta |
| 404 | Not Found | Run ID incorrecto o expirado | Re-ejecutar el scraper |
| 429 | Too Many Requests | Rate limit de la API | Añadir delay entre requests |
| 500 | Internal Server Error | Error del actor de Apify | Reintentar. Si persiste, cambiar actor |

**Error: actor da 0 resultados**
Causas posibles:
- Hashtag muy pequeño en ese mercado (< 1K videos)
- El hashtag está banneado en ese mercado
- Problema temporal de TikTok
Solución: probar hashtags alternativos del mercado

**Error: subtítulos vacíos (no transcript)**
Causa: TikTok no procesó el video con ASR (puede ser música, sin habla, o video muy corto)
Solución: el script usa el caption como fallback automático

---

## Optimización de créditos

Para maximizar el valor de los créditos disponibles:

1. **Priorizar mercados**: empezar por el mercado principal del cliente
2. **Reducir hashtags**: 2 hashtags × mercado en vez de 5 ahorra 60% de créditos
3. **Reducir resultados**: 50 en vez de 100 por run si el nicho es pequeño
4. **Test primero**: correr 1 hashtag con 20 resultados antes del batch completo
5. **Reutilizar datos**: si se corrió hoy, no volver a correr los mismos hashtags mañana — los datos son válidos por días
