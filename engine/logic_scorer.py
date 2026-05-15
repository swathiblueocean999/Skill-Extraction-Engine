def calculate_logic_score(analysis):

    reasoning = analysis["reasoning"]["score"]
    scenario = analysis["scenario"]["score"]
    clarity = analysis["clarity"]["score"]
    structure = analysis["structure"]["score"]
    problem_solving = analysis["problem_solving"]["score"]
    decision = analysis["decision"]["score"]

    final_score = (
        reasoning * 0.20 +
        scenario * 0.20 +
        clarity * 0.15 +
        structure * 0.10 +
        problem_solving * 0.20 +
        decision * 0.15
    )

    return round(final_score, 2)