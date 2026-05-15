def generate_breakdown(data, final_score):

    return {
        "answer_relevance": data["answer_relevance"],
        "communication_score": data["communication_score"],
        "confidence_score": data["confidence_score"],
        "consistency_score": data["consistency_score"],
        "final_hr_score": final_score
    }