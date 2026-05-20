def get_ats_summary(score):

    if score >= 85:
        return "Excellent ATS profile"

    elif score >= 70:
        return "Good ATS profile"

    return "Average ATS profile"