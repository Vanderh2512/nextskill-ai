import streamlit as st

st.set_page_config(page_title="Skill Gap Learning Path", page_icon="📚", layout="centered")

st.markdown("# 📚 Recommended Learning Paths")
st.markdown("Based on your missing skills, here are some curated course suggestions to help you close the gap and move closer to your goal career.")

# Simulated example: show missing skills and suggested courses
missing_skills = {
    "Project Management": ["Google Project Management Certificate (Coursera)", "Introduction to Project Management (edX)"],
    "SQL": ["SQL for Data Science (Coursera)", "Intro to SQL (Khan Academy)"],
    "Communication": ["Effective Communication (LinkedIn Learning)", "Business Communication (Coursera)"],
}

for skill, courses in missing_skills.items():
    st.markdown(f"### 🧩 {skill}")
    for course in courses:
        st.markdown(f"- {course}")
    st.markdown("---")

st.info("This is a prototype view. In future versions, course data will be dynamically fetched and personalized.")