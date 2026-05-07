import json

# Load weights
with open("config/scoring_weights.json") as f:
    WEIGHTS = json.load(f)

def aggregate_score(normalized_scores):
    total = 0

    # Weighted sum calculation
    for key, value in normalized_scores.items():
        weight = WEIGHTS.get(key, 0)
        total += value * weight

    # 🔥 Convert to percentage (0–100 scale)
    final_score = total * 10

    return round(final_score, 2)