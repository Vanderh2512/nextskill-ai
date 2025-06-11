import streamlit as st
import requests
import re
import fitz  # PyMuPDF
import json

st.set_page_config(page_title="NextSkill AI Prototype", layout="centered")
st.title("🧠 NextSkill AI - Personalized Career Path Generator")

st.markdown("Upload your resume (PDF or plain text) and we'll identify your skills, match career paths, detect skill gaps, and recommend courses.")

known_skills = [
    "Critical Thinking", "Complex Problem Solving", "Management of Personnel Resources",
    "Time Management", "Writing", "Speaking", "Coordination", "Judgment and Decision Making",
    "Active Listening", "Reading Comprehension", "Monitoring", "Systems Evaluation", "Learning Strategies"
]

job_skill_map = {
    "Instructional Designer": ["Critical Thinking", "Writing", "Reading Comprehension", "Coordination"],
    "Marketing Manager": ["Speaking", "Critical Thinking", "Judgment and Decision Making", "Time Management"],
    "Project Manager": ["Coordination", "Time Management", "Monitoring", "Judgment and Decision Making"],
    "Training Specialist": ["Speaking", "Active Listening", "Critical Thinking", "Learning Strategies"],
    "Operations Analyst": ["Complex Problem Solving", "Systems Evaluation", "Monitoring", "Critical Thinking"]
}

def extract_text_from_pdf(file):
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"ERROR: Failed to extract text from PDF - {e}"

uploaded_file = st.file_uploader("Upload your resume", type=["txt", "pdf"])
profile = {}

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Resume Text Preview")
    st.text(text[:500] + "..." if len(text) > 500 else text)

    extracted_skills = [skill for skill in known_skills if re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE)]

    profile["extracted_skills"] = extracted_skills

    if extracted_skills:
        st.success("✅ Skills Identified:")
        for skill in extracted_skills:
            st.markdown(f"- {skill}")
    else:
        st.warning("No known skills found in resume.")

    if extracted_skills:
        st.subheader("💼 Top Career Matches")
        match_scores = []
        for job, required_skills in job_skill_map.items():
            matched = set(extracted_skills) & set(required_skills)
            missing = set(required_skills) - set(extracted_skills)
            match_scores.append({
                "Job Title": job,
                "Matched Skills": list(matched),
                "Missing Skills": list(missing),
                "Match Score": len(matched)
            })

        sorted_matches = sorted(match_scores, key=lambda x: x["Match Score"], reverse=True)
        top_match = sorted_matches[0]
        st.markdown(f"**Best Fit Role:** {top_match['Job Title']}")
        st.markdown(f"**Matched Skills:** {', '.join(top_match['Matched Skills'])}")
        st.markdown(f"**Missing Skills:** {', '.join(top_match['Missing Skills']) if top_match['Missing Skills'] else 'None'}")

        profile["matched_role"] = top_match["Job Title"]
        profile["matched_skills"] = top_match["Matched Skills"]
        profile["missing_skills"] = top_match["Missing Skills"]

        all_courses = []

        if top_match["Missing Skills"]:
            if st.button("📚 Recommend Courses for Missing Skills"):
                st.subheader("📘 Courses to Close Skill Gaps")
                for skill in top_match["Missing Skills"]:
                    with st.spinner(f"Fetching courses for {skill}..."):
                        try:
                            url = f"http://127.0.0.1:8000/recommendations?skill={skill.replace(' ', '%20')}"
                            response = requests.get(url)
                            if response.status_code == 200:
                                data = response.json()
                                courses = data.get("courses", [])
                                if courses:
                                    for course in courses:
                                        st.subheader(course["title"])
                                        st.write(f"**Skill:** {skill}")
                                        st.write(f"**Provider:** {course['provider']}")
                                        st.write(f"**Duration:** {course['duration']}")
                                        st.write(f"**Certified:** {course['certified']}")
                                        st.markdown(f"[Go to Course]({course['url']})", unsafe_allow_html=True)
                                        st.markdown("---")
                                        all_courses.append(course)
                                else:
                                    st.warning(f"No courses found for skill: {skill}")
                            else:
                                st.error(f"Error fetching course data for {skill}")
                        except Exception as e:
                            st.error(f"An error occurred while fetching data for {skill}: {e}")
                profile["recommended_courses"] = all_courses

                # Save user profile as downloadable JSON
                profile_name = "nextskill_user_profile.json"
                with open(profile_name, "w") as f:
                    json.dump(profile, f, indent=2)

                with open(profile_name, "rb") as f:
                    st.download_button("💾 Download My Profile (JSON)", data=f, file_name=profile_name, mime="application/json")
