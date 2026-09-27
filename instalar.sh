#!/usr/bin/env bash
# Instala el Claude de Diego en Mac o Linux: skills, agentes, kb-mercado, CLAUDE.md, plugins
# y, con la clave del equipo, la capa privada (memoria de Diego y skills con casos de clientes).
#
# Instalar o actualizar:
#   curl -fsSL https://raw.githubusercontent.com/ecstudio2025-rgb/claude-cerebro/main/instalar.sh | bash
#
# Las carpetas quedan enlazadas al repo local: volver a lanzar la linea de arriba actualiza todo.
# Lo que ya hubiera en ~/.claude con el mismo nombre se renombra a .bak-FECHA, nunca se borra.
# Clave del equipo sin preguntar: CEREBRO_CLAVE=xxxx antes de bash.
set -euo pipefail

REPO_URL="${CEREBRO_REPO:-https://github.com/ecstudio2025-rgb/claude-cerebro.git}"
PRIVADO_URL="https://socialimpulso.es/cerebro/privado.tar.gz"
REPO="$HOME/claude-cerebro"
CLAUDE="$HOME/.claude"
STAMP="$(date +%Y%m%d-%H%M%S)"

command -v git >/dev/null || { echo "Falta git. En Mac: xcode-select --install  |  En Linux: sudo apt install git"; exit 1; }

if [[ -d "$REPO/.git" ]]; then
  echo "Actualizando el repo..."
  git -C "$REPO" pull --rebase --autostash -q
else
  echo "Descargando en $REPO ..."
  git clone -q "$REPO_URL" "$REPO"
fi
mkdir -p "$CLAUDE"

# --- Capa privada (antes de enlazar: se mete dentro de la copia local, sin tocar git) ---
CLAVE="${CEREBRO_CLAVE:-}"
if [[ -z "$CLAVE" && -r /dev/tty ]]; then
  printf "Clave del equipo para la memoria de Diego (Enter para saltar): "
  read -rs CLAVE </dev/tty || true; echo
fi
PRIV="$CLAUDE/cerebro-privado"
if [[ -n "$CLAVE" ]]; then
  tmp="$(mktemp -d)"
  if curl -fsSL -u "equipo:$CLAVE" -o "$tmp/p.tgz" "$PRIVADO_URL"; then
    rm -rf "$PRIV"; tar xzf "$tmp/p.tgz" -C "$CLAUDE"
    # Skills y guias privadas dentro de la copia local; git las ignora
    (cd "$PRIV/claude" && find . -type f) | sed 's|^\./|claude/|' > "$REPO/.git/info/exclude"
    cp -R "$PRIV/claude/." "$REPO/claude/"
    echo "  capa privada instalada en $PRIV"
  else
    echo "  clave incorrecta o sin conexion: sigo sin la capa privada"
  fi
  rm -rf "$tmp"
fi

enlazar() {  # $1 origen, $2 destino
  [[ -e "$1" ]] || return 0
  if [[ -L "$2" ]]; then
    [[ "$(readlink "$2")" == "$1" ]] && return 0
    rm "$2"
  elif [[ -e "$2" ]]; then
    mv "$2" "$2.bak-$STAMP"; echo "  copia de seguridad: $2.bak-$STAMP"
  fi
  ln -s "$1" "$2"; echo "  enlazado: $2"
}

echo "Carpetas:"
for d in skills agents commands kb-mercado hook-vault templates; do
  enlazar "$REPO/claude/$d" "$CLAUDE/$d"
done

echo "CLAUDE.md y guias (rutas de Diego cambiadas a las de este equipo):"
for f in CLAUDE.md voz-diego-marca.md anti-patrones-ia-redaccion.md; do
  origen="$REPO/claude/$f"; [[ -f "$origen" ]] || continue
  destino="$CLAUDE/$f"
  [[ -f "$destino" && ! -f "$destino.bak-original" ]] && cp "$destino" "$destino.bak-original"
  sed "s|/Users/diego/|$HOME/|g" "$origen" > "$destino"
  echo "  $destino"
done

cp "$REPO/claude/EQUIPO.md" "$CLAUDE/EQUIPO.md"
printf '\n@%s\n' "$CLAUDE/EQUIPO.md" >> "$CLAUDE/CLAUDE.md"
echo "  reglas del equipo: $CLAUDE/EQUIPO.md"

if [[ -d "$PRIV/memoria" ]]; then
  cat >> "$CLAUDE/CLAUDE.md" <<EOF

## Memoria de Diego (solo lectura, capa privada del equipo)
Indices de lo que Diego y Claude han hecho con cada cliente, proyecto y herramienta. Cada linea apunta a un fichero de su misma carpeta:
- $PRIV/memoria/claude/ (trabajo reciente)
- $PRIV/memoria/documents/ (ecosistema: One, Chat, Setter, facturas, clientes)
Antes de tocar un cliente o un sistema, busca aqui. No edites estos ficheros: se sobrescriben al actualizar. Tu propia memoria va aparte.
Las contraseñas y tokens estan tachados a proposito: pideselos a Diego, no los busques.

@$PRIV/memoria/claude/MEMORY.md
@$PRIV/memoria/documents/MEMORY.md
EOF
  echo "  memoria de Diego enlazada en CLAUDE.md"
fi

echo "Ajustes:"
python3 - "$REPO/settings.windows.json" "$CLAUDE/settings.json" <<'PY'
import json, os, shutil, sys, time
plantilla, destino = sys.argv[1], sys.argv[2]
p = json.load(open(plantilla))
if os.path.exists(destino):
    shutil.copy(destino, f"{destino}.bak-{time.strftime('%Y%m%d-%H%M%S')}")
    a = json.load(open(destino))
    for k, v in p.items():
        if k not in a: a[k] = v
        elif k in ("enabledPlugins", "extraKnownMarketplaces"):
            for q, w in v.items(): a[k].setdefault(q, w)
    print("  fusionado con el settings.json que ya habia")
else:
    a = p; print("  creado", destino)
json.dump(a, open(destino, "w"), indent=2, ensure_ascii=False)
PY

# Carpeta de trabajo con la configuracion Ruflo (swarm) de Diego
mkdir -p "$HOME/Claude"
if [[ ! -f "$HOME/Claude/CLAUDE.md" ]]; then
  cp "$REPO/claude/proyecto-CLAUDE.md" "$HOME/Claude/CLAUDE.md"; echo "  $HOME/Claude/CLAUDE.md (Ruflo)"
fi

if ! command -v claude >/dev/null && [[ ! -x "$HOME/.local/bin/claude" ]]; then
  echo "Instalando Claude Code..."
  curl -fsSL https://claude.ai/install.sh | bash
fi
CLAUDE_BIN="$(command -v claude || echo "$HOME/.local/bin/claude")"

# Ruflo como MCP (necesita Node). Si no hay Node, se avisa y se sigue.
if command -v npx >/dev/null; then
  if ! "$CLAUDE_BIN" mcp list 2>/dev/null | grep -q claude-flow; then
    "$CLAUDE_BIN" mcp add --scope user claude-flow -- npx -y @claude-flow/cli@latest >/dev/null 2>&1 \
      && echo "  Ruflo (claude-flow) conectado" || echo "  Ruflo no se pudo conectar: no pasa nada, Claude funciona igual"
  fi
else
  echo "  Sin Node.js: Ruflo queda para luego (instala Node LTS de nodejs.org y repite esta linea)"
fi

echo
echo "Listo. Abre una terminal nueva y lanza:  cd ~/Claude && claude"
echo "La primera vez te pide iniciar sesion: usa la cuenta de Claude del equipo. Despues reinicia el ordenador."
echo "Instala tambien la extension Claude in Chrome (solo Chrome) e inicia sesion con la misma cuenta."
echo "No vienen nunca: contraseñas, tokens de los MCP ni acceso SSH al VPS. Eso se pide a Diego."
