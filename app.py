import streamlit as st
from modules.pdf_reader import extract_text
from modules.resume_details import get_resume_details
from modules.skills import extract_skills
from modules.ats_score import calculate_ats_score

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# -----------------------------------
# Title
# -----------------------------------

st.title("📄 AI Resume Analyzer")
st.write("Welcome Rituraj 👋")
st.write("Upload your resume and get instant analysis.")

st.divider()

# -----------------------------------
# File Upload
# -----------------------------------

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF Only)",
    type=["pdf"]
)

# -----------------------------------
# Resume Analysis
# -----------------------------------

if uploaded_file is not None:

    st.success("✅ Resume Uploaded Successfully")

    # Extract Resume Text
    resume_text = extract_text(uploaded_file)

    # Resume Details
    details = get_resume_details(uploaded_file, resume_text)

    # Skills
    skills = extract_skills(resume_text)

    # ATS Score
    ats_score = calculate_ats_score(skills)

    # -----------------------------------
    # Resume Details
    # -----------------------------------

    st.subheader("📄 Resume Details")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"📁 File Name : {details['file_name']}")
        st.write(f"📄 Total Pages : {details['pages']}")
        st.write(f"🔤 Characters : {details['characters']}")

    with col2:
        st.write(f"📦 File Size : {details['file_size']} KB")
        st.write(f"📝 Total Words : {details['words']}")

    st.divider()

    # -----------------------------------
    # Skills Found
    # -----------------------------------

    st.subheader("🛠 Skills Found")

    if skills:
        for skill in skills:
            st.success(f"✅ {skill}")
    else:
        st.warning("No matching skills found.")

    st.divider()

    # -----------------------------------
    # ATS Score
    # -----------------------------------

    st.subheader("🎯 ATS Score")

    st.metric(
        label="Resume ATS Score",
        value=f"{ats_score}/100"
    )

    st.progress(ats_score / 100)

    st.divider()

    # -----------------------------------
    # Resume Text
    # -----------------------------------

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=350
    )

else:

    st.info("👆 Please upload your resume.")