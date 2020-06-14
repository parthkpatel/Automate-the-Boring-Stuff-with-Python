# A program that searches a given Google Sheet for calculation mistakes, and prints the rows with mistakes

import pyinputplus as pyip, ezsheets


def find_spreadsheet_mistakes():
    url_of_google_sheet = \
        'https://docs.google.com/spreadsheets/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg/edit#gid=289119951'
    ss = ezsheets.Spreadsheet(url_of_google_sheet)

    # Information is in sheet 1
    sheet = ss[0]

    # Exclude Headers
    rows = sheet.getRows()[1:]
    for index, row in enumerate(rows):
        # If row is blank, skip
        if not (row[0] and row[1] and row[2]):
            continue

        expected_total = int(row[0]) * int(row[1])
        if expected_total != int(row[2]):
            print(f'The row {index+2} has a mistake. Beans Per Jar: {row[0]}, Jars: {row[1]}, '
                  f'Total Beans: {row[2]}, Expected Total Beans: {expected_total}')


if __name__ == '__main__':
    find_spreadsheet_mistakes()
