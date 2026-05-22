import json
import os

print("Mock Demo Session Started")

os.makedirs("demo_outputs", exist_ok=True)

data = {
    "demo_status": "Completed",
    "system_flow": [
        "ATS",
        "Screening",
        "HR",
        "Technical",
        "Decision"
    ],
    "demo_quality": "Professional"
}

with open(
    "demo_outputs/mock_demo_report.json",
    "w"
) as f:
    json.dump(data, f, indent=4)

print("Mock Demo Session Completed")