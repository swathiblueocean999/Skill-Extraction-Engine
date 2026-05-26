def analyze_decision(answer):

    keywords = [
        "decision",
        "carefully",
        "select",
        "prioritize",
        "responsibly",
        "immediately",
        "manage",
        "compare",
        "consider",
        "evaluate"
    ]

    matched = []

    answer_lower = answer.lower()

    for word in keywords:

        if word in answer_lower:
            matched.append(word)

    score = min(len(matched) * 12, 100)

    return {
        "score": score,
        "matched_keywords": matched
    }