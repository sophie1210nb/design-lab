# Công cụ xử lý ảnh (offline, miễn phí)

## 0. Xem nhanh / render
- `scripts/preview.sh <file.html> [W] [H]` — PNG scale 1, không git, ra `../output/preview/`.
- `scripts/render-social.sh <file.html> W H "mô tả" [nhóm]` — PNG scale 2 + commit + tag version.
- `scripts/khoi-phuc.sh <ten-hoac-nhom> vN [thư-mục]` — lấy lại bản cũ thành version mới.
Cần Google Chrome (tự tìm; hoặc đặt `CHROME=…`), Git Bash/bash, mạng để tải Google Fonts.

## 1. `scripts/xoa_chu_anh.py` — xóa chữ / vật thể sau lưng người (LaMa)
Cần: `pip install onnxruntime numpy pillow opencv-python-headless`

Mô hình LaMa (~200 MB) KHÔNG có trong repo. Tải một lần:
```bash
mkdir -p ~/.thiet-ke-models
curl -L -o ~/.thiet-ke-models/lama_fp32.onnx https://huggingface.co/Carve/LaMa-ONNX/resolve/main/lama_fp32.onnx
```
(Script đọc `~/.thiet-ke-models/lama_fp32.onnx`; đổi bằng `--model <đường-dẫn>`.)

```bash
python scripts/xoa_chu_anh.py VAO.jpg RA.jpg x0,y0,x1,y1 [x0,y0,x1,y1 ...] [tùy chọn]
```
- Tọa độ là pixel ảnh GỐC. Pixel ngoài mask giữ nguyên, ảnh giữ độ phân giải; có khớp tông màu với viền.
- Hậu tố vùng: `:sang` (chỉ xóa chữ SÁNG trên nền tối) · `:toi` (chữ TỐI trên nền sáng) — dùng khi chữ sát người.
- `--poly "x,y x,y ..."` đa giác xóa chính xác · `--giu x0,y0,x1,y1` vùng bảo vệ (mặt, tay, mic) · `--mask m.png` (trắng = xóa).
- `--xem-mask xem.jpg` chỉ xuất ảnh xem trước (đỏ = vùng sẽ xóa) — NÊN chạy trước.
- Khác: `--dilate 8`, `--feather 6`, `--nguong 35`, `--nguong-max 110`, `--quality 92`.

Mẹo: chia chữ thành nhiều hình chữ nhật hẹp theo dòng; vùng sát người dùng `:sang`/`:toi` hoặc `--poly`; chạy lượt 2 cho mẩu sót. Luôn so trước/sau, phóng to chỗ sát mặt, tay, mic. KHÔNG đặt mask lên mặt người. Lưu ảnh sạch vào `assets/anh-that/clean/` cùng tên gốc.

## 2. `scripts/tach_nen.py` — tách nền (PNG trong suốt, rembg)
Cần: `pip install rembg pillow onnxruntime` (lần đầu tự tải model).
```bash
python scripts/tach_nen.py VAO.jpg RA.png [--model u2net_human_seg|u2net|isnet-general-use] [--alpha-matting]
```
Dùng cho bố cục người đứng trên nền thiết kế (vd hai diễn giả trên nền thương hiệu). KHÔNG dùng để cắt người khỏi ảnh sự kiện rồi dán lên nền khác cho quảng cáo "ảnh thật" — trông cắt dán (xem `nguyen-tac-thiet-ke.md`). Kiểm tra mép tóc, kính, mic ở 100%.

## 3. Cân sáng hai người cạnh nhau
Hai ảnh tách nền đặt cạnh nhau phải cùng độ sáng mặt và cùng cỡ đầu. Nếu một người tối hơn: làm bản đã cân sáng (vd Pillow `ImageEnhance.Brightness`) và lưu thành file riêng trong `assets/` (ghi vào `brand.md` là LUÔN dùng bản này). Với ảnh thật: filter CSS nhẹ riêng cho ảnh đó (`brightness(1.05–1.15)`), không vượt 1.2.

## 4. Quyền riêng tư
Ảnh có khách, học viên, người ngoài → để trong `assets/anh-that/` (git-ignore), không đưa lên repo công khai. Ghi cách lấy ảnh trong `assets/anh-that/DOC-TOI.md`, không ghi link/ID kho ảnh nội bộ.
