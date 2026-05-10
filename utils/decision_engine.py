def decide_next_step(state, answer):
    text = answer.lower().strip()

    # Silence
    if text == "":
        return "silence"

    # Confusion
    confusion_words = ["don't know", "not sure", "maybe"]
    if any(w in text for w in confusion_words):
        return "confusion"

    # Repeat detection (simple)
    if answer in state.answers:
        return "repeat"

    return "valid"