def calculate_score(metrics, weights):
    """
    Generic Machine Test Score Calculator
    """

    score = (
        metrics["correctness"] * weights["correctness"] +
        metrics["efficiency"] * weights["efficiency"] +
        metrics["code_quality"] * weights["code_quality"] +
        metrics["problem_solving"] * weights["problem_solving"] +
        metrics["time_score"] * weights["time_score"]
    )

    return round(score, 2)