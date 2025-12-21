from io import BytesIO
from pymupdf import PdfReader
from services.ai_service import AIService
import fitz


def extract_images_from_pdf(pdf_bytes):
    images = []
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    for page_index, page in enumerate(doc):
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            image_ext = base_image["ext"]  # 'png', 'jpeg', etc.

            # Skip tiny / decorative images
            if base_image["width"] < 200 or base_image["height"] < 200:
                continue

            images.append({
                "page": page_index + 1,
                "bytes": image_bytes,
                "mime": f"image/{image_ext}"
            })

    return images



def process_pdf(pdf_bytes: bytes, flag: bool) -> str:
    # Text-based PDF
    reader = PdfReader(BytesIO(pdf_bytes))
    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    
    if flag:
        images = extract_images_from_pdf(pdf_bytes)
        if len(images) > 20: #Just so the ai does not process over 20 images
            images = images[:20]
        for page_number, image in images:
            if image.width < 200 or image.height < 200:
                continue
            analysis = st.session_state.ai_service.analyze_image(image, page_number)
            extracted_text.append(
                f"\n[Image Analysis — Page {page_number}]\n{analysis}"
            )

    return "\n".join(text)






