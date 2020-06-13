# A program that takes a path to a folder of .txt files. The program takes the first file and writes each line to a row
# in the first column of a new spreadsheet. Then the program takes the second file and writes each line to a new row in
# the second column of the spreadsheet, and so on.

import pyinputplus as pyip, openpyxl
from pathlib import Path


def text_to_spreadsheet(path):
    p = Path(path)
    all_text_files = list(p.glob('*.txt'))

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = f'Text To Spreadsheet'

    # Set starting row and column numbers
    row_num = 1
    col_num = 1

    for file in all_text_files:
        for line in open(file).readlines():
            sheet.cell(row=row_num, column=col_num).value = line
            row_num += 1
        row_num = 1
        col_num += 1

    wb.save('text_to_spreadsheet.xlsx')
    wb.close()


if __name__ == '__main__':
    prompt = 'Please enter the full path to the directory with the text files you would like to work with:\n'
    path_to_text_files = pyip.inputFilepath(prompt=prompt)
    text_to_spreadsheet(path_to_text_files)

