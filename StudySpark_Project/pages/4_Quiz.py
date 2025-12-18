import streamlit as st

st.title("Quiz")

#This is just an example of output, do not use it

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