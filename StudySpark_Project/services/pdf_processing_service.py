from io import BytesIO
from pypdf import PdfReader

def process_pdf(pdf_bytes: bytes) -> str:
    # Text-based PDF
    reader = PdfReader(BytesIO(pdf_bytes))
    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    
    images = extract_images_from_pdf(pdf_bytes)

    for page_number, image in images:
        analysis = st.session.ianalyze_image_with_gemini(image, page_number)
        extracted_text.append(
            f"\n[Image Analysis — Page {page_number}]\n{analysis}"
        )

    return "\n".join(text)
