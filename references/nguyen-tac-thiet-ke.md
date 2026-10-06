# Nguyên tắc thiết kế chung (mọi thương hiệu)

Áp dụng khi `brand.md` không nói khác. Quy tắc của brand pack luôn thắng.
Bản tóm tắt cho mọi loại ấn phẩm (gồm in ấn). Ảnh mạng xã hội / quảng cáo: dùng bộ đầy đủ `quy-tac-social-post.md`.

## 1. Mục tiêu một ấn phẩm
- **Một thông điệp đọc được trong 1 giây** ở cỡ điện thoại. Nếu phải đọc hết mới hiểu → cắt bớt.
- Thứ tự đọc rõ: (1) hook / tiêu đề → (2) bằng chứng (người, ảnh, con số có nguồn) → (3) thông tin cần thiết → (4) hành động (CTA).
- Sang nhờ tiết chế: ít yếu tố, khoảng trống đều, một vùng nhấn lớn mỗi ảnh. Thêm trang trí không cứu được thông điệp yếu.
- Đúng sự thật tuyệt đối: không bịa số liệu, lời trích, chức danh. Thiếu → `[ ]` và hỏi.

## 2. Phân cấp (hierarchy)
- Tối đa 3 cấp cỡ chữ rõ rệt trên một ảnh (tiêu đề ≥ 2× thân; nhãn nhỏ nhất nhưng đậm, in hoa giãn chữ).
- Một màu nhấn cho từ khóa / nhãn / nút; không dùng màu nhấn cho đoạn dài.
- Căn lề nhất quán: chọn căn giữa (ảnh thông tin) hoặc căn trái (ảnh có người, quảng cáo) — không trộn trong một khối.
- Lề ngoài ≥ 56–64 px trên khổ 1080; khoảng cách giữa các khối theo bội số (8/16/24…).

## 3. Chữ
- **Cặp font**: một font tiêu đề có cá tính (serif hoặc display) + một font thân sans dễ đọc. Font phải có đủ dấu tiếng Việt (kiểm tra ẩ, ễ, ỗ, ừ, ợ).
- Serif / display chỉ cho tiêu đề, hook, ngày nổi bật; thân chữ, tên người, nhãn, số liệu dùng sans.
- Cỡ tối thiểu trên khổ 1080: thân **≥ 22 px** (carousel ≥ 28 px), dòng phụ ≥ 17 px, nhãn ≥ 15 px đậm.
- Số trong font serif: bật số lining (`font-variant-numeric:lining-nums; font-feature-settings:"lnum" 1,"onum" 0`) để "5.0" không thành "5.o".
- Không để chữ mồ côi: dùng `&nbsp;` giữ cụm 2 chữ cuối dòng. line-height tiêu đề ≥ 1.04 để dấu không bị cắt; chữ gradient cần `padding-bottom`.
- Chữ gradient (clip text): không thêm `text-shadow` (vỡ hiệu ứng); cần nổi thì dùng `filter:drop-shadow` nhẹ.
- **Tên hai màu** (`.wt` trong core): khi tên thương hiệu nằm trong dòng chữ gradient, bọc phần màu thường bằng `<span class="wt">`.

## 4. Màu & tương phản
- Tương phản chữ/nền ≥ **4.5:1** cho thân chữ, ≥ 3:1 cho chữ lớn. Kiểm tra cả chữ trên ảnh thật (vùng sáng nhất sau chữ).
- Nền tối: tránh đen phẳng #000 — dùng màu nền thương hiệu có chiều sâu (gradient nhẹ). Nền sáng: tránh trắng tinh khi in.
- Thẻ trên nền: cùng họ màu với nền (kính trong / nền sáng hơn một bậc), không chèn một màu lạ.

## 5. Ảnh người thật
- **Giữ ảnh như chụp**: màu gốc, nét. Filter gần trung tính (sáng ~1.0, tương phản ≤ 1.03, bão hòa 1.0).
- Chữ đè lên ảnh: chỉ dùng **gradient màu nền (blend thường) ở phía có chữ**, mờ hết trước khi tới người. **Không bao giờ phủ lên mặt.**
- Không: vầng sáng/halo sau người, lớp nhuộm màu (`mix-blend-mode:color`, multiply đậm) lên da, làm nhòe nền mạnh, cắt người dán sang nền khác (trông giả, "giống AI làm").
- Phóng người đủ to để thấy mặt trên điện thoại (thường ×1.15–1.25 so với ảnh gốc), giữ người ở giữa khung hoặc theo bố cục; đầu không sát mép trên.
- Nhiều người cạnh nhau: cùng cỡ, đầu ngang nhau, độ sáng mặt tương đương.
- Tên + chức danh cạnh người: lower-third chữ trắng có bóng nhẹ, không hộp nặng. Chức danh đúng nguyên văn đã duyệt.
- Ảnh có người ngoài: chỉ dùng khi được phép; không đưa vào repo công khai.

## 6. Thông tin & CTA
- Thông tin chương trình gom vào **một thẻ thông tin** (ngày + 3–4 mục ngắn) thay vì rải nhiều dòng.
- **Một nút CTA mỗi ảnh**, chữ động từ rõ ("Đăng ký ngay", "Đăng ký tư vấn ngay"). Quảng cáo ảnh thật: đặt nút trong thẻ thông tin ở đáy.
- Bài đăng thường thường không cần nút; quy ước cụ thể theo `brand.md`.
- Mặc định KHÔNG ghi số điện thoại, link form, mã họp trực tuyến lên ảnh — để ở caption (trừ khi brand cho phép, vd ấn phẩm in).
- Không lặp một thông tin hai lần trên cùng ảnh (vd ngày khai giảng ở đầu và ở thẻ).

## 7. Bài nhiều ảnh (carousel / album)
- **Chỉ ảnh đầu** có khối chương trình + CTA; các ảnh sau (kể cả ảnh cuối) không có ngày / CTA / chân trang lặp.
- Không số trang "01/05", không vạch tiến trình, không "vuốt để xem" — Facebook đã tự hiện.
- Ảnh 1–2 mạnh nhất; gọn: gộp nhiều ý nhỏ vào một ảnh thay vì nhiều slide một ý.
- Logo đứng một mình, cùng vị trí ở mọi ảnh.

## 8. Đa khổ
Làm khổ chính trước, duyệt rồi mới chuyển khổ khác. Giữ cùng lề, cùng vị trí nhãn, cùng thứ tự đọc. 9:16: nội dung trong vùng an toàn; 9:16 thẻ 4 mục → lưới 2×2. Ảnh bìa: nội dung trong vùng 16:9 giữa.

## 9. Quản lý file
- Tên `<mã>-<chủ đề>-<khổ>`; tên cố định, version bằng git (tag), không hậu tố `-v2`, không bản copy đổi tên.
- Một thư mục xuất. Mỗi quyết định của khách ghi vào `brand.md` có ngày.

## 10. Checklist QC chung (mở PNG ra NHÌN, đừng chỉ tin lệnh chạy xong)
- [ ] Đúng brand pack: font, màu, logo đúng file, tên thương hiệu ghi đúng cách.
- [ ] Một thông điệp chính; đọc được trong 1 giây ở cỡ điện thoại.
- [ ] Font tải đúng (không phải Times/Arial thay thế); dấu tiếng Việt không bị cắt/vỡ; số lining.
- [ ] Thân chữ ≥ 22 px (khổ 1080); tương phản đủ; không chữ mồ côi.
- [ ] Dữ kiện, chức danh, ngày đúng nguyên văn; không ô `[ ]` nào còn sót (hoặc đã báo "cần bổ sung").
- [ ] Ảnh thật: màu gốc, nét, không halo/nhuộm/cắt dán; lớp phủ chỉ sau chữ, không phủ mặt.
- [ ] Đúng số nút CTA theo loại ấn phẩm; không SĐT / link / mã họp trên ảnh (trừ khi brand cho phép).
- [ ] Bài nhiều ảnh: chỉ ảnh đầu có CTA; không số trang / vạch tiến trình / "vuốt".
- [ ] Vùng an toàn: 9:16 (y 250–1580), ảnh bìa (x 266–1374), in (≥ 5 mm trong mép xén).
- [ ] Tên file đúng quy ước; đã render bản giao (scale 2) và có tag version.
- [ ] Checklist riêng trong `brand.md`.
