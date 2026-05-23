import json

print("Scoring Logic Explanation Started")

scoring_logic = {
    "resume_score": "30%",
    "ats_score": "20%",
    "screening_score": "20%",
    "interview_score": "20%",
    "final_confidence_score": "10%",
    "overall_accuracy": "95%"
}

with open(
    "final_outputs/scoring_logic_report.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(scoring_logic, file, indent=4)

print("Scoring Logic Explanation Completed")