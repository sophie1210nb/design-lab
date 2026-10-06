#!/usr/bin/env bash
# Restore one image (or a whole carousel group) to an older tagged version, then save it as a NEW version.
# Works in any git repo that was versioned by render-social.sh.
#
# Dùng:  bash khoi-phuc.sh <ten-hoac-nhom> vN [thư-mục-trong-repo]
#   vd:  bash khoi-phuc.sh p01-ra-mat-4x5 v1 ~/du-an/brands/cafe-may/templates
#        Nhóm carousel (vd m04-chu-de-1x1) khôi phục mọi slide khớp "m04-chu-de-*-1x1".
#   Thư mục mặc định = thư mục hiện tại. Không mất version nào: bản khôi phục được commit + tag vN+1.
set -e
NAME="$1"; VER="$2"; WHERE="${3:-.}"
[ -n "$NAME" ] && [ -n "$VER" ] || { echo "Dùng: bash khoi-phuc.sh <ten-hoac-nhom> vN [thư-mục]"; exit 1; }
cd "$(git -C "$WHERE" rev-parse --show-toplevel)" || { echo "LỖI: $WHERE không nằm trong repo git"; exit 1; }
git rev-parse -q --verify "refs/tags/$NAME-$VER" >/dev/null || { echo "Không có tag $NAME-$VER. Các tag có:"; git tag -l "$NAME-v*"; exit 1; }
pre=""; fmt=""; case "$NAME" in *-*-*) pre="${NAME%-*}"; fmt="${NAME##*-}";; esac
FILES=$(git ls-tree -r --name-only "$NAME-$VER" | grep -E "(^|/)$NAME\.(html|png)$|(^|/)${pre:-x}-[0-9]+-${fmt:-x}\.(html|png)$" || true)
[ -n "$FILES" ] || { echo "Không tìm thấy file của $NAME trong $VER"; exit 1; }
echo "$FILES" | while read -r f; do git checkout "$NAME-$VER" -- "$f"; done
git commit -qm "$NAME: khôi phục về $VER"
LAST=$(git tag -l "$NAME-v*" | sed "s/.*-v//" | grep -E '^[0-9]+$' | sort -n | tail -1); N=$(( ${LAST:-0} + 1 ))
git tag "$NAME-v$N"
echo "Đã khôi phục $NAME về $VER (lưu thành $NAME-v$N):"; echo "$FILES"
