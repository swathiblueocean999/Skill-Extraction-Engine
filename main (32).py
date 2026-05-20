import json
import os

from aggregation_engine.role_weights import get_role_weights
from aggregation_engine.aggregator import aggregate_scores

print("\nSTARTING CROSS-ROUND AGGREGATION ENGINE\n")

# =========================
# LOAD DATASETS
# =========================

with open("datasets/ats_scores.json") as f:
    ats_scores = json.load(f)

with open("datasets/screening_scores.json") as f:
    screening_scores = json.load(f)

with open("datasets/hr_scores.json") as f:
    hr_scores = json.load(f)

with open("datasets/technical_scores.json") as f:
    technical_scores = json.load(f)

with open("datasets/machine_test_scores.json") as f:
    machine_test_scores = json.load(f)

# =========================
# ROLE CONFIG
# =========================

role = "Accountant"

weights = get_role_weights(role)

# =========================
# FINAL OUTPUT STORAGE
# =========================

final_results = {}

# =========================
# AGGREGATION
# =========================

for candidate_id in ats_scores.keys():

    candidate_scores = {

        "ats": ats_scores[candidate_id],
        "screening": screening_scores[candidate_id],
        "hr": hr_scores[candidate_id],
        "technical": technical_scores[candidate_id],
        "machine_test": machine_test_scores[candidate_id]

    }

    result = aggregate_scores(candidate_scores, weights)

    final_results[candidate_id] = {

        "ats_score": ats_scores[candidate_id],
        "screening_score": screening_scores[candidate_id],
        "hr_score": hr_scores[candidate_id],
        "technical_score": technical_scores[candidate_id],
        "machine_test_score": machine_test_scores[candidate_id],
        "final_hiring_score": result["final_score"],
        "hiring_fit": result["hiring_fit"]

    }

# =========================
# CREATE OUTPUT FOLDER
# =========================

os.makedirs("outputs", exist_ok=True)

# =========================
# SAVE OUTPUTS
# =========================

with open("outputs/unified_candidate_scores.json", "w") as f:
    json.dump(final_results, f, indent=4)

# =========================
# HIRING FIT REPORT
# =========================

hiring_report = {

    "selected": [],
    "review": [],
    "rejected": []

}

for cid, data in final_results.items():

    if data["hiring_fit"] == "Excellent":
        hiring_report["selected"].append(cid)

    elif data["hiring_fit"] == "Good":
        hiring_report["review"].append(cid)

    else:
        hiring_report["rejected"].append(cid)

with open("outputs/hiring_fit_report.json", "w") as f:
    json.dump(hiring_report, f, indent=4)

# =========================
# SUMMARY
# =========================

summary = {

    "system": "Cross-Round Aggregation Engine",
    "role": role,
    "total_candidates": len(final_results),
    "status": "Completed"

}

with open("outputs/aggregation_summary.json", "w") as f:
    json.dump(summary, f, indent=4)

print("ALL OUTPUTS GENERATED SUCCESSFULLY")
print("System Completed\n")