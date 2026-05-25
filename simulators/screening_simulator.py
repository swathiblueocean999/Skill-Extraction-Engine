import json

def run_screening():

    with open(
        "outputs/ats_demo_results.json"
    ) as file:

        ats_results = json.load(file)

    shortlisted = []

    for candidate in ats_results:

        if candidate["ats_score"] >= 60:

            shortlisted.append(candidate)

    with open(
        "outputs/screening_demo_results.json",
        "w"
    ) as file:

        json.dump(shortlisted, file, indent=4)

    print("Screening Simulation Completed")