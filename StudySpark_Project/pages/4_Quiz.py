import streamlit as st
from services.ai_service import AIService

st.title("Quiz")

if not st.session_state.get("pdf_uploaded", False):
    st.warning("Please upload a PDF first!")
    st.stop()

document_text = st.session_state.pdf_text

if "ai_service" not in st.session_state:
    st.session_state.ai_service = AIService()

num_questions = st.number_input("How many questions would you like?", 1, 30, 10)

if st.button("Generate quiz", type="primary"):
    with st.spinner("Generating..."):
        # This returns a Python list of dicts (see AIService below)
        st.session_state.quiz = st.session_state.ai_service.generate_quiz(document_text, num_questions)
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.submitted = False

quiz = st.session_state.get("quiz")

if quiz:
    i = st.session_state.q_index
    q = quiz[i]

    st.write(f"**Question {i+1}/{len(quiz)}**")
    st.write(q["question"])

    user_choice = st.radio(
        "Choose one:",
        ["A", "B", "C", "D"],
        format_func=lambda k: f"{k}) {q['options'][k]}",
        key=f"choice_{i}"
    )

    if st.button("Submit"):
        st.session_state.submitted = True
        if user_choice == q["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error("Incorrect.")
        st.write(f"**Explanation:** {q['explanation']}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Previous", disabled=(i == 0)):
            st.session_state.q_index -= 1
            st.session_state.submitted = False
            st.rerun()

    with col2:
        if st.button("Next", disabled=(i == len(quiz) - 1)):
            st.session_state.q_index += 1
            st.session_state.submitted = False
            st.rerun()

    st.info(f"Score so far: {st.session_state.score}")


