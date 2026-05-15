def check_problem_solving(answer):

    keywords = [
        "solve",
        "improve",
        "fix",
        "correct",
        "manage",
        "reduce",
        "efficient",
        "identify",
        "verify",
        "support"
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