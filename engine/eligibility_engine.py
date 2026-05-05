def check_eligibility(profile, rule):
    score = profile.get("score", 0)

    # Eligible
    if score >= rule["min_score"]:
        return "Eligible"

    # Review (slightly below)
    elif score >= (rule["min_score"] - 10):
        return "Review"

    # Rejected
    else:
        return "Rejected"