def debug_scoring(candidate):

    score = candidate["final_hiring_score"]

    if score > 100:

        return "Invalid Score Detected"

    if score < 0:

        return "Negative Score Error"

    return "Scoring Stable"