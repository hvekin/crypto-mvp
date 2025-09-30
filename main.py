import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Kripto MVP", page_icon="💰", layout="centered")

st.markdown("""
<style>
.stApp, section[data-testid="stSidebar"] {
    background: #000515;
}
section[data-testid="stSidebar"] > div {
    padding: 0rem;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    try:
        logo_path = Path(__file__).parent / "assets" / "logo.png"
        logo_image = Image.open(logo_path)
        st.image(logo_image, width=100)
    except:
        pass