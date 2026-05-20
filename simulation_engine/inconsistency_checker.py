def detect_inconsistency(candidate):

    scores = [

        candidate["ats_score"],
        candidate["screening_score"],
        candidate["hr_score"],
        candidate["technical_score"],
        candidate["machine_test_score"]

    ]

    difference = max(scores) - min(scores)

    if difference > 40:

        return "High Inconsistency"

    elif difference > 20:

        return "Moderate Inconsistency"

    return "Stable Evaluation"