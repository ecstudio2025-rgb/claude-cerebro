#!/usr/bin/env bash
# Descarga una URL sin caché y cuenta cuántas veces aparece cada texto.
# Uso: comprobar_landing.sh URL "texto1" ["texto2" ...]
# Lo nuevo debe dar > 0 y lo retirado 0. Sale con código 1 si la URL no da 200.
set -uo pipefail
URL="${1:?url}"; shift
SEP='?'; [[ "$URL" == *\?* ]] && SEP='&'
TMP="$(mktemp)"
CODE=$(curl -s -o "$TMP" -w "%{http_code}" "${URL}${SEP}nc=$RANDOM$RANDOM")
echo "HTTP $CODE  $URL"
for t in "$@"; do
  printf '  %-45s %s\n' "$t" "$(grep -o -- "$t" "$TMP" | wc -l | tr -d ' ')"
done
rm -f "$TMP"
[ "$CODE" = "200" ] || exit 1
