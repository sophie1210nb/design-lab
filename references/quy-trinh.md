# Quy trình: brief → khổ → mẫu → xem nhanh → render & version → QC → xuất

## 0. Xác định thương hiệu
- Người dùng nhắc tên thương hiệu / chương trình / sản phẩm → tìm `brands/<brand>/` tương ứng (đối chiếu tên pack và dòng đầu `brand.md`).
- Có pack → đọc **toàn bộ** `brands/<brand>/brand.md` trước khi làm; quy tắc trong đó thắng mọi mặc định của skill.
- Chưa có pack nhưng đội có brand pack riêng (.zip / thư mục) → cài: `python scripts/nap_tu_lieu.py --brand <tên> <file.zip>`.
- Chưa có pack nào → `references/tao-brand-moi.md` (hỏi vài câu hoặc rút từ tài liệu tham khảo) rồi mới thiết kế.
- Dự án có file bối cảnh riêng mới hơn `brand.md` → file đó là nguồn sự thật; cập nhật lại `brand.md` sau.

## 1. Brief
Ghi rõ: mã ấn phẩm (vd `P07`, `AD16`, `M08`), kênh (fanpage nào / quảng cáo / in), loại ấn phẩm, số ảnh, nội dung chữ đã duyệt, có chạy quảng cáo không, hạn giao.
- Đối chiếu mọi dữ kiện (tên, chức danh, ngày, con số) với `brand.md`.
- Thiếu dữ kiện → để `[ ]` trên ảnh và báo "cần bổ sung". Không bịa số liệu, lời trích, tên người. Lời trích phải có nguồn.

## 2. Chọn khổ
Theo `references/kich-thuoc-an-pham.md` (bài 1 ảnh = 3 khổ; nhiều ảnh theo cách Facebook dàn; quảng cáo; ảnh bìa; in ấn).

## 3. Dự án làm việc + chép mẫu
Không sửa thẳng trong thư mục skill.
```bash
bash <skill>/scripts/khoi-tao-du-an.sh --brand <brand> ~/Downloads/thiet-ke-<brand>
```
Kết quả:
```
thiet-ke-<brand>/
  core/                      CSS dùng chung (core.css)
  brands/<brand>/brand.md    DNA thương hiệu
  brands/<brand>/tokens.css  màu, font
  brands/<brand>/assets/     logo, nền; anh-that/ cho ảnh thật (không commit)
  brands/<brand>/templates/  HTML làm việc — sửa ở đây
  brands/<brand>/output/     PNG xuất ra
  .git                       repo lưu version
```
Mẫu dùng đường dẫn tương đối `../assets/…`, `../tokens.css`, `../../../core/core.css` nên phải giữ nguyên cấu trúc này.

Copy mẫu gần nhất, đặt tên `<mã>-<chủ đề>-<khổ>.html` (vd `ad16-gia-tri-4x5.html`). Tên cố định, KHÔNG hậu tố version (git lo version). Carousel: `m04-chu-de-01-1x1.html`, `…-02-1x1.html`. Quy ước riêng (vd đuôi `-ads` cho bài kiêm quảng cáo) ghi trong `brand.md`.

Sửa chữ và vị trí trong `<style>` cục bộ của file; không sửa CSS dùng chung cho một ảnh lẻ. Làm khổ chính (thường 4:5) trước, duyệt xong mới chuyển 1:1 và 9:16 (giữ cùng lề, cùng thứ tự đọc).

## 4. Xem nhanh (không lưu version)
```bash
bash <skill>/scripts/preview.sh brands/<brand>/templates/<ten>.html 1080 1350
# → brands/<brand>/output/preview/<ten>.png (scale 1)
```
Mở PNG ra NHÌN ở cỡ feed. Chỉ render bản giao khi đã qua checklist (mục 6).

## 5. Render bản giao + version git
```bash
bash <skill>/scripts/render-social.sh brands/<brand>/templates/<ten>.html <W> <H> "<mô tả thay đổi>" [nhóm-carousel]
```
- Xuất `brands/<brand>/output/<ten>.png` (scale 2 → 2160 px rộng cho khổ 1080).
- Trong repo git: tự `git add` HTML + PNG + `_*.css`/`_*.js` cùng thư mục, commit "`<ten> vN: <mô tả>`", gắn tag `<ten>-vN`.
- Carousel: render từng ảnh, truyền tên nhóm ở ảnh CUỐI để tag cả bộ, vd `m04-chu-de-1x1`.
- Biến môi trường: `OUT_DIR=…`, `SCALE=1|2|3`, `NO_GIT=1`, `CHROME=…` (đường dẫn Chrome nếu không tự tìm thấy).
- Cần mạng (Google Fonts). Mỗi lúc chỉ MỘT tiến trình render trong cùng repo — chạy song song làm tag lệch commit.
- In ấn: dựng ở 150 dpi rồi `SCALE=2` → 300 dpi (xem `kich-thuoc-an-pham.md`).

Xem version: `git tag -l "<ten>-v*"` · `git log --oneline -- "brands/<brand>/output/<ten>.png"`.

Khôi phục (không mất version nào — bản khôi phục thành vN+1):
```bash
bash <skill>/scripts/khoi-phuc.sh <ten-hoac-nhom> vN brands/<brand>/templates
```

## 6. QC
Checklist chung ở `references/nguyen-tac-thiet-ke.md` mục cuối + checklist riêng trong `brand.md`. Mở PNG, phóng to chỗ dấu tiếng Việt, chữ gradient, mép ảnh người, nút CTA. Font hiện dạng Times/Arial → mất mạng hoặc font chưa tải kịp: render lại.

## 7. Xuất & giao
- Một thư mục xuất duy nhất (`output/`), mỗi ảnh một bản, không tạo bản copy đổi tên.
- Giao PNG (hoặc PDF khi in) cho người phụ trách. Nếu dự án có script đồng bộ lên kho ảnh của khách, script đó nằm NGOÀI repo này (chứa ID thư mục, thông tin đăng nhập) — không đưa ID, token, link nội bộ vào skill.
- Quyết định mới của khách → ghi ngay vào `brand.md` (có ngày).
