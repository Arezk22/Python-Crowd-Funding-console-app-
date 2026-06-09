
import re

def validate_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_egyptian_phone(phone):
    pattern = r'^(010|011|012|015)\d{8}$'
    return re.match(pattern, phone) is not None

def validate_date(date_str):
    from datetime import datetime
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False