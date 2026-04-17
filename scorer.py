from semantic import get_similarity_score

def calculate_scores(candidate, jd):

    # Skill score
    skill_score = 100 if any(skill in jd["skills"] for skill in candidate["skills"]) else 0

    # Experience score
    exp_score = min(candidate["experience"] * 20, 100)

    # Education score
    edu_score = 100 if jd["education"] in candidate["education"] else 0

    # Semantic score
    semantic_score = get_similarity_score(candidate["text"], jd["text"]) * 100

    return {
        "skill": skill_score,
        "experience": exp_score,
        "education": edu_score,
        "semantic": semantic_score
    }


def final_score(scores):
    weights = {
        "skill": 0.4,
        "experience": 0.2,
        "education": 0.2,
        "semantic": 0.2
    }

    total = 0
    for key in scores:
        total += scores[key] * weights.get(key, 0)

    return total