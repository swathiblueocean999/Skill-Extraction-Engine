def calculate_score(result):

    score = 0

    # skill scoring
    score += len(result["skills"]) * 15

    # experience scoring
    if result["experience"]:
        score += 30

    # availability scoring
    if result["availability"]:
        score += 10

    # penalties
    if result["off_topic"]:
        score -= 40

    if result["uncertainty"]:
        score -= 20

    if result["missing_answer"]:
        score = 0

    # score limits
    if score < 0:
        score = 0

    if score > 100:
        score = 100

    return score