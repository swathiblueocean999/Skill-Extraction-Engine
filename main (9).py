import json
from utils.scorer import score_answer
from utils.normalizer import normalize_scores
from utils.aggregator import aggregate_score
from utils.explainer import generate_explanation

# Load data
with open("data/structured_answers.json") as f:
    data = json.load(f)

results = []

for item in data:
    scores = score_answer(item)
    normalized = normalize_scores(scores)
    total = aggregate_score(normalized)
    explanation = generate_explanation(item, total)

    result = {
        "candidate_id": item["candidate_id"],
        "scores": normalized,
        "total_score": total,
        "explanation": explanation
    }

    results.append(result)

# Save output
with open("output/final_scores.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Scoring Engine Completed")