import streamlit as st
from utils import set_background

# ---------- Page Configuration ----------
st.set_page_config(page_title="Projects", page_icon="🚀", layout="wide")

# ---------- Apply Background ----------
set_background("assets/bg.jpg")

# ---------- Header ----------
st.title("🚀 Featured Projects")
st.markdown("<h4 style='color:#5C4B3B;'>Choose a project to explore:</h4>", unsafe_allow_html=True)

# ---------- Project Selector ----------
project = st.selectbox("", [
    "POS System with Flutter & Firestore",
    "Testing Automation with Playwright",
    "Responsive UI Components",
    "Workflow Documentation & SDLC Mapping"
])

# ---------- Project Details ----------
if project == "POS System with Flutter & Firestore":
    st.markdown("""
    🔧 **Built a real-time inventory management system** using Flutter and Firestore.  
    📦 Features include barcode scanning, dynamic filtering, and inventory updates.
    """)
elif project == "Testing Automation with Playwright":
    st.markdown("""
    🧪 **Automated system testing** for web and mobile modules.  
    🚀 Used Playwright and Firebase App Distribution for efficient QA cycles.
    """)
elif project == "Responsive UI Components":
    st.markdown("""
    🎨 **Developed modular UI components** with Vue.js and Flutter.  
    🧩 Focused on accessibility, responsiveness, and user experience.
    """)
elif project == "Workflow Documentation & SDLC Mapping":
    st.markdown("""
    🗂️ **Mapped internship tasks to SDLC phases** for clarity and efficiency.  
    📋 Created structured documentation for hardware/software infrastructure.
    """)

# ---------- Footer ----------
st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 14px; color: #5C4B3B; margin-top: 30px;'>
    Made with ❤️ using Streamlit<br>
    © 2025 Saravanapriya
</div>
""", unsafe_allow_html=True)