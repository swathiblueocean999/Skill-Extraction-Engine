from engine.weight_manager import WEIGHTS

def calculate_hr_score(data):

    score = (
        data["answer_relevance"] * WEIGHTS["answer_relevance"]
        +
        data["communication_score"] * WEIGHTS["communication_score"]
        +
        data["confidence_score"] * WEIGHTS["confidence_score"]
        +
        data["consistency_score"] * WEIGHTS["consistency_score"]
    )

    return round(score, 2)