import streamlit as st
from PIL import Image
from pathlib import Path
import base64

# SAYFA AYARI
st.set_page_config(page_title="Kripto MVP", page_icon="💰", layout="centered")

# LOGO'YU BASE64'E ÇEVİR VE TAM KÖŞEYE KOY
def add_logo():
    try:
        logo_path = Path(__file__).parent / "assets" / "logo.png"
        with open(logo_path, "rb") as f:
            logo_base64 = base64.b64encode(f.read()).decode()
        
        logo_html = f"""
        <div style="
            position: fixed !important;
            top: 0px !important;
            left: 0px !important;
            z-index: 999999 !important;
            margin: 0 !important;
            padding: 0 !important;
        ">
            <img src="data:image/png;base64,{logo_base64}" width="80" style="margin: 0; padding: 0;">
        </div>
        """
        st.markdown(logo_html, unsafe_allow_html=True)
        return True
    except Exception as e:
        return False

# STREAMLIT'İN TÜM PADDING'LERİNİ SIFIRLA
st.markdown("""
<style>
.stApp {
    background: #000515;
    padding: 0px !important;
    margin: 0px !important;
}

.block-container {
    padding: 0px !important;
    margin: 0px !important;
}

header {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# LOGO'YU EKLE
logo_loaded = add_logo()

# LOGO ALTINA BOŞLUK
if logo_loaded:
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

# İÇERİK
st.title("Kripto & Borsa AI")