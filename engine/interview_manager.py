from engine.response_analyzer import analyze_response
from engine.followup_engine import generate_followup
from engine.difficulty_adapter import get_difficulty_level
from engine.decision_tree import get_decision
from engine.state_tracker import ConversationState


def process_interview(questions, candidate):

    state = ConversationState()

    results = []

    for index, question in enumerate(questions):

        answer = candidate["answers"][index]

        analysis = analyze_response(answer)

        decision = get_decision(analysis)

        difficulty = get_difficulty_level(analysis)

        followup = generate_followup(
            question["question"],
            analysis
        )

        if followup["question"]:

            if not state.already_asked(
                followup["question"]
            ):

                state.add_followup(
                    followup["question"]
                )

        results.append({

            "question_id": question["id"],
            "question": question["question"],
            "answer": answer,
            "analysis": analysis,
            "decision": decision,
            "difficulty": difficulty,
            "followup": followup
        })

        state.next_question()

    return {
        "candidate_id": candidate["candidate_id"],
        "results": results
    }