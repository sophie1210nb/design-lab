---
name: design-lab
description: Design Lab - bộ quy trình + mẫu HTML/CSS để thiết kế ấn phẩm theo đúng thương hiệu — ảnh social (bài 1 ảnh, carousel, album, story/reels), ảnh quảng cáo Meta có CTA, ảnh bìa fanpage, poster, flyer, tờ rơi A4/A5, danh thiếp, banner, slide — render PNG bằng Chrome headless và lưu version bằng git. Đa thương hiệu, mỗi thương hiệu có một brand pack (DNA thương hiệu) trong brands/. DÙNG SKILL NÀY mỗi khi người dùng muốn thiết kế ấn phẩm, làm ảnh post, ảnh quảng cáo, carousel, ảnh bìa, poster, flyer theo thương hiệu; đổi khổ 1:1/4:5/9:16; thêm nút CTA; khôi phục version ảnh; kiểm tra ảnh có đúng nhận diện không; tạo bộ nhận diện thiết kế cho thương hiệu mới; hoặc cài brand pack riêng (.zip) của một đội. Việc đầu tiên luôn là xác định thương hiệu - có brands/ten-brand thì theo đúng brand.md; chưa có thì cài brand pack riêng (scripts/nap_tu_lieu.py) hoặc tạo mới từ brands/_mau (references/tao-brand-moi.md).
---

# Design Lab — thiết kế ấn phẩm theo thương hiệu

Mỗi ấn phẩm = một file HTML/CSS → render PNG bằng Chrome headless → mỗi lần sửa là một version git khôi phục được. Skill tách làm hai lớp:
- **Chung** (mọi thương hiệu): quy trình, kích thước, nguyên tắc thiết kế, CSS thành phần `core/core.css`, script.
- **Brand pack** `brands/<brand>/`: DNA thương hiệu (`brand.md`), token màu/font (`tokens.css`), tài sản, mẫu đã duyệt. Đội nào cũng theo đúng pack của mình.

Repo công khai chỉ có khung `brands/_mau/`. Brand pack thật của từng đội là tài sản riêng: chia sẻ nội bộ dưới dạng file .zip và cài bằng `scripts/nap_tu_lieu.py` (thư mục `brands/<brand>/` đã được `.gitignore`, không bao giờ bị đẩy lên repo).

## Bộ quy tắc thiết kế social post — BẮT BUỘC
Mọi việc thiết kế ảnh mạng xã hội / quảng cáo (post, carousel, story, reels, ảnh bìa, thumbnail, ads): **đọc `references/quy-tac-social-post.md` trước khi dựng** và **chạy checklist QC mục 14 của file đó trước khi giao**. File gồm: khổ & vùng an toàn từng nền tảng, một giây đầu, chữ (gồm tiếng Việt), bố cục, màu & tương phản, ảnh người thật, 15 mẫu nội dung, carousel, CTA, quảng cáo Meta, accessibility, hệ thống nhất quán, 20 lỗi thường gặp. `brand.md` thắng khi khác.

## Bản đồ skill
```
SKILL.md                     quy trình chung (file này)
references/
  quy-tac-social-post.md     BỘ QUY TẮC SOCIAL POST (đọc cho mọi ảnh social/ads) + checklist QC 31 mục
  quy-trinh.md               brief → khổ → mẫu → xem nhanh → render/version → QC → xuất
  kich-thuoc-an-pham.md      khổ & vùng an toàn: FB/IG, story, quảng cáo, ảnh bìa, slide, in ấn
  nguyen-tac-thiet-ke.md     phân cấp, chữ, màu, ảnh người thật, CTA, carousel + checklist QC chung
  tao-brand-moi.md           tạo brand pack mới; đóng gói & chia sẻ brand pack riêng (.zip)
  cong-cu-anh.md             preview/render, xóa chữ (LaMa), tách nền (rembg), cân sáng
core/core.css                thành phần dùng chung chạy bằng biến CSS: thẻ, chip, nút CTA, tên hai màu .wt,
                             ảnh thật + lớp phủ, thẻ thông tin (lưới 2×2), lower-third, khối ảnh đầu carousel
scripts/                     khoi-tao-du-an.sh --brand · preview.sh · render-social.sh · khoi-phuc.sh ·
                             nap_tu_lieu.py (cài brand pack / gói ảnh) · xoa_chu_anh.py · tach_nen.py
brands/
  _mau/                      brand pack khởi đầu (brand.md để điền, tokens trung tính, 7 mẫu theo kiểu nội dung)
  <brand>/                   brand pack riêng của đội (cài từ .zip, không commit)
```

## Bước 0 — Xác định thương hiệu (luôn làm trước)
1. Tìm tên thương hiệu / chương trình / sản phẩm trong yêu cầu. Liệt kê `brands/` để đối chiếu (tên pack, dòng đầu của từng `brand.md`).
2. **Có `brands/<brand>/`** → đọc TOÀN BỘ `brands/<brand>/brand.md` trước khi làm. Quy tắc trong đó (tên, màu, font, ảnh, CTA, danh sách đã bị bác) thắng mọi mặc định của skill. Nếu dự án có file bối cảnh mới hơn, file đó là nguồn sự thật — làm theo rồi cập nhật lại `brand.md`.
3. **Chưa có pack, nhưng đội đã có brand pack riêng (.zip / thư mục)** → cài trước:
   `python scripts/nap_tu_lieu.py --brand <tên> <file .zip hoặc thư mục>`
   Script cài cả pack vào `brands/<tên>/` và báo mẫu nào còn thiếu ảnh. Hỏi người dùng đường dẫn file nếu họ nhắc tới pack mà chưa cài.
4. **Chưa có pack nào** → làm theo `references/tao-brand-moi.md`: rút DNA từ tài liệu người dùng đưa (logo, guideline, ấn phẩm cũ) hoặc hỏi một lượt ngắn (tên ghi thế nào, người xem, màu/font/logo, nhân vật, điều cấm, điều không thích). Tạo `brands/<brand>/` từ `_mau`, render thử, cho duyệt — rồi mới làm ấn phẩm thật.
5. Không rõ thương hiệu → hỏi. Không tự áp DNA của thương hiệu này cho thương hiệu khác.

## Bước 1 — Brief
Mã ấn phẩm, kênh, loại ấn phẩm, số ảnh, nội dung chữ đã duyệt, có chạy quảng cáo không. Đối chiếu dữ kiện với `brand.md`. Thiếu → `[ ]` + "cần bổ sung". **Không bịa** số liệu, lời trích, chức danh, tên người.

## Bước 2 — Chọn khổ (`references/quy-tac-social-post.md` mục 1–2, `references/kich-thuoc-an-pham.md`)
| Ấn phẩm | Khổ (W × H) |
|---|---|
| Bài 1 ảnh | đủ 3 khổ: 1:1 1080×1080 · 4:5 1080×1350 · 9:16 1080×1920 |
| 2 / 3 / 4 ảnh | 1:2 1080×2160 hoặc 2:1 2160×1080 (+ vuông) — theo cách Facebook dàn ảnh |
| 5+ ảnh (carousel, album) | toàn 1:1; ảnh 1–2 mạnh nhất; gọn 3–5 ảnh |
| Quảng cáo Meta | 1:1 + 4:5 + 9:16, một nút CTA |
| Ảnh bìa fanpage | 1640×624; nội dung trong x 266→1374 |
| Story / reels | 1080×1920; nội dung trong y 250→1580 (reels: tránh thêm đáy chú thích + cột phải) |
| Slide | 1920×1080 |
| In A4 / A5 | 1240×1754 / 874×1240 (150 dpi, render ×2 = 300 dpi) + lề xén 3 mm |

## Bước 3 — Dựng từ mẫu
1. Tạo dự án làm việc (không sửa trong thư mục skill):
   `bash <skill>/scripts/khoi-tao-du-an.sh --brand <brand> <thư-mục-dự-án>`
   → `<dự án>/core/` + `<dự án>/brands/<brand>/{brand.md, tokens.css, assets/, templates/, output/}` + git.
2. Ảnh thật (có người ngoài) chép vào `brands/<brand>/assets/anh-that/` — không commit lên repo công khai.
3. Copy mẫu gần nhất trong `templates/` (bảng mẫu ở `brand.md`; pack chưa có kiểu đó → lấy mẫu cùng kiểu trong `brands/_mau/templates/` rồi áp tokens của pack), đặt tên `<mã>-<chủ đề>-<khổ>.html`. Bố cục theo mẫu nội dung tương ứng ở `quy-tac-social-post.md` mục 8.
4. Sửa chữ, vị trí trong `<style>` cục bộ. Không sửa CSS dùng chung cho một ảnh lẻ. Mẫu có nhiều khối `<style>` nối nhau: khối sau ghi đè khối trước — chỉnh ở khối cuối.
5. Bố cục mới:
   - Pack dựa trên core (như `_mau`): link `../tokens.css` → `../../../core/core.css` → `<style>` cục bộ, dùng class core.
   - Pack có CSS riêng đã duyệt (file `_*.css` trong `templates/` của pack): bắt đầu từ mẫu cùng họ của pack, giữ CSS của pack.
6. Làm khổ chính trước, duyệt xong mới chuyển các khổ khác (cùng lề, cùng thứ tự đọc).

## Bước 4 — Xem nhanh, rồi render bản giao
```bash
bash <skill>/scripts/preview.sh brands/<brand>/templates/<ten>.html 1080 1350      # scale 1, không git
bash <skill>/scripts/render-social.sh brands/<brand>/templates/<ten>.html 1080 1350 "mô tả" [nhóm-carousel]
bash <skill>/scripts/khoi-phuc.sh <ten-hoac-nhom> vN brands/<brand>/templates      # lấy lại bản cũ
```
`render-social.sh` xuất `output/<ten>.png` (scale 2), commit + tag `<ten>-vN`. Mỗi lúc chỉ MỘT tiến trình render trong một repo. Chi tiết: `references/quy-trinh.md`.

## Bước 5 — QC: mở PNG ra NHÌN
Chạy **checklist 31 mục trong `references/quy-tac-social-post.md` mục 14** (ảnh social/ads) hoặc checklist chung `references/nguyen-tac-thiet-ke.md` mục 10 (ấn phẩm in), rồi checklist riêng trong `brand.md`. Tóm tắt:
- [ ] Đúng brand pack (tên, font, màu, logo); font tải đúng, dấu tiếng Việt không vỡ, số lining.
- [ ] Một thông điệp, đọc được trong 1 giây ở cỡ điện thoại; thân chữ ≥ 22 px (khổ 1080).
- [ ] Dữ kiện đúng nguyên văn; không còn `[ ]` chưa báo.
- [ ] Ảnh thật màu gốc; lớp phủ chỉ sau chữ, không phủ mặt; không halo, không nhuộm, không cắt dán.
- [ ] Một nút CTA theo quy ước; không SĐT / link form trên ảnh (trừ khi brand cho phép).
- [ ] Bài nhiều ảnh: chỉ ảnh đầu có khối chương trình + CTA; không số trang / vạch tiến trình / "vuốt".
- [ ] Đúng vùng an toàn của khổ; tên file đúng quy ước, có tag version.

## Bước 6 — Xuất & ghi nhận
Giao PNG (PDF khi in) từ một thư mục xuất duy nhất, không bản copy đổi tên. Chủ thương hiệu duyệt / bác điều gì → ghi ngay vào `brand.md` (có ngày, lý do) để lần sau làm đúng ngay. Pack đã cập nhật → đóng gói lại .zip và gửi lại cho đội (xem `references/tao-brand-moi.md` mục 8).

## Luật chung không đổi
1. **Brand pack là luật.** Không trộn DNA giữa các thương hiệu; không tự đổi màu/font/bố cục đã chốt — quyết định thẩm mỹ lớn thì hỏi trước.
2. **Không bịa** dữ kiện, lời trích, chức danh. Lời trích phải có nguồn.
3. **Ảnh người thật giữ như chụp**; chữ đọc được nhờ gradient sau chữ, không bao giờ phủ mặt.
4. **Một thông điệp, một vùng nhấn, một CTA** mỗi ảnh.
5. **Bài nhiều ảnh gọn**, chỉ ảnh đầu có CTA.
6. **Version bằng git**, tên file cố định; không xóa bản cũ.
7. **Quyền riêng tư**: không đưa brand pack riêng, ảnh có người ngoài, số điện thoại, link nội bộ, ID kho ảnh, token vào repo công khai.

## Brand pack
| Pack | Dùng cho | Đặc điểm nhanh |
|---|---|---|
| `_mau` | khung để tạo thương hiệu mới | Tokens trung tính (Noto Serif + Be Vietnam Pro, xanh dương); 7 mẫu: bài thông báo 4:5, sự kiện 4:5, trích dẫn 1:1, carousel bìa + ảnh nội dung 1:1, story 9:16 có lưới vùng an toàn, quảng cáo ảnh thật + CTA 4:5. |
| `<brand>` | brand pack riêng của đội | Cài từ .zip: `python scripts/nap_tu_lieu.py --brand <tên> <file.zip>`. Đọc `brands/<tên>/brand.md`. |

## Tư liệu nội bộ của thương hiệu
Ảnh thật/tư liệu riêng không nằm trong repo công khai. Nếu mẫu cần ảnh mà `brands/<brand>/assets/anh-that/` trống, nhắc người dùng chạy `python scripts/nap_tu_lieu.py --brand <brand> <gói .zip hoặc thư mục>` (gói ảnh hoặc cả brand pack) rồi mới render.
