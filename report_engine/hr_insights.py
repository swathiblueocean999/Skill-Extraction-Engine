def get_hr_insight(score):

    if score >= 80:
        return "Strong communication and HR interaction"

    elif score >= 65:
        return "Moderate HR performance"

    return "Weak HR interaction"