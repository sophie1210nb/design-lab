# Tạo brand pack mới

Một brand pack = toàn bộ "DNA thương hiệu" của một khách / một đội: quy tắc, màu, font, tài sản, mẫu. Skill chỉ thiết kế khi đã có brand pack. Đội đã có pack riêng (.zip) → cài theo mục 8. Chưa có → tạo trước khi làm ấn phẩm đầu tiên.

## 1. Chép khung
```bash
cp -R brands/_mau brands/<ten-brand>      # chữ thường, không dấu, gạch ngang: vd cafe-may, abc-academy
rm -rf brands/<ten-brand>/output
```
Trong pack:
```
brands/<ten-brand>/
  brand.md      DNA thương hiệu (điền theo mẫu)
  tokens.css    biến màu/font cho core/core.css
  assets/       logo, nền, ảnh tách nền đã được phép dùng; anh-that/ cho ảnh thật (git-ignore)
  templates/    mẫu HTML của thương hiệu
```

## 2. Lấy thông tin — hỏi ít, hỏi đúng
Ưu tiên rút ra từ tài liệu người dùng đưa (brand guideline, logo, ảnh bài đăng cũ, website, ấn phẩm họ thích). Chỉ hỏi những gì không suy ra được. Bộ câu hỏi tối thiểu (gộp vào 1 tin nhắn):
1. Tên thương hiệu ghi thế nào trên ấn phẩm (đủ tên / viết tắt / viết hoa)? Tagline?
2. Ai xem ấn phẩm, xem ở đâu (điện thoại, in, màn hình)?
3. Có bộ nhận diện không: logo (file gốc), màu, font? Nếu không: 3 tính từ mô tả cảm giác muốn có + 1–3 ấn phẩm/thương hiệu họ thích.
4. Có người/nhân vật cần xuất hiện (chủ doanh nghiệp, giảng viên…)? Chức danh nguyên văn?
5. Thông tin nào bắt buộc / cấm ghi trên ảnh (SĐT, giá, link…)?
6. Những kiểu nào họ KHÔNG thích?

Từ ảnh tham khảo: đo màu chủ đạo (nền, chữ, nhấn), nhận dạng font gần nhất có hỗ trợ tiếng Việt, ghi lại bố cục lặp lại (lề, vị trí logo, cách đặt CTA).

## 3. Điền `brand.md`
Điền đủ 9 mục của mẫu. Quy tắc nào chưa chắc → `[ ]` + câu hỏi. Mỗi quyết định của chủ thương hiệu ghi kèm **ngày** vào mục 7 (bị bác) hoặc 9 (nhật ký). Đây là "nguồn sự thật" — lần sau làm ấn phẩm chỉ cần đọc file này.

## 4. Điền `tokens.css`
Thay giá trị các biến (giữ nguyên tên biến để `core/core.css` dùng được):

| Biến | Ý nghĩa |
|---|---|
| `--font-display`, `--font-body` | font tiêu đề / thân (sửa luôn dòng `@import` Google Fonts) |
| `--bg`, `--bg-solid`, `--bg-glow` | nền tờ (gradient được), màu nền đặc, quầng sáng |
| `--text`, `--text-strong`, `--text-muted`, `--tagline` | màu chữ |
| `--accent`, `--accent-soft`, `--accent-text`, `--accent-fill`, `--on-accent` | màu nhấn, nhãn, chữ gradient, nền nút/chip, chữ trên nút |
| `--hairline`, `--surface`, `--surface-strong`, `--surface-border`, `--shadow` | đường kẻ, thẻ |
| `--overlay-rgb` | màu lớp phủ đọc chữ trên ảnh (dạng `r,g,b`) |
| `--radius`, `--margin` | bo góc, lề |
| `--cta-arrow`, `--wt-color` (tùy chọn) | màu mũi tên trong nút, màu phần thường của tên hai màu |

Kiểm tra tương phản chữ/nền ≥ 4.5:1 (thân) và ≥ 3:1 (chữ lớn).

## 5. Tài sản
- Logo: ưu tiên SVG hoặc PNG nền trong suốt, có bản trắng nếu dùng trên nền tối.
- Chỉ đưa vào repo những gì được phép công khai. Ảnh có khách / học viên / người ngoài → `assets/anh-that/` (bị git-ignore), ghi cách lấy vào `assets/anh-that/DOC-TOI.md`.
- Ảnh người cần tách nền: `scripts/tach_nen.py` (xem `cong-cu-anh.md`).

## 6. Mẫu
1. Bắt đầu từ 7 mẫu trong `_mau/templates/` (bài 4:5, sự kiện 4:5, trích dẫn 1:1, carousel bìa + nội dung 1:1, story 9:16, quảng cáo có CTA). Tất cả link `../tokens.css` rồi `../../../core/core.css`.
2. Thay chữ trong `[ ]`, chỉnh bố cục trong `<style>` cục bộ, KHÔNG sửa `core/core.css` cho riêng một thương hiệu (thêm CSS riêng vào `brands/<ten-brand>/templates/_<ten>.css` nếu cần).
3. Render thử (`scripts/preview.sh`), mở PNG ra nhìn, gửi chủ thương hiệu duyệt. Bản được duyệt = mẫu chuẩn; ghi tên file vào bảng mục 6 của `brand.md`.

## 7. Dùng
```bash
bash scripts/khoi-tao-du-an.sh --brand <ten-brand> ~/Downloads/thiet-ke-<ten-brand>
```
Rồi làm theo `references/quy-trinh.md`. Brand pack có thể có CSS riêng đã duyệt (file `_*.css` trong `templates/` của pack); khi đó mẫu của pack không cần `core/`.


## 8. Chia sẻ brand pack trong đội (riêng tư, bằng .zip)
Repo công khai chỉ chứa khung `brands/_mau/`. `.gitignore` bỏ qua mọi `brands/*` khác, nên pack của bạn (logo, ảnh người thật, quy tắc nội bộ) không bao giờ bị commit nhầm. Chia sẻ pack cho đồng đội như sau:

**Đóng gói (người giữ pack)** — gốc file zip là thư mục `<ten-brand>/` chứa `brand.md`:
```
<ten-brand>-brand-pack.zip
└── <ten-brand>/
    ├── brand.md
    ├── tokens.css
    ├── assets/            logo, nền, ảnh tách nền
    │   └── anh-that/      (tùy chọn) ảnh thật đã được phép dùng, giữ thư mục con như clean/
    └── templates/         mẫu HTML + CSS riêng của pack (_*.css)
```
```bash
cd brands && zip -r ../<ten-brand>-brand-pack.zip <ten-brand> -x "<ten-brand>/output/*"
# Windows PowerShell: Compress-Archive -Path brands\<ten-brand> -DestinationPath <ten-brand>-brand-pack.zip
```
Gửi file qua kênh nội bộ (Drive nội bộ, ổ chung…), không đăng công khai, không commit.

**Cài (thành viên)**:
```bash
python scripts/nap_tu_lieu.py --brand <ten-brand> "<đường dẫn>/<ten-brand>-brand-pack.zip"
```
- Nguồn có `brand.md` (ở gốc, trong `<x>/` hoặc `brands/<x>/`) → cài toàn bộ pack vào `brands/<ten-brand>/`, gộp và ghi đè file trùng tên (file bạn tự thêm vẫn giữ).
- Nguồn không có `brand.md` → coi là gói ảnh, chép ảnh vào `brands/<ten-brand>/assets/anh-that/`.
- Script dò tham chiếu trong `templates/` (ảnh, CSS, `../../../core/core.css`) và báo tệp còn thiếu, hoặc "Có thể thiết kế ngay".

Mẫu của pack dùng đường dẫn tương đối (`../assets/…`, `../tokens.css`, `../../../core/core.css`, `_ten.css` cùng thư mục) nên chạy được ngay sau khi cài. CSS chỉ dành cho một thương hiệu phải nằm trong pack (`templates/_*.css`), không thêm vào `core/core.css`.

Pack có bản mới → đóng gói lại và gửi lại; mọi người chạy lại lệnh cài.
