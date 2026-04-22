from weights import WEIGHTS
from semantic import semantic_score

def calculate_score(profile):

    skills = profile.get("skills", [])
    role = profile.get("role", "")
    experience = profile.get("experience", "")

    if not isinstance(skills, list):
        skills = []

    # ---------------- SKILLS (BOOSTED) ----------------
    skill_score = len(skills) * 12   # was 8 → increased

    # ---------------- EXPERIENCE (FIXED SCALE) ----------------
    exp_score = 20

    if isinstance(experience, str):
        if "0" in experience:
            exp_score = 35
        elif "1" in experience:
            exp_score = 50
        elif "2" in experience:
            exp_score = 60
        elif "3" in experience:
            exp_score = 70
        elif "5" in experience:
            exp_score = 85
        elif "10" in experience:
            exp_score = 95

    # ---------------- ROLE BOOST (FIXED) ----------------
    role_score = 30
    r = role.lower()

    if "manager" in r or "head" in r or "director" in r or "cfo" in r:
        role_score += 35
    elif "accountant" in r:
        role_score += 25
    elif "analyst" in r:
        role_score += 20

    # ---------------- SEMANTIC (BOOSTED) ----------------
    sem_score = semantic_score(profile)

    # ---------------- FINAL SCORE (RESCALED) ----------------
    final_score = (
        skill_score * WEIGHTS["skills"] +
        exp_score * WEIGHTS["experience"] +
        role_score * WEIGHTS["role"] +
        sem_score * WEIGHTS["semantic"]
    )

    # 🚀 FORCE NORMALIZATION TO ATS SCALE
    final_score = final_score * 1.4

    return round(min(100, final_score), 2)