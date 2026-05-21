import json

print("Interview Simulation Started")

# Load Screening Results
with open("outputs/screening_demo_results.json", "r") as f:
    screening_results = json.load(f)

interview_results = []

for candidate in screening_results:

    screening_score = candidate["screening_score"]

    if screening_score >= 85:
        interview_score = 92
        result = "Selected"

    elif screening_score >= 70:
        interview_score = 76
        result = "On Hold"

    else:
        interview_score = 58
        result = "Rejected"

    interview_results.append({
        "candidate_id": candidate["candidate_id"],
        "name": candidate["name"],
        "screening_score": screening_score,
        "interview_score": interview_score,
        "final_result": result
    })

# Save Results
with open("outputs/interview_demo_results.json", "w") as f:
    json.dump(interview_results, f, indent=4)

print("Interview Simulation Completed")