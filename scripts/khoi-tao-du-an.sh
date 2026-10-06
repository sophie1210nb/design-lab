#!/usr/bin/env bash
# Tạo dự án làm việc cho MỘT thương hiệu từ skill (không sửa thẳng trong thư mục skill).
# Dùng:  bash khoi-tao-du-an.sh --brand <ten-brand> <thư-mục-dự-án>
#   vd:  bash khoi-tao-du-an.sh --brand cafe-may ~/Downloads/thiet-ke-cafe-may-thang-11
#        bash khoi-tao-du-an.sh --brand _mau ~/Downloads/thiet-ke-thuong-hieu-moi
# Cấu trúc tạo ra (giữ y như trong skill để đường dẫn tương đối của mẫu chạy được):
#   <dự án>/core/                         CSS dùng chung (core.css)
#   <dự án>/brands/<brand>/brand.md       DNA thương hiệu — đọc trước khi làm
#   <dự án>/brands/<brand>/tokens.css     màu, font
#   <dự án>/brands/<brand>/assets/        logo, nền… (+ anh-that/ để chép ảnh thật, không commit)
#   <dự án>/brands/<brand>/templates/     HTML làm việc (sửa ở đây)
#   <dự án>/brands/<brand>/output/        PNG xuất ra
# Sau đó: bash <skill>/scripts/render-social.sh <dự án>/brands/<brand>/templates/<ten>.html 1080 1350 "mô tả"
set -e
SKILL="$(cd "$(dirname "$0")/.." && pwd)"
BRAND=""; DST=""
while [ $# -gt 0 ]; do
  case "$1" in
    --brand) BRAND="$2"; shift 2;;
    --brand=*) BRAND="${1#--brand=}"; shift;;
    *) DST="$1"; shift;;
  esac
done
if [ -z "$BRAND" ] || [ -z "$DST" ]; then
  echo "Dùng: bash khoi-tao-du-an.sh --brand <ten-brand> <thư-mục-dự-án>"
  echo "Các brand có sẵn:"; ls -1 "$SKILL/brands"; exit 1
fi
[ -d "$SKILL/brands/$BRAND" ] || { echo "LỖI: không có brands/$BRAND. Tạo brand mới: xem references/tao-brand-moi.md"; ls -1 "$SKILL/brands"; exit 1; }
[ -e "$DST/brands/$BRAND" ] && { echo "LỖI: $DST/brands/$BRAND đã tồn tại — không ghi đè."; exit 1; }
mkdir -p "$DST/core" "$DST/brands"
cp -R "$SKILL/core/." "$DST/core/"
cp -R "$SKILL/brands/$BRAND" "$DST/brands/$BRAND"
rm -rf "$DST/brands/$BRAND/output"; find "$DST/brands/$BRAND/assets/anh-that" -mindepth 1 ! -name DOC-TOI.md -exec rm -rf {} + 2>/dev/null || true
mkdir -p "$DST/brands/$BRAND/assets/anh-that" "$DST/brands/$BRAND/output"
cd "$DST"
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git init -q
  printf '%s\n' '**/assets/anh-that/' '*.onnx' '**/output/preview/' > .gitignore
  git add .gitignore core brands && git commit -qm "Khởi tạo dự án thiết kế ($BRAND) từ skill design-lab" || true
fi
echo "Đã tạo dự án: $DST  (brand: $BRAND)"
echo "Đọc trước: $DST/brands/$BRAND/brand.md"
