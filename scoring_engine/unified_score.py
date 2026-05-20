import json
import os

from weight_manager import get_role_weights

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input paths
ats_path = os.path.join(BASE_DIR, "input_data", "ats_scores.json")
screening_path = os.path.join(BASE_DIR, "input_data", "screening_scores.json")
hr_path = os.path.join(BASE_DIR, "input_data", "hr_scores.json")

# Output paths
unified_output_path = os.path.join(BASE_DIR, "output", "unified_scores.json")
hiring_report_path = os.path.join(BASE_DIR, "output", "hiring_fit_report.json")

# Load score files
with open(ats_path, "r", encoding="utf-8") as f:
    ats_scores = json.load(f)

with open(screening_path, "r", encoding="utf-8") as f:
    screening_scores = json.load(f)

with open(hr_path, "r", encoding="utf-8") as f:
    hr_scores = json.load(f)

# Get accountant role weights
weights = get_role_weights()

ats_weight = weights["ats"] / 100
screening_weight = weights["screening"] / 100
hr_weight = weights["hr"] / 100

unified_scores = {}

recommended = []
needs_review = []
reject = []

all_candidates = set(ats_scores.keys()) | set(screening_scores.keys()) | set(hr_scores.keys())

for cid in all_candidates:

    ats = ats_scores.get(cid, 0)
    screening = screening_scores.get(cid, 0)
    hr = hr_scores.get(cid, 0)

    # Unified score calculation
    final_score = (
        ats * ats_weight +
        screening * screening_weight +
        hr * hr_weight
    )

    # Hiring fit logic
    if final_score >= 85:
        hiring_fit = "Excellent"
        recommended.append(cid)

    elif final_score >= 70:
        hiring_fit = "Good"
        recommended.append(cid)

    elif final_score >= 50:
        hiring_fit = "Average"
        needs_review.append(cid)

    else:
        hiring_fit = "Weak"
        reject.append(cid)

    unified_scores[cid] = {
        "ats_score": ats,
        "screening_score": screening,
        "hr_score": hr,
        "final_score": round(final_score, 2),
        "hiring_fit": hiring_fit
    }

# Sort output
sorted_scores = dict(sorted(unified_scores.items()))

# Save unified scores
with open(unified_output_path, "w", encoding="utf-8") as f:
    json.dump(sorted_scores, f, indent=4)

# Save hiring fit report
with open(hiring_report_path, "w", encoding="utf-8") as f:
    json.dump({
        "recommended_for_hire": recommended,
        "needs_review": needs_review,
        "reject": reject
    }, f, indent=4)

print("✅ Accountant Unified Scoring Completed")