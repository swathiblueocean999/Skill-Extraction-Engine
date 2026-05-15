def generate_status(score):

    if score >= 75:
        return "excellent"

    elif score >= 60:
        return "strong"

    elif score >= 45:
        return "good"

    elif score >= 30:
        return "average"

    else:
        return "weak"