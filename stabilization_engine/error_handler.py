def handle_errors(candidate):

    required_fields = [

        "ats_score",
        "screening_score",
        "hr_score",
        "technical_score",
        "machine_test_score"

    ]

    missing = []

    for field in required_fields:

        if field not in candidate:

            missing.append(field)

    if missing:

        return {

            "status":
            "Error",

            "missing_fields":
            missing

        }

    return {

        "status":
        "Validated"

    }