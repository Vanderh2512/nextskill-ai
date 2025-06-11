import streamlit as st
import json

st.set_page_config(page_title="NextSkill AI", page_icon="🧠", layout="centered")

# -------- LANDING SCREEN --------
st.markdown("## 🧠 Welcome to **NextSkill AI**")
st.markdown("AI-powered career matching from resume to opportunity.")
st.image("https://images.unsplash.com/photo-1555066931-4365d14bab8c", use_container_width=True, caption="Built for the future of work.")
st.markdown("---")

st.markdown("### 🚀 What You Can Do")
st.markdown("""
- Paste your resume skills
- Match to 1,000+ real-world jobs from the U.S. O*NET database
- Discover top career fits based on your skill strengths
- See what skills you're missing — and how to close the gap
""")

st.markdown("### 🔐 Private & Secure")
st.markdown("We do not store your resume or data. This is a demo preview only.")

# Call to action
st.markdown("#### 👇 Ready to begin?")
if st.button("Start Career Matching"):
    st.switch_page("pages/01_Match_Careers.py")  # Adjusted for Streamlit multipage

# Optionally display source info
with st.expander("🔍 About the Data"):
    st.write("Matches are based on O*NET 29.3 official skills data, curated by the U.S. Department of Labor.")