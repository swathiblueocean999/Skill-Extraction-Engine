def validate_conversation(candidate):

    if candidate["hr_score"] < 40:

        return "Weak Conversation Flow"

    return "Conversation Logic Stable"