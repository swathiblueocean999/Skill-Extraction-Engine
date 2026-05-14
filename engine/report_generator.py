def generate_report(candidate_id, analysis, score, confidence):

    # default status
    final_status = "reject"

    # good candidate
    if score >= 70:
        final_status = "good"

    # average candidate
    elif score >= 15:
        final_status = "average"

    # final report object
    return {
        "candidate_id": candidate_id,
        "analysis": analysis,
        "screening_score": score,
        "confidence": confidence,
        "final_status": final_status
    }