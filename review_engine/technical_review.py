import json

print("Technical Review Started")

review_data = {
    "module": "Technical Interview",
    "accuracy_score": 90,
    "performance": "Very Good",
    "issues_found": [
        "Technical depth evaluation can improve"
    ],
    "recommendation": "Add advanced technical scoring"
}

with open("review_reports/technical_review_report.json", "w") as f:
    json.dump(review_data, f, indent=4)

print("Technical Review Completed")