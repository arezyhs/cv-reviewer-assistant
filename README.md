## CV Reviewer AI Assistant

Aplikasi web untuk review CV secara otomatis menggunakan AI (Gemini API).

### Fitur
- Upload CV (PDF)
- Pilih mode review: ATS, HR, Mentor
- Analisis struktur, kekuatan, area perbaikan, dan rekomendasi
- Output profesional dan terstruktur

### Cara Menjalankan Lokal
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set environment variable `GEMINI_API_KEY` dengan API key Gemini Anda.
3. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```

### Deploy ke Streamlit Cloud
1. Push semua file ke GitHub
2. Deploy di https://streamlit.io/cloud
3. Set secret `GEMINI_API_KEY` di pengaturan Streamlit Cloud

---
By: [Your Name]