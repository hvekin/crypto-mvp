import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Mini Dashboard", layout="wide")

st.title("📊 Mini Dashboard")
st.write("Streamlit ile küçük bir interaktif uygulama 🚀")

# --- Bölüm 1: Kullanıcı bilgisi ---
st.sidebar.header("👤 Kullanıcı Bilgileri")
isim = st.sidebar.text_input("Adınızı girin:", "")
yas = st.sidebar.slider("Yaşınızı seçin:", 10, 80, 25)

if isim:
    st.success(f"Hoş geldin, {isim}! ({yas} yaşındasın)")

# --- Bölüm 2: Veri üretim kontrolü ---
st.sidebar.header("⚙️ Veri Kontrolleri")
n = st.sidebar.slider("Kaç veri noktası olsun?", 10, 200, 50)
secim = st.sidebar.selectbox("Hangi grafik türünü görmek istersiniz?", ["Çizgi Grafiği", "Alan Grafiği", "Sütun Grafiği"])

# Veri oluştur
data = pd.DataFrame(
    np.random.randn(n, 2),
    columns=["x", "y"]
)

# --- Bölüm 3: Grafik gösterimi ---
st.subheader("📈 Grafik Alanı")

if secim == "Çizgi Grafiği":
    st.line_chart(data)
elif secim == "Alan Grafiği":
    st.area_chart(data)
else:
    st.bar_chart(data)

# --- Bölüm 4: Ekstra özellik ---
st.subheader("🔢 Hesap Makinesi")
sayi = st.number_input("Bir sayı girin:", min_value=0, max_value=100, value=5)
st.write(f"Girdiğiniz sayının karesi: **{sayi**2}**")

