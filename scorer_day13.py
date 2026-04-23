# scorer_day13.py

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


# 🔹 Skill Score
def calculate_skill_score(resume_skills, jd_skills):
    if not resume_skills or not jd_skills:
        return 0

    matched = set(resume_skills).intersection(set(jd_skills))
    score = (len(matched) / len(jd_skills)) * 100
    return round(score, 2)


# 🔹 Experience Score
def calculate_experience_score(candidate_exp, required_exp):
    if candidate_exp is None or required_exp is None:
        return 0

    if candidate_exp >= required_exp:
        return 100
    else:
        return round((candidate_exp / required_exp) * 100, 2)


# 🔹 Education Score
def calculate_education_score(candidate_edu, required_edu):
    if not candidate_edu or not required_edu:
        return 0

    candidate_edu = candidate_edu.lower()
    required_edu = required_edu.lower()

    if candidate_edu == required_edu:
        return 100
    elif candidate_edu in required_edu or required_edu in candidate_edu:
        return 70
    else:
        return 40


# 🔹 Semantic Similarity Score
def calculate_semantic_score(resume_text, jd_text):
    if not resume_text or not jd_text:
        return 0

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)


# 🔹 Adjust Weights (Missing Data Handling)
def adjust_weights(weights, resume):
    new_weights = weights.copy()

    if not resume.get("experience"):
        new_weights.pop("experience", None)

    if not resume.get("education"):
        new_weights.pop("education", None)

    # Normalize remaining weights
    total = sum(new_weights.values())
    for key in new_weights:
        new_weights[key] = new_weights[key] / total

    return new_weights


# 🔹 Final Score
def calculate_final_score(skill, exp, edu, semantic, weights, resume):
    weights = adjust_weights(weights, resume)

    final_score = 0

    if "skill" in weights:
        final_score += weights["skill"] * skill

    if "experience" in weights:
        final_score += weights["experience"] * exp

    if "education" in weights:
        final_score += weights["education"] * edu

    if "semantic" in weights:
        final_score += weights["semantic"] * semantic

    return round(final_score, 2)