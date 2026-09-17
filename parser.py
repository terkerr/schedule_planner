import re
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Optional

def parse_portal_limits(html_content: str) -> Dict[str, Any]:
    """
    Extracts student credit and subject limits from school portal HTML:
    - SoTCMax: Maximum credits
    - SoMonMax: Maximum subjects
    - SoTCDaDK: Registered credits
    - SoMonDaDK: Registered subjects
    """
    if not html_content or not html_content.strip():
        return {"max_credits": None, "max_subjects": None, "reg_credits": None, "reg_subjects": None}
    
    soup = BeautifulSoup(html_content, 'lxml')
    limits = {
        "max_credits": None,
        "max_subjects": None,
        "reg_credits": None,
        "reg_subjects": None
    }
    
    # 1. Check data-bind attributes (any tag, not only span)
    tc_max_tag = soup.find(lambda tag: tag.has_attr('data-bind') and 'SoTCMax' in tag['data-bind'])
    if tc_max_tag:
        digits = re.findall(r'\d+', tc_max_tag.get_text(strip=True))
        if digits:
            limits["max_credits"] = int(digits[0])
        
    mon_max_tag = soup.find(lambda tag: tag.has_attr('data-bind') and 'SoMonMax' in tag['data-bind'])
    if mon_max_tag:
        digits = re.findall(r'\d+', mon_max_tag.get_text(strip=True))
        if digits:
            limits["max_subjects"] = int(digits[0])

    tc_reg_tag = soup.find(lambda tag: tag.has_attr('data-bind') and 'SoTCDaDK' in tag['data-bind'])
    if tc_reg_tag:
        digits = re.findall(r'\d+', tc_reg_tag.get_text(strip=True))
        if digits:
            limits["reg_credits"] = int(digits[0])

    mon_reg_tag = soup.find(lambda tag: tag.has_attr('data-bind') and 'SoMonDaDK' in tag['data-bind'])
    if mon_reg_tag:
        digits = re.findall(r'\d+', mon_reg_tag.get_text(strip=True))
        if digits:
            limits["reg_subjects"] = int(digits[0])

    # 2. Fallback regex patterns
    if limits["max_credits"] is None:
        m = re.search(r'SoTCMax[^>]*>(\d+)<', html_content, re.IGNORECASE)
        if not m:
            m = re.search(r'Số\s+tín\s+chỉ\s+tối\s+đa\s*[:\s<>/a-z0-9="\'-]*?(\d+)', html_content, re.IGNORECASE)
        if m:
            limits["max_credits"] = int(m.group(1))

    if limits["max_subjects"] is None:
        m = re.search(r'SoMonMax[^>]*>(\d+)<', html_content, re.IGNORECASE)
        if not m:
            m = re.search(r'Số\s+môn(?:\s+học)?\s+tối\s+đa\s*[:\s<>/a-z0-9="\'-]*?(\d+)', html_content, re.IGNORECASE)
        if m:
            limits["max_subjects"] = int(m.group(1))

    return limits


def parse_time_str(time_str: str) -> List[Dict[str, Any]]:
    """
    Parse strings like:
    - "T4 13:30-17:10"
    - "T2 07:30-11:10<br>T5 13:30-15:10"
    - "Thứ 2: 7h30 - 11h30"
    - "T3 (Tiết 1-4)"
    - "CN 08:00-11:30"
    Returns a list of slots: [{"day": 4, "day_name": "T4", "start_min": 810, "end_min": 1030, "raw": "T4 13:30-17:10"}]
    """
    if not time_str:
        return []
    
    # Normalize <br>, newlines, semicolons
    cleaned = re.sub(r'<br\s*/?>', '\n', time_str, flags=re.IGNORECASE)
    cleaned = re.sub(r'[\r\t]', ' ', cleaned)
    
    lines = [line.strip() for line in cleaned.split('\n') if line.strip()]
    slots = []

    day_map = {
        '2': (2, 'Thứ 2'), 'hai': (2, 'Thứ 2'), 'mon': (2, 'Thứ 2'), 't2': (2, 'Thứ 2'),
        '3': (3, 'Thứ 3'), 'ba': (3, 'Thứ 3'), 'tue': (3, 'Thứ 3'), 't3': (3, 'Thứ 3'),
        '4': (4, 'Thứ 4'), 'tu': (4, 'Thứ 4'), 'tư': (4, 'Thứ 4'), 'wed': (4, 'Thứ 4'), 't4': (4, 'Thứ 4'),
        '5': (5, 'Thứ 5'), 'nam': (5, 'Thứ 5'), 'năm': (5, 'Thứ 5'), 'thu': (5, 'Thứ 5'), 't5': (5, 'Thứ 5'),
        '6': (6, 'Thứ 6'), 'sau': (6, 'Thứ 6'), 'sáu': (6, 'Thứ 6'), 'fri': (6, 'Thứ 6'), 't6': (6, 'Thứ 6'),
        '7': (7, 'Thứ 7'), 'bay': (7, 'Thứ 7'), 'bảy': (7, 'Thứ 7'), 'sat': (7, 'Thứ 7'), 't7': (7, 'Thứ 7'),
        'cn': (8, 'Chủ nhật'), 'chunhat': (8, 'Chủ nhật'), 'chủ nhật': (8, 'Chủ nhật'), 'sun': (8, 'Chủ nhật'), '8': (8, 'Chủ nhật')
    }

    # Standard period to minute mapping (default university shift format)
    # Tiết 1: 07:00 or 07:30
    period_map = {
        1: (7 * 60 + 30, 8 * 60 + 15),
        2: (8 * 60 + 20, 9 * 60 + 5),
        3: (9 * 60 + 15, 10 * 60 + 0),
        4: (10 * 60 + 5, 10 * 60 + 50),
        5: (10 * 60 + 55, 11 * 60 + 40),
        6: (12 * 60 + 30, 13 * 60 + 15),
        7: (13 * 60 + 30, 14 * 60 + 15),
        8: (14 * 60 + 20, 15 * 60 + 5),
        9: (15 * 60 + 15, 16 * 60 + 0),
        10: (16 * 60 + 5, 16 * 60 + 50),
        11: (17 * 60 + 0, 17 * 60 + 45),
        12: (17 * 60 + 50, 18 * 60 + 35),
        13: (18 * 60 + 40, 19 * 60 + 25),
        14: (19 * 60 + 30, 20 * 60 + 15),
        15: (20 * 60 + 20, 21 * 60 + 5),
    }

    for line in lines:
        # Match day pattern: T2, T3, Thứ 2, CN, etc.
        # Match time pattern: 13:30-17:10 or 7h30 - 11h30 or Tiết 1-4
        day_match = re.search(r'(?:thứ\s*|t)?([2-7]|cn|chủ\s*nhật)', line, re.IGNORECASE)
        if not day_match:
            continue
        
        raw_day = day_match.group(1).lower().replace(' ', '')
        if raw_day not in day_map:
            if 'cn' in raw_day or 'chủnhật' in raw_day:
                day_num, day_label = 8, 'Chủ nhật'
            else:
                continue
        else:
            day_num, day_label = day_map[raw_day]

        # Check for HH:MM - HH:MM pattern (e.g. 13:30-17:10, 7h30-11h10)
        time_match = re.search(r'(\d{1,2})[h:](\d{2})?\s*[-–—tođến]+\s*(\d{1,2})[h:](\d{2})?', line, re.IGNORECASE)
        if time_match:
            sh = int(time_match.group(1))
            sm = int(time_match.group(2)) if time_match.group(2) else 0
            eh = int(time_match.group(3))
            em = int(time_match.group(4)) if time_match.group(4) else 0
            
            start_min = sh * 60 + sm
            end_min = eh * 60 + em
            
            slots.append({
                "day": day_num,
                "day_name": day_label,
                "start_min": start_min,
                "end_min": end_min,
                "start_str": f"{sh:02d}:{sm:02d}",
                "end_str": f"{eh:02d}:{em:02d}",
                "raw": line
            })
            continue

        # Check for Period (Tiết X-Y) pattern: e.g. "Tiết 1-4", "1-3", "tiết 7->10"
        period_match = re.search(r'(?:tiết\s*)?(\d{1,2})\s*[-–—tođến]+\s*(\d{1,2})', line, re.IGNORECASE)
        if period_match:
            p_start = int(period_match.group(1))
            p_end = int(period_match.group(2))
            
            start_min = period_map.get(p_start, (7 * 60, 8 * 60))[0]
            end_min = period_map.get(p_end, (17 * 60, 18 * 60))[1]
            
            sh, sm = divmod(start_min, 60)
            eh, em = divmod(end_min, 60)
            
            slots.append({
                "day": day_num,
                "day_name": day_label,
                "start_min": start_min,
                "end_min": end_min,
                "start_str": f"{sh:02d}:{sm:02d}",
                "end_str": f"{eh:02d}:{em:02d}",
                "raw": line
            })

    return slots


def parse_portal_html(html_content: str) -> List[Dict[str, Any]]:
    """
    Parses school portal HTML table rows or full table.
    Supports Knockout.js data-bind markup as well as regular HTML tables.
    """
    if not html_content or not html_content.strip():
        return []

    soup = BeautifulSoup(html_content, 'lxml')
    rows = soup.find_all('tr')
    
    courses = []
    
    for row in rows:
        # Check for knockout data-bind attributes first
        ky_hieu_td = row.find(lambda tag: tag.name == 'td' and tag.has_attr('data-bind') and 'KyHieu' in tag['data-bind'])
        ten_mh_td = row.find(lambda tag: tag.name == 'td' and tag.has_attr('data-bind') and 'TenMH' in tag['data-bind'])
        ma_lop_td = row.find(lambda tag: tag.name == 'td' and tag.has_attr('data-bind') and 'MaLopHP' in tag['data-bind'])
        so_tc_td = row.find(lambda tag: tag.name == 'td' and tag.has_attr('data-bind') and 'SoTinChi' in tag['data-bind'])
        lt_td = row.find(lambda tag: tag.name == 'td' and tag.has_attr('data-bind') and 'LichHocLT' in tag['data-bind'])
        th_td = row.find(lambda tag: tag.name == 'td' and tag.has_attr('data-bind') and 'LichHocTH' in tag['data-bind'])
        sv_td = row.find(lambda tag: tag.name == 'td' and tag.has_attr('data-bind') and 'SoSVDK' in tag['data-bind'])

        if ky_hieu_td and ten_mh_td and ma_lop_td:
            code = ky_hieu_td.get_text(strip=True)
            name = ten_mh_td.get_text(strip=True)
            class_code = ma_lop_td.get_text(strip=True)
            
            try:
                credits = int(so_tc_td.get_text(strip=True)) if so_tc_td else 0
            except ValueError:
                credits = 0

            lt_raw = lt_td.decode_contents().strip() if lt_td else ""
            th_raw = th_td.decode_contents().strip() if th_td else ""
            sv_count = sv_td.get_text(strip=True) if sv_td else ""

            lt_slots = parse_time_str(lt_raw)
            th_slots = parse_time_str(th_raw)
            
            all_slots = []
            for s in lt_slots:
                s_copy = dict(s)
                s_copy['type'] = 'LT'
                all_slots.append(s_copy)
            for s in th_slots:
                s_copy = dict(s)
                s_copy['type'] = 'TH'
                all_slots.append(s_copy)

            if code and name and class_code:
                courses.append({
                    "id": f"{code}_{class_code}",
                    "course_code": code,
                    "course_name": name,
                    "class_code": class_code,
                    "credits": credits,
                    "schedule_lt_raw": BeautifulSoup(lt_raw, 'html.parser').get_text(separator=" ").strip(),
                    "schedule_th_raw": BeautifulSoup(th_raw, 'html.parser').get_text(separator=" ").strip(),
                    "slots": all_slots,
                    "max_sv": sv_count
                })
        else:
            # Fallback for generic HTML table where columns might be positional
            tds = row.find_all('td')
            if len(tds) >= 6:
                text_vals = [td.get_text(separator="\n").strip() for td in tds]
                # Look for code pattern (e.g. BAA00103, IT001, etc.)
                # If first column is index, second is code, third is name, etc.
                idx_offset = 0
                if text_vals[0].isdigit():
                    idx_offset = 1
                
                if len(text_vals) >= idx_offset + 5:
                    code = text_vals[idx_offset]
                    name = text_vals[idx_offset + 1]
                    class_code = text_vals[idx_offset + 2]
                    
                    try:
                        credits = int(text_vals[idx_offset + 3])
                    except (ValueError, IndexError):
                        credits = 0
                    
                    lt_raw = text_vals[idx_offset + 4] if len(text_vals) > idx_offset + 4 else ""
                    th_raw = text_vals[idx_offset + 5] if len(text_vals) > idx_offset + 5 else ""

                    # Check if this looks like a valid course row
                    if re.match(r'^[A-Z0-9_\-]+$', code, re.IGNORECASE) and len(code) >= 3 and len(name) >= 2:
                        lt_slots = parse_time_str(lt_raw)
                        th_slots = parse_time_str(th_raw)
                        
                        all_slots = []
                        for s in lt_slots:
                            s_copy = dict(s)
                            s_copy['type'] = 'LT'
                            all_slots.append(s_copy)
                        for s in th_slots:
                            s_copy = dict(s)
                            s_copy['type'] = 'TH'
                            all_slots.append(s_copy)

                        courses.append({
                            "id": f"{code}_{class_code}",
                            "course_code": code,
                            "course_name": name,
                            "class_code": class_code,
                            "credits": credits,
                            "schedule_lt_raw": lt_raw,
                            "schedule_th_raw": th_raw,
                            "slots": all_slots,
                            "max_sv": ""
                        })

    return courses
