#!/usr/bin/env python3
"""Busca claves y contraseñas antes de subir. Sale con 1 si encuentra algo.

Uso: revisar-secretos.py DIR [DIR...]
Falsos positivos: añade 'ruta:linea' o un trozo literal de la línea a PERMITIDOS.
"""
import os
import re
import sys

PATRONES = [
    ("anthropic", r"sk-ant-[A-Za-z0-9_\-]{20,}"),
    ("openai", r"sk-(?:proj-)?[A-Za-z0-9_\-]{32,}"),
    ("google_api", r"AIza[0-9A-Za-z_\-]{35}"),
    ("github", r"(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{50,}"),
    ("meta_token", r"EAA[A-Za-z0-9]{60,}"),
    ("stripe", r"(?:sk|rk)_(?:live|test)_[A-Za-z0-9]{20,}"),
    ("slack", r"xox[abposr]-[A-Za-z0-9\-]{10,}"),
    ("aws", r"AKIA[0-9A-Z]{16}"),
    ("jwt", r"eyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}"),
    ("clave_privada", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    ("url_con_credenciales", r"[a-z][a-z0-9+.\-]*://[^/\s:@'\"]+:[^/\s@'\"]{4,}@"),
    ("gmail_app_password", r"(?i)(?:contrase|password|app pass|clave|smtp)[^\n]{0,40}?(?<![A-Za-z])[a-z]{4} [a-z]{4} [a-z]{4} [a-z]{4}(?![A-Za-z])"),
    # Asignaciones: password = "valor", token: valor, contraseña es valor...
    ("asignacion", r"(?i)\b(?:pass(?:word|wd)?|contrase(?:ñ|n)a|secret|api[_\- ]?key|token|clave(?: de api)?|bearer)\b"
                   r"[\"'`]?\s*(?:[:=]|es|→)\s*[\"'`]?([A-Za-z0-9_\-\.\+/=!@#$%^&*]{12,})"),
]
COMPILADOS = [(n, re.compile(p)) for n, p in PATRONES]

# Valores que casan con "asignacion" pero no son secretos
NO_SECRETOS = re.compile(r"(?i)^(?:process\.env|os\.environ|\$\{|<|your|tu_|xxx|example|placeholder|redacted|none|null|undefined|true|false|required|optional|string|getenv|test|fake|dummy|mock|sample"
                         r"|[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+$)")
# URLs de ejemplo con usuario:clave que no apuntan a nada real
URL_EJEMPLO = re.compile(r"(?i)@(?:localhost|127\.0\.0\.1|0\.0\.0\.0|host|db|postgres|example|your|test)|://(?:user|username|postgres|test|admin):(?:pass|password|postgres|test|secret)@")

PERMITIDOS = [
    # Falsos positivos revisados a mano el 26-sep-2026 (código de skills de terceros)
    "_get_api_key(provider)", "get_bing_api_key()", "get_moz_api_key()", "_get_credentials()",
    "STOREFRONT_TOKEN,", "$GOOGLE_API_KEY", "URLPatternComponentResult", "-----BEGIN PRIVATE KEY-----\\n...\\n",
    # 28-sep-2026: ejemplos curl que leen la clave de una variable de entorno
    "$GEMINI_API_KEY", "$ELEVENLABS_API_KEY",
]

EXT_TEXTO = {".md", ".txt", ".json", ".jsonl", ".py", ".js", ".ts", ".mjs", ".cjs", ".sh", ".ps1",
             ".yaml", ".yml", ".toml", ".html", ".css", ".csv", ".xml", ".ini", ".cfg", ".env", ""}


def permitido(ruta, n, linea):
    return any(p == f"{ruta}:{n}" or (p and p in linea) for p in PERMITIDOS)


def revisar(raiz):
    avisos = []
    for base, dirs, files in os.walk(raiz):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", ".venv", "__pycache__"}]
        for f in files:
            ruta = os.path.join(base, f)
            if os.path.splitext(f)[1].lower() not in EXT_TEXTO or os.path.getsize(ruta) > 20_000_000:
                continue
            try:
                with open(ruta, encoding="utf-8", errors="ignore") as fh:
                    for n, linea in enumerate(fh, 1):
                        for nombre, rx in COMPILADOS:
                            for m in rx.finditer(linea):
                                if nombre == "asignacion" and NO_SECRETOS.match(m.group(1)):
                                    continue
                                if nombre == "url_con_credenciales" and URL_EJEMPLO.search(linea):
                                    continue
                                if permitido(ruta, n, linea):
                                    continue
                                trozo = m.group(0)
                                avisos.append((ruta, n, nombre, trozo[:12] + "…" if len(trozo) > 12 else trozo))
            except OSError:
                pass
    return avisos


if __name__ == "__main__":
    todos = [a for d in sys.argv[1:] for a in revisar(d)]
    for ruta, n, nombre, trozo in todos:
        print(f"{ruta}:{n}  [{nombre}]  {trozo}")
    print(f"{len(todos)} avisos")
    sys.exit(1 if todos else 0)
