import re

def evaluate_resume(profile):

    score = 0

    print("PROCESSING:", profile.get("profile_id"))

    # -----------------------------
    # SAFE INPUT HANDLING
    # -----------------------------
    skills = profile.get("skills") or []

    if isinstance(skills, str):
        skills_text = skills.lower()
    else:
        skills_text = " ".join([
            s.lower().strip()
            for s in skills
            if isinstance(s, str) and s.strip()
        ])

    experience = profile.get("experience") or 0
    education = (profile.get("education") or "").lower()

    # -----------------------------
    # EXPERIENCE NORMALIZATION
    # -----------------------------
    try:
        if isinstance(experience, str):
            nums = re.findall(r"\d+", experience)
            experience = int(nums[0]) if nums else 0
        else:
            experience = int(experience)
    except:
        experience = 0

    # -----------------------------
    # CORE SCORING LOGIC
    # -----------------------------

    # Strong accounting indicators
    accounting_keywords = {
        "excel": 25,
        "tally": 25,
        "gst": 20,
        "account": 20,
        "tax": 15
    }

    for k, v in accounting_keywords.items():
        if k in skills_text:
            score += v

    # Technical skills
    if "python" in skills_text:
        score += 20
    if "sql" in skills_text:
        score += 15

    # Experience scoring
    if experience >= 5:
        score += 30
    elif experience >= 3:
        score += 20
    elif experience >= 1:
        score += 10

    # Education bonus
    if education in ["bcom", "mcom", "bba", "mba", "bsc", "btech"]:
        score += 10

    # -----------------------------
    # BALANCED PENALTY (SAFE)
    # -----------------------------
    weak_profile = (
        "excel" not in skills_text and
        "tally" not in skills_text and
        "account" not in skills_text and
        "python" not in skills_text
    )

    if weak_profile:
        score = max(0, score - 5)

    # -----------------------------
    # FINAL SAFETY CHECK
    # -----------------------------
    if score < 0:
        score = 0

    # -----------------------------
    # SMART THRESHOLD (FINAL FIX)
    # -----------------------------
    if experience <= 1:
        predicted_good = score >= 25
    elif experience <= 3:
        predicted_good = score >= 22
    else:
        predicted_good = score >= 20

    print("SCORE:", score, "PREDICTED:", predicted_good)

    return {
        "score": score,
        "predicted_good": predicted_good
    }