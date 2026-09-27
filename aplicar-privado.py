#!/usr/bin/env python3
"""Aplica la configuracion privada (fuera del repo) a la copia exportada.

Uso: aplicar-privado.py CONFIG_DIR DESTINO
  CONFIG_DIR/redactar.tsv  ruta<TAB>linea|parrafo<TAB>texto -> borra la linea o el parrafo que lo contenga
                           ruta<TAB>reemplazar<TAB>texto<TAB>nuevo -> cambia solo ese texto (para codigo)
  CONFIG_DIR/nombres.txt   un nombre por linea -> si aparece en DESTINO, sale con 1 y dice donde

Las listas viven fuera del repo porque publicarlas ya destaparia a los clientes.
"""
import os
import sys

EXT_TEXTO = {".md", ".txt", ".json", ".jsonl", ".py", ".js", ".ts", ".mjs", ".cjs", ".sh", ".ps1",
             ".yaml", ".yml", ".toml", ".html", ".css", ".csv", ".xml", ".svg", ""}


def leer_lista(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, encoding="utf-8") as f:
        return [l.rstrip("\n") for l in f if l.strip() and not l.lstrip().startswith("#")]


def redactar(config, destino):
    for regla in leer_lista(os.path.join(config, "redactar.tsv")):
        partes = regla.split("\t")
        ruta, modo, texto = partes[0], partes[1], partes[2]
        archivo = os.path.join(destino, ruta)
        if not os.path.exists(archivo):
            continue
        with open(archivo, encoding="utf-8") as f:
            original = f.read()
        t = texto.lower()
        if modo == "reemplazar":
            nuevo = original.replace(texto, partes[3] if len(partes) > 3 else "")
        elif modo == "linea":
            nuevo = "".join(l for l in original.splitlines(keepends=True) if t not in l.lower())
        else:
            bloques = original.split("\n\n")
            nuevo = "\n\n".join(b for b in bloques if t not in b.lower())
        if nuevo != original:
            with open(archivo, "w", encoding="utf-8") as f:
                f.write(nuevo)
            print(f"  redactado: {ruta} ({modo})")


def comprobar_nombres(config, destino):
    nombres = [n.lower() for n in leer_lista(os.path.join(config, "nombres.txt"))]
    avisos = []
    for base, dirs, files in os.walk(destino):
        dirs[:] = [d for d in dirs if d != ".git"]
        for f in files:
            ruta = os.path.join(base, f)
            if os.path.splitext(f)[1].lower() not in EXT_TEXTO:
                continue
            try:
                with open(ruta, encoding="utf-8", errors="ignore") as fh:
                    for n, linea in enumerate(fh, 1):
                        bajo = linea.lower()
                        for nombre in nombres:
                            if nombre in bajo:
                                avisos.append(f"{os.path.relpath(ruta, destino)}:{n}  [{nombre}]")
            except OSError:
                pass
    for a in avisos:
        print(a)
    print(f"{len(avisos)} nombres privados encontrados")
    return not avisos


if __name__ == "__main__":
    config, destino = sys.argv[1], sys.argv[2]
    redactar(config, destino)
    sys.exit(0 if comprobar_nombres(config, destino) else 1)
