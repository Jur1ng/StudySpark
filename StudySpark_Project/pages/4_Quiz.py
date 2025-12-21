import streamlit as st
from services.ai_service import AIService

st.title("Quiz")

if not st.session_state.get("pdf_uploaded", False):
    st.warning("Please upload a PDF first!")
    st.stop()

document_text = st.session_state.pdf_tex

if "ai_service" not in st.session_state:
    st.session_state.ai_service = AIService()

# --- Pick number of questions ---
num_questions = st.number_input(
    "How many questions would you like?",
    min_value=1,
    max_value=30,
    value=10,
    step=1
)

# --- Generate quiz ---
if st.button("Generate quiz", type="primary"):
    with st.spinner("Generating quiz..."):
        st.session_state.quiz = st.session_state.ai_service.generate_quiz(document_text, int(num_questions))
    st.session_state.q_index = 0
    st.session_state.submitted = False
    st.session_state.last_result = None
    st.rerun()

quiz = st.session_state.get("quiz")

# --- Show one question at a time ---
if quiz:
    i = st.session_state.get("q_index", 0)
    q = quiz[i]

    st.subheader(f"Question {i+1} / {len(quiz)}")
    st.write(q["question"])

    choice = st.radio(
        "Choose an answer:",
        ["A", "B", "C", "D"],
        format_func=lambda k: f"{k}) {q['options'][k]}",
        key=f"choice_{i}"
    )

    # --- Submit answer ---
    if st.button("Submit"):
        st.session_state.submitted = True
        if choice == q["answer"]:
            st.session_state.last_result = "correct"
        else:
            st.session_state.last_result = "wrong"

    # --- Feedback ---
    if st.session_state.get("submitted", False):
        if st.session_state.last_result == "correct":
            st.success("Correct ✅")
        else:
            st.error("Wrong ❌")

        st.write(f"**Explanation:** {q['explanation']}")

    # --- Next button ---
    is_last = (i == len(quiz) - 1)
    next_disabled = (not st.session_state.get("submitted", False)) or is_last

    if st.button("Next ➜", disabled=next_disabled):
        st.session_state.q_index += 1
        st.session_state.submitted = False
        st.session_state.last_result = None
        st.rerun()

    if is_last:
        st.info("You reached the end of the quiz.")
