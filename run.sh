#!/bin/bash
set -e

# Change to script directory
cd "$(dirname "$0")"

echo "========================================================="
echo "   🌸 Pastel Schedule Planner - Xếp Thời Khóa Biểu Tự Động"
echo "========================================================="

# Check Python3 availability
if ! command -v python3 &> /dev/null; then
    echo "❌ Lỗi: Máy tính chưa cài đặt Python 3. Vui lòng cài đặt Python 3 trước."
    exit 1
fi

# Create virtual environment if it does not exist
if [ ! -d "venv" ]; then
    echo "📦 Đang tạo môi trường ảo Python (venv)..."
    python3 -m venv venv
    echo "📦 Đang cài đặt thư viện từ requirements.txt..."
    ./venv/bin/pip install --upgrade pip
    ./venv/bin/pip install -r requirements.txt
else
    # Quick check if Flask is installed
    if ! ./venv/bin/python -c "import flask" &> /dev/null; then
        echo "📦 Đang cập nhật thư viện từ requirements.txt..."
        ./venv/bin/pip install -r requirements.txt
    fi
fi

echo "========================================================="
echo "   🚀 Khởi chạy ứng dụng thành công!"
echo "   🌐 Mở trình duyệt và truy cập: http://localhost:5000"
echo "   💡 Nhấn Ctrl + C để dừng ứng dụng"
echo "========================================================="

./venv/bin/python app.py
