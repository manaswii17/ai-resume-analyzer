import streamlit as st
from src.pdf_processor import extract_text_from_pdf


st.title("AI Resume Analyzer & Job Matching System")

st.write("Upload your resume PDF to extract its text.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:
    with open("temp_resume.pdf", "wb") as file:
        file.write(uploaded_file.getbuffer())

    resume_text = extract_text_from_pdf("temp_resume.pdf")

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=400
    )