def optimize_thresholds(score):

    if score >= 85:

        return "Excellent Threshold"

    elif score >= 70:

        return "Balanced Threshold"

    return "Needs Threshold Improvement"