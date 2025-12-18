import streamlit as st

st.title("Document Upload")

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf"]
)

if uploaded_file:
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")