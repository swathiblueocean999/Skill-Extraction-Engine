import json
import os

from decision_engine.recommendation_engine import generate_recommendation

print("\nSTARTING FINAL RECOMMENDATION AI\n")

# =====================================
# LOAD DATASETS
# =====================================

with open("datasets/unified_candidate_scores.json", "r") as f:
    candidate_scores = json.load(f)

with open("datasets/behavioral_scores.json", "r") as f:
    behavioral_scores = json.load(f)

with open("datasets/integrity_scores.json", "r") as f:
    integrity_scores = json.load(f)

# =====================================
# FINAL OUTPUT STORAGE
# =====================================

final_output = {}

# =====================================
# PROCESS CANDIDATES
# =====================================

for cid, data in candidate_scores.items():

    hiring_score = data["final_hiring_score"]

    behavior_score = behavioral_scores[cid]

    integrity_score = integrity_scores[cid]

    result = generate_recommendation(
        hiring_score,
        behavior_score,
        integrity_score
    )

    final_output[cid] = {

        "ats_score": data["ats_score"],

        "screening_score": data["screening_score"],

        "hr_score": data["hr_score"],

        "technical_score": data["technical_score"],

        "machine_test_score": data["machine_test_score"],

        "final_hiring_score": hiring_score,

        "behavioral_score": behavior_score,

        "integrity_score": integrity_score,

        "hiring_fit": data["hiring_fit"],

        "final_decision": result["decision"],

        "confidence_score": result["confidence_score"],

        "risk_factor": result["risk_factor"]

    }

# =====================================
# CREATE OUTPUT DIRECTORY
# =====================================

os.makedirs("outputs", exist_ok=True)

# =====================================
# SAVE FINAL DECISION OUTPUT
# =====================================

with open("outputs/final_decision_output.json", "w") as f:
    json.dump(final_output, f, indent=4)

# =====================================
# CREATE DECISION REPORT
# =====================================

decision_report = {

    "Selected": [],
    "Hold / Review": [],
    "Rejected": []

}

for cid, result in final_output.items():

    decision = result["final_decision"]

    decision_report[decision].append(cid)

with open("outputs/decision_report.json", "w") as f:
    json.dump(decision_report, f, indent=4)

# =====================================
# CREATE SUMMARY REPORT
# =====================================

summary = {

    "system": "Final Recommendation AI",

    "total_candidates": len(final_output),

    "selected_count": len(decision_report["Selected"]),

    "review_count": len(decision_report["Hold / Review"]),

    "rejected_count": len(decision_report["Rejected"]),

    "status": "Completed"

}

with open("outputs/recommendation_summary.json", "w") as f:
    json.dump(summary, f, indent=4)

# =====================================
# TERMINAL OUTPUT
# =====================================

print("ALL OUTPUTS GENERATED SUCCESSFULLY\n")

print("FINAL DECISION OUTPUT SAVED")
print("DECISION REPORT GENERATED")
print("SUMMARY REPORT GENERATED\n")

print("FINAL RECOMMENDATION AI COMPLETED\n")