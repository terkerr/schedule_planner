#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
echo "========================================================="
echo "   🚀 Khởi chạy Webapp Xếp Thời Khóa Biểu Pastel        "
echo "   🌐 Truy cập: http://127.0.0.1:5000                   "
echo "========================================================="
python3 app.py
