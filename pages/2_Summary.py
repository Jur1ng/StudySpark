import streamlit as st
from services.ai_service import AIService

if st.button("⬅ Back to Main Menu"):
    st.switch_page("StudySpark.py")

st.title("Document Summary")

st.write("This page will show the document summary.")

if not st.session_state.get("pdf_uploaded", False):
    st.warning("Please upload a PDF first!")
    st.stop()  # stops the rest of the page from rendering
    
document_text = st.session_state.pdf_text

#make sure the ai service exists
if "ai_service" not in st.session_state:
    st.session_state.ai_service = AIService()

#----UI: pick a summary format----
summary_type = st.selectbox( "Choose your preferred summary format:",
               ["Bullet points", "Key takeaways", "Overview paragraph",
                "Key terms", "Section-by-section"])

length = st.selectbox("Length", ["Short", "Medium", "Detailed"], index = 1)

if st.button("Generate Summary", type = "primary"):
    with st.spinner("Generating..."):
        summary = st.session_state.ai_service.generate_summary(
            document_text, 
            summary_type, 
            length
        )
    
    st.subheader(summary_type)
    st.write(summary)             









