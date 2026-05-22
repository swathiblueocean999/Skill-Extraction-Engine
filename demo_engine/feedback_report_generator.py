import json

print("Feedback Report Generation Started")

feedback = {
    "mentor_feedback": "Very Good",
    "stakeholder_feedback": "Professional",
    "system_impression": "Enterprise Ready",
    "improvement_needed": "Minor"
}

with open(
    "demo_outputs/final_feedback_report.json",
    "w"
) as f:
    json.dump(feedback, f, indent=4)

print("Feedback Report Generated")