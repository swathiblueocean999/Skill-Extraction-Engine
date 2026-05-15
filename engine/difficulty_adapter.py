def get_difficulty_level(analysis):

    if analysis["is_confident"]:
        return "advanced"

    if analysis["is_vague"]:
        return "basic"

    return "medium"