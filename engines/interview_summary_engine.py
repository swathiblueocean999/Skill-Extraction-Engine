
import json
import os


class InterviewSummaryEngine:

    def __init__(self):

        self.strength_keywords = [
            "analyze",
            "solve",
            "professional",
            "efficient",
            "decision",
            "support",
            "communicate",
            "lead",
            "improve",
            "manage"
        ]

        self.weakness_keywords = [
            "confused",
            "delay",
            "mistake",
            "problem",
            "stress",
            "risk",
            "slow",
            "unclear"
        ]

        self.cultural_fit_keywords = [
            "team",
            "support",
            "respectfully",
            "professional",
            "customer",
            "collaboration",
            "responsibly"
        ]

    def detect_keywords(self, text, keywords):

        matched = []

        text = text.lower()

        for keyword in keywords:

            if keyword in text:
                matched.append(keyword)

        return matched

    def generate_summary(self, candidate):

        answer = candidate.get("answer", "")

        candidate_id = candidate.get("candidate_id")

        strengths = self.detect_keywords(
            answer,
            self.strength_keywords
        )

        weaknesses = self.detect_keywords(
            answer,
            self.weakness_keywords
        )

        cultural_fit = self.detect_keywords(
            answer,
            self.cultural_fit_keywords
        )

        risk_flags = []

        if len(answer.split()) < 10:
            risk_flags.append("Short response")

        if len(strengths) < 2:
            risk_flags.append("Low reasoning depth")

        if "professional" not in answer.lower():
            risk_flags.append("Professional communication missing")

        inconsistencies = []

        if "immediately" in answer.lower() and "carefully" not in answer.lower():
            inconsistencies.append(
                "Fast action mentioned without careful verification"
            )

        if "decision" in answer.lower() and "analyze" not in answer.lower():
            inconsistencies.append(
                "Decision mentioned without analysis"
            )

        # OVERALL PERFORMANCE

        total_score = (
            len(strengths) * 10 +
            len(cultural_fit) * 10 -
            len(weaknesses) * 5
        )

        if total_score >= 60:
            performance = "Excellent"

        elif total_score >= 35:
            performance = "Good"

        elif total_score >= 20:
            performance = "Average"

        else:
            performance = "Weak"

        # NATURAL LANGUAGE REPORT

        report = f"""
Candidate {candidate_id} demonstrated {performance.lower()} interview performance.
The candidate showed strengths in {', '.join(strengths) if strengths else 'basic communication'}.
Cultural fit indicators include {', '.join(cultural_fit) if cultural_fit else 'limited collaboration signals'}.
Potential weaknesses include {', '.join(weaknesses) if weaknesses else 'no major weaknesses detected'}.
Risk flags identified: {', '.join(risk_flags) if risk_flags else 'No major risks'}.
"""

        return {

            "candidate_id": candidate_id,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "cultural_fit": cultural_fit,

            "risk_flags": risk_flags,

            "inconsistencies": inconsistencies,

            "overall_hr_performance": performance,

            "natural_language_report": report.strip()
        }


def run_interview_summary_engine():

    input_file = "data/candidate_answers.json"

    output_json = "outputs/interview_summary_report.json"

    output_text = "outputs/hr_final_report.txt"

    if not os.path.exists(input_file):

        print(f"ERROR: {input_file} not found")
        return

    with open(input_file, "r", encoding="utf-8") as file:

        candidates = json.load(file)

    engine = InterviewSummaryEngine()

    reports = []

    final_text_report = []

    for candidate in candidates:

        summary = engine.generate_summary(candidate)

        reports.append(summary)

        final_text_report.append(
            "=" * 60
        )

        final_text_report.append(
            f"CANDIDATE ID: {summary['candidate_id']}"
        )

        final_text_report.append(
            f"OVERALL PERFORMANCE: {summary['overall_hr_performance']}"
        )

        final_text_report.append(
            f"STRENGTHS: {', '.join(summary['strengths'])}"
        )

        final_text_report.append(
            f"WEAKNESSES: {', '.join(summary['weaknesses'])}"
        )

        final_text_report.append(
            f"CULTURAL FIT: {', '.join(summary['cultural_fit'])}"
        )

        final_text_report.append(
            f"RISK FLAGS: {', '.join(summary['risk_flags'])}"
        )

        final_text_report.append(
            f"INCONSISTENCIES: {', '.join(summary['inconsistencies'])}"
        )

        final_text_report.append(
            f"REPORT: {summary['natural_language_report']}"
        )

        final_text_report.append("\n")

    os.makedirs("outputs", exist_ok=True)

    # SAVE JSON REPORT

    with open(output_json, "w", encoding="utf-8") as json_file:

        json.dump(reports, json_file, indent=2)

    # SAVE TEXT REPORT

    with open(output_text, "w", encoding="utf-8") as text_file:

        text_file.write("\n".join(final_text_report))

    print("\nInterview Summary Generator Completed Successfully.\n")

    print(f"JSON Report Saved : {output_json}")

    print(f"Text Report Saved : {output_text}")


if __name__ == "__main__":

    run_interview_summary_engine()

