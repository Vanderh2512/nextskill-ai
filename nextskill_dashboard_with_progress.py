import streamlit as st
import json

st.set_page_config(page_title="NextSkill AI Learner Dashboard", layout="centered")
st.title("📊 NextSkill AI - Learner Dashboard")

st.markdown("Upload your saved profile to view your upskilling journey and progress.")

uploaded_profile = st.file_uploader("📁 Upload your JSON profile", type=["json"])

if uploaded_profile is not None:
    profile = json.load(uploaded_profile)

    st.subheader("👤 Learner Snapshot")

    matched_role = profile.get("matched_role", "N/A")
    st.markdown(f"**🎯 Matched Role:** `{matched_role}`")

    extracted_skills = profile.get("extracted_skills", [])
    missing_skills = profile.get("missing_skills", [])
    matched_skills = profile.get("matched_skills", [])
    total_required = len(matched_skills) + len(missing_skills)
    completed = len(matched_skills)
    progress_pct = int((completed / total_required) * 100) if total_required > 0 else 0

    st.markdown("**✅ Detected Skills:**")
    for skill in extracted_skills:
        st.markdown(f"- {skill}")

    st.markdown("**📉 Skill Gaps:**")
    if missing_skills:
        for skill in missing_skills:
            st.markdown(f"- {skill}")
    else:
        st.success("You have all required skills for your matched role!")

    st.subheader("📊 Progress Toward Career Readiness")
    st.progress(progress_pct / 100)
    st.write(f"{progress_pct}% skill coverage for `{matched_role}`")

    if progress_pct == 100:
        st.balloons()
        st.success("🎉 You're fully skill-ready for this role!")

    st.subheader("📘 Recommended Courses")
    courses = profile.get("recommended_courses", [])
    if courses:
        for course in courses:
            st.markdown(f"**{course['title']}**")
            st.write(f"- Skill: {course['skill']}")
            st.write(f"- Provider: {course['provider']}")
            st.write(f"- Duration: {course['duration']}")
            st.write(f"- Certified: {'Yes' if course['certified'] else 'No'}")
            st.markdown(f"[Go to Course]({course['url']})", unsafe_allow_html=True)
            st.markdown("---")
    else:
        st.info("No course recommendations available yet.")
