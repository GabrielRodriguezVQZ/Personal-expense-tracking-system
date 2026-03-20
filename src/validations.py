# validations.py

def validate_amount(value):
    try:
        amount = float(value)
        return amount if amount > 0 else None
    except:
        return None


def validate_option(value):
    try:
        option = int(value)
        return option if 0 <= option <= 6 else None
    except:
        return None


def validate_index(value, max_length):
    try:
        index = int(value) - 1
        return index if 0 <= index < max_length else None
    except:
        return None


def validate_text(text):
    cleaned = text.strip()
    return cleaned if cleaned else None


def validate_type(value):
    value = value.lower().strip()
    return value if value in ["income", "expense"] else None