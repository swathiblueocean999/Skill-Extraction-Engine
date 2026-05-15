def generate_hr_summary(results):

    summary = {
        "total_candidates": len(results),
        "strong_candidates": 0,
        "average_candidates": 0,
        "weak_candidates": 0,
        "top_candidates": []
    }

    for r in results:

        status = r.get("final_status", "").upper()  # 🔥 FIX 1

        if status == "STRONG":
            summary["strong_candidates"] += 1

        elif status == "AVERAGE":
            summary["average_candidates"] += 1

        else:
            summary["weak_candidates"] += 1

    # top candidates
    summary["top_candidates"] = sorted(
        results,
        key=lambda x: x.get("aptitude_score", 0),
        reverse=True
    )[:5]

    return summary