import json

print("Screening Simulation Started")

# Load ATS Results
with open("outputs/ats_demo_results.json", "r") as f:
    ats_results = json.load(f)

screening_results = []

for candidate in ats_results:

    ats_score = candidate["ats_score"]

    if ats_score >= 85:
        screening_score = 90
        status = "Shortlisted"

    elif ats_score >= 70:
        screening_score = 75
        status = "Average"

    else:
        screening_score = 55
        status = "Rejected"

    screening_results.append({
        "candidate_id": candidate["candidate_id"],
        "name": candidate["name"],
        "ats_score": ats_score,
        "screening_score": screening_score,
        "screening_status": status
    })

# Save Results
with open("outputs/screening_demo_results.json", "w") as f:
    json.dump(screening_results, f, indent=4)

print("Screening Simulation Completed")