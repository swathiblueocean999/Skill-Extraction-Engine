def format_transcript(record, normalized_text, extracted_exp):
    return {
        "candidate_id": record["candidate_id"],
        "job_id": record["job_id"],
        "question_id": record["question_id"],
        "category": record.get("category"),
        "question": record["question"],
        "answer": record["answer"],
        "normalized_answer": normalized_text,
        "answer_type": record.get("answer_type"),
        "extracted_experience": extracted_exp,
        "timestamp": record["timestamp"],
        "confidence": record["confidence"],
        "is_cleaned": True
    }