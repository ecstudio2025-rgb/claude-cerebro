"""Cliente mínimo de la API de Gemini para la skill carrusel-gemini.

Sin dependencias externas (urllib de la stdlib).

La clave se lee, en este orden:
  1. Variable de entorno GEMINI_API_KEY
  2. ~/.config/ecsstudio/gemini.env   (línea GEMINI_API_KEY=...)

La clave NUNCA se guarda dentro de la carpeta de la skill.
"""

import base64
import hashlib
import json
import os
import pathlib
import time
import urllib.error
import urllib.request

API = "https://generativelanguage.googleapis.com/v1beta/models"

MODELO_IMAGEN = "gemini-3-pro-image"      # Nano Banana Pro
MODELO_IMAGEN_RAPIDO = "gemini-3.1-flash-image"
MODELO_TEXTO = "gemini-3.1-pro-preview"
MODELO_VISION = "gemini-3.1-pro-preview"

ENV_FILE = pathlib.Path.home() / ".config" / "ecsstudio" / "gemini.env"


class GeminiError(RuntimeError):
    pass


def api_key():
    k = os.environ.get("GEMINI_API_KEY")
    if k:
        return k.strip()
    if ENV_FILE.exists():
        for linea in ENV_FILE.read_text().splitlines():
            if linea.startswith("GEMINI_API_KEY="):
                return linea.split("=", 1)[1].strip().strip('"')
    raise GeminiError(
        f"Falta la clave. Exporta GEMINI_API_KEY o escríbela en {ENV_FILE}"
    )


def _post(modelo, body, timeout=300, reintentos=3):
    url = f"{API}/{modelo}:generateContent?key={api_key()}"
    datos = json.dumps(body).encode()
    ultimo = None
    for intento in range(reintentos):
        req = urllib.request.Request(
            url, data=datos, headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            cuerpo = e.read().decode()[:500]
            ultimo = f"HTTP {e.code}: {cuerpo}"
            # 429 y 5xx se reintentan con espera creciente
            if e.code in (429, 500, 502, 503, 504) and intento < reintentos - 1:
                time.sleep(5 * (intento + 1))
                continue
            raise GeminiError(ultimo) from None
        except urllib.error.URLError as e:
            ultimo = f"Red: {e.reason}"
            if intento < reintentos - 1:
                time.sleep(5 * (intento + 1))
                continue
            raise GeminiError(ultimo) from None
    raise GeminiError(ultimo or "fallo desconocido")


# --- Imagen ---------------------------------------------------------------

REGLA_SIN_TEXTO = (
    "REGLA ABSOLUTA: la imagen no debe contener NINGUNA letra, palabra, número, "
    "logo, marca de agua ni interfaz. Cero tipografía. Si aparece cualquier texto, "
    "la imagen es inválida. El texto se compone después por fuera."
)


def generar_arte(prompt, destino, aspect="4:5", size="2K", modelo=MODELO_IMAGEN,
                 referencia=None, cache=True):
    """Genera arte SIN texto y lo guarda en `destino`. Devuelve la ruta.

    `referencia`: ruta a un PNG previo que se pasa como ancla de estilo para
    que todos los slides parezcan de la misma serie.
    """
    destino = pathlib.Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)

    firma = hashlib.sha1(
        f"{modelo}|{aspect}|{size}|{prompt}|{referencia}".encode()
    ).hexdigest()[:12]
    marca = destino.with_suffix(".firma")
    if cache and destino.exists() and marca.exists() and marca.read_text() == firma:
        return destino

    partes = [{"text": f"{prompt}\n\n{REGLA_SIN_TEXTO}"}]
    if referencia:
        ref = pathlib.Path(referencia)
        if ref.exists():
            partes.insert(0, {
                "inlineData": {
                    "mimeType": "image/png",
                    "data": base64.b64encode(ref.read_bytes()).decode(),
                }
            })
            partes.append({"text": "Mantén la misma paleta, textura y lenguaje "
                                   "visual que la imagen de referencia."})

    body = {
        "contents": [{"parts": partes}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": aspect, "imageSize": size},
        },
    }
    r = _post(modelo, body)
    try:
        candidato = r["candidates"][0]
    except (KeyError, IndexError):
        raise GeminiError(f"Respuesta sin candidatos: {json.dumps(r)[:400]}")
    for p in candidato.get("content", {}).get("parts", []):
        if "inlineData" in p:
            destino.write_bytes(base64.b64decode(p["inlineData"]["data"]))
            marca.write_text(firma)
            return destino
    motivo = candidato.get("finishReason", "?")
    raise GeminiError(f"Gemini no devolvió imagen (finishReason={motivo})")


# --- Texto / visión -------------------------------------------------------

def texto(prompt, modelo=MODELO_TEXTO, json_estricto=False, imagenes=None):
    """Llama a un modelo de texto. Con `imagenes` (lista de rutas) hace visión."""
    partes = []
    for ruta in imagenes or []:
        partes.append({
            "inlineData": {
                "mimeType": "image/png",
                "data": base64.b64encode(pathlib.Path(ruta).read_bytes()).decode(),
            }
        })
    partes.append({"text": prompt})

    cfg = {}
    if json_estricto:
        cfg["responseMimeType"] = "application/json"
    body = {"contents": [{"parts": partes}]}
    if cfg:
        body["generationConfig"] = cfg

    r = _post(modelo, body)
    try:
        trozos = r["candidates"][0]["content"]["parts"]
    except (KeyError, IndexError):
        raise GeminiError(f"Respuesta vacía: {json.dumps(r)[:400]}")
    salida = "".join(p.get("text", "") for p in trozos)
    if json_estricto:
        return json.loads(salida)
    return salida
