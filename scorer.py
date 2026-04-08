from semantic import get_similarity_score

# Skill score
def calculate_skill_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0
    
    matched_skills = set(resume_skills).intersection(set(jd_skills))
    return (len(matched_skills) / len(jd_skills)) * 100


# Experience score
def calculate_experience_score(resume_exp, required_exp):
    if required_exp == 0:
        return 100
    
    return min((resume_exp / required_exp) * 100, 100)


# Education score
def calculate_education_score(resume_edu, required_edu):
    return 100 if resume_edu.lower() == required_edu.lower() else 0


#  Semantic score (NEW in Day 14)
def calculate_semantic_score(resume_text, jd_text):
    similarity = get_similarity_score(resume_text, jd_text)
    return similarity * 100


# Final ATS score
def calculate_final_score(scores, weights):
    final_score = 0
    
    for key in scores:
        final_score += scores[key] * weights.get(key, 0)
    
    return final_score