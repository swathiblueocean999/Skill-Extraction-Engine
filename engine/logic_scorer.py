def calculate_logic_score(analysis):

    reasoning = analysis["reasoning"]["score"]
    scenario = analysis["scenario"]["score"]
    clarity = analysis["clarity"]["score"]
    structure = analysis["structure"]["score"]
    problem_solving = analysis["problem_solving"]["score"]
    decision = analysis["decision"]["score"]

    final_score = (
        reasoning * 0.22 +
        scenario * 0.18 +
        clarity * 0.15 +
        structure * 0.10 +
        problem_solving * 0.20 +
        decision * 0.15
    )

    normalized_score = round(final_score * 3.5, 2)

    if normalized_score > 100:
        normalized_score = 100

    return normalized_score