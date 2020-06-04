# A program that mocks the strip() string method.

import re


def regex_strip(inputString, charactersToRemove):
    if charactersToRemove == '':
        stripRegex = re.compile(r'^\s+|\s+$')
    else:
        stripRegex = re.compile(r'[' + charactersToRemove + ']')

    return stripRegex.sub('', inputString)


if __name__ == '__main__':
    string = input('Enter a string to strip: ')
    characters = input('Enter characters to be removed from the string, or click enter: ')
    print(regex_strip(string, characters))

