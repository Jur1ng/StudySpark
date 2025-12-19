import streamlit as st
from dotenv import load_dotenv

from services.AIService import AIService

load_dotenv()

if 'AIService' not in st.session_state:
    st.session_state.AIService = AIService()

st.title("Document Upload")

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf"]
)


if uploaded_file:
    pdf_bytes = uploaded_file.read()
    with st.spinner("Processing pdf..."):
        # Call our service (all logic is in the service layer!)
        result = st.session_state.AIService.process_pdf(pdf_bytes)

        # Store in session state for chat
        st.session_state.current_ticket = result
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")
else: st.warning("Please upload a pdf")