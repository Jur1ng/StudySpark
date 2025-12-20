import streamlit as st
from dotenv import load_dotenv
from services.ai_service import AIService

load_dotenv()

st.title("Document Upload")

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf"]
)


if uploaded_file:
    pdf_bytes = uploaded_file.read()
    with st.spinner("Processing pdf..."):
        result = st.session_state.ai_service.process_pdf(pdf_bytes)

        # Store in session state for chat
        st.session_state.current_ticket = result
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")
else: st.warning("Please upload a pdf")