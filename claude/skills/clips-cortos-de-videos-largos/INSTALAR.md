# Instalar la skill «clips cortos de vídeos largos»

## 1. Copiar la carpeta

Descomprime y deja la carpeta entera aquí:

```
~/.claude/skills/clips-cortos-de-videos-largos/
```

Reinicia Claude Code y la skill aparece sola. Se invoca escribiendo
`/clips-cortos-de-videos-largos` o pidiéndolo con palabras («sácame clips de este directo»).

## 2. Lo que hace falta tener instalado

| qué | para qué | cómo |
|---|---|---|
| **ffmpeg** con drawtext | montar el clip y quemar el hook | `brew install ffmpeg` |
| **whisper.cpp** + modelo `ggml-small.bin` | transcribir y verificar los cortes | `brew install whisper-cpp` y bajar el modelo |
| **Montserrat** (Black, Bold, SemiBold) | la tipografía del hook | Google Fonts, instalar en el Mac |

Los scripts buscan los binarios en el PATH. Si los tienes en otro sitio:

```bash
export FFMPEG=/ruta/ffmpeg
export FFPROBE=/ruta/ffprobe
export WHISPER_CLI=/ruta/whisper-cli
export WHISPER_MODEL=/ruta/ggml-small.bin
```

Si las fuentes no están en `~/Library/Fonts`, pon `fonts_dir` en el spec.

## 3. Probar que va

Desde una carpeta de trabajo con el vídeo en `src/`:

```bash
python3 ~/.claude/skills/clips-cortos-de-videos-largos/scripts/preparar.py src/v1.mp4 v1
```

Tiene que dejar `audio/sil_v1.json`. Si además existe `transcripts/v1.json`, saca
también el fichero de bloques para leer y elegir los cortes.

## 4. Antes de tocar nada, dos avisos

- **La transcripción se hace en local**, nunca por API.
- **Los recortes por defecto** (`crop_slide`, `crop_cara`) son de una grabación de Zoom
  1280×720 con la diapo a la izquierda y la webcam en un PIP a la derecha. Si tu vídeo
  no es así, mira un frame primero y ajústalos en el spec.

El detalle del método y las trampas están en `SKILL.md`.
