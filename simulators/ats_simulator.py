import json

def run_ats():

    with open(
        "datasets/resumes/generated_100_candidates.json"
    ) as file:

        candidates = json.load(file)

    results = []

    for candidate in candidates:

        ats_score = candidate["score"]

        results.append({
            "candidate_id": candidate["candidate_id"],
            "ats_score": ats_score,
            "status": (
                "Selected"
                if ats_score >= 70
                else "Rejected"
            )
        })

    with open(
        "outputs/ats_demo_results.json",
        "w"
    ) as file:

        json.dump(results, file, indent=4)

    print("ATS Simulation Completed")