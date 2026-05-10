def generate_followup(question_id):
    followups = {
        "Q0": "Could you briefly summarize your background and key strengths?",
        "Q1": "How many years of experience do you have?",
        "Q2": "Can you name specific tools or technologies?",
        "Q3": "What was the outcome of that situation?",
        "Q4": "What attracted you to this role?",
        "Q5": "Could you provide a salary range?",
        "Q6": "Are you available immediately or after notice period?"
    }

    return followups.get(question_id, "")