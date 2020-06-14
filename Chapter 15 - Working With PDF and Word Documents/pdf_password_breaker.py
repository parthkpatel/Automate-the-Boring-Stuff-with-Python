# A program that, given a PDF file path and a .txt dictionary file path, tries to decrypt
# the PDF file (if it is encrypted) using the words in the dictionary. If successful, the
# program will print out the correct password.

import pyinputplus as pyip, PyPDF2, os


def break_password(pdf_path, dictionary_path):
    pdf_name = os.path.basename(pdf_path)
    dictionary_name = os.path.basename(dictionary_path)

    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    true_password = ''
    if pdf_reader.isEncrypted is True:
        dictionary_file = open(dictionary_path)
        dictionary_list_text = dictionary_file.read()
        dictionary_list = dictionary_list_text.split('\n')
        for word in dictionary_list:
            if pdf_reader.decrypt(word.upper()) == 1:
                true_password = word.upper()
                break
            elif pdf_reader.decrypt(word.lower()) == 1:
                true_password = word.lower()
                break

        if true_password:
            print(f'The password for {pdf_name} is: {true_password}')
        else:
            print(f'The dictionary {dictionary_name} does not contain the password for the encrypted file {pdf_name}')


if __name__ == '__main__':
    pdf_path_prompt = 'Please enter the full path to the encrypted PDF file you would like to decrypt:\n'
    input_pdf_path = pyip.inputFilepath(prompt=pdf_path_prompt, blockRegexes=[r'.*[^\.pdf]$'])
    dictionary_path_prompt = 'Please enter the full path to the dictionary .txt file you would use ' \
                             f'to try and decrypt {os.path.basename(input_pdf_path)}:\n'
    input_dictionary_path = pyip.inputFilepath(prompt=dictionary_path_prompt, blockRegexes=[r'.*[^\.txt]$'])
    break_password(input_pdf_path, input_dictionary_path)