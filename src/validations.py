# validations.py

def validate_amount(value):
    try:
        amount = float(value)
        if amount <= 0:
            print("Amount must be greater than 0")
            return None
        return amount
    except:
        print("Invalid amount. Please enter a number.")
        return None


def validate_option(value):
    try:
        option = int(value)
        if option < 0 or option > 6:
            print("Option out of range")
            return None
        return option
    except:
        print("Invalid option. Enter a number.")
        return None


def validate_index(value, max_length):
    try:
        index = int(value)
        if index < 0 or index >= max_length:
            print("Index out of range")
            return None
        return index
    except:
        print("Invalid index")
        return None


def validate_text(text):
    if not text.strip():
        print("Description cannot be empty")
        return None
    return text.strip()