## CV Reviewer AI Assistant

Aplikasi web untuk review CV secara otomatis menggunakan AI (Gemini API).

### Fitur
- Upload CV (PDF)
- Pilih mode review: ATS, HR, Mentor
- Analisis struktur, kekuatan, area perbaikan, dan rekomendasi
- Output profesional dan terstruktur
- Validasi otomatis: hanya file CV yang akan diproses (cek kata kunci & validasi AI)

### Cara Menjalankan Lokal
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Siapkan file `.env` di root project, isi dengan:
   ```
   GEMINI_API_KEY=isi_api_key_gemini_anda
   ```
   (atau bisa juga set environment variable `GEMINI_API_KEY` secara manual)
3. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```

### Deploy ke Streamlit Cloud
1. Push semua file ke GitHub
2. Deploy di https://streamlit.io/cloud
3. Set secret `GEMINI_API_KEY` di pengaturan Streamlit Cloud

### Penjelasan Validasi CV
- Aplikasi akan mengecek apakah file PDF yang diupload mengandung kata kunci umum CV.
- Jika lolos, aplikasi juga akan meminta AI (Gemini) memastikan file tersebut benar-benar CV/resume.
- Jika gagal validasi, user akan mendapat pesan error dan file tidak diproses.

### Catatan Keamanan
- Jangan pernah upload file .env atau API key ke GitHub (sudah di .gitignore)
- API key hanya dibaca dari environment variable atau file .env

---
By: arezyhs