def score_answer(answer_obj):
    score = {
        "clarity": 0,
        "relevance": 0,
        "completeness": 0,
        "consistency": 0
    }

    # clarity → based on word count
    word_count = len(answer_obj["raw_answer"].split())
    score["clarity"] = 1 if word_count > 8 else 0.5

    # relevance → off_topic 
    score["relevance"] = 0 if "off_topic" in answer_obj["issues"] else 1

    # completeness → missing issues check
    missing = [i for i in answer_obj["issues"] if "missing" in i]
    score["completeness"] = 1 if not missing else 0.5

    # consistency → vague 
    score["consistency"] = 0.5 if "vague_answer" in answer_obj["issues"] else 1

    return score