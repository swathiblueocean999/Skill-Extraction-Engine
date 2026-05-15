def analyze_response(answer):

    answer = answer.lower()

    vague_words = [
        "nothing",
        "basic",
        "okay",
        "some",
        "little",
        "normal"
    ]

    confident_words = [
        "handled",
        "managed",
        "improved",
        "developed",
        "solved",
        "implemented"
    ]

    result = {
        "is_vague": False,
        "is_confident": False,
        "word_count": len(answer.split())
    }

    if result["word_count"] < 4:
        result["is_vague"] = True

    for word in vague_words:

        if word in answer:
            result["is_vague"] = True

    for word in confident_words:

        if word in answer:
            result["is_confident"] = True

    return result