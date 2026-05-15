def evaluate_structure(answer):

    words = answer.split()

    score = 30

    if len(words) >= 5:
        score += 20

    if len(words) >= 10:
        score += 20

    if "." in answer or "," in answer:
        score += 10

    if "and" in answer.lower():
        score += 10

    return min(score, 100)