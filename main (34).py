import json
import os

from report_engine.report_builder import build_candidate_report

print("\nSTARTING HIRING INTELLIGENCE REPORT GENERATOR\n")

# ==========================================
# LOAD DATASETS
# ==========================================

with open("datasets/unified_candidate_scores.json") as f:
    unified_scores = json.load(f)

with open("datasets/final_decision_output.json") as f:
    final_decisions = json.load(f)

# ==========================================
# FINAL REPORT STORAGE
# ==========================================

candidate_reports = {}

# ==========================================
# PROCESS CANDIDATES
# ==========================================

for cid, score_data in unified_scores.items():

    decision_data = final_decisions[cid]

    merged_data = {

        **score_data,

        "behavioral_score":
        decision_data["behavioral_score"],

        "integrity_score":
        decision_data["integrity_score"],

        "final_decision":
        decision_data["final_decision"]

    }

    report = build_candidate_report(
        merged_data
    )

    candidate_reports[cid] = report

# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

os.makedirs("outputs", exist_ok=True)

# ==========================================
# SAVE RECRUITER REPORT
# ==========================================

with open("outputs/recruiter_report.json", "w") as f:
    json.dump(candidate_reports, f, indent=4)

# ==========================================
# SAVE AI PROFILE REPORT
# ==========================================

with open("outputs/candidate_ai_profiles.json", "w") as f:
    json.dump(candidate_reports, f, indent=4)

# ==========================================
# SAVE SUMMARY
# ==========================================

summary = {

    "system": "Hiring Intelligence Report Generator",

    "total_candidates": len(candidate_reports),

    "status": "Completed"

}

with open("outputs/report_summary.json", "w") as f:
    json.dump(summary, f, indent=4)

# ==========================================
# TERMINAL OUTPUT
# ==========================================

print("ALL REPORTS GENERATED SUCCESSFULLY")
print("HIRING INTELLIGENCE REPORT GENERATOR COMPLETED\n")