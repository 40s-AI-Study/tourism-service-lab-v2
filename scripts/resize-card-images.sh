#!/bin/bash
# Resize Instagram card-news images to exactly 1080x1350 (Instagram portrait)
# using cover-fit (scale-to-fill + center-crop) via macOS sips.
set -euo pipefail

DIR="$(cd "$(dirname "$0")/.." && pwd)/deliverables/card-news-instagram/images"
TARGET_W=1080
TARGET_H=1350
# Mode: "cover" -> exact 1080x1350 with center-crop (Instagram size, may zoom)
#       "fit"   -> longest edge = 1350 preserving aspect (full image, smaller file)
MODE="${1:-fit}"

cd "$DIR"

for f in 01-lotus-lantern-wiki.jpg \
         02-global-culture-wiki.jpg \
         03-jamsugyo-bridge-wiki.jpg \
         04-rose-festival-wiki.jpg \
         05-garden-expo-wiki.jpg; do
  [ -f "$f" ] || { echo "skip missing $f"; continue; }
  # keep an -orig backup the first time we resize
  base="${f%.jpg}"
  orig="${base}-orig.jpg"
  if [ ! -f "$orig" ]; then cp "$f" "$orig"; fi
  # always start from the original
  cp "$orig" "$f"
  W=$(sips -g pixelWidth "$f" | awk 'NR==2{print $2}')
  H=$(sips -g pixelHeight "$f" | awk 'NR==2{print $2}')
  if [ "$MODE" = "cover" ]; then
    SRC=$((W * TARGET_H))
    TGT=$((TARGET_W * H))
    if [ "$SRC" -gt "$TGT" ]; then
      sips --resampleHeight "$TARGET_H" "$f" >/dev/null
    else
      sips --resampleWidth "$TARGET_W" "$f" >/dev/null
    fi
    sips -c "$TARGET_H" "$TARGET_W" "$f" >/dev/null
  else
    # fit: scale longest edge to TARGET_H, preserve aspect
    sips -Z "$TARGET_H" "$f" >/dev/null
  fi
  NW=$(sips -g pixelWidth "$f" | awk 'NR==2{print $2}')
  NH=$(sips -g pixelHeight "$f" | awk 'NR==2{print $2}')
  SIZE=$(wc -c < "$f")
  echo "$f  ${W}x${H} -> ${NW}x${NH}  ($((SIZE/1024)) KB)"
done
