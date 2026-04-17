import json
from normalization import normalize_text, normalize_experience, normalize_skills
from bias import remove_bias_fields
from scorer import calculate_scores, final_score

# Load data
with open("output.json", "r") as f:
    profiles = json.load(f)

# Example JD
jd = {
    "skills": ["excel", "accounting"],
    "education": "bachelor",
    "text": "accounts assistant accounting excel finance"
}

candidates = []

for p in profiles:

    candidate = {
        "skills": normalize_skills(p.get("skills")),
        "experience": normalize_experience(p.get("experience")),
        "education": normalize_text(p.get("education")),
        "text": normalize_text(p.get("role", "") + " " + " ".join(p.get("responsibilities", [])))
    }

    candidate = remove_bias_fields(candidate)

    scores = calculate_scores(candidate, jd)
    total = final_score(scores)

    candidates.append({
        "candidate": p.get("profile_id"),
        "score": total
    })
    # 🔹 Ranking Output (already there)
ranked = sorted(candidates, key=lambda x: x["score"], reverse=True)

with open("ranking_output.txt", "w") as f:
    for c in ranked:
        f.write(f"{c['candidate']} - {c['score']}\n")


# 🔹 Sequential Output (NEW)
sequential = sorted(candidates, key=lambda x: x["candidate"])

with open("sequential_output.txt", "w") as f:
    for c in sequential:
        f.write(f"{c['candidate']} - {c['score']}\n")

# Sort
candidates = sorted(candidates, key=lambda x: x["score"], reverse=True)

# Save output
with open("final_output.txt", "w") as f:
    for c in candidates:
        f.write(f"{c['candidate']} - {c['score']}\n")

print("Day 15 Completed Successfully!")