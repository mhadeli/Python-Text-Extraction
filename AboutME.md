## PyPDF2 PDF Text Extractor

Hello! This script leverages the power of the `PyPDF2` library to extract text content from PDF files.

### What it does:
1. **Imports Necessary Modules:** The `os` and `PyPDF2` modules are imported to handle file operations and PDF processing, respectively.
2. **PDF Directory Setup:** Sets the directory path (`pdf_directory`) where the target PDF files are located.
3. **File Iteration:** Loops through each file in the specified directory to process only those ending with `.pdf`.
4. **PDF Reading:** For each PDF file:
    - Opens the PDF and creates a reader object.
    - Iterates through each page to extract text.
    - Combines the text from all pages into a single string.
    - Closes the PDF file.
5. **Text File Creation:** Generates a `.txt` file for each PDF, saving the extracted text content.

### How to use:
1. Ensure you have `PyPDF2` installed (`pip install PyPDF2`).
2. Set the `pdf_directory` to your target folder containing PDF files.
3. Run the script and find the generated text files in the same directory as the source PDFs.

**Note:** This script assumes that PDFs are text-readable. Some scanned PDFs might not produce accurate results.
