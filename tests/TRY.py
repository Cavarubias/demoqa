import re

def is_valid_date(date_text):
    pattern = re.compile('/\s(\d{1,2}\s[a-zA-Z]+\s\d{4})\s/')
    return pattern.match(date_text)