import streamlit as st

st.title("Quiz")

if not st.session_state.get("pdf_uploaded", False):
    st.warning("Please upload a PDF first!")
    st.stop()  # stops the rest of the page from rendering

st.write("Answer the question below:")

answer = st.radio(
    "Question?",
    ["1", "2", "3", "42"]
)

if st.button("Submit"):
    if answer == "42":
        st.success("Correct!")
    else:

        st.error("Incorrect. Try again.")
