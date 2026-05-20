def normalize_score(score):

    if score > 100:
        return 100

    if score < 0:
        return 0

    return round(score, 2)