import streamlit as st
from PIL import Image
from pathlib import Path

# SAYFA AYARI
st.set_page_config(page_title="Kripto MVP", page_icon="💰", layout="centered")

# ARKAPLAN + SIDEBAR RENGİ
st.markdown("""
<style>
.stApp {
    background: #000515;
}

/* SIDEBAR ARKAPLANI KOYU */
section[data-testid="stSidebar"] {
    background: #000515;
}

/* SIDEBAR İÇİ BOŞLUKLARI KALDIR */
section[data-testid="stSidebar"] > div {
    padding-top: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR - SADECE LOGO ÜSTTE
with st.sidebar:
    # SADECE LOGO - SIDEBAR'IN EN ÜSTÜNE
    try:
        logo_path = Path(__file__).parent / "assets" / "logo.png"
        logo_image = Image.open(logo_path)
        st.image(logo_image, width=100)
    except:
        pass

# ANA SAYFADA HİÇBİR ŞEY YOK