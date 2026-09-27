#!/usr/bin/env bash
# Exporta el Claude del Mac a este repo (PUBLICO) y lo sube a GitHub; la memoria va aparte, al VPS con login.
# Uso: bash ~/claude-cerebro/sincronizar.sh [--sin-push]
# Nunca copia la memoria, settings.json, ~/.claude.json, sesiones, historial ni MCP (datos privados y claves).
# Lo que no debe salir en publico se configura FUERA del repo, en ~/.config/claude-cerebro/:
#   excluir.txt   rutas relativas a ~/.claude que no se copian
#   redactar.tsv  lineas o parrafos que se borran de la copia
#   nombres.txt   nombres de clientes: si alguno aparece en la copia, no se sube nada
set -euo pipefail

REPO="$(cd "$(dirname "$0")" && pwd)"
SRC="${CLAUDE_SRC:-$HOME/.claude}"
PRIV="${CLAUDE_CEREBRO_PRIV:-$HOME/.config/claude-cerebro}"
cd "$REPO"
[[ -f "$PRIV/excluir.txt" && -f "$PRIV/nombres.txt" ]] || { echo "Falta la config privada en $PRIV (excluir.txt y nombres.txt). No se exporta nada."; exit 1; }
[[ -d .git ]] || git init -b main -q

if git remote get-url origin >/dev/null 2>&1; then
  git pull --rebase --autostash -q || { echo "git pull fallo: resuelve el conflicto y vuelve a lanzar"; exit 1; }
fi

EXCL=(--exclude .venv --exclude venv --exclude node_modules --exclude __pycache__ --exclude .git
      --exclude .DS_Store --exclude '*.pyc' --exclude '.env*' --exclude .claude-flow --exclude '*.log')

# excluir.txt usa rutas relativas a ~/.claude; rsync las quiere relativas a cada carpeta copiada.
excluir_de() {
  local carpeta="$1"
  grep -vE '^\s*(#|$)' "$PRIV/excluir.txt" | while IFS= read -r ruta; do
    [[ "$ruta" == "$carpeta/"* ]] && printf -- '--exclude=/%s\n' "${ruta#"$carpeta"/}"
  done
}

mkdir -p claude
rm -rf memoria

for f in CLAUDE.md voz-diego-marca.md anti-patrones-ia-redaccion.md; do
  if grep -qxF "$f" "$PRIV/excluir.txt"; then rm -f "claude/$f"; else cp "$SRC/$f" "claude/$f"; fi
done

# -L resuelve los enlaces simbolicos (en Windows se romperian). --delete-excluded borra del repo lo que pase a estar excluido.
for d in skills agents commands kb-mercado hook-vault templates; do
  if grep -qxF "$d/" "$PRIV/excluir.txt"; then rm -rf "claude/$d"; continue; fi
  extra=()
  while IFS= read -r x; do extra+=("$x"); done < <(excluir_de "$d")
  rsync -aL --delete --delete-excluded "${EXCL[@]}" ${extra[@]+"${extra[@]}"} "$SRC/$d/" "claude/$d/"
done

# Borrados de lineas/parrafos y comprobacion de nombres de clientes
if ! python3 "$REPO/aplicar-privado.py" "$PRIV" claude; then
  echo "Hay nombres privados en la copia: no se sube nada. Excluye el archivo o anade un borrado en $PRIV"; exit 1
fi

# Filtro de claves
if ! python3 "$REPO/revisar-secretos.py" claude; then
  echo "Revision de secretos con avisos: no se sube nada. Corrige o anade la excepcion en revisar-secretos.py"; exit 1
fi
rm -rf "$REPO/__pycache__"

# Capa privada del equipo (memoria + excluidos, claves tachadas) al VPS con login. El script vive fuera del repo.
if [[ "${1:-}" != "--sin-push" && -f "$PRIV/empaquetar-privado.py" ]]; then
  python3 "$PRIV/empaquetar-privado.py" --subir | tail -2 || { echo "Fallo la capa privada: el repo publico sigue adelante"; }
fi

git add -A
if git diff --cached --quiet; then echo "Sin cambios."; exit 0; fi
git commit -q -m "Sincronizado $(date '+%F %H:%M')"
[[ "${1:-}" == "--sin-push" ]] || git push -q
git log --oneline -1
