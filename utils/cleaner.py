import re

def clean_text(text):
    if not text:
        return "", "no speech detected"

    # lowercase
    text = text.lower()

    # remove fillers
    fillers = ["um", "uh", "like", "you know"]
    for f in fillers:
        text = re.sub(rf"\b{f}\b", "", text)

    # remove punctuation (keep numbers & words)
    text = re.sub(r"[^\w\s]", "", text)

    # remove extra spaces
    text = " ".join(text.split())

    # capitalize + add full stop
    text = text.capitalize() + "."

    return text, "cleaned"