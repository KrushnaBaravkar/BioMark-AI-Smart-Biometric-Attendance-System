import streamlit as st
import base64
from pathlib import Path


def header_home():

    logo_path = Path(__file__).parent / "Logo.png"

    with open(logo_path, "rb") as image_file:
        logo_base64 = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px;">
            <img src="data:image/png;base64,{logo_base64}" style="height:150px;" />
            <h1 style="text-align:center; color:#E0E3FF;">BIOMARK</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

def header_dashboard():

    logo_path = Path(__file__).parent / "Logo.png"

    with open(logo_path, "rb") as image_file:
        logo_base64 = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src="data:image/png;base64,{logo_base64}" style="height:75px;" />
            <h2 style='text-align:left; color:#5865F2; font-size:5rem;'>BIOMARK</h2>
        </div>
        """,
        unsafe_allow_html=True
    )