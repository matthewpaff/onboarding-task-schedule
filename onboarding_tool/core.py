"""Original bounded concept exercise with supplied synthetic data only."""


def fields(value, required, optional=()):
    if not isinstance(value, dict) or not set(required) <= value.keys() or not value.keys() <= set(required) | set(optional):
        raise ValueError("Unexpected or missing object fields")


def integer(value, low=0, high=10**12):
    if type(value) is not int or not low <= value <= high:
        raise ValueError("Integer outside the supported range")
    return value


def label(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 80 or any(ord(c) < 32 for c in value):
        raise ValueError("Expected a nonblank label of at most 80 characters")
    return value.strip()


def sequence(value, maximum):
    if not isinstance(value, list) or len(value) > maximum:
        raise ValueError("Expected a bounded list")
    return value


def day(value):
    from datetime import date
    import re
    if not isinstance(value,str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}",value):
        raise ValueError("Use YYYY-MM-DD")
    return date.fromisoformat(value)


def text(value,maximum=10000):
    if not isinstance(value,str) or len(value)>maximum:
        raise ValueError("Expected bounded text")
    return value

def evaluate(data):
    from datetime import timedelta
    fields(data,("employee_id","hire_date","template"))
    employee,start=integer(data["employee_id"],1),day(data["hire_date"])
    seen,rows=set(),[]
    for row in sequence(data["template"],100):
        fields(row,("id","offset_days","title"))
        ident,offset,title=label(row["id"]),integer(row["offset_days"],-30,365),label(row["title"])
        if ident in seen:
            raise ValueError("Repeated template task ID")
        seen.add(ident)
        try:
            due=(start+timedelta(days=offset)).isoformat()
        except OverflowError as error:
            raise ValueError("Task date is outside the supported calendar") from error
        rows.append({"id":ident,"employee_id":employee,"due":due,"title":title})
    return {"tasks":sorted(rows,key=lambda row:(row["due"],row["id"]))}
