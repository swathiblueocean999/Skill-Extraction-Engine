def get_final_decision(score, behavior, integrity):

    if score >= 85 and behavior >= 80 and integrity >= 80:
        return "Selected"

    elif score >= 70 and integrity >= 60:
        return "Hold / Review"

    return "Rejected"