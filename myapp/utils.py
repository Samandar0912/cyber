from datetime import datetime


def parse_date(value):
    if isinstance(value, datetime):
        return value.date()
    elif isinstance(value, str):
        return datetime.strptime(value, '%Y-%m-%d %H:%M:%S').date()
    else:
        return None