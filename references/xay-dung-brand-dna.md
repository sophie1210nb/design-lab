# Xây dựng Brand DNA & hệ thị giác

Brand pack chỉ tốt khi DNA bên dưới rõ. Trước khi làm ấn phẩm đầu tiên cho một thương hiệu mới, đi một trong hai lộ trình dưới đây:

| Tình huống | Lộ trình |
|---|---|
| Đã có logo, bài đăng cũ, website, guideline (dù chưa đồng bộ) | **A. Khai thác visual có sẵn** (brand audit) |
| Mới thành lập / muốn làm lại nhận diện / chỉ có cái tên | **B. Xây Brand DNA từ đầu** |
| Có ít tư liệu, chưa chắc giữ hay bỏ | A trước để xem có gì đáng giữ, rồi B cho phần còn thiếu |

Cả hai lộ trình kết thúc giống nhau: **`brand.md` đủ mục, `tokens.css`, bảng nhận diện `brand-board` đã duyệt, 3–7 mẫu đầu tiên** (mục 4).

Nguyên tắc chung:
- Hỏi ít, hỏi một lượt. Cái gì suy ra được từ tư liệu thì không hỏi.
- Không bịa: thiếu dữ kiện → `[ ]` + câu hỏi. Không gán cho thương hiệu sứ mệnh, con số, khách hàng mà người dùng chưa nói.
- Mọi lựa chọn thị giác phải giải thích được bằng DNA ("vì thương hiệu *tiết chế, tin cậy* nên…"). Không chọn theo sở thích cá nhân.
- Cho người dùng **xem bằng mắt** (ảnh render), không chỉ mô tả bằng chữ.

---

## Lộ trình A — Khai thác visual có sẵn

### A1. Gom tư liệu
Xin trong một tin nhắn:
- Logo file gốc (SVG/AI/PDF, PNG nền trong) + các biến thể.
- Guideline cũ nếu có (PDF, slide).
- 6–12 ấn phẩm đã đăng mà họ **thích nhất** và 2–3 cái họ **không thích** (chụp màn hình fanpage/IG là đủ).
- Link website / landing (người dùng chụp màn hình phần đầu trang nếu không truy cập được).
- Ấn phẩm in, bao bì, slide nếu có.

Đặt tất cả vào một thư mục, vd `brands/<ten-brand>/_tu-lieu/` (thư mục này bị git-ignore cùng pack).

### A2. Trích xuất tự động
```bash
python scripts/trich_xuat_brand.py brands/<ten-brand>/_tu-lieu --logo brands/<ten-brand>/assets/logo.png --out brands/<ten-brand>
```
Script tạo:
- `brand-audit.md` — bảng màu chung (mã HEX, tỉ lệ diện tích, độ sáng, độ bão hòa), màu theo từng ảnh, vai trò gợi ý (nền / chữ / nhấn / phụ), tỉ lệ tương phản các cặp chính, nhận xét nền sáng hay tối, rực hay trầm, mức độ đồng nhất giữa các ảnh.
- `tokens-goi-y.css` — bản `tokens.css` đã điền màu gợi ý (font giữ mặc định để bạn chọn ở A3).

Script chỉ **gợi ý**. Màu lấy từ ảnh chụp bị ảnh hưởng bởi ảnh người, nén JPG, ánh sáng → luôn nhìn lại và chốt bằng mắt; ưu tiên mã màu trong logo gốc/guideline nếu có.

### A3. Phân tích bằng mắt (điền vào `brand-audit.md`, mục "Nhận định")
1. **Màu**: màu nào lặp lại có chủ đích (logo, nền, nút) và màu nào chỉ là màu ảnh? Có bao nhiêu màu nhấn đang tranh nhau?
2. **Chữ**: nhóm kiểu chữ (serif cổ điển / serif hiện đại / sans hình học / sans nhân văn / viết tay / display). Ghi font **Google Fonts có tiếng Việt** gần nhất (bảng mục 3.3). Ghi số cỡ chữ đang dùng — nhiều hơn 3–4 cỡ là dấu hiệu rối.
3. **Logo**: có bản trên nền tối/sáng không, vùng an toàn, cỡ tối thiểu.
4. **Bố cục lặp lại**: vị trí logo, lề, chỗ đặt tiêu đề, kiểu nút CTA, khung/thẻ, họa tiết.
5. **Hình ảnh**: ảnh thật hay đồ họa, ánh sáng, màu ảnh (ấm/lạnh), cách cắt người, có tách nền không.
6. **Giọng chữ trên ảnh**: dài/ngắn, xưng hô, in hoa, emoji.
7. **Bất nhất**: liệt kê chỗ các ấn phẩm "nói khác nhau" (3 màu xanh khác nhau, 4 font…).

### A4. Kết luận audit: Giữ – Chuẩn hóa – Bỏ
| Nhóm | Giữ (đang tạo nhận diện) | Chuẩn hóa (giữ ý nhưng chốt 1 giá trị) | Bỏ (gây rối / lệch DNA) |
|---|---|---|---|
| Màu | | | |
| Chữ | | | |
| Bố cục | | | |
| Ảnh | | | |

Gửi bảng này + bảng nhận diện `brand-board` (mục 4.2) cho người dùng duyệt. Phần DNA "lõi" (mục B1) nếu chưa có thì hỏi bổ sung bằng bộ câu hỏi rút gọn ở B1.

---

## Lộ trình B — Xây Brand DNA từ đầu

### B1. Phỏng vấn lõi thương hiệu (một lượt, 8 câu)
1. **Tên & cách ghi**: tên đầy đủ, viết tắt, viết hoa thế nào? Tagline (nếu có)?
2. **Giúp ai, làm gì**: khách hàng chính là ai (nghề, độ tuổi, hoàn cảnh)? Họ đang gặp vấn đề gì?
3. **Khác biệt**: vì sao chọn bạn mà không chọn cách khác? (1–2 lý do thật, không phải "chất lượng tốt").
4. **Lời hứa**: sau khi dùng sản phẩm/dịch vụ, khách hàng có được điều gì?
5. **Tính cách**: 3–5 tính từ mô tả thương hiệu nếu nó là một người. Và 2–3 tính từ nó **không bao giờ** là.
6. **Tham chiếu**: 2–3 thương hiệu/ấn phẩm (bất kỳ ngành) bạn thấy "đúng chất", và 1–2 cái bạn thấy "không phải mình".
7. **Người xem thấy ấn phẩm ở đâu**: điện thoại, in, màn hình lớn, quảng cáo?
8. **Ràng buộc**: màu/biểu tượng đã có và phải giữ, điều cấm (ngành nghề, văn hóa, pháp lý), người cần xuất hiện (chủ doanh nghiệp, chuyên gia…)?

### B2. Định vị tính cách (chấm thang 1–5 cùng người dùng hoặc suy ra từ B1)
| Thang | 1 | ← → | 5 |
|---|---|---|---|
| Cổ điển ↔ Hiện đại | di sản, bền vững | | mới, công nghệ |
| Sang trọng ↔ Gần gũi | cao cấp, tiết chế | | thân thiện, đời thường |
| Nghiêm túc ↔ Vui tươi | chuyên gia, chuẩn mực | | hài hước, năng lượng |
| Tối giản ↔ Giàu chi tiết | khoảng trống, ít yếu tố | | họa tiết, nhiều lớp |
| Trầm ↔ Rực | màu tối, ít bão hòa | | màu sáng, bão hòa cao |
| Lý trí ↔ Cảm xúc | số liệu, cấu trúc | | câu chuyện, con người |

Có thể đối chiếu thêm 12 nguyên mẫu thương hiệu (Người thông thái, Người anh hùng, Người chăm sóc, Nhà sáng tạo, Người cai trị, Người khám phá, Người ngây thơ, Kẻ nổi loạn, Nhà ảo thuật, Người tình, Người bình thường, Kẻ pha trò) — chọn 1 chính, tối đa 1 phụ. Chỉ là công cụ gợi ý, không bắt buộc.

### B3. Dịch tính cách → hệ thị giác
| Tính cách | Màu | Chữ | Hình khối & bố cục | Ảnh |
|---|---|---|---|---|
| Sang trọng, tiết chế | nền tối sâu hoặc kem; 1 kim loại (vàng, đồng) làm nhấn | serif tương phản cao cho tiêu đề + sans gọn | nhiều khoảng trống, đường kẻ mảnh, căn giữa | ánh sáng mềm, ít người, chất liệu |
| Tin cậy, chuyên gia | xanh navy/xanh dương, xám ấm | sans nhân văn hoặc serif đọc tốt | lưới rõ, thẻ thông tin, số liệu nổi | chân dung chuyên gia, môi trường làm việc thật |
| Hiện đại, công nghệ | nền sáng trắng/xám hoặc tối đen; nhấn điện tử (xanh lam, tím, xanh ngọc) | sans hình học | lưới chặt, khối hình học, ảnh chụp màn hình | sạch, sắc nét, góc rộng |
| Gần gũi, ấm áp | màu đất, cam, vàng nhạt, xanh lá dịu | sans bo tròn hoặc serif mềm | bo góc lớn, hình hữu cơ | ảnh người thật cười, đời thường |
| Năng động, trẻ | 2 màu bão hòa tương phản | sans đậm, cỡ lớn | khối màu lớn, chéo, nhiều nhịp | chuyển động, góc lạ |
| Sáng tạo, nghệ thuật | bảng màu riêng, có thể bất ngờ | display cá tính + sans trung tính | bố cục phá lưới có chủ đích | ảnh nghệ thuật, đồ họa |
| Tự nhiên, bền vững | xanh lá, nâu, be | serif nhẹ hoặc sans nhân văn | khoảng trống, chất liệu giấy | ánh sáng tự nhiên, chất liệu thật |

### B4. Đề xuất 3 hướng thị giác
Mỗi hướng gồm: tên hướng (2–3 chữ) · lý do từ DNA · bảng màu theo **60–30–10** (nền – phụ – nhấn, kèm HEX) · cặp font (có tiếng Việt) · kiểu bố cục · kiểu ảnh · 1 câu "điều không làm".
- **Hướng 1 — An toàn**: sát ngành, dễ chấp nhận.
- **Hướng 2 — Cân bằng**: khác biệt vừa phải (thường được chọn).
- **Hướng 3 — Táo bạo**: khác biệt rõ, rủi ro hơn.

Với mỗi hướng: tạo `tokens-huong-<n>.css`, render `brand-board.html` + 1 mẫu bài 4:5 bằng token đó (mục 4.2), gửi 3 cặp ảnh để người dùng chọn. Cho phép trộn ("màu của hướng 2, font của hướng 1"). Chốt rồi mới viết `tokens.css` chính thức.

---

## 3. Quy tắc chọn màu & chữ (dùng cho cả hai lộ trình)

### 3.1 Màu
- Tối đa **1 màu nhấn chính** + 1 nhấn phụ. Nhấn chỉ dùng cho điều quan trọng nhất (CTA, từ khóa).
- Tỉ lệ **60–30–10**: nền 60, màu phụ (thẻ, khối) 30, nhấn 10.
- Mỗi màu có vai trò cố định (ghi trong `brand.md` mục 2), không dùng màu nhấn làm nền diện rộng trừ khi đó là chủ ý.
- Tương phản: thân chữ ≥ 4.5:1, chữ lớn ≥ 3:1 (script tính sẵn). Chữ trên ảnh dùng lớp phủ `--overlay-rgb`.
- Kiểm tra trên điện thoại ở độ sáng thấp: nền quá tối + chữ xám = không đọc được.

### 3.2 Chữ
- Tối đa **2 họ font**: 1 cho tiêu đề (display), 1 cho thân/nhãn/số liệu.
- Bắt buộc có **subset tiếng Việt** (kiểm tra trên fonts.google.com, mục Language → Vietnamese) và thử chuỗi dấu: `Ầ Ẫ Ậ Ẻ Ễ Ố Ỡ Ợ Ừ Ữ Ự ỳ ỹ đ Đ`.
- Font serif có chữ số kiểu cũ → bật số lining (`font-variant-numeric:lining-nums`).
- Chốt thang cỡ chữ 3–4 bậc cho khổ 1080 (vd tiêu đề 56–72, phụ đề 32–40, thân 24–28, nhãn 16–18).

### 3.3 Cặp font gợi ý (Google Fonts, có tiếng Việt — vẫn kiểm tra lại subset trước khi chốt)
| Cảm giác | Tiêu đề | Thân |
|---|---|---|
| Sang, cổ điển | Playfair Display | Be Vietnam Pro |
| Biên tập, trí thức | Lora / Source Serif 4 | Inter |
| Thanh lịch, mảnh | Cormorant Garamond | Be Vietnam Pro |
| Hiện đại, công nghệ | Space Grotesk / Lexend | Inter |
| Trẻ, năng động | Montserrat (đậm) | Be Vietnam Pro |
| Gần gũi, mềm | Nunito / Quicksand | Nunito |
| Trung tính, đa dụng | Plus Jakarta Sans | Plus Jakarta Sans |
| Truyền thống, trang trọng | Noto Serif / Merriweather | Noto Sans |

### 3.4 Logo
Cần: bản màu, bản trắng (nền tối), bản đen/1 màu; vùng an toàn quanh logo (thường = chiều cao 1 chữ cái của logo); cỡ tối thiểu trên khổ 1080 (thường ≥ 48 px cao). Không kéo méo, không đổ bóng, không đặt lên nền rối.

---

## 4. Đầu ra & duyệt

### 4.1 Ghi vào brand pack
- `brand.md` mục 0 (DNA lõi: định vị, lời hứa, tính cách, thang B2, nguyên mẫu, giọng), mục 1–9 như mẫu.
- `tokens.css` (màu, font, bo góc, lề).
- `brand-audit.md` (lộ trình A) hoặc phần "3 hướng đã đề xuất & lý do chọn" ghi vào mục 9 Nhật ký quyết định.

### 4.2 Bảng nhận diện (brand board)
`brands/<ten-brand>/templates/brand-board.html` (chép từ `_mau`) tự đọc `tokens.css`: logo trên nền sáng/tối, bảng màu 60–30–10 kèm HEX, cặp font + chuỗi thử dấu tiếng Việt, thang cỡ chữ, nút CTA, thẻ, 3 tính từ tính cách. Sửa các ô `[ ]` (tên, tính từ, HEX) rồi render:
```bash
bash scripts/preview.sh brands/<ten-brand>/templates/brand-board.html 1920 1080
```
Đây là trang người dùng duyệt **trước** khi làm ấn phẩm.

### 4.3 Mẫu đầu tiên
Dựng 3–7 mẫu từ `_mau/templates` bằng token mới (tối thiểu: bài 4:5, carousel bìa, story 9:16, ads có CTA). Chạy checklist `quy-tac-social-post.md` mục 14. Bản được duyệt → ghi vào bảng mục 6 của `brand.md`.

### 4.4 Checklist chốt DNA
- [ ] Một câu định vị + lời hứa, không chung chung.
- [ ] 3–5 tính từ tính cách + 2–3 "không bao giờ là".
- [ ] Màu: vai trò từng màu, 1 nhấn chính, tương phản đạt.
- [ ] Font: 2 họ, có tiếng Việt, đã thử chuỗi dấu, có thang cỡ chữ.
- [ ] Logo: các biến thể, vùng an toàn, cỡ tối thiểu.
- [ ] Ảnh: phong cách, cách cắt người, điều cấm.
- [ ] Brand board + ít nhất 3 mẫu đã được chủ thương hiệu duyệt (ghi ngày).
