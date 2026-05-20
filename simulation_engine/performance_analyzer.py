def analyze_performance(candidate):

    score = candidate["final_hiring_score"]

    if score >= 85:

        return "Excellent Pipeline Performance"

    elif score >= 70:

        return "Good Pipeline Performance"

    elif score >= 60:

        return "Average Pipeline Performance"

    return "Weak Pipeline Performance"