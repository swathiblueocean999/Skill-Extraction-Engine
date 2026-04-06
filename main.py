import json
import re
from semantic import get_similarity_score

# -----------------------------
# Load JSON (Day 12 output)
# -----------------------------
with open("output.json", "r", encoding="utf-8") as f:
    profiles = json.load(f)

# -----------------------------
# Job Description
# -----------------------------
jd = {
    "skills": ["Accounting", "Excel", "Tally"],
    "experience": 2,
    "education": "bachelor",
    "text": "Looking for accountant with Excel and Tally skills"
}

# -----------------------------
# Extract experience safely
# -----------------------------
def extract_experience(exp_text):
    exp_text = str(exp_text)
    numbers = re.findall(r"\d+", exp_text)
    return int(numbers[0]) if numbers else 0

# -----------------------------
# Scoring functions
# -----------------------------
def skill_match(c_skills, jd_skills):
    return len(set(c_skills) & set(jd_skills)) / max(len(jd_skills), 1)

def experience_match(c_exp, jd_exp):
    return min(c_exp / jd_exp, 1) if jd_exp else 0

def education_match(c_edu, jd_edu):
    c_edu = str(c_edu).lower()
    jd_edu = str(jd_edu).lower()
    return 1 if jd_edu in c_edu else 0

# -----------------------------
# Convert profiles → candidates
# -----------------------------
candidates = []

for p in profiles:
    candidate = {
        "name": f"Candidate_{p.get('profile_id')}",
        "skills": p.get("skills", []),
        "experience": extract_experience(p.get("experience")),
        "education": p.get("education", ""),
        "text": (p.get("role", "") or "") + " " + " ".join(p.get("responsibilities", []))
    }
    candidates.append(candidate)

# -----------------------------
# Weights
# -----------------------------
WEIGHTS = {
    "skill": 0.3,
    "experience": 0.2,
    "education": 0.1,
    "semantic": 0.4
}

# -----------------------------
# Calculate Scores
# -----------------------------
results = []

for c in candidates:
    s_skill = skill_match(c["skills"], jd["skills"])
    s_exp = experience_match(c["experience"], jd["experience"])
    s_edu = education_match(c["education"], jd["education"])
    s_sem = get_similarity_score(c["text"], jd["text"])

    final_score = (
        s_skill * WEIGHTS["skill"] +
        s_exp * WEIGHTS["experience"] +
        s_edu * WEIGHTS["education"] +
        s_sem * WEIGHTS["semantic"]
    )

    results.append({
        "name": c["name"],
        "score": round(final_score, 2)
    })

# -----------------------------
# Ranking
# -----------------------------
ranked = sorted(results, key=lambda x: x["score"], reverse=True)

# -----------------------------
# Shortlisting (FINAL FIX 🔥)
# -----------------------------
selected = []
review = []
rejected = []

for i, r in enumerate(ranked):
    if i < 5:  # 🔥 Top 5 always selected
        selected.append(r)
    elif r["score"] >= 0.3:
        review.append(r)
    else:
        rejected.append(r)

# -----------------------------
# Terminal Output
# -----------------------------
print("\n=== TOP 10 CANDIDATES ===\n")
for r in ranked[:10]:
    print(f"{r['name']} → {r['score']*100:.2f}%")

print("\n=== SELECTED ===")
for r in selected:
    print(f"{r['name']} → {r['score']*100:.2f}%")

print("\n=== REVIEW ===")
for r in review:
    print(f"{r['name']} → {r['score']*100:.2f}%")

print("\n=== REJECTED ===")
for r in rejected:
    print(f"{r['name']} → {r['score']*100:.2f}%")

# -----------------------------
# Save to File
# -----------------------------
with open("final_output.txt", "w", encoding="utf-8") as f:

    f.write("=== TOP CANDIDATES ===\n")
    for r in ranked:
        f.write(f"{r['name']} → {r['score']*100:.2f}%\n")

    f.write("\n=== SELECTED ===\n")
    for r in selected:
        f.write(f"{r['name']} → {r['score']*100:.2f}%\n")

    f.write("\n=== REVIEW ===\n")
    for r in review:
        f.write(f"{r['name']} → {r['score']*100:.2f}%\n")

    f.write("\n=== REJECTED ===\n")
    for r in rejected:
        f.write(f"{r['name']} → {r['score']*100:.2f}%\n")

print("\n Output saved to final_output.txt")