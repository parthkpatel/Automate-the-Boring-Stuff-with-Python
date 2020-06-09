# A program that walks through a folder tree and prints out all files that have a size > 100 MB

import os, shutil, pyinputplus as pyip


def delete_unneeded_files():
    folder_path_prompt = 'Enter the absolute filepath of the desired folder to search:\n'
    folder_path = pyip.inputStr(prompt=folder_path_prompt)

    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_size = os.path.getsize(os.path.join(foldername, filename))
            if file_size > 10**6:
                print(f'The file {filename} has a size of {round(file_size/(10**6), 2)}MB')


if __name__ == '__main__':
    delete_unneeded_files()
