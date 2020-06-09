# A program that opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression. The results are be printed to the screen.

from pathlib import Path
import pyinputplus as pyip, re


def regex_search():
    while True:
        # prompt = 'Please provide the path to the folder which contains the .txt files that you wish to search in:\n'
        # input_file_path = pyip.inputStr(prompt=prompt)
        input_file_path = r'C:'
        path = Path(input_file_path)
        if path.is_dir():
            break
        else:
            print('The given path either did not exist, or the path was not a folder.')

    regex_string_prompt = 'Please provide a regular expression to use to search the .txt files\n'
    regex_str = pyip.inputRegexStr(prompt=regex_string_prompt)
    for textFilePathObj in path.glob('*.txt'):
        file = open(textFilePathObj)
        user_regex = re.compile(regex_str)

        print(f'The following lines in {textFilePathObj.name} matched the user provided regex of {regex_str} :')
        for line in file.readlines():
            if len(user_regex.findall(line)) > 0:
                print(line)


if __name__ == '__main__':
    regex_search()
