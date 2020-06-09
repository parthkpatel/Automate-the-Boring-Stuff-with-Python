# A Mad Libs program that reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# The completed Mad Lib text is then saved to a new text file, suffixed with 'mad_lib_'

from pathlib import Path
import pyinputplus as pyip, re, os


def mad_lib():
    while True:
        prompt = 'Please provide the path to the text file you wish to mad lib:\n'
        input_file_path = pyip.inputStr(prompt=prompt)
        path = Path(input_file_path)
        if path.is_file():
            break
        else:
            print('The given path either did not exist, or the file was not a text file.')

    mad_lib_text = get_mad_lib_text(path)

    mad_lib_file = open(f'{str(path.parent)}/{path.stem}_mad_lib{path.suffix}', 'w')
    mad_lib_file.write(mad_lib_text)
    mad_lib_file.close()


def get_mad_lib_text(path):
    mad_lib_dict = {}

    adjective_prompt = 'Enter an adjective:\n'
    mad_lib_dict['ADJECTIVE'] = pyip.inputStr(prompt=adjective_prompt)
    noun_prompt = 'Enter a noun:\n'
    mad_lib_dict['NOUN'] = pyip.inputStr(prompt=noun_prompt)
    adverb_prompt = 'Enter an adverb:\n'
    mad_lib_dict['ADVERB'] = pyip.inputStr(prompt=adverb_prompt)
    verb_prompt = 'Enter a verb:\n'
    mad_lib_dict['VERB'] = pyip.inputStr(prompt=verb_prompt)

    mad_lib_text = path.read_text()

    for key, value in mad_lib_dict.items():
        mad_lib_regex = re.compile(f'({key})')
        mad_lib_text = mad_lib_regex.sub(f'{value}', mad_lib_text)

    print(mad_lib_text)
    return mad_lib_text


if __name__ == '__main__':
    mad_lib()
