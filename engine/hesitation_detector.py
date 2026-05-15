HESITATION_WORDS = ["umm", "uh", "maybe", "actually", "i think"]

def detect_hesitation(answer):
    answer = answer.lower()

    count = 0

    for word in HESITATION_WORDS:
        count += answer.count(word)

    return count