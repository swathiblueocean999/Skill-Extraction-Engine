def analyze_reasoning(answer):

    keywords = [
        "analyze",
        "because",
        "reason",
        "compare",
        "identify",
        "explain",
        "verify",
        "prioritize",
        "understand"
    ]

    matched = []

    for word in keywords:
        if word.lower() in answer.lower():
            matched.append(word)

    score = min(len(matched) * 15, 100)

    return {
        "score": score,
        "matched_keywords": matched
    }