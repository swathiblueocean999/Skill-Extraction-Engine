import json
import os


class AptitudeEngine:

    def __init__(self):

        self.strong_keywords = [
            "analyze",
            "compare",
            "verify",
            "decision",
            "professional",
            "efficiently",
            "solution",
            "improve",
            "leadership",
            "responsible",
            "prioritize",
            "communicate",
            "identify",
            "resolve",
            "manage",
            "support",
            "team",
            "problem",
            "customer",
            "workflow"
        ]

        self.average_keywords = [
            "work",
            "task",
            "help",
            "issue",
            "approach",
            "understand",
            "carefully"
        ]

        self.weak_keywords = [
            "maybe",
            "guess",
            "probably",
            "not sure",
            "try"
        ]

    def analyze_answer(self, answer):

        answer_lower = answer.lower()

        strong_hits = sum(
            1 for word in self.strong_keywords
            if word in answer_lower
        )

        average_hits = sum(
            1 for word in self.average_keywords
            if word in answer_lower
        )

        weak_hits = sum(
            1 for word in self.weak_keywords
            if word in answer_lower
        )

        score = (
            strong_hits * 15 +
            average_hits * 8 -
            weak_hits * 5
        )

        word_count = len(answer.split())

        if word_count >= 30:
            score += 20

        elif word_count >= 20:
            score += 15

        elif word_count >= 12:
            score += 10

        score = max(0, min(score, 100))

        if score >= 60:
            status = "STRONG"

        elif score >= 35:
            status = "AVERAGE"

        else:
            status = "WEAK"

        return {
            "analysis": {
                "strong_hits": strong_hits,
                "average_hits": average_hits,
                "weak_hits": weak_hits,
                "word_count": word_count
            },

            "aptitude_score": score,
            "final_status": status
        }


def run_aptitude_engine():

    input_file = "data/candidate_answers.json"

    output_file = "output/aptitude_results.json"

    if not os.path.exists(input_file):
        print(f"ERROR: {input_file} not found")
        return

    with open(input_file, "r", encoding="utf-8") as file:
        candidates = json.load(file)

    engine = AptitudeEngine()

    results = []

    for candidate in candidates:

        answer = candidate.get("answer", "")

        analysis_result = engine.analyze_answer(answer)

        result = {
            "candidate_id": candidate.get("candidate_id"),
            "question_id": candidate.get("question_id"),
            "answer": answer,
            "analysis": analysis_result["analysis"],
            "aptitude_score": analysis_result["aptitude_score"],
            "final_status": analysis_result["final_status"]
        }

        results.append(result)

    os.makedirs("output", exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as output:
        json.dump(results, output, indent=4)

    strong_count = len(
        [r for r in results if r["final_status"] == "STRONG"]
    )

    average_count = len(
        [r for r in results if r["final_status"] == "AVERAGE"]
    )

    weak_count = len(
        [r for r in results if r["final_status"] == "WEAK"]
    )

    print("\n===== SUMMARY =====")
    print(f"Strong Candidates : {strong_count}")
    print(f"Average Candidates: {average_count}")
    print(f"Weak Candidates   : {weak_count}")
    print("===================")

    print("\n=======================================================")
    print(" Aptitude analysis completed successfully.")
    print(" Results generated inside output folder.")
    print("=======================================================")