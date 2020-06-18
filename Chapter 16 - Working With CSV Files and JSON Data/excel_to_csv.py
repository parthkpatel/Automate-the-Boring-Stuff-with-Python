# A program that takes a path to a directory containing excel files.
# The program will create a .csv file for every sheet within every excel file


import pyinputplus as pyip, openpyxl, os, csv
from pathlib import Path


def excel_to_csv(path):
    p = Path(path)
    # Skip non-xlsx files
    all_excel_files = list(p.glob('*.xlsx'))
    for file in all_excel_files:
        wb = openpyxl.load_workbook(file)
        for sheet_name in wb.sheetnames:
            # Loop through every sheet in the workbook.
            sheet = wb[sheet_name]

            # Create the CSV filename from the Excel filename and sheet title.
            csv_file_name = f'{os.path.basename(file)[:-5]}_{sheet.title}.csv'
            csv_file = open(csv_file_name, 'w', newline='')

            # Create the csv.writer object for this CSV file.
            csv_writer = csv.writer(csv_file)

            # Loop through every row in the sheet.
            for row in sheet.rows:
                row_data = []    # append each cell to this list
                # Loop through each cell in the row.
                for cell in row:
                    # Append each cell's data to rowData.
                    row_data.append(cell.value)
                # Write the rowData list to the CSV file.
                csv_writer.writerow(row_data)
            csv_file.close()


if __name__ == '__main__':
    prompt = 'Please enter the path to the directory to where the excel files that you wish to convert are:\n'
    path_to_folder = pyip.inputFilepath(prompt=prompt)
    excel_to_csv(path_to_folder)

