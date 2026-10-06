#!/usr/bin/env bash
# Quick preview: render an HTML to a 1x PNG, no git commit/tag.
# Dùng:  bash preview.sh <duong-dan>/<ten>.html [W] [H]
#   Xuất ra <thư mục html>/../output/preview/<ten>.png (đổi bằng OUT_DIR=...).
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
HTML="$1"; W="${2:-1080}"; H="${3:-1350}"
[ -f "$HTML" ] || { echo "Dùng: bash preview.sh <file.html> [W] [H]"; exit 1; }
HTML_DIR="$(cd "$(dirname "$HTML")" && pwd)"
OUT_DIR="${OUT_DIR:-$HTML_DIR/../output/preview}" SCALE=1 NO_GIT=1 \
  bash "$HERE/render-social.sh" "$HTML" "$W" "$H" "preview"
