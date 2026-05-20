from aggregation_engine.score_normalizer import normalize_score
from aggregation_engine.hiring_fit_calculator import get_hiring_fit


def aggregate_scores(candidate_scores, weights):

    final_score = (

        candidate_scores["ats"] * weights["ats"] +
        candidate_scores["screening"] * weights["screening"] +
        candidate_scores["hr"] * weights["hr"] +
        candidate_scores["technical"] * weights["technical"] +
        candidate_scores["machine_test"] * weights["machine_test"]

    )

    final_score = normalize_score(final_score)

    hiring_fit = get_hiring_fit(final_score)

    return {
        "final_score": final_score,
        "hiring_fit": hiring_fit
    }