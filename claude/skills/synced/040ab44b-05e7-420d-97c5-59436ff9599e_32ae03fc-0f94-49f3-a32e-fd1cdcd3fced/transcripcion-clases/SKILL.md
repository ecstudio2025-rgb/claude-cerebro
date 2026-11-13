---
name: transcripcion-clases
description: Transcribe videos de clases o cursos locales en la Mac y genera resúmenes orientados a creación de guiones y contenido. Usá esta skill siempre que el usuario mencione transcribir clases, videos, cursos, lecciones, o quiera extraer información de archivos de video (.mp4, .mov). También activá esta skill si dice "transcribí los videos de X", "quiero el texto de las clases", "generá un resumen de los videos", "procesá los videos de la carpeta", "bajá los videos de Drive y transcribílos", o cualquier variación de convertir video en texto o resumen. Requiere Whisper y Ollama instalados en la Mac del usuario.
---

# Skill: Transcripción de Clases

Descarga videos desde Google Drive (carpeta compartida o propia) y los transcribe usando **Whisper** (gratis, local), generando resúmenes orientados a guiones con **Ollama/llama3.2** (gratis, local).

## Requisitos del sistema
- `ffmpeg` instalado (`brew install ffmpeg`)
- `openai-whisper` instalado (`pip3 install openai-whisper`)
- `gdown` instalado (`pip3 install gdown`)
- `ollama` corriendo con un modelo (`ollama serve`)
- `pip3 install ollama`

## Flujo de trabajo

### Paso 1 — Obtener información del usuario
Preguntá al usuario:
1. **URL de la carpeta de Google Drive** (formato: `https://drive.google.com/drive/folders/ID`)
2. **Modelo de Ollama disponible** (si no sabe, decirle que corra `ollama list`)
3. **Objetivo del resumen**: guiones, notas, ideas de contenido, o entrenamiento de IA

### Paso 2 — Generar el script Python
Usá el script base en `scripts/transcribir.py`.
Personalizá:
- `DRIVE_URL` con la URL que dio el usuario
- `MODELO_OLLAMA` con el modelo disponible
- `OBJETIVO` según lo que quiere hacer

El script:
1. Extrae el ID de la carpeta de la URL
2. Descarga los videos a `~/Downloads/nombre_carpeta/`
3. Transcribe cada video con Whisper
4. Genera el resumen con Ollama
5. Guarda `_transcripcion.txt` y `_resumen.txt` en la misma carpeta

### Paso 3 — Instrucciones de ejecución
Siempre indicá al usuario:
1. Abrir una Terminal y correr `ollama serve` (dejarla abierta)
2. En otra Terminal correr el script: `python3 ~/Desktop/transcribir_clases.py`

### Paso 4 — Output esperado
En `~/Downloads/nombre_carpeta/` se generan por cada video:
- `{nombre}_transcripcion.txt` — texto completo
- `{nombre}_resumen.txt` — resumen según el objetivo elegido

### Manejo de errores comunes

| Error | Solución |
|---|---|
| `whisper: command not found` | `echo 'export PATH="$HOME/Library/Python/3.13/bin:$PATH"' >> ~/.zprofile && source ~/.zprofile` |
| `ollama: connection refused` | Correr `ollama serve` en una Terminal aparte |
| `gdown: cannot retrieve` | La carpeta de Drive debe ser pública o compartida con acceso de lectura |
| `Permission denied` | La carpeta de Drive es privada, pedir acceso al dueño |

## Modos de resumen disponibles
- **guiones**: hooks, estructura gancho-desarrollo-CTA, frases de impacto
- **notas**: conceptos clave, definiciones, ejemplos
- **contenido**: ángulos de contenido, formatos sugeridos, ideas derivadas
- **entrenamiento**: estilo del speaker, patrones, vocabulario característico
