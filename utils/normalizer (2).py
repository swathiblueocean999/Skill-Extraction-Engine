def normalize_scores(score_dict):
    return {k: round(v * 10, 2) for k, v in score_dict.items()}