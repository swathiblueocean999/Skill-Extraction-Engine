def analyze_decision(answer):

    keywords = [
        "decision",
        "carefully",
        "select",
        "prioritize",
        "responsibly",
        "immediately",
        "manage"
    ]

    matched = []

    for word in keywords:
        if word.lower() in answer.lower():
            matched.append(word)

    score = min(len(matched) * 20, 100)

    return {
        "score": score,
        "matched_keywords": matched
    }