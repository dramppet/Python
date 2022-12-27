def length_password(pass_input):
    if  len(pass_input) < 6 or len(pass_input) > 10:
        print('Password must be between 6 and 10 characters')
        return False
    return True


def password_contains_letters_or_digits(pass_input):
    if not pass_input.isalnum():
        print('Password must consist only of letters and digits')
        return False
    return True


def digit_min_tho(pass_input):
    count_digit = 0
    for digit in pass_input:
        if digit.isdigit():
            count_digit +=1

    if count_digit < 2:
        print('Password must have at least 2 digits')
        return False
    return True


password_input = input()

if length_password(password_input) and password_contains_letters_or_digits(password_input) \
        and digit_min_tho(password_input):
    print('Password is valid')