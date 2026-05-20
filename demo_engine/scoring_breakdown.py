import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

scores_path = os.path.join(BASE_DIR, "demo_data", "demo_scores.json")

with open(scores_path, "r", encoding="utf-8") as f:
    scores = json.load(f)

print("\n SCORING BREAKDOWN\n")

for cid, score in scores.items():

    if score >= 85:
        fit = "Excellent"

    elif score >= 70:
        fit = "Good"

    elif score >= 50:
        fit = "Average"

    else:
        fit = "Weak"

    print(f"{cid}")
    print(f"Final Unified Score : {score}")
    print(f"Hiring Fit : {fit}")
    print("-" * 40)

print("\n Scoring Breakdown Completed")