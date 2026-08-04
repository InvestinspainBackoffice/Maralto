#!/bin/bash
# Haalt een externe foto op, zet ze om naar WebP (zelfde resolutie, kwaliteit
# 88 - visueel lossless) en bewaart ze in images/<slug>/. Vercel serveert
# de hele repo statisch, dus het resultaat is meteen bereikbaar op
# https://investinspain.be/images/<slug>/<naam>.webp (of via het
# projects-subdomein) zonder dat er iets naar WordPress geupload moet worden.
#
# Gebruik: _build/fetch_image.sh <bron-url> <project-slug> <output-naam-zonder-extensie>
# Voorbeeld: _build/fetch_image.sh https://emare.immo/.../084A5415x.jpg emare hero

set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "Gebruik: $0 <bron-url> <project-slug> <output-naam>" >&2
  exit 1
fi

SRC_URL="$1"
SLUG="$2"
NAME="$3"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$ROOT/images/$SLUG"
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

mkdir -p "$OUT_DIR"

SRC_FILE="$TMP_DIR/source"
curl -sL -o "$SRC_FILE" "$SRC_URL"

OUT_FILE="$OUT_DIR/$NAME.webp"
cwebp -q 88 "$SRC_FILE" -o "$OUT_FILE" >/dev/null 2>&1

DIMS=$(sips -g pixelWidth -g pixelHeight "$SRC_FILE" 2>/dev/null | tail -2 | awk '{print $2}' | paste -sd'x' -)
SIZE_BEFORE=$(stat -f%z "$SRC_FILE")
SIZE_AFTER=$(stat -f%z "$OUT_FILE")

echo "OK: $OUT_FILE"
echo "  Resolutie: ${DIMS}"
echo "  Grootte: $SIZE_BEFORE -> $SIZE_AFTER bytes"
echo "  Pad in site: /images/$SLUG/$NAME.webp"
