# DNA thương hiệu — [TÊN THƯƠNG HIỆU] (brand pack `[ten-brand]`)

> Mẫu để tạo brand pack mới. Chép cả thư mục `brands/_mau` → `brands/<ten-brand>` (chữ thường, không dấu, nối bằng gạch ngang), rồi điền từng mục dưới đây.
> Chỗ nào chưa có câu trả lời thì để `[ ]` và hỏi chủ thương hiệu. KHÔNG bịa dữ kiện.
> Hướng dẫn chi tiết: `references/tao-brand-moi.md`.
> Cập nhật lần cuối: [dd.mm.yyyy] · Người duyệt: [vai trò, không ghi thông tin liên hệ cá nhân]

## 1. Nhận diện
- **Tên thương hiệu / sản phẩm**: [tên đầy đủ] — cách ghi trên ấn phẩm: [đủ tên hay viết tắt? viết hoa thế nào?]
- **Tagline**: [nguyên văn, có/không ngoặc kép]
- **Một câu định vị**: [thương hiệu giúp ai, làm gì, khác biệt ở đâu]
- **Người xem chính**: [độ tuổi, nghề, nơi họ thấy ấn phẩm (điện thoại / in / màn hình lớn), họ nhạy với điều gì]
- **Giọng thị giác** (3 tính từ): [vd sang – tiết chế – tin cậy]
- **Nhân vật bảo chứng** (nếu có): [tên + chức danh nguyên văn; quy tắc xuất hiện]

## 2. Màu (ghi vào `tokens.css`)
| Vai | Mã màu | Ghi chú |
|---|---|---|
| Nền chính (`--bg`, `--bg-solid`) | [#] | [sáng/tối, có gradient không] |
| Chữ thân (`--text`) / tiêu đề (`--text-strong`) | [#] / [#] | tương phản ≥ 4.5:1 với nền |
| Màu nhấn (`--accent`, `--accent-soft`) | [#] | dùng cho nhãn, từ khóa, nút |
| Chữ nhấn dạng gradient (`--accent-text`) | [gradient] | chỉ 1 vùng lớn mỗi ảnh |
| Nền nút / chip (`--accent-fill`) + chữ trên nó (`--on-accent`) | [#] / [#] | |
| Thẻ (`--surface`, `--surface-border`) | [#] | |
| Lớp phủ trên ảnh thật (`--overlay-rgb`) | [r,g,b] | chỉ đặt sau chữ |

Nhánh phụ (nếu có, vd sự kiện, dòng sản phẩm khác): [tên nhánh → bảng màu riêng, dùng class trên `.sheet`].

## 3. Chữ
- **Font tiêu đề** (`--font-display`): [tên] — dùng cho: [tiêu đề, hook, ngày]
- **Font thân** (`--font-body`): [tên] — dùng cho mọi chữ còn lại
- Font phải có đủ dấu tiếng Việt. Số trong font serif: bật số lining nếu cần.
- Cỡ tối thiểu trên khổ 1080 px: thân [22] px, nhãn [15] px.
- Chính tả / quy ước: [vd "hóa" hay "hoá", định dạng ngày dd.mm.yyyy, viết hoa từ khóa?]

## 4. Logo
- File: `assets/[logo].svg|png` — [bản màu / bản trắng]; khoảng trống quanh logo: [ ]
- Cấm: [kéo méo, đổi màu, đặt trên nền rối, đặt thêm chữ cạnh logo…]

## 5. Hình ảnh
- Ảnh thật: [giữ màu gốc? được chỉnh gì?] — mặc định của skill: giữ nguyên màu, lớp phủ chỉ sau chữ, không phủ mặt, không halo, không tách nền dán.
- Ảnh tách nền / minh họa / icon: [phong cách, nét mảnh hay đặc]
- Quyền sử dụng: ảnh có người ngoài → không đưa vào repo công khai (để ở `assets/anh-that/`, đã git-ignore).

## 6. Ấn phẩm và mẫu
| Loại ấn phẩm | Khổ | Mẫu trong `templates/` | Ghi chú (CTA, thông tin bắt buộc) |
|---|---|---|---|
| Bài đăng 1 ảnh | 1:1 · 4:5 · 9:16 | `post-4x5.html` | [ ] |
| Carousel / album | 1:1 | `carousel-01-1x1.html` | chỉ ảnh đầu có CTA |
| Quảng cáo ảnh thật + CTA | 1:1 · 4:5 · 9:16 | `ad-cta-4x5.html` | [chữ trên nút] |
| Sự kiện | 4:5 | `event-4x5.html` | ngày · giờ · nơi trong một khối |
| Thẻ trích dẫn | 1:1 | `quote-1x1.html` | lời trích nguyên văn, có nguồn |
| Carousel — ảnh nội dung | 1:1 | `carousel-02-1x1.html` | một ý mỗi ảnh, không CTA |
| Story / reels | 9:16 | `story-9x16.html` | bỏ class `show-safe` trước khi render bản giao |
| [ảnh bìa / poster / flyer / name card…] | [ ] | [ ] | [ ] |

Thông tin bắt buộc trên ấn phẩm: [ngày, địa điểm, tên chương trình…]. Thông tin KHÔNG được ghi trên ảnh: [vd số điện thoại, giá…].

## 7. Nên / Không nên
**Nên**: [ ]
**Không nên** (đã bị chủ thương hiệu bác — ghi kèm ngày và lý do):
| Ngày | Đã thử | Vì sao bị bác |
|---|---|---|
| [dd.mm] | [ ] | [ ] |

## 8. Checklist riêng của thương hiệu (chạy sau checklist chung)
- [ ] Tên thương hiệu ghi đúng cách
- [ ] Đúng bảng màu, đúng font
- [ ] [quy tắc riêng]

## 9. Nhật ký quyết định
- [dd.mm.yyyy] — [quyết định] — [lý do]
