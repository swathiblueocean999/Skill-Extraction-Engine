from utils.file_handler import load_json, save_json
from engine.interview_manager import process_interview


def main():

    questions = load_json("data/questions.json")

    candidates = load_json("data/candidates.json")

    final_results = []

    for candidate in candidates:

        result = process_interview(
            questions,
            candidate
        )

        final_results.append(result)

    save_json(
        "output/interview_output.json",
        final_results
    )

    print("\nInterview completed successfully")


if __name__ == "__main__":
    main()