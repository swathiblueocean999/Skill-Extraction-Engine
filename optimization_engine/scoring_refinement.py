def refine_scoring(score):

    if score >= 90:

        return "Very High Confidence Scoring"

    elif score >= 80:

        return "High Confidence Scoring"

    elif score >= 70:

        return "Moderate Confidence Scoring"

    elif score >= 60:

        return "Low Confidence Scoring"

    return "Very Low Confidence Scoring"