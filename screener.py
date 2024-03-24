from PyPDF2 import PdfReader

def extract_resume_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text


# pdf_path = "test-resume.pdf"
# pdf_text = extract_resume_text(pdf_path)
