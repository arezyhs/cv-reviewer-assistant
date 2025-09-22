# utils.py
# Utility functions for CV Reviewer AI

from dotenv import load_dotenv
load_dotenv()
import pdfplumber
import google.generativeai as genai
import os

# Hanya ambil API key dari environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def extract_text_from_pdf(file) -> str:
    """Extract text from uploaded PDF file."""
    with pdfplumber.open(file) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    return text

def review_cv_with_gemini(cv_text: str, mode: str, additional: str = "") -> str:
    """Send prompt to Gemini API and return review result."""
    if not GEMINI_API_KEY:
        return "[ERROR] Gemini API key belum diatur di environment variable. Silakan set GEMINI_API_KEY."
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = build_prompt(cv_text, mode, additional)
    response = model.generate_content(prompt)
    return response.text

def build_prompt(cv_text: str, mode: str, additional: str = "") -> str:
    mode_instruction = {
        "ATS": "Analisa CV ini seperti sistem ATS (Applicant Tracking System). Fokus pada struktur, keyword, dan kelayakan lolos screening awal.",
        "HR": "Analisa CV ini dari sudut pandang HR. Soroti kekuatan, area perbaikan, dan rekomendasi agar lebih menarik bagi HR.",
        "Mentor": "Analisa CV ini sebagai mentor karir. Berikan saran pengembangan, highlight keunggulan, dan area yang bisa ditingkatkan.",
    }.get(mode, "Analisa CV ini secara profesional.")
    prompt = (
        f"{mode_instruction}\n\n"
        f"Teks CV:\n{cv_text}\n\n"
        f"Berikan analisis struktur, poin kekuatan, area perbaikan, dan rekomendasi tambahan. {additional}\n"
        f"Gunakan bahasa profesional dan terstruktur."
    )
    return prompt
