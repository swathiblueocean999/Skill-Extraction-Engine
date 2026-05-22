import json

print("Demo Script Generation Started")

script = {
    "intro": "Welcome to the Zecpath AI Hiring System demo.",
    "demo_flow": [
        "Resume Upload",
        "ATS Evaluation",
        "Candidate Screening",
        "HR Analysis",
        "Technical Evaluation",
        "Hiring Recommendation"
    ],
    "closing": "The AI system automates enterprise hiring workflows."
}

with open("presentations/demo_script.json", "w") as f:
    json.dump(script, f, indent=4)

print("Demo Script Generated")