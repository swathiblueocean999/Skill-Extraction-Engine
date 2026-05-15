POSITIVE_WORDS = [
    "confidently",
    "comfortable",
    "successfully",
    "managed"
]

NEGATIVE_WORDS = [
    "not sure",
    "confused",
    "difficult",
    "stress"
]

def analyze_sentiment(answer):
    answer = answer.lower()

    positive = 0
    negative = 0

    for word in POSITIVE_WORDS:
        if word in answer:
            positive += 1

    for word in NEGATIVE_WORDS:
        if word in answer:
            negative += 1

    if positive > negative:
        return "positive"

    if negative > positive:
        return "negative"

    return "neutral"