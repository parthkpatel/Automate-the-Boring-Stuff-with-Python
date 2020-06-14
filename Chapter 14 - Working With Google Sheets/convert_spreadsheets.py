# A program that takes a spreadsheet file, uploads it to Google Sheets,
# and downloads it in a format specified by the user (HTML, PDF, ODS, EXCEL)

import pyinputplus as pyip, ezsheets, os


def convert_spreadsheet(path, export_type):
    print(f'Uploading file {os.path.basename(path)} to Google Sheets...')
    ss = ezsheets.upload(path)

    print(f'Downloading file in {export_type} format...')
    if export_type == 'HTML':
        ss.downloadAsHTML()
    elif export_type == 'ODS':
        ss.downloadAsODS()
    elif export_type == 'PDF':
        ss.downloadAsPDF()
    elif export_type == 'EXCEL':
        ss.downloadAsExcel()


if __name__ == '__main__':
    path_to_file = pyip.inputFilepath(prompt='Enter the full file name of the spreadsheet you want to convert:\n')
    export_type_selection = pyip.inputMenu(['HTML', 'ODS', 'PDF', 'EXCEL'],
                                           prompt='Please enter the type of file you would like to '
                                           'convert this spreadsheet to (HTML, ODS, PDF, or EXCEL):\n')

    convert_spreadsheet(path_to_file, export_type_selection)
