from engine.role_question_generator import generate_questions
from engine.state_manager import InterviewState
from engine.phase_manager import get_phase


def run_interview(candidate):

    state = InterviewState()

    questions = generate_questions(
        candidate["level"],
        candidate["role_type"]
    )

    print("\n===================================")
    print("Starting HR Interview")
    print("Candidate:", candidate["name"])
    print("===================================\n")

    for index, question in enumerate(questions):

        phase = get_phase(index)

        print(f"\nPHASE: {phase}")
        print("AI:", question["question"])

        response = input("Candidate: ")

        state.save_response(
            question["id"],
            response
        )

        state.next_question()

    return {
        "candidate_id": candidate["candidate_id"],
        "responses": state.responses
    }