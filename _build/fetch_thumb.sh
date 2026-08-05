#!/bin/bash
# Zelfde als fetch_image.sh, maar verkleint de foto eerst naar een
# kaartje-formaat (max breedte 900px, kwaliteit 82) - bedoeld voor
# HUB.THUMB, dat op de projectenpagina maar als klein kaartje getoond
# wordt en geen volledige hero-resolutie nodig heeft.
#
# Gebruik: _build/fetch_thumb.sh <bron-url> <project-slug>
# Resultaat: images/<slug>/thumb.webp

set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Gebruik: $0 <bron-url> <project-slug>" >&2
  exit 1
fi

SRC_URL="$1"
SLUG="$2"
MAX_WIDTH=900

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$ROOT/images/$SLUG"
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

mkdir -p "$OUT_DIR"

SRC_FILE="$TMP_DIR/source"
curl -sL -o "$SRC_FILE" "$SRC_URL"

WIDTH=$(sips -g pixelWidth "$SRC_FILE" 2>/dev/null | tail -1 | awk '{print $2}')
OUT_FILE="$OUT_DIR/thumb.webp"

if [ "$WIDTH" -gt "$MAX_WIDTH" ]; then
  cwebp -q 82 -resize "$MAX_WIDTH" 0 "$SRC_FILE" -o "$OUT_FILE" >/dev/null 2>&1
else
  cwebp -q 82 "$SRC_FILE" -o "$OUT_FILE" >/dev/null 2>&1
fi

SIZE_BEFORE=$(stat -f%z "$SRC_FILE")
SIZE_AFTER=$(stat -f%z "$OUT_FILE")

echo "OK: $OUT_FILE ($SIZE_BEFORE -> $SIZE_AFTER bytes)"
echo "/images/$SLUG/thumb.webp"
