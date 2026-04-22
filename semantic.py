def semantic_score(profile):
    skills = profile.get("skills", [])
    responsibilities = profile.get("responsibilities", [])

    if not isinstance(skills, list):
        skills = []

    if not isinstance(responsibilities, list):
        responsibilities = []

    score = len(skills) * 6 + len(responsibilities) * 2

    return min(100, score)