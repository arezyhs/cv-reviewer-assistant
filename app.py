# CV Reviewer AI Assistant
# Streamlit app entry point


import streamlit as st
from utils import extract_text_from_pdf, review_cv_with_gemini, is_cv_text

st.set_page_config(page_title="CV Reviewer AI", layout="centered")
st.title("CV Reviewer AI Assistant")

st.write("""
Upload CV Anda (PDF), pilih mode review, dan dapatkan analisis profesional dari AI.
""")

uploaded_file = st.file_uploader("Upload CV (PDF)", type=["pdf"])
mode = st.selectbox("Pilih Mode Review", ["ATS", "HR", "Mentor"])

prompt_additional = st.text_area("Instruksi tambahan (opsional)")

if st.button("Review CV") and uploaded_file:
    with st.spinner("Memproses CV..."):
        cv_text = extract_text_from_pdf(uploaded_file)
        if not is_cv_text(cv_text):
            st.error("File yang diupload tidak terdeteksi sebagai CV. Pastikan Anda mengupload dokumen CV yang benar.")
        else:
            result = review_cv_with_gemini(cv_text, mode, prompt_additional)
            st.subheader("Hasil Review:")
            st.write(result)
