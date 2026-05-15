import json
from engine.interview_flow import run_interview


def load_candidates():

    with open("data/sample_candidates.json", "r") as file:
        return json.load(file)


def save_output(data):

    with open("output/interview_sessions.json", "w") as file:
        json.dump(data, file, indent=2)


def main():

    candidates = load_candidates()

    all_sessions = []

    for candidate in candidates:

        session = run_interview(candidate)

        all_sessions.append(session)

    save_output(all_sessions)

    print("\nInterview sessions saved successfully")


if __name__ == "__main__":
    main()