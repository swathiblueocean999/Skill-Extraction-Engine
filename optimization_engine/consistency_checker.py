def check_consistency(candidate):

    scores = [

        candidate["ats_score"],
        candidate["screening_score"],
        candidate["hr_score"],
        candidate["technical_score"],
        candidate["machine_test_score"]

    ]

    difference = max(scores) - min(scores)

    if difference <= 20:

        return "Highly Consistent"

    elif difference <= 40:

        return "Moderately Consistent"

    return "Inconsistent Performance"