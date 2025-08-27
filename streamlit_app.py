import streamlit as st
import base64

# Page configuration
st.set_page_config(page_title="Saravanapriya | AI Portfolio", layout="wide")

# Top Navigation Boxes
col1, col2, col3 = st.columns([1, 1, 6])

with col1:
    st.markdown("""
    <a href="https://www.linkedin.com/in/spriyabala/" target="_blank">
        <div style="background-color:#0077B5;padding:10px;border-radius:8px;text-align:center;color:white;font-weight:bold;">
            💼 LinkedIn
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="https://github.com/MayaPriss" target="_blank">
        <div style="background-color:#333;padding:10px;border-radius:8px;text-align:center;color:white;font-weight:bold;">
            💻 GitHub
        </div>
    </a>
    """, unsafe_allow_html=True)

# Header
st.title("👩‍💻 Saravanapriya")
st.subheader("Final-year Software Engineering Student | AI Enthusiast | Future Tech Leader")
st.markdown("Welcome to my portfolio! Explore my journey, projects, and passion for building scalable, user-friendly systems.")

st.header("📖 About Me")
st.write("""
    I'm currently pursuing Software Engineering with a specialization in AI at Taylor's University.
    My experience spans frontend development, testing automation, and technical documentation — all backed by a love for structured workflows and real-world impact.

    I recently interned at Caction Sdn. Bhd. and now work part-time at M-TITANS SOFTWARE SDN. BHD., where I continue to refine my skills in building scalable systems and collaborating across teams.

    Outside of work, I enjoy badminton, gaming, and continuous learning through hackathons and AI projects.
    """)

st.header("📝 My Resume")

pdf_path = "files/priya_resume.pdf"

try:
    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📥 Download Resume",
            data=f,
            file_name="priya_resume.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.error("Resume file not found. Please make sure 'priya_resume.pdf' is in the same folder as your app.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | © 2025 Saravanapriya")
