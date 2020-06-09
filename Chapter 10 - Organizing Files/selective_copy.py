# A program that walks through a folder tree, searches for files with a given file extension,
# and copies these files from whatever location they are in to a provided destination folder.

import os, shutil, pyinputplus as pyip


def selective_copy():
    folder_path_prompt = 'Enter the absolute filepath of the desired folder to copy from:\n'
    source_folder = pyip.inputStr(prompt=folder_path_prompt)

    extension_prompt = 'Enter the file extension for the files you would like to copy:\n'
    extension = pyip.inputStr(prompt=extension_prompt)

    destination_folder_prompt = 'Enter the absolute filepath of the desired folder to copy to:\n'
    destination_folder = pyip.inputStr(prompt=destination_folder_prompt)

    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith(extension):
                print(f'Copying {filename} from {os.path.basename(foldername)} '
                      f'to {os.path.basename(destination_folder)}.')
                shutil.copy(os.path.join(foldername, filename), destination_folder)

    print('All files with the extension', extension,
          'have been copied from', os.path.basename(source_folder), 'to',
          os.path.basename(destination_folder))


if __name__ == '__main__':
    selective_copy()
