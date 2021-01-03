"""Original case templates with independently supplied expected results."""
import copy
import re

TEMPLATES = [('expand task offsets across a month boundary', {'employee_id': '@i+1', 'hire_date': '2021-01-31', 'template': [{'id': 't{n}', 'offset_days': 1, 'title': 'Read handbook'}]}, {'tasks': [{'id': 't{n}', 'employee_id': '@i+1', 'due': '2021-02-01', 'title': 'Read handbook'}]}), ('sort pre-start and hire-day assignments by due date', {'employee_id': 1, 'hire_date': '2021-01-04', 'template': [{'id': 'b{n}', 'offset_days': 0, 'title': 'Meet team'}, {'id': 'a{n}', 'offset_days': -1, 'title': 'Read welcome note'}]}, {'tasks': [{'id': 'a{n}', 'employee_id': 1, 'due': '2021-01-03', 'title': 'Read welcome note'}, {'id': 'b{n}', 'employee_id': 1, 'due': '2021-01-04', 'title': 'Meet team'}]}), ('allow an empty onboarding template', {'employee_id': 1, 'hire_date': '2021-01-01', 'template': []}, {'tasks': []}), ('reject duplicate template task IDs', {'employee_id': 1, 'hire_date': '2021-01-01', 'template': [{'id': 'a{n}', 'offset_days': 0, 'title': 'A'}, {'id': 'a{n}', 'offset_days': 1, 'title': 'B'}]}, None), ('reject task dates that overflow the supported calendar', {'employee_id': 1, 'hire_date': '9999-12-31', 'template': [{'id': 'a{n}', 'offset_days': 1, 'title': 'A'}]}, None)]


def make_case(index):
    description, source, expected = copy.deepcopy(TEMPLATES[index % len(TEMPLATES)])
    def fill(value):
        if isinstance(value, str):
            if re.fullmatch(r"@i[+]\d+", value):
                return index + int(value[3:])
            return value.replace("{n}", str(index))
        if isinstance(value, list):
            return [fill(item) for item in value]
        if isinstance(value, dict):
            return {fill(key): fill(item) for key, item in value.items()}
        return value
    case = {"id": "onboarding-{:04d}".format(index), "description": description, "input": fill(source)}
    case.update({"expected_error": True} if expected is None else {"expected": fill(expected)})
    return case
