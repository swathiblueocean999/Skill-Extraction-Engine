def calculate_skill_score(resume_skills, jd_skills):
    if not resume_skills or not jd_skills:
        return 0

    match = set(resume_skills).intersection(set(jd_skills))
    return len(match) / len(jd_skills)


def calculate_experience_score(resume_exp, jd_exp):
    try:
        resume_exp = int(resume_exp)
        jd_exp = int(jd_exp)
    except:
        return 0

    if jd_exp == 0:
        return 1

    if resume_exp >= jd_exp:
        return 1.0
    else:
        return resume_exp / jd_exp


def calculate_education_score(resume_edu, jd_edu):
    return 1.0 if resume_edu == jd_edu else 0.5


def calculate_final_score(scores, weights):
    final = 0
    for key in scores:
        final += scores[key] * weights.get(key, 0)

    return round(final, 4)