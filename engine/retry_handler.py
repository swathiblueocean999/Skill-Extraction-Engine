def retry_logic(case_type):

    retry_messages = {

        "missing_answer":
        "Could you please answer the question?",

        "silence":
        "I could not hear anything. Please respond again.",

        "background_noise":
        "There seems to be background noise. Please speak clearly.",

        "language_mixing":
        "Please respond using one language.",

        "repeated_answer":
        "Your response seems repeated. Please explain clearly.",

        "uncertain_answer":
        "Please provide a confident answer if possible.",

        "poor_audio":
        "Audio quality is unclear. Please repeat your answer.",

        "confusing_response":
        "Your response is unclear. Please simplify your answer."
    }

    return retry_messages.get(case_type, "Proceed")