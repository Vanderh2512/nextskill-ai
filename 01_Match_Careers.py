
import streamlit as st
import json

# Load full O*NET job-to-skill mapping
with open("onet_job_skill_full.json", "r") as f:
    job_skill_map = json.load(f)

st.title("NextSkill AI: Job Match by Resume Skills")

# Simulate a resume skill input
st.subheader("Step 1: Paste your resume skills")
user_input = st.text_area("Enter comma-separated skills:", "Critical Thinking, Speaking, Learning Strategies")

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
        st.markdown(f"- ✅ Matched Skills: {', '.join(result['Matched Skills'])}")
        st.markdown(f"- 🔍 Missing Skills: {', '.join(result['Missing Skills'])}")
        st.markdown("---")
