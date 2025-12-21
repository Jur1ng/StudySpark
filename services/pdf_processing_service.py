from io import BytesIO
from pypdf import PdfReader

def process_pdf(pdf_bytes: bytes) -> str:

    reader = PdfReader(BytesIO(pdf_bytes))
    text = []
    for page in reader.pages:
        
        page_text = page.extract_text()
        
        if page_text:
            text.append(page_text)
            
    return "\n".join(text)













