# A program that takes a spreadsheet filename string. The program opens the spreadsheet and writes
# the cells of column A into one text file, the cells of column B into another text file, and so on.

import pyinputplus as pyip, openpyxl, os


def spreadsheet_to_text(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active

    name_of_file_prefix = os.path.basename(path).split('.xlsx')[0]
    for col_num in range(1, sheet.max_column + 1):
        file = open(os.path.join(os.path.dirname(path), f'{name_of_file_prefix}_col_{col_num}.txt'), 'w')
        for row_num in range(1, sheet.max_row+1):
            value = sheet.cell(row=row_num, column=col_num).value
            if value is not None:
                file.write(value)
        file.close()
    wb.close()


if __name__ == '__main__':
    prompt = 'Please enter the full path to the spreadsheet you would like to work with:\n'
    path_to_file = pyip.inputFilepath(prompt=prompt)
    spreadsheet_to_text(path_to_file)

