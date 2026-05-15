def get_decision(analysis):

    if analysis["is_vague"]:
        return "clarification_needed"

    if analysis["is_confident"]:
        return "deep_followup"

    return "continue"