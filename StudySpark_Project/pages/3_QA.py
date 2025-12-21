import streamlit as st
from services.ai_service import AIService

if st.button("⬅ Back to Main Menu"):
    st.switch_page("StudySpark.py")

st.title("Questions & Answers")

if not st.session_state.get("pdf_uploaded", False):
    st.warning("Please upload a PDF first!")
    st.stop()  # stops the rest of the page from rendering
    
#question = st.text_input("Ask a question about the document:")

#if st.button("Get Answer"):
#    if question:
#        st.success("Answer will be generated here.")
#    else:
#        st.warning("Please enter a question.")


document_text = st.session_state.pdf_text

# Maintain conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat messages from history on app rerun
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if user_question := st.chat_input("Ask a question about the document:"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_question)
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_question})

    response = st.session_state.ai_service.question_answer(document_text, user_question)
    
    # Display assistant message in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.chat_history.append(
        {"role": "assistant", "content": response}
    )



