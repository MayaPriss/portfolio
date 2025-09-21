import streamlit as st
import base64

def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
        color: #2E2E2E;
    }}

    /* Remove underline from all link states */
    a, a:visited, a:hover, a:active {{
        text-decoration: none !important;
        color: inherit !important;
    }}

    /* Button styling */
    .nav-button {{
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        box-shadow: 1px 1px 5px rgba(0,0,0,0.2);
        margin-bottom: 10px;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
    }}

    .linkedin, .github, .resume {{
        background-color: #5C4B3B;
        color: #F5F5DC;
    }}

    .nav-button:hover {{
        opacity: 0.95;
        transform: scale(1.02);
    }}

    /* Selectbox styling */
    div[data-baseweb="select"] > div {{
        background-color: #5C4B3B !important;
        color: #F5F5DC !important;
        border-radius: 8px;
        font-weight: bold;
    }}

    div[data-baseweb="select"] div[role="option"] {{
        color: black !important;
        background-color: #F5F5DC !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)