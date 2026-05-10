import json
from utils.state_manager import ConversationState
from utils.decision_engine import decide_next_step
from utils.error_handler import handle_error
from utils.followup_generator import generate_followup
from utils.context_manager import ContextManager

# Load questions
with open("data/questions.json") as f:
    questions = json.load(f)

state = ConversationState()
context = ContextManager()
log = []

while state.current_question < len(questions):
    q = questions[state.current_question]

    print(f"\nAI: {q['text']}")
    answer = input("User: ")

    decision = decide_next_step(state, answer)

    if decision != "valid":
        state.repeat_question()

        if state.can_retry():
            response = handle_error(decision, state)
            print("AI:", response)
            continue
        else:
            print("AI: Let's move to the next question.")
            state.next_question()
            continue

    # Valid answer
    state.add_answer(answer)
    context.add(q["text"], answer)

    # Follow-up trigger (short answer)
    if len(answer.split()) < 5:
        followup = generate_followup(q["id"])
        if followup:
            print("AI (follow-up):", followup)

    state.next_question()

    log.append({
        "question": q["text"],
        "answer": answer,
        "decision": decision
    })

# Save log
with open("output/conversation_log.json", "w") as f:
    json.dump(log, f, indent=2)

print("\n✅ Conversation completed successfully!")