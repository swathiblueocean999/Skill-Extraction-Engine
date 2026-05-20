def analyze_risk(behavior, integrity):

    if integrity < 60:
        return "High Integrity Risk"

    if behavior < 65:
        return "Behavioral Concern"

    return "Low Risk"