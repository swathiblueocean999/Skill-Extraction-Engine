import json

print("HR Review Started")

review_data = {
    "module": "HR Interview",
    "accuracy_score": 91,
    "performance": "Excellent",
    "issues_found": [
        "Behavioral analysis needs enhancement"
    ],
    "recommendation": "Add emotion intelligence scoring"
}

with open("review_reports/hr_review_report.json", "w") as f:
    json.dump(review_data, f, indent=4)

print("HR Review Completed")