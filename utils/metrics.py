def calculate_metrics(results):
    total = len(results)
    matches = sum(1 for r in results if r["status"] == "match")

    accuracy = (matches / total) * 100 if total > 0 else 0

    return {
        "total_cases": total,
        "matches": matches,
        "accuracy": round(accuracy, 2)
    }