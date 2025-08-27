import streamlit as st

st.set_page_config(page_title="Projects", page_icon="🚀")

st.title("🚀 Featured Projects")

project = st.selectbox("Choose a project to explore:", [
    "POS System with Flutter & Firestore",
    "Testing Automation with Playwright",
    "Responsive UI Components",
    "Workflow Documentation & SDLC Mapping"
])

if project == "POS System with Flutter & Firestore":
    st.write("""
    🔧 Built a real-time inventory management system using Flutter and Firestore.
    📦 Features include barcode scanning, dynamic filtering, and inventory updates.
    """)
elif project == "Testing Automation with Playwright":
    st.write("""
    🧪 Automated system testing for web and mobile modules.
    🚀 Used Playwright and Firebase App Distribution for efficient QA cycles.
    """)
elif project == "Responsive UI Components":
    st.write("""
    🎨 Developed modular UI components with Vue.js and Flutter.
    🧩 Focused on accessibility, responsiveness, and user experience.
    """)
elif project == "Workflow Documentation & SDLC Mapping":
    st.write("""
    🗂️ Mapped internship tasks to SDLC phases for clarity and efficiency.
    📋 Created structured documentation for hardware/software infrastructure.
    """)