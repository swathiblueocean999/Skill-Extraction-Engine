import json

with open("config/intent_keywords.json") as f:
    KEYWORDS = json.load(f)

def classify_intent(answer):
    answer = answer.lower()
    intents = []

    for intent, words in KEYWORDS.items():
        for w in words:
            if w in answer:
                intents.append(intent)
                break

    return list(set(intents))