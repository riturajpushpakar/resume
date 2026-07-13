import streamlit as st
from modules.pdf_reader import extract_text
from modules.resume_details import get_resume_details

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Analyzer")

st.error("VERSION 2 - TEST")

st.write("Welcome Rituraj 👋")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume Uploaded Successfully ✅")

    resume_text = extract_text(uploaded_file)

    details = get_resume_details(uploaded_file, resume_text)

    st.subheader("📄 Resume Details")

    st.divider()

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume",
        resume_text,
        height=350
    )

else:

    st.warning("Please upload your resume.")