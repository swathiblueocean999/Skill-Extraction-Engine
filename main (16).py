from utils.file_handler import load_json, save_json

from engine.communication_scorer import (
    evaluate_communication
)


def main():

    candidates = load_json(
        "data/candidate_answers.json"
    )

    final_results = []

    for candidate in candidates:

        result = evaluate_communication(
            candidate["answer"]
        )

        final_results.append({

            "candidate_id":
            candidate["candidate_id"],

            "answer":
            candidate["answer"],

            "evaluation":
            result
        })

    save_json(
        "output/communication_scores.json",
        final_results
    )

    print("\nCommunication evaluation completed successfully")


if __name__ == "__main__":
    main()