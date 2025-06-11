import streamlit as st
import json

st.set_page_config(page_title="Skill Gap Learning Path", page_icon="📚", layout="centered")

st.title("📚 Recommended Learning Paths")
st.markdown("These suggestions are based on your missing skills from the job matching results.")

# Example placeholder: In real app this comes from session state or previous page
user_missing_skills = ["Project Management", "SQL", "Communication"]

# Load course mapping from external JSON file
try:
    with open("sample_skill_course_map.json", "r") as file:
        skill_course_map = json.load(file)
except Exception as e:
    st.error("Could not load course recommendations file.")
    st.stop()

# Show learning recommendations per missing skill
for skill in user_missing_skills:
    st.subheader(f"🧩 {skill}")
    if skill in skill_course_map:
        for course in skill_course_map[skill]:
            st.markdown(f"- [{course['title']}]({course['url']})  
  _{course['provider']}_")
    else:
        st.warning("No courses found for this skill.")
    st.markdown("---")

st.info("More personalized, dynamic recommendations coming soon!")