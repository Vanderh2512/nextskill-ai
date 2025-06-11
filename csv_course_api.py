from fastapi import FastAPI
import pandas as pd

# Load course data from CSV
csv_path = "course_recommendations.csv"
df = pd.read_csv(csv_path)

# Convert to dictionary grouped by skill
course_data = {}
for _, row in df.iterrows():
    skill = row["Skill"]
    course = {
        "title": row["Title"],
        "url": row["URL"],
        "provider": row["Provider"],
        "duration": row["Duration"],
        "certified": row["Certified"]
    }
    course_data.setdefault(skill, []).append(course)

# Initialize FastAPI app
app = FastAPI(title="NextSkill AI - CSV-Based Course Recommender")

@app.get("/recommendations")
def get_recommendations(skill: str):
    skill = skill.strip()
    recommendations = course_data.get(skill, [])
    return {
        "skill": skill,
        "course_count": len(recommendations),
        "courses": recommendations
    }

# Run with: uvicorn csv_course_api:app --reload
