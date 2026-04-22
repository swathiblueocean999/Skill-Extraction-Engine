import json
from scorer import calculate_score

# ---------------- LOAD DATA ----------------
with open("output.json", "r", encoding="utf-8") as f:
    profiles = json.load(f)

selected = []
review = []
rejected = []

# ---------------- SCORING LOOP ----------------
for profile in profiles:

    score = calculate_score(profile)
    profile["score"] = score

    # ---------------- CLASSIFICATION FIX ----------------
    if score >= 55:
        profile["status"] = "SELECTED"
        selected.append(profile)

    elif score >= 40:
        profile["status"] = "REVIEW"
        review.append(profile)

    else:
        profile["status"] = "REJECTED"
        rejected.append(profile)

# ---------------- SORT TOP CANDIDATES ----------------
selected.sort(key=lambda x: x["score"], reverse=True)
review.sort(key=lambda x: x["score"], reverse=True)

# ---------------- OUTPUT REPORT ----------------
report = {
    "TOTAL": len(profiles),
    "SELECTED": len(selected),
    "REVIEW": len(review),
    "REJECTED": len(rejected),
    "TOP_CANDIDATES": (selected[:10] + review[:10])
}

# ---------------- WRITE OUTPUT ----------------
with open("final_output.txt", "w", encoding="utf-8") as f:
    f.write("=== DAY 14 ATS REPORT ===\n\n")
    f.write(f"TOTAL: {report['TOTAL']}\n")
    f.write(f"SELECTED: {report['SELECTED']}\n")
    f.write(f"REVIEW: {report['REVIEW']}\n")
    f.write(f"REJECTED: {report['REJECTED']}\n\n")

    f.write("TOP CANDIDATES:\n")
    for c in report["TOP_CANDIDATES"]:
        f.write(f"{c['profile_id']} | {c['role']} | {c['score']}\n")

print("ATS RUN COMPLETE")