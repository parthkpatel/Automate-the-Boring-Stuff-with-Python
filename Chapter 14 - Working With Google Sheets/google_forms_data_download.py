# A program that collects the data from the results of a google form
# and stores the email addresses in a list, which is printed out

import pyinputplus as pyip, ezsheets


def download_google_forms_data(url):
    ss = ezsheets.Spreadsheet(url)

    # Assuming form responses are on the first sheet
    responses_sheet = ss[0]

    # The email addresses are stored in the third column, only want values that have non empty email addresses
    email_address_responses = [response for response in responses_sheet.getColumn(3) if response]

    # If only value is the form question, return
    if len(email_address_responses) == 1:
        return

    print('*'*10, 'Email addresses from the Google Form:', '*'*10)

    # Skip the row containing the form question
    for i in range(1, len(email_address_responses)):
        print(f'Email address: {email_address_responses[i]}')


if __name__ == '__main__':
    google_sheet_url = pyip.inputURL(prompt='Enter the URL of the google sheet containing the form results:\n')
    download_google_forms_data(google_sheet_url)
