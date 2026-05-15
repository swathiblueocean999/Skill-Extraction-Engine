import re

def analyze_answer(answer):

    if not answer:
        return {
            "analysis": {"strong_hits": 0, "average_hits": 0},
            "aptitude_score": 0,
            "final_status": "WEAK"
        }

    text = answer.lower()

    # keep only words
    words = re.findall(r"[a-z]+", text)

    strong_keywords = {
        "analyze", "compare", "improve", "efficient",
        "decision", "solve", "strategy", "identify"
    }

    average_keywords = {
        "manage", "communicate", "support",
        "work", "handle", "understand"
    }

    strong_hits = len([w for w in words if w in strong_keywords])
    average_hits = len([w for w in words if w in average_keywords])

    # REAL scoring
    score = (strong_hits * 10) + (average_hits * 5)

    if score >= 15:
        status = "STRONG"
    elif score >= 5:
        status = "AVERAGE"
    else:
        status = "WEAK"

    return {
        "analysis": {
            "strong_hits": strong_hits,
            "average_hits": average_hits
        },
        "aptitude_score": score,
        "final_status": status
    }