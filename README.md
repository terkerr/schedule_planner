# Webapp Xếp Thời Khóa Biểu Đại Học (Pastel Schedule Planner)

Webapp tự động xếp và tối ưu thời khóa biểu cho sinh viên đại học từ dữ liệu HTML của Web Portal trường, sử dụng giao diện màu Pastel trang nhã, hiện đại.

---

## 🌟 Các tính năng nổi bật

1. **Nhập dữ liệu cực kỳ nhanh chóng từ Web Portal**:
   - **Cách 1 (1-Click Console)**: Nhấn `F12` trên trang portal &rarr; Dán lệnh `copy((document.querySelector('[data-bind*="SoTCMax"], [data-bind*="SoMonMax"]')?.closest('.panel-default, .panel, .panel-body')?.outerHTML || document.querySelector('.panel.panel-default, .panel-body')?.outerHTML || '') + '\n' + (document.querySelector('#tblSinhVien, table')?.outerHTML || '')); alert('Đã sao chép danh sách môn học, số tín chỉ & số môn tối đa vào Clipboard!');` &rarr; Webapp tự trích xuất toàn bộ môn học, lớp học phần, lịch Lý thuyết (LT), Thực hành (TH), cùng giới hạn số tín chỉ tối đa và số môn tối đa.
   - **Cách 2**: Copy bảng HTML trực tiếp hoặc tải file `.html` / `.txt` lên.
   - **Dữ liệu mẫu**: Có sẵn nút nạp dữ liệu mẫu để trải nghiệm ngay.

2. **Lựa chọn môn học linh hoạt**:
   - Tìm kiếm môn học theo tên hoặc mã môn.
   - Chọn nhiều môn cùng lúc.
   - Tùy chọn **"Chọn lớp cụ thể"** cho từng môn nếu chỉ muốn học một số lớp nhất định (hoặc để mặc định cho hệ thống tự động tìm lớp tối ưu).
   - Đảm bảo quy tắc: Mỗi môn học chỉ đăng ký 1 lớp duy nhất.

3. **Thuật toán xếp lịch & giải quyết xung đột**:
   - Tự động kiểm tra và loại bỏ hoàn toàn các trường hợp trùng lịch giữa các môn/lớp (bao gồm cả tiết LT và TH).
   - **Sắp xếp biến thể**: Sắp xếp theo nhiều ngày nghỉ nhất (học dồn ngày để có kỳ nghỉ dài), ít ngày nghỉ nhất (rải đều), ít số ngày đến trường nhất.
   - **Lọc ngày nghỉ bắt buộc**: Chọn các thứ muốn nghỉ (T2, T3, T4, T5, T6, T7, CN).

4. **Lịch biểu trực quan & Xuất dữ liệu**:
   - Giao diện lưới thời khóa biểu (Thứ 2 &rarr; Chủ Nhật, 7:00 &rarr; 18:00) với màu Pastel phân biệt từng môn học.
   - **Tải ảnh TKB (PNG)** chất lượng cao chỉ với 1 click.
   - **In / Lưu PDF** hỗ trợ in ấn tiện lợi.
   - **Sao chép mã lớp** nhanh để dán vào form đăng ký môn học của trường.

---

## 🚀 Hướng dẫn khởi chạy

### Chạy trực tiếp qua script:
```bash
cd /home/terkerr/projects/schedule_planner
./run.sh
```

### Hoặc kích hoạt môi trường ảo:
```bash
cd /home/terkerr/projects/schedule_planner
source venv/bin/activate
python3 app.py
```

Truy cập ứng dụng tại: **`http://localhost:5000`** (hoặc `http://127.0.0.1:5000`)
