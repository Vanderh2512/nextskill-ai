import streamlit as st
import json

st.set_page_config(page_title="Match Careers", page_icon="🧠", layout="centered")

st.title("🧠 Match Careers to Your Skills")
st.markdown("Enter your known skills below to find top-matching careers based on real-world data.")

# Load job-skill mapping (ensure this JSON file exists in your repo)
try:
    with open("onet_job_skill_full.json", "r") as f:
        job_skill_map = json.load(f)
except Exception as e:
    st.error("Could not load job-skill data. Please ensure 'onet_job_skill_full.json' is present in the root directory.")
    st.stop()

# Input from user
user_input = st.text_area("Paste your skills (comma-separated):", "Project Management, SQL, Communication")

if user_input:
    user_skills = [s.strip().lower() for s in user_input.split(",")]
    results = []

    for job, skills in job_skill_map.items():
        required_skills = [s.lower() for s in skills]
        matched = set(user_skills) & set(required_skills)
        missing = set(required_skills) - set(user_skills)
        score = len(matched)
        if score > 0:
            results.append({
                "job": job,
                "matched": list(matched),
                "missing": list(missing),
                "score": score,
                "total_required": len(required_skills),
                "coverage": round((score / len(required_skills)) * 100, 1) if required_skills else 0
            })

    # Sort by match score
    sorted_results = sorted(results, key=lambda x: (-x["score"], -x["coverage"]))

    # Show results
    st.subheader("Top Career Matches")
    for r in sorted_results[:10]:
        st.markdown(f"### {r['job']}")
        st.markdown(f"- ✅ Matched Skills: {', '.join(r['matched']) or 'None'}")
        st.markdown(f"- 🔍 Missing Skills: {', '.join(r['missing']) or 'None'}")
        st.markdown(f"- 🔢 Match Score: {r['score']} / {r['total_required']} ({r['coverage']}%)")
        st.markdown("---")