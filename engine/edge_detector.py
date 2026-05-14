def detect_edge_case(answer):

    text = answer.lower().strip()

    # missing answer
    if text == "":
        return "missing_answer"

    # silence
    if text == "...":
        return "silence"

    # background noise
    if "umm" in text or "noise" in text:
        return "background_noise"

    # language mixing
    if any(ord(char) > 128 for char in text):
        return "language_mixing"

    # poor audio
    if text == "asdfghjkl":
        return "poor_audio"

    # uncertain answer
    if "don't know" in text or "not sure" in text or "maybe" in text:
        return "uncertain_answer"

    # repeated words detection
    words = text.split()

    repeated = False

    for word in words:
        if words.count(word) >= 3:
            repeated = True

    if repeated:
        return "repeated_answer"

    # confusing long response
    if len(words) > 15:
        return "confusing_response"

    return "normal"