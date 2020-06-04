# A program that will detect whether a password is strong or not

import re


def detect_strong_password(password):
    passwordLengthRegex = re.compile(r'.{8}')
    passwordUppercaseRegex = re.compile(r'[A-Z]')
    passwordLowercaseRegex = re.compile(r'[a-z]')
    passwordDigitRegex = re.compile(r'\d')

    if passwordLengthRegex.search(password) is None:
        return False
    elif passwordUppercaseRegex.search(password) is None:
        return False
    elif passwordLowercaseRegex.search(password) is None:
        return False
    elif passwordDigitRegex.search(password) is None:
        return False
    else:
        return True


if __name__ == '__main__':
    inputPassword = input('Please enter your password: ')
    if detect_strong_password(inputPassword):
        print('This is a strong password.')
    else:
        print('This is not a strong password.')

