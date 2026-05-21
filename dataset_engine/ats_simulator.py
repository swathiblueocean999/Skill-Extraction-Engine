import json
import random

print("ATS Simulation Started")

with open("datasets/unified_candidate_scores.json", "r") as f:
    candidates = json.load(f)

ats_results = []

for candidate in candidates:

    strength = candidate["candidate_strength"]

    if strength == "Strong":
        ats_score = random.randint(85, 98)
        status = "Selected"

    elif strength == "Average":
        ats_score = random.randint(60, 84)
        status = "Review"

    else:
        ats_score = random.randint(35, 59)
        status = "Rejected"

    ats_results.append({
        "candidate_id": candidate["candidate_id"],
        "name": candidate["name"],
        "ats_score": ats_score,
        "status": status
    })

with open("outputs/ats_demo_results.json", "w") as f:
    json.dump(ats_results, f, indent=4)

print("ATS Simulation Completed")