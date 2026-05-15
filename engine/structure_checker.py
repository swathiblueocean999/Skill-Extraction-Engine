def check_structure(answer):

    structure_words = [
        "first",
        "second",
        "finally",
        "before",
        "after",
        "then",
        "because",
        "approach",
        "immediately"
    ]

    detected = []

    for word in structure_words:
        if word.lower() in answer.lower():
            detected.append(word)

    score = min(len(detected) * 15, 100)

    return {
        "score": score,
        "structure_detected": detected
    }