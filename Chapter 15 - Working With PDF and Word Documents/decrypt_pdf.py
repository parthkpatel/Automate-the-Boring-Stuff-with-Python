# A program that, given a folder path and password, goes through each PDF in that folder (and its subfolders)
# and tries to decrypt each encrypted PDF with the given password.
# If the PDF was successfully decrypted, the program will create a decrypted version of that file

import pyinputplus as pyip, PyPDF2, os


def decrypt_pdf(path, password):
    # Get all the PDF filenames.
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.pdf'):
                original_file = open(os.path.join(foldername, filename), 'rb')
                pdf_reader = PyPDF2.PdfFileReader(original_file)
                if pdf_reader.isEncrypted is True:
                    if pdf_reader.decrypt(password) == 1:
                        # Create new, decrypted version of the pdf
                        pdf_writer = PyPDF2.PdfFileWriter()
                        for page_num in range(pdf_reader.numPages):
                            pdf_writer.addPage(pdf_reader.getPage(page_num))

                        decrypted_pdf_path = os.path.join(foldername, f'{filename[:-4]}_decrypted.pdf')
                        decrypted_pdf_output = open(decrypted_pdf_path, 'wb')
                        pdf_writer.write(decrypted_pdf_output)
                        decrypted_pdf_output.close()
                        original_file.close()

                        # Verify that the pdf was properly decrypted
                        decrypted_pdf = open(decrypted_pdf_path, 'rb')
                        pdf_reader = PyPDF2.PdfFileReader(decrypted_pdf)
                        if pdf_reader.isEncrypted is False:
                            print(f'{os.path.basename(decrypted_pdf_path)} was decrypted successfully.')
                        else:
                            print(f'{os.path.basename(decrypted_pdf_path)} was not decrypted successfully,')
                        decrypted_pdf.close()
                    else:
                        print(f'The password to decrypt the {filename} was incorrect, so it wil be skipped.')
                else:
                    print(f'{filename} is already decrypted, so it will be skipped.')


if __name__ == '__main__':
    path_prompt = 'Please enter the full path to the directory you would like to work with:\n'
    input_path = pyip.inputFilepath(prompt=path_prompt)
    input_password = pyip.inputStr(prompt='Enter the password you would like to use to decrypt the pdf files:\n')
    decrypt_pdf(input_path, input_password)
