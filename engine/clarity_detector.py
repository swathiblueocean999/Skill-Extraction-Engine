def check_clarity(answer):

    words = answer.split()

    word_count = len(words)

    if word_count >= 25:
        score = 100

    elif word_count >= 18:
        score = 85

    elif word_count >= 12:
        score = 70

    elif word_count >= 8:
        score = 50

    else:
        score = 25

    return {
        "score": score,
        "word_count": word_count
    }