def normalize_score(score, question_count):

    if question_count >= 8:
        return round(score, 2)

    adjustment = (8 - question_count) * 1.5

    return round(score + adjustment, 2)