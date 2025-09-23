import streamlit as st
import base64
from utils import set_background

# ---------- Apply Background ----------
set_background("assets/bg.jpg")

# ---------- Page Configuration ----------
st.set_page_config(page_title="Saravanapriya | AI Portfolio", layout="wide")

# ---------- Top Navigation ----------
col1, col2, col3 = st.columns([1, 1, 6])

with col1:
    st.markdown("""
    <a href="https://www.linkedin.com/in/spriyabala/" target="_blank">
        <div class="nav-button linkedin">💼 LinkedIn</div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="https://github.com/MayaPriss" target="_blank">
        <div class="nav-button github">💻 GitHub</div>
    </a>
    """, unsafe_allow_html=True)

# ---------- Header ----------
st.title("👩‍💻 Saravanapriya")
st.subheader("AI-Focused Software Engineer | Bachelor of Software Engineering (Honours) specializing in AI | Future Tech Leader")
st.markdown("""
Welcome to my digital portfolio. Here, you'll find a curated snapshot of my academic journey, technical expertise, and passion for building scalable, user-centric systems.
""")

# ---------- About Me ----------
st.header("📖 About Me")
st.write("""
I've recently completed Degree in Software Engineering with a specialization in Artificial Intelligence at Taylor's University. My experience spans frontend development, testing automation, and technical documentation—driven by a love for structured workflows and real-world impact.

I’ve interned at Caction Sdn. Bhd. and currently work part-time at M-TITANS SOFTWARE SDN. BHD., where I continue refining my skills in scalable system design and cross-functional collaboration.

Outside of work, I enjoy badminton, gaming, and continuous learning through workshops and AI-driven projects.
""")

# ---------- Resume Section ----------
st.header("📝 My Resume")

pdf_path = "files/priya_resume.pdf"

try:
    with open(pdf_path, "rb") as f:
        resume_data = f.read()
        resume_base64 = base64.b64encode(resume_data).decode()

        download_html = f"""
        <a href="data:application/pdf;base64,{resume_base64}" download="priya_resume.pdf">
            <div class="nav-button resume">📥 Download Resume</div>
        </a>
        """
        st.markdown(download_html, unsafe_allow_html=True)

except FileNotFoundError:
    st.error("Resume file not found. Please ensure 'priya_resume.pdf' is in the 'files' folder.")

# ---------- Footer ----------
st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 14px; color: #5C4B3B;'>
    Made with ❤️ using Streamlit<br>
    © 2025 Saravanapriya
</div>
""", unsafe_allow_html=True)