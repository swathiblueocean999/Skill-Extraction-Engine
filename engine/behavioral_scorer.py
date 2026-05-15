def calculate_behavior_score(
    hesitation_count,
    uncertainty,
    contradiction,
    stress,
    sentiment
):
    score = 100

    score -= hesitation_count * 10

    if uncertainty:
        score -= 20

    if contradiction:
        score -= 25

    if stress:
        score -= 15

    if sentiment == "negative":
        score -= 10

    if score < 0:
        score = 0

    return score