#!/usr/bin/env bash
# Render one social HTML -> PNG (scale 2 by default) and, if the HTML folder is inside a git repo,
# commit HTML + PNG + shared CSS/JS and tag <name>-vN (N auto-increments).
#
# Dùng:  bash render-social.sh <duong-dan>/<ten>.html <W> <H> "<mô tả thay đổi>" [TAG_NHOM]
#   W×H: 1080 1080 (1:1) · 1080 1350 (4:5) · 1080 1920 (9:16) · 1080 2160 (1:2) · 2160 1080 (2:1)
#   TAG_NHOM: dùng cho carousel, truyền ở slide cuối để tag cả bộ (vd m04-chu-de-1x1).
#
# Biến môi trường (tùy chọn):
#   OUT_DIR  thư mục xuất PNG. Mặc định: <thư mục html>/../output
#   SCALE    hệ số phóng (mặc định 2 → PNG 2160 px rộng cho khổ 1080)
#   NO_GIT=1 không commit/tag dù đang ở trong repo git
#   CHROME   đường dẫn Chrome/Chromium nếu không tự tìm được
set -e
HTML_ARG="$1"; W="${2:-1080}"; H="${3:-1350}"; MSG="${4:-cập nhật}"; GROUP="$5"; SCALE="${SCALE:-2}"
[ -n "$HTML_ARG" ] && [ -f "$HTML_ARG" ] || { echo "LỖI: không thấy file html: $HTML_ARG"; exit 1; }

HTML_DIR="$(cd "$(dirname "$HTML_ARG")" && pwd)"; HTML="$(basename "$HTML_ARG")"; BASE="${HTML%.html}"
OUT_DIR="${OUT_DIR:-$HTML_DIR/../output}"; mkdir -p "$OUT_DIR"; OUT_DIR="$(cd "$OUT_DIR" && pwd)"
OUT="$OUT_DIR/$BASE.png"

# --- find Chrome ---
find_chrome() {
  [ -n "$CHROME" ] && { echo "$CHROME"; return; }
  for c in "/c/Program Files/Google/Chrome/Application/chrome.exe" \
           "/c/Program Files (x86)/Google/Chrome/Application/chrome.exe" \
           "$LOCALAPPDATA/Google/Chrome/Application/chrome.exe" \
           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
    [ -x "$c" ] && { echo "$c"; return; }
  done
  for c in google-chrome google-chrome-stable chromium chromium-browser chrome; do
    command -v "$c" >/dev/null 2>&1 && { command -v "$c"; return; }
  done
}
CHROME_BIN="$(find_chrome)"; [ -n "$CHROME_BIN" ] || { echo "LỖI: không tìm thấy Chrome (đặt biến CHROME=...)"; exit 1; }

# --- path conversion (Git Bash on Windows needs Windows paths for Chrome) ---
if command -v cygpath >/dev/null 2>&1; then
  winp() { cygpath -w "$1"; }; URL="file:///$(cygpath -m "$HTML_DIR/$HTML" | sed 's/ /%20/g')"
else
  winp() { echo "$1"; }; URL="file://$(echo "$HTML_DIR/$HTML" | sed 's/ /%20/g')"
fi
PROFILE="$(mktemp -d "${TEMP:-/tmp}/chrome-social-XXXXXX")"; trap 'rm -rf "$PROFILE"' EXIT

rm -f "$OUT"
timeout 240 "$CHROME_BIN" --headless --disable-gpu --hide-scrollbars --no-sandbox \
  --user-data-dir="$(winp "$PROFILE")" --force-device-scale-factor="$SCALE" --window-size="$W,$H" \
  --virtual-time-budget=12000 --screenshot="$(winp "$OUT")" "$URL" >/dev/null 2>&1 || true
[ -s "$OUT" ] || { echo "LỖI: không xuất được $OUT"; exit 1; }

# --- optional git versioning ---
if [ "${NO_GIT:-0}" = "1" ] || ! git -C "$HTML_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "OK -> $OUT  (không lưu version git)"; exit 0
fi
cd "$HTML_DIR"
git add -- "$HTML" "$OUT" 2>/dev/null || git add -- "$HTML"
git add -- _*.css _*.js 2>/dev/null || true
if git diff --cached --quiet; then echo "OK (không đổi) -> $OUT"; exit 0; fi
T="${GROUP:-$BASE}"; LAST=$(git tag -l "$T-v*" | sed "s/.*-v//" | grep -E '^[0-9]+$' | sort -n | tail -1)
N=$(( ${LAST:-0} + 1 ))
for i in 1 2 3 4 5; do git commit -qm "$T v$N: $MSG" && break || sleep 2; done
git tag "$T-v$N"
echo "OK -> $OUT  [$T-v$N]"
