# Design Lab — skill thiết kế ấn phẩm đa thương hiệu

Skill cho Claude Code để **tự thiết kế ấn phẩm theo đúng thương hiệu của mình**: ảnh bài đăng (1:1, 4:5, 9:16), carousel/album, ảnh quảng cáo Meta có nút CTA, ảnh bìa fanpage, poster, flyer A4/A5, danh thiếp, banner, slide.

Mỗi ấn phẩm là một file HTML/CSS → render PNG bằng Chrome headless → lưu version bằng git (khôi phục được mọi bản cũ).

Đây là **repo chung, không gắn thương hiệu nào**: phần quy trình, kích thước, nguyên tắc và CSS thành phần dùng cho mọi thương hiệu. Mỗi đội / mỗi khách có một **brand pack** riêng — "DNA thương hiệu thiết kế" để cả đội cùng theo. Repo chỉ có khung `brands/_mau/`; brand pack thật được chia sẻ riêng dưới dạng file .zip.

Phiên bản: **v1.0.0** (06/10/2026) — xem `CHANGELOG.md`.

## Điểm mạnh nhất: Bộ quy tắc thiết kế social post
`references/quy-tac-social-post.md` — bộ quy tắc thực hành, có số đo cụ thể, không gắn thương hiệu, Claude đọc cho mọi ảnh social/quảng cáo:
- **Nền tảng & khổ**: Facebook, Instagram, LinkedIn, TikTok/Reels/Shorts, Zalo OA, YouTube thumbnail; feed 1:1/4:5, story 9:16, link 1.91:1, ảnh bìa; Facebook dàn bài 2/3/4/5+ ảnh và ảnh nào bị phủ "+N".
- **Vùng an toàn**: story/reels (250 px trên, 340 px dưới, cột nút bên phải), ảnh đại diện đè bìa, cách từng nền tảng cắt ảnh.
- **Một giây đầu**: một điểm nhìn, hook 6–10 chữ, tỉ lệ chữ/ảnh.
- **Chữ**: cỡ tối thiểu trên khổ 1080, độ dài dòng, tối đa 2 font, **quy tắc riêng cho tiếng Việt** (font đủ dấu, line-height, không giãn chữ thường, tránh IN HOA câu dài, `&nbsp;`), số lining, không đậm giả.
- **Bố cục, màu, tương phản** (WCAG, 60-30-10, chữ trên ảnh chỉ dùng gradient sau chữ, không phủ mặt), **ảnh người thật** (ánh mắt, headroom, nhiều người cùng cỡ, khi nào tách nền trông giả).
- **15 mẫu nội dung**: trích dẫn, thông báo, sự kiện, FAQ, trước/sau, danh sách, con số, testimonial, so sánh, timeline, đếm ngược, thẻ sản phẩm…; **carousel**; **nút CTA**; **quảng cáo Meta** (sáng tạo là nhắm chọn, 3 khổ, primary text, thử biến thể, chính sách); **accessibility**; **hệ thống nhất quán**.
- **Checklist QC 31 mục** trước khi xuất và **20 lỗi thường gặp**.

Mẫu minh họa chạy được trong `brands/_mau/templates/`: `post-4x5`, `event-4x5`, `quote-1x1`, `carousel-01-1x1` + `carousel-02-1x1`, `story-9x16` (có lưới vùng an toàn), `ad-cta-4x5`.

## Cài đặt
**Cách 1 — clone repo** (dễ cập nhật):
```bash
git clone <URL repo> ~/.claude/skills/design-lab
```
(Windows: `%USERPROFILE%\.claude\skills\design-lab`)

**Cách 2 — file `.skill`**: giải nén `design-lab.skill` (file zip) vào `~/.claude/skills/`.

Khởi động lại Claude Code. Thử: *"Thiết kế ảnh bài đăng 4:5 cho thương hiệu …"* — Claude sẽ tự dùng skill.

## Yêu cầu
- **Google Chrome** (render headless). Script tự tìm; nếu không thấy, đặt `CHROME=<đường dẫn chrome>`.
- **Git Bash** (Windows) hoặc bash (macOS/Linux) + **git**.
- **Internet** khi render (Google Fonts).
- **Python 3 + Pillow** (`pip install pillow`).
- Tùy chọn: `rembg` (tách nền), `onnxruntime numpy opencv-python-headless` + mô hình LaMa (xóa chữ trong ảnh) — xem `references/cong-cu-anh.md`.

## Sơ đồ thư mục
```
design-lab/
├── SKILL.md                   quy trình chung (Claude đọc)
├── README.md · CHANGELOG.md
├── references/                quy-tac-social-post (bộ quy tắc chính) · quy-trinh · kich-thuoc-an-pham ·
│                              nguyen-tac-thiet-ke · tao-brand-moi · cong-cu-anh
├── core/core.css              thành phần dùng chung chạy bằng biến CSS (thẻ, chip, CTA, tên hai màu, thẻ thông tin, lower-third…)
├── scripts/                   khoi-tao-du-an.sh --brand · preview.sh · render-social.sh · khoi-phuc.sh ·
│                              nap_tu_lieu.py (cài brand pack / gói ảnh) · xoa_chu_anh.py · tach_nen.py
└── brands/
    ├── _mau/                  brand pack khởi đầu: brand.md (câu hỏi để điền), tokens.css trung tính, 7 mẫu
    └── <brand>/               brand pack riêng của bạn (cài từ .zip — đã .gitignore, không bao giờ bị commit)
```

## Bắt đầu nhanh
```bash
S=~/.claude/skills/design-lab
# 1. Tạo dự án làm việc cho một thương hiệu (vd từ khung _mau)
bash $S/scripts/khoi-tao-du-an.sh --brand _mau ~/Downloads/thiet-ke-thu
cd ~/Downloads/thiet-ke-thu
# 2. Copy một mẫu, đổi tên, sửa chữ
cp brands/_mau/templates/post-4x5.html brands/_mau/templates/p01-ra-mat-4x5.html
# 3. Xem nhanh (scale 1, không git)
bash $S/scripts/preview.sh brands/_mau/templates/p01-ra-mat-4x5.html 1080 1350
# 4. Render bản giao (scale 2) + lưu version git
bash $S/scripts/render-social.sh brands/_mau/templates/p01-ra-mat-4x5.html 1080 1350 "bản đầu"
# 5. Khôi phục bản cũ nếu cần
bash $S/scripts/khoi-phuc.sh p01-ra-mat-4x5 v1 brands/_mau/templates
```
Hoặc chỉ cần nói với Claude: *"Làm ảnh quảng cáo 3 khổ cho thương hiệu X, hook '…', dùng ảnh thật của diễn giả"*.

## Thêm thương hiệu của mình
1. Chép khung: `cp -R brands/_mau brands/<ten-brand>` (chữ thường, không dấu, gạch ngang).
2. Điền `brands/<ten-brand>/brand.md` — tên ghi thế nào, người xem, màu, font, logo, ảnh, CTA, điều cấm, những kiểu đã bị bác (kèm ngày).
3. Sửa `tokens.css` (màu, font — giữ nguyên tên biến), thay logo trong `assets/`.
4. Render các mẫu trong `templates/` bằng `scripts/preview.sh`, chỉnh tới khi chủ thương hiệu duyệt.
5. Từ đó: `bash scripts/khoi-tao-du-an.sh --brand <ten-brand> <thư-mục>` cho mỗi đợt thiết kế.

Không muốn tự điền? Nói với Claude: *"Tạo brand pack cho thương hiệu X"* và đưa logo / ảnh ấn phẩm cũ — Claude hỏi vài câu rồi tạo pack. Chi tiết: `references/tao-brand-moi.md`.

## Chia sẻ brand pack riêng trong đội (.zip)
Brand pack chứa logo, ảnh người thật, quy tắc nội bộ — **không đưa lên repo công khai**. `.gitignore` đã bỏ qua mọi `brands/*` trừ `brands/_mau/`, nên pack của bạn không thể bị commit nhầm.

**Người giữ pack — đóng gói:** nén thư mục `brands/<ten-brand>/` thành một file .zip (gốc zip là thư mục `<ten-brand>/` chứa `brand.md`; có thể kèm ảnh thật trong `<ten-brand>/assets/anh-that/`). Gửi file qua kênh nội bộ (Drive nội bộ, ổ chung…), không đăng công khai.

**Thành viên — cài pack:**
```bash
python scripts/nap_tu_lieu.py --brand <ten-brand> "<đường dẫn tới file .zip hoặc thư mục>"
```
- Nguồn có `brand.md` (ở gốc, trong `<x>/` hoặc `brands/<x>/`) → **brand pack**: cài toàn bộ (brand.md, tokens.css, assets/, templates/…) vào `brands/<ten-brand>/`, gộp và ghi đè file trùng tên.
- Nguồn không có `brand.md` → **gói ảnh**: chép ảnh vào `brands/<ten-brand>/assets/anh-that/` (giữ thư mục con, vd `clean/`).
- Sau khi cài, script dò các mẫu trong `templates/` và báo ảnh còn thiếu, hoặc "Đủ ảnh… Có thể thiết kế ngay".

Pack có bản mới (thêm mẫu, thêm ảnh, quy tắc mới)? Nhận file .zip mới và chạy lại lệnh trên — file mới ghi đè file cũ, file bạn tự thêm vẫn giữ.

## Giấy phép sử dụng
Mã nguồn (HTML/CSS/script/tài liệu) dùng chung được. Logo, ảnh và nhận diện trong brand pack của bạn thuộc về thương hiệu của bạn.
