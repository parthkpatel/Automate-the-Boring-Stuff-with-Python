# A program that mocks the strip() string method.

import re


def regex_strip(input_string, characters_to_remove):
    if characters_to_remove == '':
        strip_regex = re.compile(r'^\s+|\s+$')
    else:
        strip_regex = re.compile(r'[' + characters_to_remove + ']')

    return strip_regex.sub('', input_string)


if __name__ == '__main__':
    string = input('Enter a string to strip: ')
    characters = input('Enter characters to be removed from the string, or click enter: ')
    print(regex_strip(string, characters))

