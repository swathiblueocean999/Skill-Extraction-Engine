UNCERTAIN_PHRASES = [
    "not sure",
    "maybe",
    "i think",
    "probably",
    "little bit"
]

def detect_uncertainty(answer):
    answer = answer.lower()

    for phrase in UNCERTAIN_PHRASES:
        if phrase in answer:
            return True

    return False