from semantic import calculate_similarity

def calculate_skill_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0
    matched = set(resume_skills).intersection(set(jd_skills))
    return len(matched) / len(jd_skills)


def calculate_experience_score(resume_exp, jd_exp):
    if jd_exp == 0:
        return 0
    return min(resume_exp / jd_exp, 1)


def calculate_education_score(resume_edu, jd_edu):
    if resume_edu == jd_edu:
        return 1
    return 0.5


def calculate_semantic_score(resume_text, jd_text):
    return calculate_similarity(resume_text, jd_text)


def calculate_final_score(scores, weights):
    final = (
        scores["skill"] * weights["skill"] +
        scores["experience"] * weights["experience"] +
        scores["education"] * weights["education"] +
        scores["semantic"] * weights["semantic"]
    )
    return round(final, 2)