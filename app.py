import streamlit as st

# Page settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# Title
st.title("📄 AI Resume Analyzer")

# Welcome message
st.write("Welcome Rituraj! 👋")

# Description
st.write("This is our AI-based Mini Project.")

uploaded_file = st.file_uploader(
    "📄 Upload your Resume",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("Resume Uploaded Successfully ✅")
else:
    st.warning("Please upload your resume.")