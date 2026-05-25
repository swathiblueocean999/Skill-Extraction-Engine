import json
import random

def run_interview():

    with open(
        "outputs/ats_demo_results.json"
    ) as file:

        candidates = json.load(file)

    results = []

    for candidate in candidates:

        if candidate["status"] == "Selected":

            interview_score = random.randint(60, 100)

        else:

            interview_score = random.randint(40, 59)

        results.append({

            "candidate_id":
            candidate["candidate_id"],

            "interview_score":
            interview_score
        })

    with open(
        "outputs/interview_demo_results.json",
        "w"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )

    print("Interview Simulation Completed")