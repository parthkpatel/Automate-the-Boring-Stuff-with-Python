# A program that walks through a folder tree, searches for files with a given file extension,
# and copies these files from whatever location they are in to a provided destination folder.

from pathlib import Path
import os, shutil, re, pyinputplus as pyip


def fill_in_gaps():
    folder_path_prompt = 'Enter the absolute filepath of the desired folder to copy from:\n'
    folder_path = pyip.inputStr(prompt=folder_path_prompt)

    prefix_prompt = 'Enter the prefix of the files that you want to check:\n'
    prefix = pyip.inputStr(prompt=prefix_prompt)

    file_regex = re.compile(rf'^({prefix})(\d+)(.*?)$')
    matching_file_list = sorted([file for file in os.listdir(folder_path) if file_regex.match(file)])

    if len(matching_file_list) == 0:
        return

    start_value = int(file_regex.search(matching_file_list[0]).group(2))
    count = start_value
    max_length = len(file_regex.search(matching_file_list[-1]).group(2))

    for file in matching_file_list:
        mo = file_regex.search(file)
        file_num = int(mo.group(2))

        if file_num != count:
            new_file_name = prefix + '0'*(max_length-len(str(file_num))) + str(count) + mo.group(3)
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, new_file_name))
        count += 1


if __name__ == '__main__':
    fill_in_gaps()
