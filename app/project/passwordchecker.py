def is_password_strong(password):
    if len(password) < 8:
        return False

    if " " in password:
        return False

    has_digit = False
    has_letter = False
    has_symbol = False

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isalpha():
            has_letter = True
        else:
            has_symbol = True

    if has_digit and has_letter and has_symbol:
        return True

    return False