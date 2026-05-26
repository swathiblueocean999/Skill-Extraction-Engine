import json


def generate_interview_summary():

    with open(
        "output/aptitude_results.json",
        "r",
        encoding="utf-8"
    ) as file:

        results = json.load(file)

    summary = []

    for candidate in results:

        summary.append({
            "candidate_id": candidate["candidate_id"],
            "question_id": candidate["question_id"],
            "aptitude_score": candidate["aptitude_score"],
            "final_status": candidate["final_status"]
        })

    with open(
        "output/interview_summary_report.json",
        "w",
        encoding="utf-8"
    ) as output:

        json.dump(summary, output, indent=2)

    print("Interview summary report generated.")