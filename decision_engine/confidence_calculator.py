def calculate_confidence(score, behavior, integrity):

    confidence = (
        score * 0.5 +
        behavior * 0.2 +
        integrity * 0.3
    )

    return round(confidence, 2)