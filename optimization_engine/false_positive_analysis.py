def analyze_false_decisions(candidate):

    score = candidate["final_hiring_score"]

    integrity = candidate["integrity_score"]

    behavioral = candidate["behavioral_score"]

    # ==========================================
    # FALSE POSITIVE CHECK
    # ==========================================

    if score >= 80 and integrity < 60:

        return "Potential False Positive"

    # ==========================================
    # FALSE NEGATIVE CHECK
    # ==========================================

    if score < 70 and integrity >= 80:

        return "Potential False Negative"

    # ==========================================
    # BEHAVIORAL RISK CHECK
    # ==========================================

    if behavioral < 60:

        return "Behavioral Risk Detected"

    return "No Major Issue"