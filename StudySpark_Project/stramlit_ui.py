import streamlit as st

st.set_page_config(page_title="StudySpark", layout="centered")

st.title("StudySpark")

st.write("Select an option below:")

col1, col2 = st.columns(2)

with col1:
    if st.button("Document Upload", use_container_width=True):
        st.switch_page("pages/1_Document_Upload.py")

    if st.button("Summary", use_container_width=True):
        st.switch_page("pages/2_Summary.py")

with col2:
    if st.button("Q&A", use_container_width=True):
        st.switch_page("pages/3_QA.py")

    if st.button("Quiz", use_container_width=True):
        st.switch_page("pages/4_Quiz.py")