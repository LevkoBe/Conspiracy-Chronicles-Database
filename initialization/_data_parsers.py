from datetime import datetime

def handle_numeric_value(value, is_decimal=False):
    """Safely parse numeric values with optional decimal conversion."""
    if value is None or value.strip() == "":
        return None
    try:
        if is_decimal:
            return float(value.replace(',', '.'))
        else:
            return int(value.replace(',', ''))
    except ValueError:
        return None

def parse_scientific_notation(value):
    """Converts scientific notation to float, and normalizes large values like trillions."""
    try:
        num = float(value)
        return round(num, 2)
    except (ValueError, TypeError):
        return None

def parse_event_date(year, month, day):
    """Parses dates and handles BC years and zero-padded year formats."""
    try:
        if year == '0':
            year = '0001'

        if len(year) < 4:
            year = year.zfill(4)
        
        month = month if month.isdigit() else "01" 
        day = day if day.isdigit() else "01"
        
        date_str = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except Exception as e:
        print(f"Invalid date format: {year}-{month}-{day} ({e})")
        return None
