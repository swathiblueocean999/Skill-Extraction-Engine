from scorer_day13 import (
    calculate_skill_score,
    calculate_experience_score,
    calculate_education_score,
    calculate_semantic_score,
    calculate_final_score
)
from weights_day13 import WEIGHTS


# 🔹 Sample Resume
resume = {
    "skills": ["Python", "Machine Learning"],
    "experience": 2,
    "education": "B.Tech",
    "text": "Python developer with machine learning experience"
}

# 🔹 Sample Job Description
jd = {
    "skills": ["Python", "Machine Learning"],
    "experience": 3,
    "education": "B.Tech",
    "text": "Looking for a machine learning engineer with Python skills"
}


# 🔹 Calculate Individual Scores
skill_score = calculate_skill_score(resume.get("skills"), jd.get("skills"))
exp_score = calculate_experience_score(resume.get("experience"), jd.get("experience"))
edu_score = calculate_education_score(resume.get("education"), jd.get("education"))
semantic_score = calculate_semantic_score(resume.get("text"), jd.get("text"))


# 🔹 Get Weights
weights = WEIGHTS["default"]


# 🔹 Calculate Final Score
final_score = calculate_final_score(
    skill_score,
    exp_score,
    edu_score,
    semantic_score,
    weights,
    resume
)


# 🔹 Print Output
print("\n========== ATS SCORE REPORT ==========")

print(f"\nSkill Match: {skill_score}%")
print(f"Experience Match: {exp_score}%")
print(f"Education Match: {edu_score}%")
print(f"Semantic Similarity: {semantic_score}%")

print(f"\nFinal ATS Score: {final_score}%")


# 🔹 Explainable Output
print("\n========== EXPLANATION ==========")

matched_skills = set(resume.get("skills", [])) & set(jd.get("skills", []))

print(f"- Matched Skills: {len(matched_skills)} / {len(jd.get('skills', []))}")
print(f"- Candidate Experience: {resume.get('experience', 0)} years")
print(f"- Required Experience: {jd.get('experience', 0)} years")
print(f"- Education: {resume.get('education', 'Not Provided')}")
print("- Semantic similarity calculated using resume & JD text")


# 🔹 Optional: Save to file
with open("output_day13.txt", "w") as f:
    f.write("ATS SCORE REPORT\n")
    f.write(f"Skill: {skill_score}%\n")
    f.write(f"Experience: {exp_score}%\n")
    f.write(f"Education: {edu_score}%\n")
    f.write(f"Semantic: {semantic_score}%\n")
    f.write(f"\nFinal Score: {final_score}%\n")