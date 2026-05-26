import json


def generate_hr_summary():

    with open(
        "output/aptitude_results.json",
        "r",
        encoding="utf-8"
    ) as file:

        results = json.load(file)

    report = []

    for candidate in results:

        score = candidate["aptitude_score"]

        if score >= 85:
            performance = "Excellent"

        elif score >= 70:
            performance = "Strong"

        elif score >= 50:
            performance = "Average"

        else:
            performance = "Weak"

        report.append({
            "candidate_id": candidate["candidate_id"],
            "aptitude_score": score,
            "performance": performance,
            "final_status": candidate["final_status"]
        })

    with open(
        "output/hr_summary_report.json",
        "w",
        encoding="utf-8"
    ) as output:

        json.dump(report, output, indent=2)

    with open(
        "output/hr_summary_report.txt",
        "w",
        encoding="utf-8"
    ) as text_file:

        for item in report:

            text_file.write(
                f"{item['candidate_id']} | "
                f"{item['aptitude_score']} | "
                f"{item['performance']}\n"
            )

    print("HR summary report generated.")