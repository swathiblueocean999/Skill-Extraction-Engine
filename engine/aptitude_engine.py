import json
import os


class AptitudeEngine:

    def __init__(self):

        self.reasoning_keywords = [
            "analyze",
            "compare",
            "because",
            "reason",
            "identify",
            "verify",
            "understand",
            "approach",
            "prioritize",
            "explain"
        ]

        self.scenario_keywords = [
            "professional",
            "calm",
            "respectfully",
            "support",
            "teamwork",
            "customer",
            "issue",
            "resolve",
            "solution",
            "communicate"
        ]

        self.problem_solving_keywords = [
            "solve",
            "fix",
            "improve",
            "reduce",
            "efficient",
            "correct",
            "manage",
            "identify",
            "verify",
            "support"
        ]

        self.decision_keywords = [
            "decision",
            "select",
            "choose",
            "prioritize",
            "responsibly",
            "carefully",
            "manage",
            "compare"
        ]

        self.structure_words = [
            "first",
            "then",
            "finally",
            "before",
            "after",
            "because",
            "immediately"
        ]

    def detect_keywords(
        self,
        answer,
        keyword_list
    ):

        matched = []

        answer_lower = answer.lower()

        for keyword in keyword_list:

            if keyword in answer_lower:
                matched.append(keyword)

        return matched

    def calculate_score(
        self,
        matched_count,
        multiplier
    ):

        return min(matched_count * multiplier, 100)

    def analyze_answer(self, answer):

        # REASONING
        reasoning_matches = self.detect_keywords(
            answer,
            self.reasoning_keywords
        )

        reasoning_score = self.calculate_score(
            len(reasoning_matches),
            15
        )

        # SCENARIO
        scenario_matches = self.detect_keywords(
            answer,
            self.scenario_keywords
        )

        scenario_score = self.calculate_score(
            len(scenario_matches),
            12
        )

        # PROBLEM SOLVING
        problem_matches = self.detect_keywords(
            answer,
            self.problem_solving_keywords
        )

        problem_score = self.calculate_score(
            len(problem_matches),
            15
        )

        # DECISION
        decision_matches = self.detect_keywords(
            answer,
            self.decision_keywords
        )

        decision_score = self.calculate_score(
            len(decision_matches),
            15
        )

        # STRUCTURE
        structure_matches = self.detect_keywords(
            answer,
            self.structure_words
        )

        structure_score = self.calculate_score(
            len(structure_matches),
            12
        )

        # CLARITY
        word_count = len(answer.split())

        if word_count >= 20:
            clarity_score = 100

        elif word_count >= 15:
            clarity_score = 90

        elif word_count >= 10:
            clarity_score = 80

        elif word_count >= 6:
            clarity_score = 70

        else:
            clarity_score = 50

        # RAW SCORE
        raw_score = (
            reasoning_score * 0.20 +
            scenario_score * 0.20 +
            clarity_score * 0.20 +
            structure_score * 0.10 +
            problem_score * 0.15 +
            decision_score * 0.15
        )

        # BOOSTED FINAL SCORE
        aptitude_score = round(raw_score * 2.2, 2)

        if aptitude_score > 100:
            aptitude_score = 100

        # STATUS
        if aptitude_score >= 65:
            final_status = "strong"

        elif aptitude_score >= 45:
            final_status = "average"

        else:
            final_status = "weak"

        return {

            "analysis": {

                "reasoning": {
                    "score": reasoning_score,
                    "matched_keywords": reasoning_matches
                },

                "scenario": {
                    "score": scenario_score,
                    "matched_keywords": scenario_matches
                },

                "clarity": {
                    "score": clarity_score,
                    "word_count": word_count
                },

                "structure": {
                    "score": structure_score,
                    "structure_detected": structure_matches
                },

                "problem_solving": {
                    "score": problem_score,
                    "matched_keywords": problem_matches
                },

                "decision": {
                    "score": decision_score,
                    "matched_keywords": decision_matches
                }
            },

            "aptitude_score": aptitude_score,
            "final_status": final_status
        }


def run_aptitude_engine():

    input_file = "data/candidate_answers.json"
    output_file = "outputs/aptitude_results.json"

    if not os.path.exists(input_file):

        print(f"ERROR: {input_file} not found")
        return

    with open(
        input_file,
        "r",
        encoding="utf-8"
    ) as file:

        candidates = json.load(file)

    engine = AptitudeEngine()

    results = []

    for candidate in candidates:

        candidate_id = candidate.get("candidate_id")
        question_id = candidate.get("question_id")
        answer = candidate.get("answer", "")

        analysis_result = engine.analyze_answer(answer)

        results.append({

            "candidate_id": candidate_id,
            "question_id": question_id,
            "analysis": analysis_result["analysis"],
            "aptitude_score": analysis_result["aptitude_score"],
            "final_status": analysis_result["final_status"]
        })

    os.makedirs("outputs", exist_ok=True)

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as output:

        json.dump(
            results,
            output,
            indent=2
        )

    print("\nAPTITUDE ANALYSIS COMPLETED")
    print("===================================")
    print(f"Results saved to: {output_file}")

    strong_count = len([
        r for r in results
        if r["final_status"] == "strong"
    ])

    average_count = len([
        r for r in results
        if r["final_status"] == "average"
    ])

    weak_count = len([
        r for r in results
        if r["final_status"] == "weak"
    ])

    print("\n===== SUMMARY =====")
    print(f"Strong Candidates : {strong_count}")
    print(f"Average Candidates: {average_count}")
    print(f"Weak Candidates   : {weak_count}")
    print("===================\n")

    print("=======================================================")
    print(" Aptitude analysis completed successfully.")
    print(" Results generated inside outputs folder.")
    print("=======================================================")


if __name__ == "__main__":
    run_aptitude_engine()