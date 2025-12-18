import streamlit as st

st.title("Questions & Answers")

question = st.text_input("Ask a question about the document:")

if st.button("Get Answer"):
    if question:
        st.success("Answer will be generated here.")
    else:
        st.warning("Please enter a question.")