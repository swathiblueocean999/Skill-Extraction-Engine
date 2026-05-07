def format_output(candidate_id, answer, intents, entities, issues):
    return {
        "candidate_id": candidate_id,
        "raw_answer": answer,
        "intents": intents,
        "entities": {
            "experience": entities.get("experience"),
            "salary": entities.get("salary"),
            "skills": entities.get("skills"),
            "availability": entities.get("availability")
        },
        "issues": issues,
        "status": "valid" if not issues else "needs_review"
    }