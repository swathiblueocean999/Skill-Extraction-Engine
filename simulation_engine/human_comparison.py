def compare_human_vs_ai(candidate):

    ai_score = candidate["final_hiring_score"]

    if ai_score >= 85:

        human_decision = "Selected"

    elif ai_score >= 70:

        human_decision = "Hold / Review"

    else:

        human_decision = "Rejected"

    ai_decision = candidate["final_decision"]

    if human_decision == ai_decision:

        return "AI & Human Decision Match"

    return "Decision Mismatch Detected"