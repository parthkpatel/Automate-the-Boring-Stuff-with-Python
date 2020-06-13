# A program that takes two integers (N and M) and a spreadsheet filename string.
# Starting at row N, the program inserts M blank rows into the spreadsheet

import pyinputplus as pyip, openpyxl, os


def insert_blank_rows(file_path, row, blanks):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    if row > sheet.max_row:
        print(f'The given row ({row}) is larger than the maximum row ({sheet.max_row}) in the file. Exiting program.')
        return

    new_wb = openpyxl.Workbook()
    new_sheet = new_wb.active
    new_sheet.title = f'{sheet.title} with blanks'

    for row_num in range(1, sheet.max_row+blanks+1):
        for col_num in range(1, sheet.max_column+1):
            if row_num < row:
                new_sheet.cell(row=row_num, column=col_num).value = sheet.cell(row=row_num, column=col_num).value
            elif row_num > row+blanks-1:
                new_sheet.cell(row=row_num, column=col_num).value = sheet.cell(row=row_num-blanks, column=col_num).value

    new_wb.save(f'blanked_{os.path.basename(file_path)}')
    new_wb.close()
    wb.close()


if __name__ == '__main__':
    path_to_file = pyip.inputFilepath(prompt='Please enter the full path to the spreadsheet you want to work with:\n')
    row_number = pyip.inputInt(prompt='Input the row you want start adding blank lines at:\n', min=1)
    num_blanks = pyip.inputInt(prompt='Input the number of blank rows you want to insert:\n', min=0)
    insert_blank_rows(path_to_file, row_number, num_blanks)
