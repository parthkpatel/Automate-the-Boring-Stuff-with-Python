# A program that, given a folder path and password, goes through each PDF in that folder (and its subfolders)
# and creates and encrypted version of the non encrypted PDF files with the password.
# After verifying a successful encryption,the program will then safe delete the original PDF file

import pyinputplus as pyip, PyPDF2, os, send2trash


def encrypt_pdf(path, password):
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.pdf'):
                original_file = open(os.path.join(foldername, filename), 'rb')
                pdf_reader = PyPDF2.PdfFileReader(original_file)
                if pdf_reader.isEncrypted is False:
                    # Create new, encrypted version of the pdf
                    pdf_writer = PyPDF2.PdfFileWriter()
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page_num))

                    pdf_writer.encrypt(password)
                    encrypted_pdf_path = os.path.join(foldername, f'{filename[:-4]}_encrypted.pdf')
                    encrypted_pdf_output = open(encrypted_pdf_path, 'wb')
                    pdf_writer.write(encrypted_pdf_output)
                    encrypted_pdf_output.close()
                    original_file.close()

                    # Verify that the pdf was properly encrypted
                    encrypted_pdf = open(encrypted_pdf_path, 'rb')
                    pdf_reader = PyPDF2.PdfFileReader(encrypted_pdf)
                    if pdf_reader.isEncrypted is True and pdf_reader.decrypt(password) == 1:
                        print(f'{os.path.basename(encrypted_pdf_path)} was properly encrypted. Deleting {filename}')
                        send2trash.send2trash(os.path.join(foldername, filename))
                    else:
                        print(f'{os.path.basename(encrypted_pdf_path)} was not encrypted successfully, '
                              f'so the original file {filename} will not be deleted.)')
                    encrypted_pdf.close()
                else:
                    print(f'{filename} is already encrypted, so it will be skipped.')


if __name__ == '__main__':
    path_prompt = 'Please enter the full path to the directory you would like to work with:\n'
    input_path = pyip.inputFilepath(prompt=path_prompt)
    input_password = pyip.inputStr(prompt='Enter the password you would like to use to encrypt the pdf files:\n')
    encrypt_pdf(input_path, input_password)
