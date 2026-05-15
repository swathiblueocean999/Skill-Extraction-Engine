def generate_followup(question, analysis):

    if analysis["is_vague"]:

        return {
            "type": "clarification",
            "question":
            f"Could you explain more about {question}?"
        }

    if analysis["is_confident"]:

        return {
            "type": "deep_probe",
            "question":
            "Can you provide a real example?"
        }

    return {
        "type": "none",
        "question": None
    }