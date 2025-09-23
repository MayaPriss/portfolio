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
    "The Grand Cinema (TGC)",
    "Testing Automation with Playwright",
    "Responsive UI Components",
    "Workflow Documentation & SDLC Mapping"
])

# ---------- Project Details ----------
if project == "The Grand Cinema (TGC)":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image("assets/tgc.png", width=300)

    with col2:
        st.markdown("### The Grand Cinema (TGC)")
        st.markdown("""
        - Malay-Language Ticketing System (SPM Sains Komputer Project)
        - Modular PHP Architecture  
        - Secure User Authentication  
        - Dynamic Seat Mapping
        - Clean UI with Custom CSS
        """)
    with col3:
        st.markdown("""
        <a href="https://github.com/MayaPriss/tgc_cinema" target="_blank">
            <div class="nav-button github">🚀 Click Me</div>
        </a>
        """, unsafe_allow_html=True)

elif project == "Testing Automation with Playwright":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image("assets/playwright_testing.png", width=150)
    with col2:
        st.markdown("### Testing Automation with Playwright")
        st.markdown("""
        - Automated web and mobile QA workflows  
        - Used Playwright for cross-browser testing  
        - Integrated Firebase App Distribution  
        - Reduced manual testing time by 60%  
        - Logged test results with custom dashboards  
        """)
    with col3:
        st.markdown("""
        <a href="https://github.com/MayaPriss/playwright-automation" target="_blank">
            <div class="nav-button github">🚀 Click Me</div>
        </a>
        """, unsafe_allow_html=True)

elif project == "Responsive UI Components":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image("assets/ui_components.png", width=150)
    with col2:
        st.markdown("### Responsive UI Components")
        st.markdown("""
        - Designed modular UI elements in Vue.js and Flutter  
        - Focused on accessibility and responsiveness  
        - Created reusable component libraries  
        - Implemented dark/light theme toggles  
        - Tested across mobile and desktop breakpoints  
        """)
    with col3:
        st.markdown("""
        <a href="https://github.com/MayaPriss/ui-components" target="_blank">
            <div class="nav-button github">🚀 Click Me</div>
        </a>
        """, unsafe_allow_html=True)

elif project == "Workflow Documentation & SDLC Mapping":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image("assets/sdlc_docs.png", width=150)
    with col2:
        st.markdown("### Workflow Documentation & SDLC Mapping")
        st.markdown("""
        - Mapped internship tasks to SDLC phases  
        - Documented hardware/software infrastructure  
        - Created visual diagrams for workflows  
        - Standardized reporting formats  
        - Improved onboarding with structured guides  
        """)
    with col3:
        st.markdown("""
        <a href="https://github.com/MayaPriss/sdlc-docs" target="_blank">
            <div class="nav-button github">🚀 Click Me</div>
        </a>
        """, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 14px; color: #5C4B3B; margin-top: 30px;'>
    Made with ❤️ using Streamlit<br>
    © 2025 Saravanapriya
</div>
""", unsafe_allow_html=True)