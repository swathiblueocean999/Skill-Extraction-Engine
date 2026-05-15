def evaluate_scenario(answer):

    keywords = [
        "professional",
        "customer",
        "teamwork",
        "support",
        "issue",
        "resolve",
        "solution",
        "communicate",
        "calm",
        "respectfully"
    ]

    matched = []

    for word in keywords:
        if word.lower() in answer.lower():
            matched.append(word)

    score = min(len(matched) * 10, 100)

    return {
        "score": score,
        "matched_keywords": matched
    }