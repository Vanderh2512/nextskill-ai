import streamlit as st
import json

st.set_page_config(page_title="Match Careers", page_icon="🧠", layout="centered")

st.title("🧠 Match Careers to Your Skills")
st.markdown("Paste your resume skills below to find the most compatible job roles based on the U.S. O*NET database.")

# Load job skill data
try:
    with open("onet_job_skill_full.json", "r") as f:
        job_skill_map = json.load(f)
except Exception as e:
    st.error("Failed to load job-skill database.")
    st.stop()

# User skill input
user_input = st.text_area("Enter your skills (comma-separated):", "Project Management, SQL, Communication")

if user_input:
    resume_skills = [skill.strip() for skill in user_input.split(",")]
    match_results = []

    for job, required_skills in job_skill_map.items():
        matched = set(resume_skills) & set(required_skills)
        missing = set(required_skills) - set(resume_skills)
        match_results.append({
            "Job Title": job,
            "Matched Skills": list(matched),
            "Missing Skills": list(missing),
            "Match Score": len(matched),
            "Total Skills": len(required_skills),
            "Coverage %": round((len(matched) / len(required_skills)) * 100, 1) if required_skills else 0
        })

    sorted_matches = sorted(match_results, key=lambda x: x["Match Score"], reverse=True)
    st.subheader("Top Matching Jobs")

    for result in sorted_matches[:10]:
        st.markdown(f"### {result['Job Title']}")
        st.markdown(f"- Match Score: {result['Match Score']} / {result['Total Skills']} ({result['Coverage %']}%)")
        st.markdown(f"- ✅ Matched: {', '.join(result['Matched Skills']) or 'None'}")
        st.markdown(f"- 🔍 Missing: {', '.join(result['Missing Skills']) or 'None'}")
        st.markdown("---")