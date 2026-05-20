import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

scores_path = os.path.join(BASE_DIR, "demo_data", "demo_scores.json")

with open(scores_path, "r", encoding="utf-8") as f:
    scores = json.load(f)

print("\n FINAL HIRING RECOMMENDATIONS\n")

for cid, score in scores.items():

    if score >= 85:
        recommendation = "Strong Hire"

    elif score >= 70:
        recommendation = "Hire"

    elif score >= 50:
        recommendation = "Needs Review"

    else:
        recommendation = "Reject"

    print(f"{cid} : {recommendation}")

print("\n Hiring Recommendation Completed")