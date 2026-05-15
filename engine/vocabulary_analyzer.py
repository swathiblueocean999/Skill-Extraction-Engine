def analyze_vocabulary(answer):

    unique_words = len(set(answer.lower().split()))

    advanced_words = [
        "coordinated",
        "managed",
        "improved",
        "implemented",
        "financial",
        "operations",
        "efficiency"
    ]

    score = 30

    if unique_words >= 5:
        score += 20

    if unique_words >= 10:
        score += 20

    for word in advanced_words:

        if word in answer.lower():
            score += 5

    return min(score, 100)