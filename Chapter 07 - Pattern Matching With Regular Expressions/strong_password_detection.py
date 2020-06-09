# A program that will detect whether a password is strong or not

import re


def detect_strong_password(password):
    password_length_regex = re.compile(r'.{8}')
    password_uppercase_regex = re.compile(r'[A-Z]')
    password_lowercase_regex = re.compile(r'[a-z]')
    password_digit_regex = re.compile(r'\d')

    if password_length_regex.search(password) is None:
        return False
    elif password_uppercase_regex.search(password) is None:
        return False
    elif password_lowercase_regex.search(password) is None:
        return False
    elif password_digit_regex.search(password) is None:
        return False
    else:
        return True


if __name__ == '__main__':
    input_password = input('Please enter your password: ')
    if detect_strong_password(input_password):
        print('This is a strong password.')
    else:
        print('This is not a strong password.')

