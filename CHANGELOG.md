# Lịch sử phiên bản

## v1.0.0 — 06/10/2026
Bản công khai đầu tiên của **Design Lab** (`design-lab`): skill thiết kế ấn phẩm **đa thương hiệu**, không gắn với thương hiệu cụ thể nào — để mỗi người / mỗi đội tự thiết kế ảnh theo nhận diện của mình.

### Có gì
- `SKILL.md`: quy trình chung cho mọi thương hiệu, mọi loại ấn phẩm. Bước 0 luôn là xác định thương hiệu → có `brands/<brand>` thì theo đúng `brand.md`; chưa có thì cài brand pack riêng (.zip) hoặc tạo mới từ `brands/_mau`.
- **Bộ quy tắc thiết kế social post** `references/quy-tac-social-post.md` (phần chính): khổ & vùng an toàn từng nền tảng (Facebook, Instagram, LinkedIn, TikTok/Reels/Shorts, Zalo OA, YouTube), một giây đầu, chữ (gồm quy tắc tiếng Việt), bố cục, màu & tương phản, ảnh người thật, 15 mẫu nội dung, carousel, CTA, quảng cáo Meta, accessibility, hệ thống nhất quán, checklist QC 31 mục, 20 lỗi thường gặp, nguồn tham khảo.
- `references/`:
  - `quy-trinh.md` — brief → khổ → mẫu → xem nhanh → render & version → QC → xuất;
  - `kich-thuoc-an-pham.md` — khổ & vùng an toàn: bài đăng FB/IG, story/reels, quảng cáo Meta, ảnh bìa fanpage 1640×624, slide, in A4/A5/A3, danh thiếp, standee;
  - `nguyen-tac-thiet-ke.md` — phân cấp, chữ, màu, ảnh người thật, thông tin & CTA, bài nhiều ảnh + checklist QC chung;
  - `tao-brand-moi.md` — tạo brand pack mới; đóng gói và chia sẻ brand pack riêng dưới dạng .zip;
  - `cong-cu-anh.md` — preview/render, xóa chữ (LaMa), tách nền (rembg), cân sáng hai người.
- `core/core.css`: thành phần không gắn thương hiệu chạy bằng biến CSS — tờ theo khổ (gồm ảnh bìa, A4, A5, slide), vùng an toàn, chữ gradient, tên hai màu `.wt`, thẻ, chip ruy-băng, nút CTA, ảnh thật + lớp phủ chỉ sau chữ, khối đáy xếp chồng, lower-third, thẻ thông tin (lưới 2×2 cho 9:16), khối ảnh đầu carousel. Biến mặc định ở `:where(:root)` nên `tokens.css` của brand luôn thắng.
- `brands/_mau/`: `brand.md` (câu hỏi để điền DNA), `tokens.css` trung tính (Noto Serif + Be Vietnam Pro), logo mẫu SVG, 7 mẫu chạy được: `post-4x5`, `event-4x5`, `quote-1x1`, `carousel-01-1x1`, `carousel-02-1x1`, `story-9x16` (lưới vùng an toàn `show-safe`), `ad-cta-4x5`.
- `scripts/`:
  - `khoi-tao-du-an.sh --brand <tên>` — tạo dự án làm việc giữ cấu trúc `core/` + `brands/<brand>/…`;
  - `preview.sh`, `render-social.sh` (render + commit + tag version), `khoi-phuc.sh`;
  - `nap_tu_lieu.py --brand <tên> <zip|thư mục>` — cài **brand pack riêng** (brand.md, tokens.css, assets/, templates/) hoặc **gói ảnh** vào `brands/<tên>/`, rồi báo mẫu nào còn thiếu ảnh;
  - `xoa_chu_anh.py` (LaMa, mô hình ở `~/.thiet-ke-models/`), `tach_nen.py` (rembg).
- `.gitignore`: bỏ qua mọi `brands/*` trừ `brands/_mau/` — brand pack riêng không bao giờ bị commit nhầm lên repo công khai.
