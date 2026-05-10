def handle_error(error_type, state):
    if error_type == "silence":
        return "I didn't hear anything. Could you please respond?"

    if error_type == "confusion":
        return "No problem, let me simplify the question."

    if error_type == "repeat":
        return "You already mentioned that. Could you provide more details?"

    return "Let's continue."