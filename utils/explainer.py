def generate_explanation(answer_obj, total_score):
    if "off_topic" in answer_obj["issues"]:
        return "Answer is off-topic and not relevant."

    if answer_obj["issues"]:
        return "Answer has missing or unclear details."

    if total_score > 8:
        return "Strong and relevant answer."

    return "Average response quality."