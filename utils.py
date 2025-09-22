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

def is_cv_text(text: str) -> bool:
    """Cek apakah teks mengandung kata kunci umum CV."""
    keywords = [
        "curriculum vitae", "cv", "resume", "biodata",
        "pendidikan", "education", "pengalaman", "experience",
        "skills", "keahlian", "pekerjaan", "work", "contact", "kontak",
        "summary", "profil", "profile", "sertifikat", "certification"
    ]
    text_lower = text.lower()
    found = 0
    for kw in keywords:
        if kw in text_lower:
            found += 1
    return found >= 2  # minimal 2 kata kunci ditemukan agar lebih yakin

def is_cv_by_ai(text: str) -> bool:
    """Validasi dengan Gemini API: apakah teks ini CV/resume?"""
    if not GEMINI_API_KEY:
        return False
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = (
        "Apakah teks berikut adalah CV atau resume seseorang? "
        "Jawab hanya dengan satu kata: YA atau TIDAK.\n\n"
        f"Teks:\n{text[:3000]}"  # batasi panjang prompt
    )
    try:
        response = model.generate_content(prompt)
        answer = response.text.strip().lower()
        return answer.startswith("ya")
    except Exception:
        return False

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
        f"Tahun saat ini adalah 2025. Gunakan konteks ini saat menganalisis tanggal pada CV.\n"
        f"{mode_instruction}\n\n"
        f"Teks CV (hanya analisa isi CV, abaikan topik lain di luar CV):\n{cv_text}\n\n"
        f"Fokuskan seluruh analisis dan rekomendasi hanya pada isi CV di atas. Jangan bahas topik lain di luar CV.\n"
        f"Berikan analisis struktur, poin kekuatan, area perbaikan, dan rekomendasi tambahan. {additional}\n"
        f"Gunakan bahasa profesional dan terstruktur."
    )
    return prompt
