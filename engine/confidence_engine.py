def confidence_level(answer):

    words = len(answer.split())

    text = answer.lower()

    if text == "":
        return "low"

    if "maybe" in text or "not sure" in text:
        return "low"

    if words >= 10:
        return "high"

    if words >= 5:
        return "medium"

    return "low"