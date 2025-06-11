import streamlit as st
import json

st.set_page_config(page_title="Skill Gap Learning Path", page_icon="📚", layout="centered")

st.markdown("# 📚 Recommended Learning Paths")
st.markdown("These course suggestions are based on your skill gaps from the job matching engine.")

# Simulated missing skills (in real app, this comes from session state or earlier flow)
user_missing_skills = ["Project Management", "SQL", "Communication"]

# Load skill-to-course map from external JSON file in project root
try:
    with open("sample_skill_course_map.json", "r") as f:
        skill_course_map = json.load(f)
except Exception as e:
    st.error("Failed to load skill-course mapping.")
    st.stop()

# Show dynamic course suggestions per missing skill
for skill in user_missing_skills:
    st.markdown(f"### 🧩 {skill}")
    if skill in skill_course_map:
        for course in skill_course_map[skill]:
            st.markdown(f"- [{course['title']}]({course['url']})  
  _{course['provider']}_")
    else:
        st.warning("No course recommendations available yet.")
    st.markdown("---")

st.info("This prototype pulls real-time recommendations based on your skill gaps.")