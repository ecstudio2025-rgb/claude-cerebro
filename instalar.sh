#!/usr/bin/env bash
# Instala el Claude de Diego en Mac o Linux: skills, agentes, kb-mercado, CLAUDE.md, plugins
# y, con la clave del equipo, la capa privada (memoria de Diego y skills con casos de clientes).
#
# Instalar o actualizar:
#   curl -fsSL https://raw.githubusercontent.com/ecstudio2025-rgb/claude-cerebro/main/instalar.sh | bash
#
# Las carpetas quedan enlazadas al repo local: volver a lanzar la linea de arriba actualiza todo.
# Lo que ya hubiera en ~/.claude con el mismo nombre se renombra a .bak-FECHA, nunca se borra.
# Clave del equipo sin preguntar: CEREBRO_CLAVE=xxxx antes de bash. Se guarda en ~/.config/claude-cerebro-equipo/clave.
# Se actualiza solo cada dia a las 09:00 (launchd en Mac, cron en Linux) con CEREBRO_AUTO=1:
# baja lo nuevo del repo, la memoria de Diego y los aportes del equipo, sin preguntar nada.
set -euo pipefail
# Si se lanza desde el propio repo, corre desde una copia: el git pull de abajo puede reescribir este fichero.
if [[ -f "${BASH_SOURCE[0]:-}" && -z "${CEREBRO_COPIA:-}" ]]; then
  c="$(mktemp)"; cp "${BASH_SOURCE[0]}" "$c"; CEREBRO_COPIA=1 exec bash "$c" "$@"
fi

REPO_URL="${CEREBRO_REPO:-https://github.com/ecstudio2025-rgb/claude-cerebro.git}"
PRIVADO_URL="https://socialimpulso.es/cerebro/privado.tar.gz"
REPO="$HOME/claude-cerebro"
CLAUDE="$HOME/.claude"
CONF="$HOME/.config/claude-cerebro-equipo"
AUTO="${CEREBRO_AUTO:-}"
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
[[ -z "$CLAVE" && -s "$CONF/clave" ]] && CLAVE="$(cat "$CONF/clave")"
if [[ -z "$CLAVE" && -z "$AUTO" && -r /dev/tty ]]; then
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
    mkdir -p "$CONF"; chmod 700 "$CONF"; printf '%s' "$CLAVE" > "$CONF/clave"; chmod 600 "$CONF/clave"
    printf '%s' "${PRIVADO_URL%privado.tar.gz}aportes/" > "$CONF/buzon"
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
if [[ -f "$PRIV/aportes/INDICE.md" ]]; then
  cat >> "$CLAUDE/CLAUDE.md" <<EOF

## Aportes del equipo (lo que ha aprendido el Claude de cada uno)
Indice en $PRIV/aportes/INDICE.md; cada linea apunta a una nota de esa carpeta. Miralo antes de resolver algo que otro ya resolvio.
Cuando aprendas algo que le sirva al resto (un procedimiento que funciono, un fallo y su arreglo, un criterio de cliente), usa la skill cerebro-aportar.
EOF
fi

if [[ -n "$AUTO" ]]; then echo "Actualizacion automatica hecha $(date '+%F %H:%M')"; exit 0; fi

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
# Que "claude" funcione en terminales nuevas: ~/.local/bin al PATH si no esta
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
  for rc in "$HOME/.zshrc" "$HOME/.bashrc"; do
    grep -qs 'claude-cerebro: PATH' "$rc" || printf '\nexport PATH="$HOME/.local/bin:$PATH"  # claude-cerebro: PATH\n' >> "$rc"
  done
  echo "  anadido ~/.local/bin al PATH (terminales nuevas)"
fi

# Ruflo como MCP (necesita Node). Si no hay Node, se avisa y se sigue.
if command -v npx >/dev/null; then
  if ! "$CLAUDE_BIN" mcp list 2>/dev/null | grep -q claude-flow; then
    "$CLAUDE_BIN" mcp add --scope user claude-flow -- npx -y @claude-flow/cli@latest >/dev/null 2>&1 \
      && echo "  Ruflo (claude-flow) conectado" || echo "  Ruflo no se pudo conectar: no pasa nada, Claude funciona igual"
  fi
else
  echo "  Sin Node.js: Ruflo queda para luego (instala Node LTS de nodejs.org y repite esta linea)"
fi

# Actualizacion diaria automatica (09:00): repo, memoria de Diego y aportes del equipo
LINEA="CEREBRO_AUTO=1 bash $REPO/instalar.sh"
if [[ -n "${CEREBRO_SIN_PROGRAMAR:-}" ]]; then
  echo "  (sin programar la actualizacion diaria)"
elif [[ "$(uname)" == "Darwin" ]]; then
  PL="$HOME/Library/LaunchAgents/com.ecs.claude-cerebro.plist"
  mkdir -p "$HOME/Library/LaunchAgents" "$HOME/Library/Logs"
  cat > "$PL" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>com.ecs.claude-cerebro</string>
  <key>ProgramArguments</key><array><string>/bin/bash</string><string>-lc</string><string>$LINEA</string></array>
  <key>StartCalendarInterval</key><dict><key>Hour</key><integer>9</integer><key>Minute</key><integer>0</integer></dict>
  <key>StandardOutPath</key><string>$HOME/Library/Logs/claude-cerebro.log</string>
  <key>StandardErrorPath</key><string>$HOME/Library/Logs/claude-cerebro.log</string>
</dict></plist>
EOF
  launchctl unload "$PL" 2>/dev/null || true; launchctl load "$PL" && echo "  actualizacion diaria 09:00 activada"
elif command -v crontab >/dev/null; then
  ( crontab -l 2>/dev/null | grep -v 'claude-cerebro/instalar.sh'; echo "0 9 * * * $LINEA >> \$HOME/.claude-cerebro.log 2>&1" ) | crontab - \
    && echo "  actualizacion diaria 09:00 activada (cron)"
fi

echo
echo "Listo. Abre una terminal nueva y lanza:  cd ~/Claude && claude"
echo "La primera vez te pide iniciar sesion: usa la cuenta de Claude del equipo. Despues reinicia el ordenador."
echo "Instala tambien la extension Claude in Chrome (solo Chrome) e inicia sesion con la misma cuenta."
echo "No vienen nunca: contraseñas, tokens de los MCP ni acceso SSH al VPS. Eso se pide a Diego."
