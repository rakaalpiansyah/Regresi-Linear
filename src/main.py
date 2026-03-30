import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st
import os

# --- KONFIGURASI HALAMAN PANEL ---
st.set_page_config(page_title="Dashboard Regresi Linear", page_icon="📈", layout="wide")

st.title("📊 Dashboard Eksplorasi Regresi Linear")
st.markdown("Aplikasi panel ini menampilkan hasil eksperimen pemodelan *Simple Linear Regression*.")

# --- SIDEBAR NAVIGASI ---
st.sidebar.header("Navigasi Modul")
pilihan_modul = st.sidebar.radio(
    "Pilih Eksperimen:", 
    ("Modul 1: Data Sembarang", "Modul 2: Emisi Kendaraan")
)

# Inisiasi Model Machine Learning
model = LinearRegression()

# ==========================================
# EKSPERIMEN 1: DATA SEMBARANG
# ==========================================
if pilihan_modul == "Modul 1: Data Sembarang":
    st.header("Modul 1: Prediksi Harga Berdasarkan Penjualan")
    
    # Menyiapkan Data
    penjualan = np.array([6, 5, 5, 4, 4, 3, 2, 2, 2, 1]).reshape(-1, 1)
    harga = np.array([16000, 18000, 27000, 34000, 50000, 68000, 65000, 81000, 85000, 90000])
    
    # Melatih Model
    model.fit(penjualan, harga)
    harga_pred = model.predict(penjualan)
    
    # Evaluasi Metrik
    mse = mean_squared_error(harga, harga_pred)
    r2 = r2_score(harga, harga_pred)
    
    # Menampilkan Panel Metrik (Kartu Angka)
    st.subheader("Kinerja Model")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Koefisien (Slope)", f"{model.coef_[0]:.2f}")
    col2.metric("Intercept", f"{model.intercept_:.2f}")
    col3.metric("Mean Squared Error (MSE)", f"{mse:,.2f}")
    col4.metric("R-Squared (R²)", f"{r2:.4f}")
    
    st.divider()
    
    # Menampilkan Visualisasi Grafik
    st.subheader("Visualisasi Garis Regresi")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(penjualan, harga, color='red', label='Data Asli')
    ax.plot(penjualan, harga_pred, color='blue', linewidth=2, label='Garis Regresi')
    ax.set_title("Regresi Linear: Penjualan vs Harga")
    ax.set_xlabel("Penjualan")
    ax.set_ylabel("Harga")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    
    st.pyplot(fig) # Menggambar plot Matplotlib ke dalam panel Streamlit

# ==========================================
# EKSPERIMEN 2: DATASET EMISI KENDARAAN
# ==========================================
elif pilihan_modul == "Modul 2: Emisi Kendaraan":
    st.header("Modul 2: Prediksi Emisi CO2 Berdasarkan Ukuran Mesin")
    
    # Pastikan file CSV ada di folder "data" yang sejajar dengan folder "src"
    filepath = "data/FuelConsumptionCo2.csv" 
    
    if not os.path.exists(filepath):
        st.error(f"⚠️ File dataset tidak ditemukan di path: `{filepath}`. Pastikan file CSV sudah diunduh dan posisinya benar.")
    else:
        # Membaca Data
        df = pd.read_csv(filepath)
        cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'CO2EMISSIONS']]
        
        # Menampilkan tabel data di panel
        with st.expander("Tampilkan Cuplikan Dataset Mentah"):
            st.dataframe(cdf.head(10), use_container_width=True)
        
        # Data Splitting (80% Train, 20% Test)
        np.random.seed(42)
        msk = np.random.rand(len(df)) < 0.8
        train = cdf[msk]
        test = cdf[~msk]

        train_x = np.asanyarray(train[['ENGINESIZE']])
        train_y = np.asanyarray(train[['CO2EMISSIONS']])
        test_x = np.asanyarray(test[['ENGINESIZE']])
        test_y = np.asanyarray(test[['CO2EMISSIONS']])

        # Melatih Model
        model.fit(train_x, train_y)
        test_y_pred = model.predict(test_x)

        # Evaluasi Metrik
        mse = mean_squared_error(test_y, test_y_pred)
        r2 = r2_score(test_y, test_y_pred)
        
        # Menampilkan Panel Metrik (Kartu Angka)
        st.subheader("Kinerja Model pada Data Uji (Testing Set)")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Koefisien (Slope)", f"{model.coef_[0][0]:.2f}")
        col2.metric("Intercept", f"{model.intercept_[0]:.2f}")
        col3.metric("Mean Squared Error", f"{mse:,.2f}")
        col4.metric("R-Squared (R²)", f"{r2:.4f}")
        
        st.divider()
        
        # Menampilkan Visualisasi Grafik
        st.subheader("Visualisasi Model pada Data Latih (Training Set)")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue', alpha=0.5, label='Data Train')
        ax.plot(train_x, model.predict(train_x), '-r', linewidth=2, label='Garis Regresi')
        ax.set_title("Regresi Linear: Engine Size vs CO2 Emissions")
        ax.set_xlabel("Ukuran Mesin (Engine Size)")
        ax.set_ylabel("Emisi CO2 (Emission)")
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)
        
        st.pyplot(fig)