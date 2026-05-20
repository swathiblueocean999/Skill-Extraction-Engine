def validate_edge_cases(candidate):

    score = candidate["final_hiring_score"]

    if score == 0:

        return "Zero Score Edge Case"

    if score == 100:

        return "Perfect Score Edge Case"

    if score < 50:

        return "Low Score Edge Case"

    return "Normal Candidate Flow"