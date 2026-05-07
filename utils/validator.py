def validate_answer(intents, entities, answer):
    issues = []

    # Off-topic detection
    if not intents:
        issues.append("off_topic")

    # Missing experience
    if "experience" in intents and not entities.get("experience"):
        issues.append("missing_experience")

    # Missing salary
    if "salary" in intents and not entities.get("salary"):
        issues.append("missing_salary")

    # Missing skills
    if "skills" in intents and not entities.get("skills"):
        issues.append("missing_skills")

    # Vague answer detection
    vague_words = ["some", "few", "many"]
    if any(word in answer.lower() for word in vague_words):
        issues.append("vague_answer")

    return issues