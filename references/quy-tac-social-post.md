# Bộ quy tắc thiết kế social post

> File chính của skill cho mọi việc thiết kế ảnh mạng xã hội và ảnh quảng cáo. Đọc trước khi dựng, chạy **checklist QC (mục 14)** trước khi giao.
> Quy tắc ở đây là mặc định chung, không gắn thương hiệu. `brand.md` của brand pack luôn thắng khi hai bên khác nhau.
> Số đo tính theo px CSS trên khổ rộng 1080 px (render ×2 → 2160 px). Thông số nền tảng thay đổi theo thời gian: con số có ghi nguồn thì tra lại nguồn trước chiến dịch lớn; con số ghi "theo hướng dẫn phổ biến" là quy ước nghề, không phải thông số chính thức.

## Mục lục
1. Nền tảng & khổ ảnh
2. Vùng an toàn & cách nền tảng cắt ảnh
3. Một giây đầu: dừng lướt
4. Chữ (typography) — gồm tiếng Việt
5. Phân cấp & bố cục
6. Màu & tương phản
7. Ảnh & con người
8. Mẫu nội dung thường gặp (15 kiểu)
9. Carousel & bài nhiều ảnh
10. Nút CTA
11. Quảng cáo (Meta và nền tảng khác)
12. Khả năng tiếp cận (accessibility)
13. Hệ thống nhất quán: mẫu, token, đặt tên, version
14. Checklist QC trước khi xuất (30 mục)
15. 20 lỗi thường gặp
16. Nguồn tham khảo

---

## 1. Nền tảng & khổ ảnh

### 1.1 Bảng khổ nhanh (dựng ở px CSS, render ×2)
| Nền tảng / vị trí | Khổ nên làm | W × H | Ghi chú |
|---|---|---|---|
| Facebook feed — ảnh đơn | **4:5** (ưu tiên) · 1:1 | 1080 × 1350 · 1080 × 1080 | 4:5 chiếm nhiều màn hình điện thoại nhất trên feed |
| Facebook story / reels | 9:16 | 1080 × 1920 | xem vùng an toàn mục 2 |
| Facebook link preview | 1.91:1 | 1200 × 630 | ảnh og:image của trang web; chữ ít, to, ở giữa |
| Facebook ảnh bìa fanpage | 2.63:1 | 1640 × 624 | điện thoại cắt hai bên → nội dung trong x 266–1374 |
| Facebook ảnh sự kiện | 1.91:1 | 1920 × 1005 | (theo hướng dẫn phổ biến) |
| Instagram feed | **4:5** · 1:1 · 3:4 | 1080 × 1350 · 1080 × 1080 · 1080 × 1440 | lưới trang cá nhân hiện cắt dạng dọc 3:4 → giữ nội dung chính ở giữa |
| Instagram story / reels | 9:16 | 1080 × 1920 | reels hiện trên lưới trang cá nhân cắt 3:4 ở giữa |
| Instagram carousel | toàn bộ cùng tỉ lệ (1:1 hoặc 4:5) | — | ảnh 1 quyết định tỉ lệ cả bộ; tối đa 20 ảnh |
| LinkedIn feed — ảnh | 1:1 · 4:5 · 1.91:1 | 1200 × 1200 · 1080 × 1350 · 1200 × 627 | khán giả công sở đọc trên máy tính nhiều hơn → chữ có thể dày hơn một chút |
| LinkedIn tài liệu (PDF carousel) | 1:1 hoặc 4:5 | 1080 × 1080 · 1080 × 1350 | xuất PDF, mỗi trang một ý |
| LinkedIn ảnh bìa cá nhân / trang | 4:1 · ~5.9:1 | 1584 × 396 · 1128 × 191 | ảnh đại diện che góc trái dưới |
| TikTok / YouTube Shorts | 9:16 | 1080 × 1920 | cột nút bên phải + chú thích dưới che nhiều nhất |
| YouTube thumbnail | 16:9 | 1280 × 720 | file < 2 MB; ô thời lượng che góc phải dưới |
| Zalo OA — bài viết / ảnh bìa | 16:9 hoặc 1:1 tùy vị trí | — | thông số Zalo đổi thường xuyên — kiểm tra trong trang quản trị Zalo OA trước khi dựng |
| Slide / video ngang | 16:9 | 1920 × 1080 | lề ~5% mỗi bên |

### 1.2 Chọn khổ theo mục đích
- **Bài 1 ảnh trên feed**: làm khổ chính 4:5, rồi chuyển 1:1 và 9:16 (cùng nội dung, cùng thứ tự đọc). Một nội dung = đủ 3 khổ khi có thể chạy quảng cáo.
- **Thông tin dày** (lịch, danh sách, so sánh): 4:5 hoặc carousel 1:1 thay vì nhồi vào 1:1.
- **Story / reels / TikTok**: luôn 9:16 riêng, không lấy ảnh 4:5 phóng lên (bị cắt hai đầu, chữ rơi vào vùng giao diện).
- **Link chia sẻ**: chuẩn bị ảnh 1.91:1 riêng, đừng để nền tảng tự cắt ảnh 4:5.

### 1.3 Bài nhiều ảnh — Facebook dàn ảnh thế nào
Facebook tự xếp ảnh theo số lượng và tỉ lệ ảnh đầu tiên (theo cách hiển thị thường gặp; nền tảng có thể đổi):
| Số ảnh | Cách dựng | Facebook hiện |
|---|---|---|
| 2 | cả hai dọc **1:2** (1080 × 2160) | đặt cạnh nhau |
| 2 | cả hai ngang **2:1** (2160 × 1080) | xếp chồng |
| 3 | ảnh 1 dọc 1:2 + 2 ảnh vuông | ảnh 1 to bên trái, 2 ảnh nhỏ bên phải |
| 3 | ảnh 1 ngang 2:1 + 2 ảnh vuông | ảnh 1 to phía trên, 2 ảnh nhỏ bên dưới |
| 4 | 4 ảnh vuông | lưới 2 × 2 |
| 4 | ảnh 1 dọc 2:3 / ngang 3:2 + 3 vuông | ảnh 1 to + 3 ảnh nhỏ |
| 5+ | toàn ảnh vuông 1:1 | 2 ảnh lớn trên + 3 ảnh nhỏ dưới; **ảnh thứ 5 bị phủ "+N"** |

Hệ quả: với 5+ ảnh, **ảnh 1–2 phải mạnh nhất**; ảnh 5 gần như không đọc được (bị phủ); nội dung chốt không đặt từ ảnh 6 trở đi. Hai người ở hai ảnh cạnh nhau: đầu ngang nhau, cùng cỡ.

### 1.4 Định dạng & dung lượng file
- **PNG** cho ảnh nhiều chữ, đồ họa phẳng (chữ sắc nét, không nhiễu nén). **JPG chất lượng 85–92** cho ảnh chụp toàn khung.
- Không gian màu **sRGB** (Chrome headless xuất sRGB). Không dùng CMYK cho mạng xã hội.
- Xuất ở **2× (2160 px rộng)**: nền tảng nén lại vẫn giữ chữ sắc hơn bản 1×. Nếu PNG > 8–10 MB, chuyển JPG 90 hoặc giảm vùng nhiễu (grain).
- YouTube thumbnail: < 2 MB (theo trợ giúp YouTube) → JPG.

---

## 2. Vùng an toàn & cách nền tảng cắt ảnh

### 2.1 Story / reels / TikTok (1080 × 1920)
| Vùng | Bị che bởi | Quy tắc |
|---|---|---|
| Trên **~250 px** | ảnh đại diện, tên tài khoản, thanh tiến trình, nút đóng | không đặt chữ, logo, mặt người |
| Dưới **~340 px** (story) | ô trả lời, nút gửi, nhãn quảng cáo + CTA của nền tảng | không đặt chữ, CTA vẽ trên ảnh |
| Dưới **~450–670 px** (reels, TikTok, Shorts) | chú thích, tên nhạc, tên tài khoản | chữ quan trọng đặt cao hơn; reels nhiều chữ → giữ trong y 250–1250 |
| Phải **~120–140 px** (reels, TikTok, Shorts) | cột nút thích / bình luận / chia sẻ | không đặt chữ sát mép phải |

Vùng an toàn thực dụng cho ảnh story: **x 64–1016, y 250–1580** (core: `.s916 .zone`). Meta khuyến nghị chừa khoảng 14% trên và dưới không chữ/logo cho story (Meta Ads Guide); reels chừa nhiều hơn ở đáy. Mẫu `brands/_mau/templates/story-9x16.html` có lớp lưới vùng an toàn bật/tắt được.

### 2.2 Feed
- Facebook/Instagram có thể cắt ảnh 4:5 thành gần vuông ở một số chỗ (lưới, xem trước, chia sẻ lại) → **đặt tiêu đề và mặt người trong vùng vuông 1080 × 1080 ở giữa** của ảnh 4:5 (tức y 135–1215) khi có thể.
- Instagram lưới trang cá nhân cắt dọc 3:4 ở giữa: chữ sát mép trái/phải ảnh 4:5 vẫn còn, nhưng chữ sát mép trên/dưới của ảnh 9:16 bị mất.
- Lề ngoài tối thiểu **60–80 px** (khổ 1080) để không dính viền khi nền tảng bo góc / thu nhỏ.

### 2.3 Ảnh bìa & ảnh đại diện
- Bìa fanpage Facebook 1640 × 624: máy tính hiện gần đủ; **điện thoại cắt hai bên còn khung giữa** → chữ + người trong **x 266–1374**. Ảnh đại diện tròn đè góc trái dưới (máy tính) → không đặt chữ ở đó.
- LinkedIn bìa: ảnh đại diện đè trái dưới, nút đè phải dưới → nội dung ở nửa phải, trên.
- Ảnh đại diện: logo đặt trong vòng tròn nội tiếp, lề ≥ 15%; không chữ nhỏ.

### 2.4 YouTube thumbnail
- Ô thời lượng che góc phải dưới (~ 180 × 60 px trên khổ 1280 × 720) → không đặt chữ/mặt ở đó.
- Thumbnail xem ở cỡ ~ 168–360 px rộng: tối đa 3–5 chữ, cỡ chữ ≥ 90–120 px trên khổ 1280.

---

## 3. Một giây đầu: dừng lướt

Người xem lướt feed nhanh; ảnh có khoảng 1 giây để được chú ý (theo hướng dẫn phổ biến của Meta về "thumb-stopping creative").
- **Một điểm nhìn (focal point)** duy nhất: một gương mặt, một con số lớn, hoặc một câu hook lớn. Không ba thứ cùng to.
- **Hook 6–10 chữ**, đọc được trong một hơi. Dài hơn → tách thành tiêu đề (hook) + dòng phụ nhỏ.
- **Thứ tự đọc** rõ: (1) hook / hình nổi bật → (2) bằng chứng (người, ảnh, số liệu có nguồn) → (3) thông tin cần thiết → (4) hành động.
- **Tỉ lệ chữ / ảnh**: Meta đã bỏ quy tắc "20% chữ" từ 2020–2021, quảng cáo nhiều chữ không còn bị chặn; nhưng ảnh ít chữ thường hiệu quả hơn → giữ chữ chiếm **khoảng 20–30% diện tích** (ảnh thông tin có thể hơn, quảng cáo nên ít hơn).
- **Thử cỡ điện thoại**: thu ảnh xuống ~ 360 px rộng (cỡ thật trên điện thoại). Không đọc được hook → chữ quá nhỏ hoặc quá nhiều.
- **Nhịp tương phản**: vùng nhấn có độ tương phản cao nhất trên ảnh; phần còn lại lùi xuống.
- **Ảnh người thật** (mặt nhìn được, ánh mắt rõ) thường dừng lướt tốt hơn đồ họa thuần — nhưng chỉ khi ảnh đẹp và thật.
- Câu hook dạng câu hỏi hoặc mâu thuẫn ("Làm nhiều hơn mà vẫn không kịp việc?") hiệu quả hơn khẩu hiệu chung chung; nhưng tránh khẳng định thuộc tính cá nhân người xem trong quảng cáo (mục 11).

---

## 4. Chữ (typography)

### 4.1 Cỡ chữ tối thiểu (khổ 1080 px)
| Vai | Cỡ tối thiểu | Thường dùng | Ghi chú |
|---|---|---|---|
| Tiêu đề / hook | **56–64 px** | 64–96 px | 9:16 to hơn 10–20% |
| Thân chữ | **24–28 px** | 26–30 px | carousel ≥ 28 px; đoạn ≤ 3–4 dòng |
| Chú thích, nhãn | **18 px** | 18–22 px | nhãn in hoa đậm có thể 16–17 px nếu giãn chữ |
| Chữ trên nút CTA | 22 px | 24–30 px | đậm |
| Con số nổi bật (stat) | 120 px | 140–260 px | dùng số lining |

Kiểm tra: ảnh 1080 px hiện trên điện thoại rộng ~ 360–430 pt → chữ 24 px còn ~ 8–10 pt. Dưới 18 px gần như không đọc được.

### 4.2 Độ dài dòng, khoảng cách
- Dòng thân **25–45 ký tự** trên ảnh mạng xã hội (ngắn hơn nhiều so với web 45–75 ký tự).
- line-height: thân **1.35–1.5**; tiêu đề **1.05–1.2**; tiếng Việt nhiều dấu chồng → tiêu đề **≥ 1.1**, thân **≥ 1.3**, nhãn nhiều dòng ≥ 1.2.
- Khoảng cách đoạn = 0.5–1 dòng; không thụt đầu dòng trên ảnh.
- Ngắt dòng có chủ đích: mỗi dòng hook là một cụm nghĩa; không để chữ mồ côi (1 chữ đứng một dòng) — dùng `&nbsp;` giữ 2 chữ cuối dòng, giữ cụm số + đơn vị ("15&nbsp;phút", "6&nbsp;tháng"), tên riêng 2 chữ.

### 4.3 Chọn font
- **Tối đa 2 họ font** (một tiêu đề có cá tính + một thân sans dễ đọc). Thêm biến thể đậm/nghiêng của cùng họ, không thêm họ thứ 3.
- Serif / display chỉ cho tiêu đề, hook, ngày nổi bật. Thân, tên người, nhãn, số liệu dùng sans.
- Không dùng font viết tay / trang trí cho đoạn dài.

### 4.4 Tiếng Việt
- Font phải **hỗ trợ đủ tiếng Việt** (subset `vietnamese` trên Google Fonts). Thử chuỗi kiểm: **"Ẩm ướt, nghỉ ngơi, Hưởng ứng — ỗ ễ ử ợ ỹ Ỷ ặ ậ"**. Dấu lệch, chồng sai hoặc rơi về font khác → đổi font.
- Font hợp với tiếng Việt thường gặp trên Google Fonts: Be Vietnam Pro, Inter, Montserrat, Lexend, Nunito Sans, Noto Sans/Serif, Lora, Playfair Display, Source Serif, Roboto Slab.
- **line-height ≥ 1.2** (tiêu đề ≥ 1.1) để dấu dòng dưới (ặ, ậ) không chạm dấu dòng trên (Ẩ, Ỗ). Chữ gradient cần thêm `padding-bottom` để móc chữ "g, y" và dấu nặng không bị cắt.
- **Không giãn chữ (letter-spacing) chữ thường** tiếng Việt — dấu tách khỏi chữ, đọc rời rạc. Chỉ giãn chữ cho nhãn IN HOA ngắn (0.12–0.24 em).
- **Tránh IN HOA đoạn dài** tiếng Việt: dấu trên chữ hoa (Ấ, Ể, Ỗ) dễ chạm dòng trên và khó đọc. In hoa chỉ cho nhãn ≤ 4–5 chữ, tên nút.
- Thống nhất một kiểu đặt dấu trong cả bộ (vd "hóa, khóa, hòa" hoặc "hoá, khoá, hoà") theo `brand.md`.
- Đơn vị và ngày: "20.11.2026" hoặc "20/11/2026" — chọn một; giờ "19:30"; tiền "1.990.000đ" hoặc "1,99 triệu" — thống nhất trong cả chiến dịch.

### 4.5 Số
- Font serif thường mặc định **số kiểu cũ (oldstyle)** — "5.0" thành "5.o". Bật số thẳng hàng: `font-variant-numeric: lining-nums; font-feature-settings: "lnum" 1, "onum" 0` (core: `.display`, `.num`).
- Bảng số / giá / đếm ngược: `tabular-nums` để cột số thẳng.
- Con số lớn: tách đơn vị nhỏ hơn (60%), cùng đường chân chữ.

### 4.6 Đậm, nghiêng, hiệu ứng
- **Không đậm giả (faux bold)**: chỉ dùng độ đậm có thật trong file font (tải đúng weight 600/700/800 từ Google Fonts). Thiếu weight → trình duyệt tự tô dày, chữ nhòe.
- Không nghiêng giả: tải bản italic thật.
- Chữ gradient (clip text): **không thêm text-shadow** (vỡ hiệu ứng); cần nổi trên ảnh → `filter: drop-shadow()` nhẹ.
- Bóng chữ trên ảnh: mềm, cùng tông nền (vd `0 2px 14px rgba(nền,.85)`), không viền đen cứng.
- Không kéo giãn / bóp chữ theo chiều ngang hoặc dọc.

---

## 5. Phân cấp & bố cục

### 5.1 Lưới và lề
- Lề ngoài **≥ 60–80 px** trên khổ 1080 (core: `--margin: 64px`). Story: lề trên/dưới theo vùng an toàn (mục 2).
- Lưới 12 cột (cột ~ 70 px, rãnh 24 px trong vùng 952 px) hoặc lưới 4 cột cho bố cục thẻ. Mọi khối bám mép cột.
- **Thang khoảng cách** bội số 8: 8 · 16 · 24 · 32 · 48 · 64 · 96. Khoảng cách trong nhóm < khoảng cách giữa nhóm (luật gần nhau — proximity).

### 5.2 Thứ tự đọc
- **Mẫu Z** cho ảnh ít chữ: logo trái trên → hook → hình → CTA phải dưới.
- **Mẫu F** cho ảnh nhiều chữ (danh sách, FAQ): người đọc quét đầu dòng bên trái, nên từ khóa đặt đầu dòng (NN/g, nghiên cứu theo dõi mắt "F-shaped pattern").
- Căn lề: **căn trái** cho ảnh có người, quảng cáo, danh sách; **căn giữa** cho ảnh thông báo, trích dẫn ngắn. Không trộn căn trái và căn giữa trong cùng một khối.

### 5.3 Mức nhấn
- **Tối đa 3 cấp** cỡ chữ rõ rệt (tiêu đề ≥ 2× thân; nhãn nhỏ nhất nhưng đậm).
- **Tối đa 3 mức nhấn**: (1) vùng nhấn chính — 1 chỗ; (2) nhấn phụ — từ khóa màu, nhãn; (3) nền. Một ảnh chỉ một vùng nhấn chính.
- Nhóm thông tin liên quan vào một thẻ (ngày + giờ + nơi = một khối), không rải khắp ảnh.

### 5.4 Khoảng trống
- Khoảng trống là một phần thiết kế: **30–40% diện tích** không chữ/không hình trang trí giúp ảnh "sang" và dễ đọc.
- Thêm trang trí không cứu được thông điệp yếu. Cắt chữ trước, rồi mới thu nhỏ.

### 5.5 Logo
- Một logo mỗi ảnh, **cao ~ 48–72 px** trên khổ 1080 (logo ngang); cùng vị trí ở mọi ảnh trong một chuỗi.
- Đặt góc trên (trái hoặc giữa) hoặc dưới phải; không đặt trong vùng giao diện story.
- Vùng trống quanh logo ≥ chiều cao chữ trong logo. Nền tối dùng bản logo trắng/sáng.

---

## 6. Màu & tương phản

### 6.1 Tương phản (WCAG 2.x)
| Loại chữ | Tỉ lệ tối thiểu (AA) | Khuyến nghị |
|---|---|---|
| Thân chữ | **4.5 : 1** | ≥ 7 : 1 cho chữ nhỏ trên ảnh |
| Chữ lớn (≥ 24 px thường hoặc ≥ 18.66 px đậm, ở cỡ hiển thị) | **3 : 1** | ≥ 4.5 : 1 |
| Thành phần đồ họa (viền nút, icon mang nghĩa) | 3 : 1 | — |

Ảnh mạng xã hội bị thu nhỏ khi xem → đối xử với "chữ lớn" trên khổ 1080 như chữ thường: nhắm **≥ 4.5 : 1** cho mọi chữ cần đọc.

### 6.2 Chữ trên ảnh
- Lớp phủ (scrim) là **gradient tuyến tính màu nền, blend thường**, chỉ ở phía có chữ, **mờ hết trước khi tới mặt người** (core: `.ov-top`, `.ov-bottom`, chỉnh `--ov-h`).
- Đo tương phản tại **điểm sáng nhất** của ảnh phía sau chữ.
- Không: phủ đen 50% toàn ảnh, làm nhòe nền mạnh, hộp đặc che nửa ảnh (trừ khi đó là phong cách đã duyệt).
- Chữ trắng trên ảnh sáng → thêm bóng mềm hoặc kéo dài gradient, không viền chữ.

### 6.3 Phân bổ màu: 60-30-10
- **60%** màu nền chủ đạo · **30%** màu phụ (thẻ, khối) · **10%** màu nhấn (từ khóa, nút, nhãn).
- Màu nhấn chỉ cho thứ cần hành động hoặc cần nhớ. Không dùng màu nhấn cho đoạn dài.
- Màu thương hiệu là nền tảng; màu nhấn chiến dịch (nếu có) ghi vào `brand.md`, không tự thêm.

### 6.4 Nền tối / nền sáng
- Nền tối: không đen phẳng `#000` — dùng màu tối thương hiệu có chiều sâu (gradient nhẹ, quầng sáng). Chữ trắng ngà (không trắng tinh khi cỡ lớn trên nền rất tối).
- Nền sáng: tránh trắng tinh khi cần in; thẻ trắng trên nền sáng cần viền hoặc bóng nhẹ.
- Ở chế độ tối của ứng dụng, ảnh nền trắng phát sáng gắt — cân nhắc nền kem/xám nhạt.

### 6.5 Tránh ám màu
- Không phủ lớp màu (`mix-blend-mode: color`, `multiply` đậm, overlay màu thương hiệu) lên da người: da ám xanh/tím, trông giả.
- Ảnh người cạnh nhau phải cân sáng và cân màu da (xem `cong-cu-anh.md` mục 3).
- Kiểm tra trên ít nhất hai màn hình (điện thoại + máy tính) — màu bão hòa cao trông khác nhau nhiều.

---

## 7. Ảnh & con người

### 7.1 Bố cục người
- **Mặt nhìn rõ**: trên ảnh 1080 px, mặt người chính cao **≥ 180–250 px**. Phóng ảnh gốc ×1.15–1.25 nếu người quá nhỏ.
- **Khoảng trên đầu (headroom)**: 40–120 px; đầu không sát mép trên, không bị nhãn/logo đè.
- **Quy tắc 1/3**: mắt nằm gần đường 1/3 trên; người lệch sang một bên → chữ ở phía đối diện.
- **Hướng nhìn**: người nhìn / quay về phía chữ hoặc CTA, không nhìn ra ngoài khung (mắt người xem đi theo ánh mắt trong ảnh).
- Không cắt ngang khớp (cổ, khuỷu, đầu gối, cổ tay); cắt ở giữa thân/đùi.

### 7.2 Giữ ảnh thật tự nhiên
- Màu gốc, nét. Filter gần trung tính: sáng ~ 1.0 (tối đa 1.1–1.15 cho người tối hơn), tương phản ≤ 1.03, bão hòa 1.0.
- Không làm mịn da nặng, không "đẹp hóa" bằng AI, không halo / vầng sáng sau người, không nhuộm màu.
- Không làm nhòe nền mạnh để "tách người" — trông ẩu. Muốn đọc chữ → gradient sau chữ.

### 7.3 Nhiều người
- Cùng cỡ đầu, đầu ngang nhau (đo ở cùng tỉ lệ), độ sáng mặt tương đương. Người tối hơn → bản đã cân sáng, ghi vào `brand.md` là luôn dùng bản đó.
- Không xếp một người to hơn hẳn trừ khi có chủ đích (vai trò khác nhau).
- Tên + chức danh: lower-third chữ trắng có bóng mềm cạnh người, không hộp nặng; chức danh đúng nguyên văn đã duyệt.

### 7.4 Không cắt mặt
- Không để chữ, nhãn, logo, nút, vùng giao diện story/reels đè lên mặt hoặc tay đang cầm vật quan trọng (micro, sản phẩm).
- Kiểm tra cả ba khổ: mặt đẹp ở 4:5 có thể bị chữ đè ở 9:16.

### 7.5 Ảnh tách nền (cut-out)
- **Dùng được** khi: ảnh chụp chân dung chất lượng, ánh sáng mềm, đặt lên nền thiết kế đơn giản (đồ họa, gradient) với bóng đổ nhẹ; nhiều người tách nền cùng nguồn sáng.
- **Trông giả** khi: cắt người khỏi ảnh sự kiện rồi dán lên ảnh sự kiện khác; mép tóc răng cưa; ánh sáng trên người ngược hướng nền; người "lơ lửng" không bóng; viền sáng quanh người.
- Quảng cáo "ảnh thật" → dùng ảnh gốc nguyên khung, không cắt dán.
- Kiểm tra mép tóc, kính, micro ở 100%.

### 7.6 Quyền & đạo đức
- Chỉ dùng ảnh có người ngoài khi được phép; ảnh người ngoài không đưa vào repo công khai (`assets/anh-that/` đã git-ignore).
- Không dùng ảnh người nổi tiếng / logo đối tác khi chưa được đồng ý. Ảnh kho (stock) phải có giấy phép thương mại.
- Ảnh do AI tạo hình người: ghi rõ nếu nền tảng yêu cầu; không dùng làm "khách hàng thật".

---

## 8. Mẫu nội dung thường gặp

Mỗi kiểu: bố cục chuẩn + điều phải có + lỗi hay gặp. Mẫu chạy được ở `brands/_mau/templates/`.

### 8.1 Thẻ trích dẫn (quote card) — 1:1 hoặc 4:5 · mẫu `quote-1x1.html`
- Dấu ngoặc kép lớn (serif, màu nhấn, 160–240 px) làm điểm nhìn; câu trích 44–64 px, **≤ 25–30 chữ**.
- Dưới: ảnh tròn người nói (120–180 px) + tên (đậm) + chức danh (nhỏ). Có thể nguồn/ngữ cảnh ("Trích bài nói tại…").
- **Lời trích phải có nguồn và nguyên văn**; cắt ngắn thì dùng "…", không sửa ý.
- Lỗi: trích quá dài; ảnh người nhỏ hơn dấu ngoặc; không ghi ai nói.

### 8.2 Thông báo / key visual — 4:5 · mẫu `post-4x5.html`
- Logo → tên chương trình / sản phẩm là **hero** (to nhất) → tagline → 1 câu giá trị → thẻ thông tin (ngày + 3 mục).
- Tên chương trình hai màu (core `.wt`): phần chính màu thường, phần nhấn (số phiên bản, từ khóa) màu nhấn.
- Lỗi: tiêu đề "Thông báo" to hơn tên chương trình; nhồi cả lịch + giá + liên hệ.

### 8.3 Sự kiện — 4:5 · mẫu `event-4x5.html`
- Ba dữ kiện bắt buộc trong một khối: **ngày (chip nổi bật) · giờ · nơi** (hoặc "Trực tuyến"). Ngày dạng "Thứ Sáu, 20.11" dễ nhớ hơn chỉ số.
- Tên sự kiện + chủ đề + diễn giả (ảnh + tên + chức danh) + CTA (nếu là quảng cáo).
- Không ghi link họp, mã phòng, số điện thoại trên ảnh — để ở caption (trừ ấn phẩm in).
- Lỗi: thiếu thứ trong tuần; giờ không ghi múi/không ghi kết thúc khi cần; địa chỉ quá dài (rút gọn, chi tiết ở caption).

### 8.4 Hỏi đáp (FAQ card) — 1:1 hoặc 4:5
- Nhãn "HỎI – ĐÁP" → câu hỏi (đậm, 40–52 px, có dấu "?") → câu trả lời 3–5 dòng (26–30 px) → nguồn/người trả lời.
- 1 câu hỏi mỗi ảnh; nhiều câu → carousel. Câu hỏi viết bằng lời người hỏi thật.
- Lỗi: trả lời dài như văn bản; câu hỏi và trả lời cùng cỡ.

### 8.5 Trước / sau (before / after) — 1:1, 4:5 hoặc 2 ảnh 1:2
- Chia đôi dọc (trái = trước, phải = sau) hoặc trên/dưới; nhãn "TRƯỚC" / "SAU" in hoa đậm cùng vị trí ở hai nửa.
- Hai nửa cùng góc chụp, cùng ánh sáng, cùng tỉ lệ — chỉ khác điều cần chứng minh. Mũi tên/chia vạch ở giữa.
- Kết quả phải thật và có thể kiểm chứng; ngành sức khỏe/làm đẹp/tài chính có quy định riêng (Meta giới hạn ảnh trước–sau về cơ thể).

### 8.6 Danh sách / mẹo (list, tips) — 4:5 hoặc carousel
- Tiêu đề có con số ("5 cách…", "3 sai lầm…") → 3–5 mục, mỗi mục một thẻ: số thứ tự + từ khóa đậm + 1 câu.
- Từ khóa đầu dòng (mẫu F); các mục cùng cấu trúc ngữ pháp; > 5 mục → carousel.
- Lỗi: 7–10 mục trên một ảnh 1:1; mục dài 3 dòng.

### 8.7 Con số nổi bật (stat callout) — 1:1 hoặc 4:5
- Một con số rất lớn (140–260 px, số lining) + đơn vị + 1 câu giải thích + **nguồn** (16–18 px, cuối ảnh).
- Chỉ một con số chính mỗi ảnh; số phụ ≤ 2 và nhỏ hơn hẳn.
- Lỗi: số không nguồn; làm tròn sai; dùng % mà không có mẫu số.

### 8.8 Cảm nhận khách hàng (testimonial) — 1:1 hoặc 4:5
- Ảnh thật người nói (được phép) + câu cảm nhận ngắn (≤ 30 chữ, nguyên văn) + tên + vai trò/ngữ cảnh ("Học viên khóa 3", "Khách tham dự sự kiện…").
- Có thể chụp màn hình bình luận/tin nhắn thật (che thông tin cá nhân), không dựng giả giao diện.
- Lỗi: testimonial không tên; "chỉnh" lời cho hay hơn; dùng ảnh kho làm khách hàng.

### 8.9 So sánh (comparison) — 4:5
- Hai cột (A | B) hoặc bảng 3–5 hàng; cột được khuyên dùng có màu nhấn/viền, cột kia trung tính. Dấu ✓ / ✗ kèm chữ (không chỉ màu).
- Tiêu chí so sánh công bằng, cùng đơn vị. Không nêu tên/logo đối thủ trong quảng cáo nếu chưa chắc về pháp lý.

### 8.10 Infographic / timeline / lộ trình — 4:5, 9:16 hoặc carousel
- Trục dọc (điện thoại đọc từ trên xuống) với 3–6 mốc; mỗi mốc: chip ngày/giai đoạn + tiêu đề + 1 dòng.
- Đường nối mảnh, icon nét đều một bộ. Nhiều hơn 6 mốc → tách carousel theo giai đoạn.
- Lỗi: trục ngang trên 4:5 (chữ bé); icon lẫn nhiều phong cách.

### 8.11 Đếm ngược / hạn chót (countdown, deadline) — 1:1, 4:5, 9:16
- Con số lớn "Còn 3 ngày" hoặc ngày hạn ("Hạn 23:59 · 30.11") là hero; ưu đãi ngắn gọn; CTA.
- Ngày giờ chính xác, ghi rõ giờ kết thúc. Chuỗi đếm ngược dùng cùng bố cục, chỉ đổi số.
- Không tạo khan hiếm giả (hết suất khi còn) — vi phạm niềm tin và chính sách quảng cáo.

### 8.12 Thẻ sản phẩm / dịch vụ (product / service card) — 1:1 hoặc 4:5
- Ảnh sản phẩm thật (nền sạch) chiếm 50–60% → tên → 2–3 lợi ích (không phải tính năng) → giá/ưu đãi (nếu brand cho phép) → CTA.
- Giá: số lớn, đơn vị nhỏ; giá gốc gạch ngang nhỏ hơn và nhạt.

### 8.13 Ảnh trích video / ảnh bìa video
- Khung hình có mặt người biểu cảm rõ + 3–6 chữ hook. 9:16 cho reels (chữ trong vùng an toàn), 16:9 cho YouTube.

### 8.14 Tuyển dụng / thông báo nội bộ
- Vị trí (hero) → 3 điểm hấp dẫn → nơi làm/hình thức → CTA "Ứng tuyển". Không ghi lương nếu chưa được duyệt.

### 8.15 Chúc mừng / sự kiện mùa (lễ, Tết)
- Ít chữ, hình ảnh mùa tiết chế theo màu thương hiệu; logo nhỏ; không biến thành quảng cáo trá hình.

---

## 9. Carousel & bài nhiều ảnh

- **Ảnh 1 = bìa hook**: câu hook mạnh nhất + lời hứa ("5 điều…", "Cách…"). Đây là ảnh duy nhất chắc chắn được xem.
- **Một ý mỗi ảnh**; ảnh sau tiếp ảnh trước (tiến trình rõ: vấn đề → nguyên nhân → cách làm → kết quả → hành động).
- **Gọn**: 3–7 ảnh là phổ biến; gộp ý nhỏ vào một ảnh thay vì nhiều ảnh một dòng. Facebook album: ảnh 1–2 mạnh nhất (mục 1.3).
- **Ảnh cuối**: tóm tắt hoặc CTA — trừ khi brand yêu cầu "ảnh sạch" (xem dưới).
- **Phong cách nhất quán**: cùng lề, cùng vị trí logo, cùng vị trí tiêu đề, cùng nền; chỉ nội dung thay đổi. Có thể để một hình chạy nối qua mép giữa hai ảnh (Instagram) — kiểm tra từng ảnh vẫn đứng riêng được.
- **Kiểu "ảnh sạch"** (mặc định của skill, đổi được trong `brand.md`): **chỉ ảnh đầu** có khối chương trình + CTA (core `.first-bar`); các ảnh sau không lặp chân trang, không số trang "01/05", không vạch tiến trình, không "Vuốt để xem →" — nền tảng đã có chấm/số trang. Logo đứng một mình.
- Kiểu "có chỉ dẫn" (khi brand muốn): số trang nhỏ góc dưới, mũi tên "→" ở ảnh 1, ảnh cuối có CTA. Dùng một kiểu cho cả chuỗi.
- Đặt tên `<mã>-<chủ đề>-01-1x1`, `…-02-1x1`; render ảnh cuối kèm tên nhóm để tag cả bộ.
- Mẫu: `carousel-01-1x1.html` (bìa) + `carousel-02-1x1.html` (ảnh nội dung).

---

## 10. Nút CTA

### 10.1 Hình dạng & kích thước
- Pill hoặc bo góc 12–16 px; cao **≥ 64–76 px** trên khổ 1080 (9:16: 80–90 px); chữ 22–30 px đậm, có thể in hoa giãn chữ 0.08–0.12 em.
- Mũi tên trong vòng tròn bên phải giúp nhận ra "nút" ngay (core `.cta`).
- Tương phản nút / nền ≥ 3:1, chữ / nút ≥ 4.5:1. Nút là vùng màu nhấn mạnh nhất sau hook.

### 10.2 Chữ trên nút
- **Động từ đứng đầu**, 2–4 chữ: "Đăng ký ngay", "Nhận tư vấn", "Xem lịch học", "Tải tài liệu", "Đặt chỗ".
- Khớp với nút CTA thật của nền tảng / trang đích (ảnh ghi "Đăng ký ngay" thì nút quảng cáo cũng "Đăng ký").
- Không: "Click here", "Xem thêm" chung chung; không ghi URL, số điện thoại trên nút.

### 10.3 Vị trí & số lượng
- **Một CTA mỗi ảnh**. Đặt cuối thứ tự đọc: góc dưới phải (mẫu Z) hoặc trong thẻ thông tin ở đáy (quảng cáo ảnh thật).
- Story / reels: CTA vẽ trên ảnh phải nằm **trên** vùng đáy bị che (y ≤ 1580); nền tảng thêm nút thật ở đáy.
- **Bài thường (organic)**: thường không cần nút — lời mời nằm ở caption; dùng nút khi bài là lời mời đăng ký rõ ràng (theo `brand.md`).
- **Quảng cáo**: có nút vẽ trên ảnh giúp tăng nhận biết hành động, nhưng không giả nút giao diện nền tảng (mục 11).

---

## 11. Quảng cáo (Meta và nền tảng khác)

### 11.1 Sáng tạo là nhắm chọn
- Meta hiện ưu tiên nhắm chọn rộng (broad / Advantage+); **chính hình ảnh và câu chữ quyết định ai dừng lại** ("creative is the new targeting"). Mỗi mẫu nên nói rõ người xem là ai qua hình (nghề, bối cảnh) và hook.
- Làm **nhiều góc tiếp cận khác nhau** (nỗi đau, kết quả, bằng chứng, người dẫn dắt, ưu đãi) thay vì nhiều biến thể màu của cùng một ý.

### 11.2 Đủ khổ cho mỗi mẫu
- Mỗi mẫu: **1:1 + 4:5 + 9:16** (feed, cột phải/tìm kiếm, story/reels). Cùng nội dung, bố cục điều chỉnh theo khổ; 9:16 không phải ảnh 4:5 thêm nền.
- 9:16: thẻ thông tin 4 mục → lưới 2 × 2 (core `.fx.grid2`).

### 11.3 Chữ trên ảnh vs primary text
- **Trên ảnh**: hook (6–10 chữ) + 1 bằng chứng + 1 CTA. Không đoạn văn.
- **Primary text** (đoạn chữ phía trên ảnh): giải thích, lợi ích, chi tiết, link, liên hệ. 125 ký tự đầu là phần hiển thị trước "Xem thêm" (theo Meta Ads Guide) → đặt hook ở đó.
- **Tiêu đề quảng cáo** (headline dưới ảnh): ~ 27–40 ký tự, nhắc lại lợi ích / ưu đãi, không lặp nguyên hook trên ảnh.

### 11.4 Thử nghiệm biến thể
- Đổi **một biến số mỗi lần**: hook, hình (người / không người), CTA, khổ. Đặt tên biến thể rõ (`AD07-A-hook-cauhoi-4x5`, `AD07-B-hook-so-lieu-4x5`).
- 3–5 mẫu khác góc cho mỗi nhóm quảng cáo là điểm khởi đầu phổ biến; thay mẫu khi tần suất cao và hiệu quả giảm (mỏi sáng tạo).

### 11.5 Chính sách (tóm tắt — đọc Meta Advertising Standards khi chạy thật)
- **Không khẳng định / ám chỉ thuộc tính cá nhân** của người xem (sức khỏe, tài chính, tôn giáo, chủng tộc, xu hướng tính dục, tình trạng nợ…): tránh "Bạn đang nợ nần?", "Bạn bị mất ngủ?" → viết "Dành cho người muốn…", "Nhiều người đi làm lâu năm…".
- **Không giả giao diện**: nút "Phát" giả, thông báo hệ thống giả, thanh tìm kiếm / hộp thoại giả, con trỏ chuột — bị coi là gây hiểu nhầm.
- Không hứa kết quả phi thực tế, không "trước–sau" cơ thể, không khan hiếm giả; giá và ưu đãi đúng trang đích.
- Nội dung trên ảnh phải khớp trang đích (cùng tên, giá, ngày).

### 11.6 Quảng cáo ảnh thật — cấu trúc đã kiểm chứng
- Trên: hook trên gradient chỉ sau chữ (không phủ mặt). Giữa: người ở giữa khung, phóng ×1.15–1.25.
- Đáy xếp chồng (core `.stack`): **lower-third** (tên + chức danh, chữ trắng, không hộp) → **thẻ thông tin có CTA** trong hàng đầu → **hàng 3–4 mục** (9:16: lưới 2 × 2). Mẫu: `ad-cta-4x5.html`.
- Không lặp ngày ở đầu và ở thẻ.

### 11.7 Nền tảng khác
- **LinkedIn**: giọng chuyên nghiệp, ít biểu tượng cảm xúc; ảnh có người + số liệu hoạt động tốt; tài liệu PDF carousel cho nội dung hướng dẫn.
- **TikTok / Reels / Shorts quảng cáo**: ưu tiên video; ảnh tĩnh 9:16 phải có chuyển động nhẹ hoặc chuỗi ảnh; tôn trọng vùng an toàn cột phải + chú thích đáy.
- **Google Display / YouTube**: theo bộ khổ riêng của Google Ads; logo + tiêu đề tách rời vì hệ thống tự ghép.

---

## 12. Khả năng tiếp cận (accessibility)

- Tương phản đạt mục 6.1; không đặt chữ trên vùng ảnh rối.
- **Không truyền thông tin chỉ bằng màu**: đúng / sai dùng ✓ / ✗ + chữ; trạng thái dùng nhãn; biểu đồ có nhãn trực tiếp.
- **Alt text** khi đăng: mô tả nội dung + chép lại chữ quan trọng trên ảnh (Facebook, Instagram, LinkedIn, X đều có ô alt text). Ví dụ: "Ảnh thông báo hội thảo ngày 20.11, 9:00–11:30, trực tuyến. Nút: Đăng ký ngay."
- **Phụ đề cho video** (luôn có): đa số xem video không bật tiếng; chữ phụ đề ≥ 40–48 px trên khổ 1080, trong vùng an toàn, nền mờ sau chữ.
- Không dùng chữ nhấp nháy / chuyển động nhanh (> 3 lần mỗi giây — ngưỡng WCAG về chớp sáng).
- Biểu tượng cảm xúc trong ảnh/caption: ít, không thay thế từ quan trọng (trình đọc màn hình đọc tên emoji).
- Font dễ đọc, không dùng chữ viết tay cho thông tin quan trọng (ngày, giá, giờ).

---

## 13. Hệ thống nhất quán

- **Mẫu (template)**: mỗi kiểu nội dung có một mẫu đã duyệt trong `brands/<brand>/templates/`; ảnh mới = copy mẫu gần nhất, sửa nội dung. Không dựng lại từ đầu mỗi lần.
- **Token**: màu, font, bo góc, lề, đổ bóng nằm trong `tokens.css` (biến CSS); CSS thành phần trong `core/core.css`. Đổi nhận diện = đổi token, không sửa từng ảnh.
- **Chuỗi bài (series look)**: một chuỗi có cùng bố cục khung (vị trí logo, nhãn chuỗi, nền) để người xem nhận ra trên feed; đổi màu nhấn hoặc ảnh theo từng tập.
- **Đặt tên**: `<mã>-<chủ đề>-<khổ>` (vd `p07-ra-mat-4x5`, `ad12-hook-cauhoi-9x16`, `m03-meo-02-1x1`), chữ thường không dấu, không hậu tố "final", "v2", "moi".
- **Version**: git + tag (`render-social.sh`), khôi phục bằng `khoi-phuc.sh`; không xóa bản cũ, không bản copy đổi tên.
- **Ghi quyết định**: mọi điều chủ thương hiệu duyệt / bác → ghi vào `brand.md` kèm ngày, lý do.
- **Một thư mục xuất** (`output/`), một bản cho mỗi ảnh.

---

## 14. Checklist QC trước khi xuất

Mở PNG ra **nhìn** ở cỡ thật và ở cỡ điện thoại (~ 360 px rộng). Đừng chỉ tin lệnh render chạy xong.

**Nội dung**
- [ ] 1. Một thông điệp chính; hook đọc được trong 1 giây ở cỡ điện thoại.
- [ ] 2. Chính tả đúng; kiểu đặt dấu thống nhất (hóa/hoá…) theo `brand.md`.
- [ ] 3. Dấu tiếng Việt hiển thị đúng, không chồng, không bị cắt (ặ, ậ, Ỗ, Ẩ), không rơi về font khác.
- [ ] 4. Số, ngày, giờ, giá đúng nguyên văn đã duyệt; định dạng ngày/giờ/tiền thống nhất; thứ trong tuần khớp ngày.
- [ ] 5. Tên người, chức danh, tên chương trình đúng nguyên văn; lời trích có nguồn.
- [ ] 6. Không còn ô `[ ]` chưa thay (hoặc đã báo "cần bổ sung").
- [ ] 7. Không SĐT / link / mã họp / email trên ảnh (trừ khi brand cho phép).

**Chữ**
- [ ] 8. Tiêu đề ≥ 56 px, thân ≥ 24 px, nhãn ≥ 18 px (khổ 1080).
- [ ] 9. Tối đa 2 họ font, đúng font thương hiệu, đã tải xong (không phải Times/Arial thay thế).
- [ ] 10. Số lining trong font serif ("5.0" không thành "5.o").
- [ ] 11. Không chữ mồ côi; cụm số + đơn vị không bị ngắt dòng.
- [ ] 12. Không đậm/nghiêng giả; chữ gradient không bị cắt chân.

**Bố cục & màu**
- [ ] 13. Lề ngoài ≥ 60 px; các khối thẳng hàng, khoảng cách theo thang.
- [ ] 14. Tối đa 3 cấp chữ, một vùng nhấn chính.
- [ ] 15. Tương phản chữ/nền ≥ 4.5 : 1 (đo ở chỗ sáng nhất sau chữ trên ảnh).
- [ ] 16. Màu đúng token; không màu lạ ngoài bảng màu.

**Ảnh & người**
- [ ] 17. Mặt người rõ, không bị chữ / logo / nút / vùng giao diện đè.
- [ ] 18. Ảnh màu gốc, nét; không halo, không nhuộm, không nhòe nền mạnh, không cắt dán giả.
- [ ] 19. Gradient đọc chữ chỉ sau chữ, mờ hết trước mặt.
- [ ] 20. Nhiều người: cùng cỡ đầu, đầu ngang nhau, sáng tương đương.
- [ ] 21. Ảnh người ngoài đã được phép dùng.

**Khổ & vùng an toàn**
- [ ] 22. Đúng khổ (W × H) cho vị trí đăng; bài 1 ảnh đủ 3 khổ khi cần.
- [ ] 23. 9:16: không chữ/logo/CTA ở 250 px trên và 340 px dưới; reels/TikTok tránh cột phải và đáy chú thích.
- [ ] 24. Ảnh bìa: nội dung trong vùng cắt điện thoại; không chữ dưới ảnh đại diện.
- [ ] 25. 4:5: tiêu đề + mặt trong vùng vuông giữa khi có thể.

**CTA & logo**
- [ ] 26. Đúng một CTA (hoặc không có, với bài thường); động từ đầu; nút cao ≥ 64 px.
- [ ] 27. Logo đúng file, đúng bản màu cho nền, cao ~ 48–72 px, cùng vị trí trong chuỗi.
- [ ] 28. Carousel: chỉ ảnh đầu có khối chương trình + CTA (kiểu "ảnh sạch"); không số trang / vạch tiến trình / "vuốt".

**Xuất file**
- [ ] 29. PNG cho ảnh nhiều chữ, JPG 85–92 cho ảnh chụp toàn khung; sRGB; xuất 2× (2160 px rộng).
- [ ] 30. Tên file `<mã>-<chủ đề>-<khổ>`, đã có tag version; alt text đã soạn sẵn cho người đăng.
- [ ] 31. Checklist riêng trong `brand.md` đã chạy.

---

## 15. 20 lỗi thường gặp

1. Ba thứ cùng to tranh nhau — không có điểm nhìn.
2. Nhồi cả đoạn văn lên ảnh; chữ thân < 22 px.
3. Dùng ảnh 4:5 cho story → chữ rơi vào vùng giao diện.
4. Chữ / logo đè mặt người, hoặc gradient đen phủ cả mặt.
5. Font thiếu dấu tiếng Việt hoặc dấu chạm dòng trên (line-height quá chặt).
6. IN HOA cả câu dài tiếng Việt; giãn chữ chữ thường.
7. Số serif kiểu cũ ("2o26", "5.o").
8. Ba–bốn họ font trên một ảnh.
9. Màu nhấn dùng tràn lan → không còn gì nổi.
10. Tương phản kém: chữ xám trên ảnh, chữ vàng nhạt trên nền trắng.
11. Ảnh người bị nhuộm màu thương hiệu, da xanh/tím; làm mịn da quá tay.
12. Cắt người dán lên nền khác trông "giống AI làm".
13. Hai người cạnh nhau lệch cỡ, lệch độ cao đầu, lệch sáng.
14. Hai–ba nút CTA trên một ảnh; chữ nút "Xem thêm" mơ hồ.
15. Ghi số điện thoại, link dài, mã QR nhỏ không quét được trên ảnh mạng xã hội.
16. Carousel lặp chân trang, số trang, "vuốt để xem" ở mọi ảnh; ảnh 1 yếu.
17. Lặp cùng một thông tin hai lần trên ảnh (ngày ở đầu và ở thẻ).
18. Logo quá to hoặc mỗi ảnh một vị trí.
19. Dữ kiện sai / không nguồn (số liệu, lời trích, chức danh), ngày không khớp thứ.
20. Xuất JPG chất lượng thấp cho ảnh nhiều chữ → chữ nhòe; tên file "final-final-2.png".

---

## 16. Nguồn tham khảo
- Meta — Ads Guide (khổ, tỉ lệ, vùng an toàn story/reels, độ dài chữ quảng cáo): facebook.com/business/ads-guide
- Meta — Advertising Standards (thuộc tính cá nhân, nội dung gây hiểu nhầm, trước–sau): transparency.meta.com/policies/ad-standards
- Instagram Help Center — kích thước và tỉ lệ ảnh, carousel: help.instagram.com
- LinkedIn Help — thông số ảnh bài đăng, ảnh bìa, tài liệu: linkedin.com/help
- YouTube Help — thumbnail tùy chỉnh (1280 × 720, < 2 MB): support.google.com/youtube
- W3C — WCAG 2.1, tiêu chí 1.4.3 (tương phản tối thiểu), 1.4.1 (dùng màu), 2.3.1 (chớp sáng): w3.org/TR/WCAG21
- Nielsen Norman Group — "F-Shaped Pattern of Reading on the Web": nngroup.com/articles/f-shaped-pattern-reading-web-content
- Google Fonts — subset `vietnamese` để chọn font hỗ trợ tiếng Việt: fonts.google.com
- Cách Facebook dàn bài nhiều ảnh, vùng an toàn chi tiết, tỉ lệ chữ 20–30%, cỡ chữ tối thiểu: theo hướng dẫn phổ biến của người làm thiết kế mạng xã hội — kiểm tra lại trên nền tảng trước chiến dịch lớn.
