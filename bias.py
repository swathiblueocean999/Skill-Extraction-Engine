def remove_bias_fields(candidate):
    # Remove unnecessary fields (if any)
    return {
        "skills": candidate.get("skills", []),
        "experience": candidate.get("experience", 0),
        "education": candidate.get("education", ""),
        "text": candidate.get("text", "")
    }