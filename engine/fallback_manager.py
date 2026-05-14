def fallback_action(case_type):

    fallback_actions = {

        "missing_answer": "skip_question",

        "silence": "retry",

        "background_noise": "retry",

        "language_mixing": "clarify",

        "repeated_answer": "clarify",

        "uncertain_answer": "human_review",

        "poor_audio": "retry",

        "confusing_response": "human_review"
    }

    return fallback_actions.get(case_type, "continue")