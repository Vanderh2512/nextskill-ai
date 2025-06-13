import streamlit as st
import json

st.set_page_config(page_title="Skill Gap Learning Path", page_icon="📚", layout="centered")

st.title("📚 Recommended Learning Paths")
st.markdown("These suggestions are based on your missing skills from the job matching results.")

# Simulated list of missing skills
user_missing_skills = ["Project Management", "SQL", "Communication"]

# Load external skill-to-course mapping from JSON file
try:
    with open("sample_skill_course_map.json", "r") as file:
        skill_course_map = json.load(file)
except Exception as e:
    st.error("Could not load course recommendations file.")
    st.stop()

# Display personalized learning suggestions
for skill in user_missing_skills:
    st.subheader(f"🧩 {skill}")
    if skill in skill_course_map:
        for course in skill_course_map[skill]:
            title = course.get("title", "Untitled Course")
            url = course.get("url", "#")
            provider = course.get("provider", "Unknown")
            st.markdown(f"- [{title}]({url})  
  _{provider}_")
    else:
        st.warning("No courses found for this skill.")
    st.markdown("---")

st.info("This version dynamically loads courses from a JSON file in your project root.")