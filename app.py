# CV Reviewer AI Assistant
# Streamlit app entry point


import streamlit as st
from utils import extract_text_from_pdf, review_cv_with_gemini, is_cv_text, is_cv_by_ai

st.set_page_config(page_title="CV Reviewer AI", layout="centered")
st.title("CV Reviewer AI Assistant")

st.write("""
Upload CV Anda (PDF), pilih mode review, dan dapatkan analisis profesional dari AI.
""")

uploaded_file = st.file_uploader("Upload CV (PDF)", type=["pdf"])
mode = st.selectbox("Pilih Mode Review", ["ATS", "HR", "Mentor", "Roast"])

prompt_additional = st.text_area("Instruksi tambahan (opsional)")

if st.button("Review CV") and uploaded_file:
    with st.spinner("Memproses CV..."):
        cv_text = extract_text_from_pdf(uploaded_file)
        # Validasi kata kunci dulu, lalu validasi AI
        if not is_cv_text(cv_text):
            st.error("File yang diupload tidak terdeteksi sebagai CV. Pastikan Anda mengupload dokumen CV yang benar.")
        elif not is_cv_by_ai(cv_text):
            st.error("Berdasarkan analisis AI, file ini bukan CV/resume. Pastikan Anda mengupload dokumen CV yang benar.")
        else:
            result = review_cv_with_gemini(cv_text, mode, prompt_additional)
            st.subheader("Hasil Review:")
            st.write(result)
    
    # Footer: dibuat oleh arezyhs dan tanggal sekarang
    from datetime import datetime
    st.markdown("---")
    st.markdown(f"<div style='text-align:center; color:gray;'>Dibuat oleh <b>arezyhs</b> &middot; {datetime.now().strftime('%d %B %Y')}</div>", unsafe_allow_html=True)
