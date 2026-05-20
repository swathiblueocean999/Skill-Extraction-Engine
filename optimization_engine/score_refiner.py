import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

scores_path = os.path.join(BASE_DIR, "input_data", "candidate_scores.json")
output_path = os.path.join(BASE_DIR, "output", "refined_scores.json")

with open(scores_path, "r", encoding="utf-8") as f:
    scores = json.load(f)

refined = {}

for cid, score in scores.items():

    if score > 85:
        score -= 2

    elif score < 55:
        score += 3

    refined[cid] = round(score, 2)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(refined, f, indent=4)

print("✅ Score Refinement Completed")