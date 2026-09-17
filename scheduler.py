from itertools import product
from typing import List, Dict, Any, Optional, Set

def check_slots_conflict(slot1: Dict[str, Any], slot2: Dict[str, Any]) -> bool:
    """
    Returns True if slot1 and slot2 overlap on the same day.
    """
    if slot1['day'] != slot2['day']:
        return False
    
    # Overlap occurs if start of one is strictly before end of the other
    overlap = max(slot1['start_min'], slot2['start_min']) < min(slot1['end_min'], slot2['end_min'])
    return overlap


def check_classes_conflict(class1: Dict[str, Any], class2: Dict[str, Any]) -> bool:
    """
    Returns True if any slot from class1 conflicts with any slot from class2.
    """
    for s1 in class1.get('slots', []):
        for s2 in class2.get('slots', []):
            if check_slots_conflict(s1, s2):
                return True
    return False


def generate_schedules(
    course_groups: Dict[str, List[Dict[str, Any]]],
    selected_courses: List[str],
    user_class_selections: Dict[str, List[str]], # course_code -> list of chosen class_codes (if empty, all are eligible)
    filter_days_off: Optional[List[int]] = None, # days that MUST be free (e.g. [6, 7] for Fri, Sat)
    filter_study_days: Optional[List[int]] = None, # days that MUST have classes
    sort_by: str = "days_off_desc" # "days_off_desc", "days_off_asc", "study_days_asc", "study_days_desc"
) -> List[Dict[str, Any]]:
    """
    Finds all non-overlapping schedule combinations.
    """
    if not selected_courses:
        return []

    # Prepare candidate classes for each selected course
    candidate_pools = []
    for code in selected_courses:
        all_classes_for_course = course_groups.get(code, [])
        chosen_classes = user_class_selections.get(code, [])
        
        if chosen_classes:
            filtered = [c for c in all_classes_for_course if c['class_code'] in chosen_classes]
        else:
            filtered = all_classes_for_course

        if not filtered:
            # If a selected course has no available class options, no complete schedule is possible
            return []
        
        candidate_pools.append(filtered)

    valid_schedules = []
    
    # Generate Cartesian product of candidate classes
    for combination in product(*candidate_pools):
        # combination is a tuple of class objects, one per selected course
        has_conflict = False
        n = len(combination)
        
        for i in range(n):
            for j in range(i + 1, n):
                if check_classes_conflict(combination[i], combination[j]):
                    has_conflict = True
                    break
            if has_conflict:
                break
        
        if not has_conflict:
            # Compute schedule statistics
            all_slots = []
            study_days_set: Set[int] = set()
            total_credits = 0
            
            for cls in combination:
                total_credits += cls.get('credits', 0)
                for slot in cls.get('slots', []):
                    slot_info = dict(slot)
                    slot_info['course_name'] = cls['course_name']
                    slot_info['course_code'] = cls['course_code']
                    slot_info['class_code'] = cls['class_code']
                    slot_info['credits'] = cls['credits']
                    all_slots.append(slot_info)
                    study_days_set.add(slot['day'])

            # Calculate days off (from Mon 2 to Sun 8)
            all_days = {2, 3, 4, 5, 6, 7, 8}
            days_off_set = all_days - study_days_set
            
            # Apply filters if any
            if filter_days_off:
                # Every requested day off MUST be in days_off_set
                if not set(filter_days_off).issubset(days_off_set):
                    continue
            
            if filter_study_days:
                # Every requested study day MUST be in study_days_set
                if not set(filter_study_days).issubset(study_days_set):
                    continue

            day_names_map = {2: 'T2', 3: 'T3', 4: 'T4', 5: 'T5', 6: 'T6', 7: 'T7', 8: 'CN'}
            
            valid_schedules.append({
                "classes": list(combination),
                "slots": all_slots,
                "total_credits": total_credits,
                "num_classes": len(combination),
                "study_days": sorted(list(study_days_set)),
                "study_days_names": [day_names_map[d] for d in sorted(list(study_days_set))],
                "num_study_days": len(study_days_set),
                "days_off": sorted(list(days_off_set)),
                "days_off_names": [day_names_map[d] for d in sorted(list(days_off_set))],
                "num_days_off": len(days_off_set),
            })

    # Sorting
    if sort_by == "days_off_desc":
        valid_schedules.sort(key=lambda s: (s['num_days_off'], -s['num_study_days']), reverse=True)
    elif sort_by == "days_off_asc":
        valid_schedules.sort(key=lambda s: s['num_days_off'])
    elif sort_by == "study_days_asc":
        valid_schedules.sort(key=lambda s: s['num_study_days'])
    elif sort_by == "study_days_desc":
        valid_schedules.sort(key=lambda s: s['num_study_days'], reverse=True)

    return valid_schedules
