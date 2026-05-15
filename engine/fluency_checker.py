def check_fluency(answer):

    words = answer.split()

    word_count = len(words)

    long_sentences = answer.count(",") + answer.count("and")

    score = 30

    if word_count >= 5:
        score += 20

    if word_count >= 10:
        score += 20

    if word_count >= 15:
        score += 20

    if long_sentences >= 2:
        score += 10

    return min(score, 100)