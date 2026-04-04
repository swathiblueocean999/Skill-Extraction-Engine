from scorer import (
    calculate_skill_score,
    calculate_experience_score,
    calculate_education_score,
    calculate_semantic_score,
    calculate_final_score
)
from weights import WEIGHTS

# Sample Resume
resume = {
    "skills": ["Python", "Machine Learning"],
    "experience": 2,
    "education": "B.Tech",
    "text": "Python developer with machine learning experience"
}

# Sample Job Description
jd = {
    "skills": ["Python", "Machine Learning"],
    "experience": 3,
    "education": "B.Tech",
    "text": "Looking for a machine learning engineer with Python skills"
}

# Calculate individual scores
scores = {
    "skill": calculate_skill_score(resume["skills"], jd["skills"]),
    "experience": calculate_experience_score(resume["experience"], jd["experience"]),
    "education": calculate_education_score(resume["education"], jd["education"]),
    "semantic": calculate_semantic_score(resume["text"], jd["text"])
}

# Choose weight type
weights = WEIGHTS["default"]

# Final score
final_score = calculate_final_score(scores, weights)

# Output
print("\n--- ATS SCORE BREAKDOWN ---")
print(f"Skill Match: {scores['skill']*100:.2f}%")
print(f"Experience Match: {scores['experience']*100:.2f}%")
print(f"Education Match: {scores['education']*100:.2f}%")
print(f"Semantic Match: {scores['semantic']*100:.2f}%")

print(f"\nFinal ATS Score: {final_score*100:.2f}%")