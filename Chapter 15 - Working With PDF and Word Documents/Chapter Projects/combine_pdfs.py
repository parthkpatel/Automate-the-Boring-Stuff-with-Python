#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# into a single PDF.

import PyPDF2, os

# Get all the PDF filenames.
pdf_files = []
for file_name in os.listdir('.'):
    if file_name.endswith('.pdf'):
        pdf_files.append(file_name)
pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for file_name in pdf_files:
    pdf_file_obj = open(file_name, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # Loop through all the pages (except the first) and add them.
    for page_num in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

# Save the resulting PDF to a file.
pdf_output = open('allminutes.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
