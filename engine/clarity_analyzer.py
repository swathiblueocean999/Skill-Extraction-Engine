def analyze_clarity(answer):

    answer = answer.lower()

    clarity_keywords = [
        "handled",
        "managed",
        "developed",
        "improved",
        "prepared",
        "coordinated",
        "solved"
    ]

    score = 30

    for word in clarity_keywords:

        if word in answer:
            score += 10

    if len(answer.split()) >= 10:
        score += 10

    return min(score, 100)