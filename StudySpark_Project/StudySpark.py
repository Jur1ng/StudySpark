import streamlit as st
from dotenv import load_dotenv, find_dotenv
from services.ai_service import AIService
from services.pdf_processing_service import process_pdf
from utils.lang_tracing import init_tracing

if 'api_key' not in st.session_state:
    ENV_FILE = find_dotenv()
    if ENV_FILE:
        load_dotenv(ENV_FILE)
        st.session_state.api_key = os.getenv("GOOGLE_API_KEY")
    else: st.session_state.api_key = st.secrets["GOOGLE_API_KEY"]

init_tracing()

if 'ai_service' not in st.session_state:
    st.session_state.ai_service = AIService(key=st.session_state.api_key)

if 'pdf_uploaded' not in st.session_state:
    st.session_state.pdf_uploaded = False
    
st.set_page_config(page_title="StudySpark", layout="centered")
st.title("StudySpark")

st.write("Select an option below:")

col1, col2 = st.columns(2)

with col1:
    if st.button("Document Upload", use_container_width=True):
        st.switch_page("pages/1_Document_Upload.py")

    # Disable if PDF not uploaded
    if st.session_state.pdf_uploaded:
        if st.button("Summary", use_container_width=True):
            st.switch_page("pages/2_Summary.py")
    else:
        st.button("Summary (Upload PDF first)", disabled=True, use_container_width=True)

with col2:
    if st.session_state.pdf_uploaded:
        if st.button("Q&A", use_container_width=True):
            st.switch_page("pages/3_QA.py")
        if st.button("Quiz", use_container_width=True):
            st.switch_page("pages/4_Quiz.py")
    else:
        st.button("Q&A (Upload PDF first)", disabled=True, use_container_width=True)
        st.button("Quiz (Upload PDF first)", disabled=True, use_container_width=True)

#Sidebar
st.sidebar.title("Navigation")

if st.session_state.get("pdf_uploaded", False):
    if st.sidebar.button("Summary"):
        st.switch_page("pages/2_Summary.py")
    if st.sidebar.button("Q&A"):
        st.switch_page("pages/3_QA.py")
    if st.sidebar.button("Quiz"):
        st.switch_page("pages/4_Quiz.py")
else:
    st.sidebar.write("Upload a PDF first to unlock these options")











