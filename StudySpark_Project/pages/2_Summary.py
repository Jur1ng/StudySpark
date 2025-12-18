import streamlit as st

st.title("Document Summary")

st.write("This page will show the document summary.")

if st.button("Generate Summary"):
    st.info("Summary generation goes here.")