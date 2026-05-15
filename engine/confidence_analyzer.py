def confidence_level(score):
    if score >= 75:
        return "high"

    if score >= 45:
        return "medium"

    return "low"