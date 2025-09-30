import streamlit as st
import os
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Kripto MVP", page_icon="💰", layout="centered")

# === TEMA ve LOGO KONUMU ===
st.markdown("""
<style>
.stApp {
    background: #000515;
    color: white;
}

/* LOGO KONUMU - SABİT SOL ÜST */
.fixed-logo {
    position: fixed;
    top: 20px;
    left: 20px;
    z-index: 9999;
    background: transparent;
}

/* İçerik kaydırma */
.main .block-container {
    padding-top: 120px;
}

/* Mobil */
@media (max-width: 768px) {
    .fixed-logo {
        top: 10px;
        left: 10px;
    }
    .main .block-container {
        padding-top: 100px;
    }
}
</style>
""", unsafe_allow_html=True)

# === LOGO VAR MI? KONTROL ET ===
logo_path = Path(__file__).parent / "assets" / "logo.png"
st.write(f"🔍 Logo path: {logo_path}")
st.write(f"📁 Logo exists: {logo_path.exists()}")

if logo_path.exists():
    try:
        logo_image = Image.open(logo_path)
        st.markdown('<div class="fixed-logo">', unsafe_allow_html=True)
        st.image(logo_image, width=120)
        st.markdown('</div>', unsafe_allow_html=True)
        st.success("✅ Logo başarıyla yüklendi ve sabitlendi!")
        
    except Exception as e:
        st.error(f"❌ Logo açılamadı: {e}")
else:
    st.error("❌ Logo dosyası bulunamadı!")
    st.info("Logo path: assets/logo.png")

# === ANA İÇERİK ===
st.title("Kripto & Borsa AI")
st.write("Logo konumu ve varlığı test ediliyor...")