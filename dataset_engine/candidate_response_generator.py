import json

responses = [

    {
        "candidate_id": "C101",
        "communication": "Excellent",
        "technical_response": "Advanced",
        "confidence": "High",
        "behavior": "Professional"
    },

    {
        "candidate_id": "C201",
        "communication": "Good",
        "technical_response": "Intermediate",
        "confidence": "Moderate",
        "behavior": "Stable"
    },

    {
        "candidate_id": "C301",
        "communication": "Basic",
        "technical_response": "Beginner",
        "confidence": "Low",
        "behavior": "Nervous"
    }
]

with open("datasets/demo_candidate_responses.json", "w") as f:
    json.dump(responses, f, indent=4)

print("Candidate Responses Generated")