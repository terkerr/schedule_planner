# 🌸 Pastel Schedule Planner - Xếp Thời Khóa Biểu Đại Học

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1%2B-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Webapp tự động tạo và tối ưu hóa **Thời Khóa Biểu không trùng lịch** cho sinh viên đại học từ dữ liệu mã nguồn HTML trích xuất từ Web Portal của trường, sử dụng giao diện màu **Pastel** nhẹ nhàng, trực quan và hiện đại.

---

## 🌟 Tính Năng Nổi Bật

- ⚡ **Lấy dữ liệu 1-Click từ Portal**: Trích xuất toàn bộ bảng môn học (Lý thuyết, Thực hành), số tín chỉ tối đa, số môn tối đa chỉ với 1 câu lệnh console trình duyệt.
- 🎯 **Lựa chọn môn học & Lớp linh hoạt**:
  - Tìm kiếm nhanh theo mã môn hoặc tên môn.
  - Môn được chọn tự động nhảy lên đầu danh sách để dễ theo dõi.
  - Tùy chọn **"Chọn lớp cụ thể"** qua Popup modal ở giữa màn hình hoặc để hệ thống tự động tìm lớp phù hợp nhất.
- 🚫 **Thuật toán giải quyết xung đột 100%**: Loại bỏ toàn bộ phương án trùng giờ giữa các tiết học Lý thuyết (LT) và Thực hành (TH).
- 🏖️ **Tối ưu ngày nghỉ & Lịch học**:
  - Sắp xếp theo: *Nhiều ngày nghỉ nhất (học dồn)*, *Ít ngày nghỉ nhất (rải đều)*, *Số ngày đến trường ít nhất*.
  - Lọc ngày nghỉ bắt buộc (T2, T3, T4, T5, T6, T7, CN).
- 🛡️ **Kiểm soát hạn mức tín chỉ & môn học**: Cảnh báo tức thì nếu chọn vượt quá số tín chỉ tối đa (`SoTCMax`) hoặc số môn tối đa (`SoMonMax`).
- 📸 **Lịch biểu Calendar & Xuất dữ liệu**:
  - Lưới thời khóa biểu trực quan (Thứ 2 &rarr; Chủ Nhật, 7:00 &rarr; 18:00) với màu Pastel phân biệt từng môn.
  - **Tải ảnh TKB (PNG)** chất lượng cao.
  - **In / Lưu PDF**.
  - **Sao chép mã lớp** để đăng ký trực tiếp trên portal trường.

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy Ứng Dụng

### Cách 1: Chạy nhanh bằng 1 lệnh script (Khuyên dùng)
Clone repository và chạy script `run.sh` (script sẽ tự động tạo môi trường ảo `venv`, cài đặt thư viện và khởi chạy ứng dụng):

```bash
git clone https://github.com/your-username/schedule-planner.git
cd schedule-planner
chmod +x run.sh
./run.sh
```

Truy cập: **`http://localhost:5000`**

---

### Cách 2: Cài đặt thủ công với Python Virtualenv

1. **Clone repository:**
   ```bash
   git clone https://github.com/your-username/schedule-planner.git
   cd schedule-planner
   ```

2. **Tạo và kích hoạt môi trường ảo (`venv`):**
   - **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows (Command Prompt / PowerShell):**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Khởi chạy ứng dụng:**
   ```bash
   python app.py
   ```
   Hoặc chạy với Gunicorn (Production):
   ```bash
   gunicorn -w 2 -b 0.0.0.0:5000 app:app
   ```

5. Mở trình duyệt và truy cập: **`http://localhost:5000`** (hoặc `http://127.0.0.1:5000`)

---

### Cách 3: Chạy bằng Docker / Docker Compose

Nếu máy tính đã cài đặt **Docker**:

```bash
# Sử dụng Docker Compose
docker compose up -d
```
Hoặc build Docker image thủ công:
```bash
docker build -t schedule-planner .
docker run -d -p 5000:5000 --name schedule-planner-app schedule-planner
```
Truy cập: **`http://localhost:5000`**

---

## ☁️ Hướng Dẫn Deploy Lên Cloud (Render, Railway, Fly.io, Heroku)

Dự án đã có sẵn `Dockerfile`, `Procfile` và `requirements.txt`.

### Deploy lên [Render.com](https://render.com):
1. Tạo tài khoản và chọn **New Web Service** &rarr; Kết nối Github Repository.
2. Cấu hình:
   - **Runtime**: `Python 3` hoặc `Docker`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
3. Nhấn **Create Web Service**.

### Deploy lên [Railway.app](https://railway.app):
1. Chọn **New Project** &rarr; **Deploy from GitHub repo**.
2. Railway sẽ tự động nhận diện `Procfile` / `Dockerfile` và deploy trong vài giây.

---

## 📋 Hướng Dẫn Lấy Dữ Liệu Từ Web Portal Trường

1. Mở trang **Đăng ký học phần** trên website portal của trường bạn.
2. Nhấn phím <kbd>F12</kbd> (hoặc click chuột phải chọn **Inspect / Kiểm tra**) &rarr; Chuyển sang tab **Console**.
3. Dán đoạn mã sau và nhấn <kbd>Enter</kbd>:

```javascript
copy((document.querySelector('[data-bind*="SoTCMax"], [data-bind*="SoMonMax"]')?.closest('.panel-default, .panel, .panel-body')?.outerHTML || document.querySelector('.panel.panel-default, .panel-body')?.outerHTML || '') + '\n' + (document.querySelector('#tblSinhVien, table')?.outerHTML || '')); alert('Đã sao chép danh sách môn học, số tín chỉ & số môn tối đa vào Clipboard!');
```

4. Quay lại giao diện webapp &rarr; Nhấn <kbd>Ctrl + V</kbd> vào ô Bước 1 &rarr; Nhấn **"Xử lý dữ liệu học phần"**.

---

## 📁 Cấu Trúc Thư Mục Dự Án

```
schedule_planner/
├── app.py                 # Flask server chính & API endpoints
├── parser.py              # Xử lý & trích xuất HTML, thời gian học phần, hạn mức tín chỉ
├── scheduler.py           # Thuật toán xếp lịch & kiểm tra xung đột thời gian
├── sample_data.py         # Dữ liệu mẫu demo
├── requirements.txt       # Danh sách thư viện Python
├── Dockerfile             # Cấu hình container Docker
├── docker-compose.yml     # Khởi chạy đa container nhanh
├── Procfile               # Cấu hình deploy cloud (Gunicorn)
├── run.sh                 # Script chạy tự động (tự tạo venv & cài package)
├── .gitignore             # File bỏ qua cho Git
├── .dockerignore           # File bỏ qua cho Docker
├── README.md              # Tài liệu hướng dẫn sử dụng
└── templates/
    └── index.html         # Giao diện Pastel Single Page Application (HTML/Tailwind/JS)
```

---

## 📄 Giấy Phép (License)
Dự án được phân phối dưới giấy phép [MIT License](LICENSE).
