# Kích thước ấn phẩm & vùng an toàn

Số đo dùng cho script render (W × H tính bằng px CSS; PNG ra gấp `SCALE`, mặc định ×2). Nền tảng thay đổi thông số theo thời gian — đối chiếu lại nguồn trước chiến dịch lớn.

## 1. Facebook / Instagram — bài đăng
| Khổ | W × H | Dùng khi | Class `.sheet` (core) |
|---|---|---|---|
| 1:1 | 1080 × 1080 | carousel/album, ảnh phụ bài 3–4 ảnh | `s11` |
| 4:5 | 1080 × 1350 | ảnh đơn trên feed (khổ chính, chiếm nhiều màn hình nhất) | `s45` |
| 9:16 | 1080 × 1920 | story, reels | `s916` |
| 1:2 | 1080 × 2160 | bài 2 ảnh dọc đặt cạnh nhau; ảnh 1 của bài 3 ảnh | `s12` |
| 2:1 | 2160 × 1080 | bài 2 ảnh ngang xếp chồng | `s21` |

**Bài 1 ảnh** → làm đủ 3 khổ 1:1, 4:5, 9:16 (cùng nội dung, cùng lề, cùng thứ tự đọc).

### Bài nhiều ảnh — cách Facebook dàn ảnh
- **2 ảnh**: cả hai dọc 1:2 (đặt cạnh nhau) hoặc cả hai ngang 2:1 (xếp chồng). Người ở hai ảnh cạnh nhau: đầu ngang nhau.
- **3 ảnh**: ảnh 1 dọc 1:2 + 2 vuông (ảnh 1 bên trái), hoặc ảnh 1 ngang 2:1 + 2 vuông bên dưới.
- **4 ảnh**: 4 vuông (lưới 2×2), hoặc ảnh 1 dọc 2:3 / ngang 3:2 + 3 vuông.
- **5 ảnh trở lên** (carousel, album): toàn vuông 1:1. Facebook hiện 2 ảnh lớn trên + 3 nhỏ dưới, ảnh thứ 5 phủ "+N" → **ảnh 1–2 mạnh nhất**, không đặt nội dung chốt từ ảnh 6. Gọn nhất 3–5 ảnh; gộp ý vào một ảnh tốt hơn nhiều slide một ý.

Nguồn: sapo.vn/blog/kich-thuoc-anh-dang-facebook-moi-nhat (05/2026); dienthoaivui.com.vn/cach-dang-anh-facebook-theo-bo-cuc.

## 2. Story / Reels — vùng an toàn
Khổ 1080 × 1920. Giao diện ứng dụng (ảnh đại diện, nút trả lời, chú thích) che khoảng **250 px trên và ~340 px dưới** → nội dung chính trong **y 250–1580** (core: `.s916 .zone`). Reels/TikTok che thêm đáy (chú thích) và cột phải — chi tiết ở `quy-tac-social-post.md` mục 2. Thêm class `show-safe` (và `reels`) vào `.sheet` để xem lưới vùng an toàn khi dựng. Nút CTA to hơn (`.cta.lg`).

## 3. Quảng cáo Meta (Facebook / Instagram)
| Vị trí | Khổ nên làm |
|---|---|
| Feed Facebook / Instagram | 4:5 (ưu tiên) hoặc 1:1 |
| Story, Reels | 9:16 (vùng an toàn như mục 2) |
| Cột phải, Marketplace, Tìm kiếm | 1:1 |
| Carousel quảng cáo | 1:1, mỗi thẻ một ý, thẻ 1 mạnh nhất |

Thường đặt đủ 1:1 + 4:5 + 9:16 cho mỗi mẫu. Chữ trên ảnh ít và to (tiêu đề đọc được trong 1 giây); một nút CTA mỗi ảnh. Không khẳng định thuộc tính cá nhân người xem ("Bạn đang nợ nần?") — chính sách quảng cáo Meta.
Nguồn: Meta Ads Guide — facebook.com/business/ads-guide (tra lại theo vị trí cụ thể).

## 4. Ảnh bìa Fanpage Facebook
- Xuất **1640 × 624** (tỉ lệ 2.63:1, chuẩn Meta; tối thiểu 400 × 150). Core: `.sheet.cover`.
- Máy tính hiện gần đủ khung; **điện thoại cắt hai bên còn khung 16:9 ở giữa** → toàn bộ chữ + người nằm trong **x 266 → 1374** (core: `.cover .zone`). Ảnh đại diện tròn che góc dưới trái trên máy tính — không đặt chữ ở đó.
- Có thể dựng ở hệ tọa độ lớn hơn rồi `transform:scale()` về 1640 × 624 (vd dựng 1958 × 745 rồi thu ×0,83759).

## 5. Slide trình chiếu
16:9 = **1920 × 1080** (core: `.sheet.slide169`); lề an toàn ~5% mỗi bên. 4:3 = 1440 × 1080 khi máy chiếu cũ.

## 6. In ấn — cơ bản
Dựng ở **150 dpi** (px CSS) rồi render `SCALE=2` → 300 dpi. Thêm **lề xén (bleed) 3 mm** mỗi cạnh nếu nền tràn mép; giữ chữ cách mép xén ≥ 5 mm (vùng an toàn). Gửi nhà in PDF/PNG 300 dpi; màu in (CMYK) sẽ lệch nhẹ so với màn hình — in thử khi màu nhận diện quan trọng.

| Ấn phẩm | Kích thước | Px ở 150 dpi (render ×2 = 300 dpi) | Core |
|---|---|---|---|
| A4 (tờ rơi, poster nhỏ) | 210 × 297 mm | 1240 × 1754 | `.sheet.a4` |
| A5 (flyer) | 148 × 210 mm | 874 × 1240 | `.sheet.a5` |
| A3 (poster) | 297 × 420 mm | 1754 × 2480 | — |
| Danh thiếp (phổ biến ở VN) | 90 × 54 mm | 531 × 319 | — |
| Danh thiếp (quốc tế) | 85 × 55 mm | 502 × 325 | — |
| Standee cuốn | 80 × 180 cm | in ở 100 dpi: 3150 × 7087 (dựng 1575 × 3543, ×2) | — |
| Backdrop / banner ngang | theo thực tế (vd 3 × 2 m) | 72–100 dpi đủ cho xem từ xa | — |

Nguồn: khổ giấy A theo ISO 216; lề xén 3 mm là quy ước phổ biến của nhà in (hỏi lại nhà in cụ thể). Kích thước danh thiếp/standee là cỡ thường gặp — xác nhận với nhà in trước khi dựng.

Khi tạo khổ không có class sẵn: đặt `width/height` cho `.sheet` trong `<style>` cục bộ và truyền đúng W H cho script.
