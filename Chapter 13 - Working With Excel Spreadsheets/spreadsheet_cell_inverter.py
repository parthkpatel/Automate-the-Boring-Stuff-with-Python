# A program that takes a spreadsheet filename string. The program opens the spreadsheet and writes
# the cells of column A into one text file, the cells of column B into another text file, and so on.

import pyinputplus as pyip, openpyxl, os


def invert_cells(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    new_wb = openpyxl.Workbook()
    new_sheet = new_wb.active
    new_sheet.title = f'{sheet.title} Inverted'

    for row_num in range(1, sheet.max_row+1):
        for col_num in range(1, sheet.max_column+1):
            new_sheet.cell(row=col_num, column=row_num).value = sheet.cell(row=row_num, column=col_num).value

    new_wb.save(f'Inverted_{os.path.basename(file_path)}')
    new_wb.close()
    wb.close()


if __name__ == '__main__':
    path_to_file = pyip.inputFilepath(prompt='Please enter the full path to the spreadsheet you want to work with:\n')
    invert_cells(path_to_file)
