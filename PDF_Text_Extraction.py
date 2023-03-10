import os

pip install PyPDF2

import PyPDF2

# set the directory where the PDF files are located
pdf_directory = '/Users/adeli/Desktop/pdf_sample'

# loop through each file in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        # create a PDF file object
        pdf_file = open(os.path.join(pdf_directory, filename), 'rb')
        
        # create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        
        # loop through each page in the PDF file
        text = ''
        for page_num in range(pdf_reader.numPages):
            # extract the text from the page
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        
        # close the PDF file object
        pdf_file.close()
        
        # create a text file object
        text_file = open(os.path.join(pdf_directory, filename[:-4] + '.txt'), 'w')
        
        # write the extracted text to the text file
        text_file.write(text)
        
        # close the text file object
        text_file.close()

