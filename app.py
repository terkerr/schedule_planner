import os
import json
from flask import Flask, render_template, request, jsonify
from parser import parse_portal_html, parse_portal_limits
from scheduler import generate_schedules
from sample_data import SAMPLE_HTML

app = Flask(__name__)
app.config['SECRET_KEY'] = 'schedule-planner-pastel-secret'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/sample-data', methods=['GET'])
def get_sample_data():
    parsed = parse_portal_html(SAMPLE_HTML)
    limits = parse_portal_limits(SAMPLE_HTML)
    return jsonify({
        "status": "success",
        "raw_html": SAMPLE_HTML,
        "courses": parsed,
        "limits": limits
    })


@app.route('/api/parse-html', methods=['POST'])
def parse_html_endpoint():
    data = request.get_json() or {}
    html_content = data.get('html', '')
    
    if not html_content.strip():
        return jsonify({"status": "error", "message": "Vui lòng nhập mã HTML từ web portal."}), 400

    courses = parse_portal_html(html_content)
    limits = parse_portal_limits(html_content)
    if not courses:
        return jsonify({
            "status": "error",
            "message": "Không tìm thấy dữ liệu học phần hợp lệ trong đoạn HTML. Vui lòng kiểm tra lại định dạng bảng điểm/đăng ký học phần."
        }), 400

    # Group courses by course_code
    grouped = {}
    for c in courses:
        code = c['course_code']
        if code not in grouped:
            grouped[code] = {
                "course_code": code,
                "course_name": c['course_name'],
                "credits": c['credits'],
                "classes": []
            }
        grouped[code]['classes'].append(c)

    return jsonify({
        "status": "success",
        "total_classes": len(courses),
        "total_courses": len(grouped),
        "course_groups": list(grouped.values()),
        "raw_parsed": courses,
        "limits": limits
    })


@app.route('/api/generate-schedules', methods=['POST'])
def generate_schedules_endpoint():
    data = request.get_json() or {}
    
    course_data = data.get('courses', []) # Flat list of all available class items
    selected_course_codes = data.get('selected_courses', []) # List of selected course codes
    user_class_selections = data.get('class_selections', {}) # {course_code: [class_code_1, ...]}
    
    filter_days_off = data.get('filter_days_off', []) # e.g. [6, 7]
    filter_study_days = data.get('filter_study_days', []) # e.g. [2]
    sort_by = data.get('sort_by', 'days_off_desc')

    if not selected_course_codes:
        return jsonify({
            "status": "error",
            "message": "Vui lòng chọn ít nhất một môn học để xếp thời khóa biểu."
        }), 400

    # Group classes by course code
    course_groups = {}
    for item in course_data:
        code = item['course_code']
        if code not in course_groups:
            course_groups[code] = []
        course_groups[code].append(item)

    # Convert filter days to integers
    days_off = [int(d) for d in filter_days_off if str(d).isdigit()]
    study_days = [int(d) for d in filter_study_days if str(d).isdigit()]

    schedules = generate_schedules(
        course_groups=course_groups,
        selected_courses=selected_course_codes,
        user_class_selections=user_class_selections,
        filter_days_off=days_off,
        filter_study_days=study_days,
        sort_by=sort_by
    )

    return jsonify({
        "status": "success",
        "total_schedules": len(schedules),
        "schedules": schedules
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
