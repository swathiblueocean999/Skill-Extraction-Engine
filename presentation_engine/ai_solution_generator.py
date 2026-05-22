import json

print("AI Solution Generation Started")

data = {
    "solution": "AI-powered hiring automation system",
    "features": [
        "ATS Simulation",
        "Candidate Screening",
        "HR Evaluation",
        "Technical Assessment",
        "Final Hiring Decision"
    ],
    "automation_level": "High"
}

with open("presentations/system_architecture.json", "w") as f:
    json.dump(data, f, indent=4)

print("AI Solution Generated")