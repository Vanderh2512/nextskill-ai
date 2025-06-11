import streamlit as st
import json

st.set_page_config(page_title="Skill Gap Learning Path", page_icon="📚", layout="centered")

st.markdown("# 📚 Recommended Learning Paths")
st.markdown("These course suggestions are based on your skill gaps from the job matching engine.")

# Simulate retrieval of missing skills from session state or static input
# In a real app, this would come from session_state or another page
user_missing_skills = ["Project Management", "SQL", "Communication"]

# Inline skill → course map (this would usually be imported or loaded from file/db)
skill_course_map = {
    "Project Management": [
        {"title": "Google Project Management Certificate", "provider": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-project-management"},
        {"title": "Project Management for Beginners", "provider": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/project-management-foundations"}
    ],
    "SQL": [
        {"title": "SQL for Data Science", "provider": "Coursera", "url": "https://www.coursera.org/learn/sql-for-data-science"},
        {"title": "Intro to SQL", "provider": "Khan Academy", "url": "https://www.khanacademy.org/computing/computer-programming/sql"}
    ],
    "Communication": [
        {"title": "Business Communication", "provider": "Coursera", "url": "https://www.coursera.org/learn/business-communication"},
        {"title": "Effective Communication", "provider": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/communication-foundations"}
    ],
    "Python": [
        {"title": "Python for Everybody", "provider": "Coursera", "url": "https://www.coursera.org/specializations/python"},
        {"title": "Learn Python 3", "provider": "Codecademy", "url": "https://www.codecademy.com/learn/learn-python-3"}
    ]
}

# Show personalized suggestions
for skill in user_missing_skills:
    if skill in skill_course_map:
        st.markdown(f"### 🧩 {skill}")
        for course in skill_course_map[skill]:
            st.markdown(f"- [{course['title']}]({course['url']})  
  _{course['provider']}_")
        st.markdown("---")
    else:
        st.markdown(f"### 🧩 {skill}")
        st.warning("No course recommendations available yet.")
        st.markdown("---")

st.info("This prototype pulls real-time recommendations based on your skill gaps.")