import json
import random
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input paths
candidates_path = os.path.join(BASE_DIR, "input_data", "candidates.json")
questions_path = os.path.join(BASE_DIR, "input_data", "interview_questions.json")

# Output paths
ai_output_path = os.path.join(BASE_DIR, "ai_output", "ai_scores.json")
feedback_output_path = os.path.join(BASE_DIR, "ai_output", "ai_feedback.json")


# Load data
def load_data():
    with open(candidates_path, "r", encoding="utf-8") as f:
        candidates = json.load(f)

    with open(questions_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    return candidates, questions


# Generate score based on type
def generate_score(candidate_type):
    base = 50

    if candidate_type == "confident":
        base += random.randint(20, 35)
    elif candidate_type == "hesitant":
        base += random.randint(0, 15)
    elif candidate_type == "inexperienced":
        base += random.randint(-10, 10)
    elif candidate_type == "overqualified":
        base += random.randint(15, 30)

    return max(0, min(100, base))


# Generate feedback (NEW PART)
def generate_feedback(candidate_type, score):

    if score >= 80:
        return "Strong candidate with excellent communication and confidence"
    elif score >= 60:
        return "Average performance, good but needs improvement"
    else:
        return "Weak performance, requires training and development"


def run_simulation():
    candidates, questions = load_data()

    ai_scores = {}
    ai_feedback = {}

    for c in candidates:

        # Score generation
        scores = []

        for q in questions:
            score = generate_score(c["type"])
            scores.append(score)

        final_score = sum(scores) / len(scores)

        ai_scores[c["id"]] = {
            "score": round(final_score, 2),
            "type": c["type"]
        }

        # Feedback generation
        feedback = generate_feedback(c["type"], final_score)

        ai_feedback[c["id"]] = feedback

    # Save AI scores
    with open(ai_output_path, "w", encoding="utf-8") as f:
        json.dump(ai_scores, f, indent=4)

    # Save AI feedback
    with open(feedback_output_path, "w", encoding="utf-8") as f:
        json.dump(ai_feedback, f, indent=4)

    print("✅ Simulation Completed (Scores + Feedback Generated)")


if __name__ == "__main__":
    run_simulation()