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

if st.button("Generate Summary, type = "primary"):
             prompt_map = {
              "Bullet points": f"Summarize the document as bullet points. Keep it {length.lower()}.",
              "Key takeaways": f"Give the key takeaways from the document. Keep it {length.lower()}.",
              "Overview paragraph": f"Write a clear overview paragraph of the document. Keep it {length.lower()}.",
              "Key terms": f"Extract important key terms and define each briefly. Keep it {length.lower()}.",
              "Section-by-section": f"Summarize the document section-by-section with short bullets per section. Keep it {length.lower()}."
             }
             prompt = prompt_map[summary_type]

             with st.spinner("Generating..."):
                 summary  = st.session_state.ai_service.generate_summary(document, prompt)

             st.subheader(summary_type)
             st.write(summary)             

