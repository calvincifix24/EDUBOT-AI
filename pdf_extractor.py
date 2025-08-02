import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file using PyMuPDF.
    Args:
        file_path (str): Path to the PDF file
    Returns:
        str: Extracted text
    """
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text
