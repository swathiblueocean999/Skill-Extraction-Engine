import json

print("Confidence Improvement Started")

data = {
    "speaker_confidence": "High",
    "demo_delivery": "Professional",
    "communication_quality": "Excellent"
}

with open(
    "demo_outputs/confidence_report.json",
    "w"
) as f:
    json.dump(data, f, indent=4)

print("Confidence Improvement Completed")