# 📈 Dashboard Eksplorasi Simple Linear Regression

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.4.1-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.2.1-150458?style=for-the-badge&logo=pandas&logoColor=white)

Repositori ini berisi implementasi dan eksplorasi model **Simple Linear Regression** menggunakan ekosistem *Data Science* Python yang dibungkus dalam antarmuka web interaktif menggunakan **Streamlit**. 

Proyek ini dibuat untuk memenuhi tugas eksplorasi praktikum Pembelajaran Mesin.

---

## 📑 Daftar Isi
- [Deskripsi Proyek](#-deskripsi-proyek)
- [Struktur Direktori](#-struktur-direktori)
- [Dataset](#-dataset)
- [Persiapan & Instalasi](#-persiapan--instalasi)
- [Cara Menjalankan Aplikasi](#-cara-menjalankan-aplikasi)
- [Cuplikan Dashboard](#-cuplikan-dashboard-preview)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Referensi](#-referensi)

---

## 💡 Deskripsi Proyek
Proyek ini mengimplementasikan dua eksperimen utama untuk memahami konsep dasar hingga penerapan riil dari algoritma Regresi Linier:

1. **Modul 1: Data Sembarang (Dummy Data)**
   Menganalisis hubungan sebab-akibat antara satu variabel bebas (X = Penjualan) terhadap variabel terikat (Y = Harga) menggunakan array sederhana. Tujuannya adalah memahami cara kerja *fitting* garis regresi secara fundamental.
2. **Modul 2: Dataset Emisi Kendaraan (Real Data)**
   Menggunakan dataset nyata untuk memprediksi tingkat emisi karbon dioksida (`CO2EMISSIONS`) dari sebuah kendaraan berdasarkan kapasitas atau ukuran mesinnya (`ENGINESIZE`). Model dievaluasi secara kuantitatif menggunakan metrik *Mean Squared Error* (MSE) dan koefisien determinasi (R-Squared).

---

## 📂 Struktur Direktori
Struktur *codebase* disusun secara modular untuk memisahkan antara data, *source code*, dan *environment*:

```text
TUGAS2/
│
├── data/
│   └── FuelConsumptionCo2.csv    # Dataset mentah emisi kendaraan
│
├── env/                          # Virtual environment Python (Diabaikan oleh Git)
│
├── src/
│   └── app.py                    # Skrip utama panel dashboard Streamlit
│
├── assets/                       # Folder untuk menyimpan screenshot/gambar
│
├── README.md                     # Dokumentasi repositori
└── requirements.txt              # Daftar pustaka dependencies
🗂️ Dataset
Dataset yang digunakan pada Modul 2 bersumber dari IBM Object Storage (Cognitive Class) yang memuat informasi konsumsi bahan bakar dan emisi dari berbagai model kendaraan.

Tautan Unduhan Original: FuelConsumptionCo2.csv

Fitur Utama yang Dianalisis: ENGINESIZE (Fitur/X) dan CO2EMISSIONS (Target/Y).

⚙️ Persiapan & Instalasi
Pastikan Anda telah menginstal Python 3.8+. Berikut adalah langkah-langkah untuk menjalankan dashboard ini di komputer lokal Anda:

Clone repositori ini:

Bash
git clone <URL-GITHUB-ANDA>
cd TUGAS2
Aktifkan Virtual Environment (Disarankan):

Windows: env\Scripts\activate

Mac/Linux: source env/bin/activate

Instal dependensi pustaka:

Bash
pip install -r requirements.txt
🚀 Cara Menjalankan Aplikasi
Setelah semua pustaka terinstal, jalankan perintah berikut di terminal (pastikan posisi direktori Anda saat ini berada di dalam folder TUGAS2):

Bash
streamlit run src/app.py
Aplikasi dashboard akan terbuka secara otomatis di browser bawaan Anda pada alamat http://localhost:8501.

📸 Cuplikan Dashboard (Preview)
Eksperimen 1: Data Sembarang
Eksperimen 2: Emisi Kendaraan
🛠️ Teknologi yang Digunakan
Bahasa Utama: Python

Machine Learning: scikit-learn

Manipulasi Data: pandas, numpy

Visualisasi Data: matplotlib

Antarmuka Web (GUI): streamlit

📚 Referensi
Modul Praktikum Pembelajaran Mesin: Mengenal Simple Linear Regression.

Dokumentasi Streamlit

Dokumentasi Scikit-Learn (Linear Models)

Referensi Repositori: Ilham Fauzi - Regresi Linier Sederhana
