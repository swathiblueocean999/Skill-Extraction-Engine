def detect_stress(answer):
    answer = answer.lower()

    stress_words = [
        "stress",
        "confused",
        "nervous",
        "pressure"
    ]

    for word in stress_words:
        if word in answer:
            return True

    return False