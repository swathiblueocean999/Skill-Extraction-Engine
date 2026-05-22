import json

print("Explanation Review Started")

review = {
    "weak_areas": [
        "Technical scoring explanation",
        "ATS filtering logic"
    ],
    "improvement_status": "Improved",
    "presentation_clarity": "Enhanced"
}

with open(
    "demo_outputs/explanation_review.json",
    "w"
) as f:
    json.dump(review, f, indent=4)

print("Explanation Review Completed")