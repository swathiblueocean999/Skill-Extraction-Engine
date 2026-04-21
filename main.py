import json
from scorer import (
    calculate_skill_score,
    calculate_experience_score,
    calculate_education_score,
    calculate_final_score
)
from semantic import calculate_semantic_score
from weights import WEIGHTS

# 🔹 Load profiles (JSON is a LIST)
with open("output.json", "r", encoding="utf-8") as f:
    profiles = json.load(f)

# 🔹 Job Description (manual)
job = {
    "role": "Machine Learning Engineer",
    "responsibilities": "Build ML models using Python",
    "skills": ["Python", "Machine Learning"],
    "experience": 3,
    "education": "B.Tech"
}

results = []

# 🔹 Process each candidate
for profile in profiles:
    try:
        scores = {
            "skill": calculate_skill_score(
                profile.get("skills", []),
                job.get("skills", [])
            ),
            "experience": calculate_experience_score(
                profile.get("experience", 0),
                job.get("experience", 0)
            ),
            "education": calculate_education_score(
                profile.get("education", ""),
                job.get("education", "")
            ),
            # 🔥 semantic = role + responsibilities
            "semantic": calculate_semantic_score(
                profile.get("role", "") + " " + profile.get("responsibilities", ""),
                job.get("role", "") + " " + job.get("responsibilities", "")
            )
        }

        final = calculate_final_score(scores, WEIGHTS["default"])

        results.append({
            "id": profile.get("profile_id", "N/A"),  # ✅ FIXED HERE
            "score": final
        })

    except Exception as e:
        print(f"Error in profile {profile.get('profile_id', 'N/A')}: {e}")

# 🔹 Sort (Ranking)
results = sorted(results, key=lambda x: x["score"], reverse=True)

# 🔹 Thresholds
SELECTED_THRESHOLD = 0.4
REVIEW_THRESHOLD = 0.25

selected, review, rejected = [], [], []

for r in results:
    if r["score"] >= SELECTED_THRESHOLD:
        selected.append(r)
    elif r["score"] >= REVIEW_THRESHOLD:
        review.append(r)
    else:
        rejected.append(r)

# 🔹 Output (Terminal)
print("\n=== TOP CANDIDATES ===")
for r in results[:5]:
    print(f"{r['id']} -> {r['score']*100:.2f}%")

print("\n=== SELECTED ===")
for r in selected:
    print(f"{r['id']} -> {r['score']*100:.2f}%")

print("\n=== REVIEW ===")
for r in review:
    print(f"{r['id']} -> {r['score']*100:.2f}%")

print("\n=== REJECTED ===")
for r in rejected:
    print(f"{r['id']} -> {r['score']*100:.2f}%")

# 🔹 Save to file
with open("final_output.txt", "w", encoding="utf-8") as f:
    f.write("=== TOP CANDIDATES ===\n")
    for r in results[:5]:
        f.write(f"{r['id']} -> {r['score']*100:.2f}%\n")

    f.write("\n=== SELECTED ===\n")
    for r in selected:
        f.write(f"{r['id']} -> {r['score']*100:.2f}%\n")

    f.write("\n=== REVIEW ===\n")
    for r in review:
        f.write(f"{r['id']} -> {r['score']*100:.2f}%\n")

    f.write("\n=== REJECTED ===\n")
    for r in rejected:
        f.write(f"{r['id']} -> {r['score']*100:.2f}%\n")

print("\n✅ Results saved to final_output.txt")