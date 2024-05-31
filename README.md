# PDF Text Extractor

This Python script extracts text from PDF files and saves it as text files. It utilizes the PyPDF2 library to parse PDF files and extract text.

## Installation

Before running the script, ensure you have installed the PyPDF2 library. You can install it using pip:

```bash
pip install PyPDF2

```

## Usage
Set the directory where the PDF files are located by modifying the pdf_directory variable in the script.
Run the script. It will loop through each PDF file in the specified directory, extract the text from each page, and save it as a separate text file in the same directory.
The text files will have the same name as the original PDF files but with a .txt extension.

## What it does:
Imports Necessary Modules: The os and PyPDF2 modules are imported to handle file operations and PDF processing, respectively.
PDF Directory Setup: Sets the directory path (pdf_directory) where the target PDF files are located.
File Iteration: Loops through each file in the specified directory to process only those ending with .pdf.
PDF Reading: For each PDF file:
Opens the PDF and creates a reader object.
Iterates through each page to extract text.
Combines the text from all pages into a single string.
Closes the PDF file.
Text File Creation: Generates a .txt file for each PDF, saving the extracted text content.

## Example
Suppose you have a directory named pdf_sample on your desktop containing PDF files. After running the script, text files containing the extracted text will be created in the same directory.

## Notes
Ensure that the PDF files you want to extract text from are located in the specified directory.
This script may not handle complex PDF layouts or non-standard fonts perfectly, so manual review may be necessary for accuracy.
