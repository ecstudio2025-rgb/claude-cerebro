#!/usr/bin/env python3
"""
Script generado por la skill transcripcion-clases.
Descarga videos de Google Drive y los transcribe con Whisper + Ollama.
"""

import os
import re
import subprocess
import glob
import ollama
import gdown

# ─── CONFIGURACIÓN ────────────────────────────────────────────────
DRIVE_URL      = "PEGAR_URL_DE_DRIVE_AQUI"
MODELO_OLLAMA  = "llama3.2"
EXTENSION      = "mp4"
OBJETIVO       = "guiones"   # guiones | notas | contenido | entrenamiento
# ──────────────────────────────────────────────────────────────────

PROMPTS = {
    "guiones": """Sos un experto en creación de contenido y guiones para redes sociales.

Analizá esta transcripción de "{nombre}" y generá:

1. RESUMEN GENERAL (3-5 oraciones)
2. IDEAS CLAVE PARA GUIONES (5-10 puntos): conceptos poderosos, frases impactantes
3. HOOKS POTENCIALES (3-5 opciones): frases de apertura que generen curiosidad
4. ESTRUCTURA DE GUIÓN SUGERIDA: gancho → desarrollo → CTA
5. PALABRAS Y FRASES CLAVE del tema

Respondé en español.""",

    "notas": """Analizá esta transcripción de "{nombre}" y generá notas de estudio:

1. CONCEPTOS PRINCIPALES
2. DEFINICIONES IMPORTANTES
3. EJEMPLOS MENCIONADOS
4. PUNTOS CLAVE A RECORDAR

Respondé en español.""",

    "contenido": """Sos un estratega de contenido. Analizá "{nombre}" y generá:

1. RESUMEN DEL TEMA
2. ÁNGULOS DE CONTENIDO DERIVADOS (5-8 ideas de videos/posts)
3. FORMATOS SUGERIDOS (reel, carrusel, hilo, etc.)
4. PREGUNTAS QUE GENERA EL CONTENIDO (para engagement)

Respondé en español.""",

    "entrenamiento": """Analizá esta transcripción de "{nombre}" para entrenar una IA con el estilo del speaker.

1. ESTILO DE COMUNICACIÓN: cómo habla, qué frases usa
2. PATRONES RECURRENTES: estructuras que repite
3. VOCABULARIO CARACTERÍSTICO: palabras y expresiones propias
4. EJEMPLOS LIMPIOS: fragmentos representativos (5-10)

Respondé en español."""
}


def extraer_id_carpeta(url):
    """Extrae el ID de carpeta de una URL de Google Drive."""
    match = re.search(r"/folders/([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    raise ValueError(f"No se pudo extraer el ID de la URL: {url}")


def descargar_carpeta(drive_url, destino):
    """Descarga una carpeta de Google Drive con gdown."""
    print(f"  ☁️  Descargando desde Google Drive...")
    folder_id = extraer_id_carpeta(drive_url)
    gdown.download_folder(
        id=folder_id,
        output=destino,
        quiet=False,
        use_cookies=False
    )


def extraer_audio(video_path, audio_path):
    print(f"  🎵 Extrayendo audio...")
    subprocess.run([
        "ffmpeg", "-i", video_path,
        "-vn", "-acodec", "pcm_s16le",
        "-ar", "16000", "-ac", "1",
        audio_path, "-y", "-loglevel", "error"
    ], check=True)


def transcribir_audio(audio_path):
    print(f"  📝 Transcribiendo...")
    subprocess.run([
        "whisper", audio_path,
        "--language", "Spanish",
        "--model", "small",
        "--output_format", "txt",
        "--output_dir", os.path.dirname(audio_path)
    ], capture_output=True, text=True)

    txt_path = audio_path.replace(".wav", ".txt")
    if os.path.exists(txt_path):
        with open(txt_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def generar_resumen(transcripcion, nombre):
    print(f"  🤖 Generando resumen ({OBJETIVO})...")
    prompt_template = PROMPTS.get(OBJETIVO, PROMPTS["guiones"])
    prompt = prompt_template.replace("{nombre}", nombre)
    prompt += f"\n\nTRANSCRIPCIÓN:\n{transcripcion[:6000]}"

    response = ollama.chat(
        model=MODELO_OLLAMA,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


def procesar_video(video_path):
    nombre = os.path.splitext(os.path.basename(video_path))[0]
    carpeta = os.path.dirname(video_path)

    print(f"\n{'='*50}")
    print(f"📹 {nombre}")
    print(f"{'='*50}")

    audio_path         = os.path.join(carpeta, f"{nombre}_audio.wav")
    transcripcion_path = os.path.join(carpeta, f"{nombre}_transcripcion.txt")
    resumen_path       = os.path.join(carpeta, f"{nombre}_resumen.txt")

    if os.path.exists(transcripcion_path):
        print(f"  ⏭️  Transcripción ya existe, reutilizando...")
        with open(transcripcion_path, "r", encoding="utf-8") as f:
            transcripcion = f.read()
    else:
        extraer_audio(video_path, audio_path)
        transcripcion = transcribir_audio(audio_path)
        with open(transcripcion_path, "w", encoding="utf-8") as f:
            f.write(transcripcion)
        print(f"  ✅ Transcripción guardada")
        if os.path.exists(audio_path):
            os.remove(audio_path)

    if transcripcion.strip():
        resumen = generar_resumen(transcripcion, nombre)
        with open(resumen_path, "w", encoding="utf-8") as f:
            f.write(resumen)
        print(f"  ✅ Resumen guardado")
    else:
        print(f"  ⚠️  Transcripción vacía")


def main():
    # Nombre de carpeta destino basado en el ID de Drive
    folder_id = extraer_id_carpeta(DRIVE_URL)
    carpeta_destino = os.path.join(os.path.expanduser("~/Downloads"), folder_id)
    os.makedirs(carpeta_destino, exist_ok=True)

    print(f"\n🎬 TRANSCRIPTOR DE CLASES")
    print(f"☁️  Drive: {DRIVE_URL}")
    print(f"📁 Destino: {carpeta_destino}")
    print(f"🤖 {MODELO_OLLAMA} | 🎯 {OBJETIVO}\n")

    # Descargar videos de Drive
    descargar_carpeta(DRIVE_URL, carpeta_destino)

    # Buscar videos descargados (incluyendo subcarpetas)
    videos = glob.glob(os.path.join(carpeta_destino, "**", f"*.{EXTENSION}"), recursive=True)

    if not videos:
        print(f"❌ No se encontraron archivos .{EXTENSION} en la carpeta descargada.")
        return

    print(f"\n✅ {len(videos)} video(s) encontrado(s)\n")

    for video in videos:
        try:
            procesar_video(video)
        except Exception as e:
            print(f"  ❌ Error: {e}")

    print(f"\n\n🎉 ¡Listo! Archivos guardados en:\n   {carpeta_destino}")


if __name__ == "__main__":
    main()
