from utils.file_handler import load_json, save_json

from engine.hr_score_engine import calculate_hr_score
from engine.score_normalizer import normalize_score
from engine.score_explainer import generate_breakdown

candidates = load_json(
    "data/candidate_hr_data.json"
)

results = []

for candidate in candidates:

    raw_score = calculate_hr_score(candidate)

    normalized = normalize_score(
        raw_score,
        candidate["question_count"]
    )

    breakdown = generate_breakdown(
        candidate,
        normalized
    )

    if normalized >= 75:
        status = "strong"

    elif normalized >= 50:
        status = "average"

    else:
        status = "weak"

    results.append({
        "candidate_id": candidate["candidate_id"],
        "score_breakdown": breakdown,
        "normalized_score": normalized,
        "final_status": status
    })

save_json(
    "output/hr_interview_scores.json",
    results
)

print("HR Interview scoring completed.")