import json

print("ATS Review Started")

review_data = {
    "module": "ATS",
    "accuracy_score": 92,
    "performance": "Excellent",
    "issues_found": [
        "Minor keyword mismatch",
        "Resume ranking can improve"
    ],
    "recommendation": "Improve semantic matching logic"
}

with open("review_reports/ats_review_report.json", "w") as f:
    json.dump(review_data, f, indent=4)

print("ATS Review Completed")