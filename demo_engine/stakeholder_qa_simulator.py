import json
import os

print("Stakeholder Q&A Simulation Started")

qa = {
    "questions_answered": 15,
    "confidence_level": "High",
    "clarity_score": "92%",
    "stakeholder_feedback": "Positive"
}

with open(
    "demo_outputs/stakeholder_qa_report.json",
    "w"
) as f:
    json.dump(qa, f, indent=4)

print("Stakeholder Q&A Simulation Completed")