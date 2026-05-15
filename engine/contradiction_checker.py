def detect_contradiction(answer):
    answer = answer.lower()

    positive = "handled" in answer or "worked" in answer
    negative = "never worked" in answer or "no experience" in answer

    return positive and negative