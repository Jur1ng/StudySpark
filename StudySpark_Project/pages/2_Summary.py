import streamlit as st
from services.ai_service import AIService

st.title("Document Summary")

st.write("This page will show the document summary.")

document_text = st.session_state.pdf_text

#make sure the ai service exists
if "ai_service" not in st.session_state:
    st.session_state.ai_service = AIService()

#----UI: pick a summary format----
summary_type = st.selectbox( "Choose your prefered summary format:",
               ["Bullet points", "key takeaways", "Overview paragraph",
                "Key terms", "Section-by-section"])

length = st.selectbox("Length", ["Short", "Medium", "Detailed"], index = 1)

if st.button("Generate Summary", type = "primary"):
    with st.spinner("Generating..."):
        summary  = st.session_state.ai_service.generate_summary(document_text, prompt)
    st.subheader(summary_type)
    st.write(summary)             




