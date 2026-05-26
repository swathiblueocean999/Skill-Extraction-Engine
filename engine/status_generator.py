def generate_status(score):

    # SAFETY CHECK

    if score < 0:
        score = 0

    if score > 100:
        score = 100

    # STATUS GENERATION

    if score >= 90:

        status = "elite"

        recommendation = "Highly Recommended"

    elif score >= 75:

        status = "excellent"

        recommendation = "Strongly Recommended"

    elif score >= 60:

        status = "strong"

        recommendation = "Recommended"

    elif score >= 45:

        status = "good"

        recommendation = "Consider"

    elif score >= 30:

        status = "average"

        recommendation = "Needs Improvement"

    else:

        status = "weak"

        recommendation = "Not Recommended"

    # PERFORMANCE BAND

    if score >= 85:
        performance_band = "Top Performer"

    elif score >= 70:
        performance_band = "High Performer"

    elif score >= 55:
        performance_band = "Moderate Performer"

    elif score >= 40:
        performance_band = "Low Performer"

    else:
        performance_band = "Risk Candidate"

    return {

        "status": status,

        "recommendation": recommendation,

        "performance_band": performance_band,

        "score": score
    }