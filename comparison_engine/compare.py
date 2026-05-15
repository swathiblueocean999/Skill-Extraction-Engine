import json
import os

# Base path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# File paths
ai_path = os.path.join(BASE_DIR, "ai_output", "ai_scores.json")
manual_path = os.path.join(BASE_DIR, "manual_evaluation", "manual_scores.json")

mismatch_path = os.path.join(BASE_DIR, "reports", "mismatch_report.json")
inconsistency_path = os.path.join(BASE_DIR, "reports", "inconsistency_report.json")
evaluator_notes_path = os.path.join(BASE_DIR, "manual_evaluation", "evaluator_notes.json")

# Load data
with open(ai_path, "r", encoding="utf-8") as f:
    ai_data = json.load(f)

with open(manual_path, "r", encoding="utf-8") as f:
    manual_data = json.load(f)

report = {}
inconsistencies = []
evaluator_notes = {}

all_ids = set(ai_data.keys()) | set(manual_data.keys())

# Comparison logic
for cid in all_ids:

    ai_score = ai_data.get(cid, {}).get("score", 0)
    manual_score = manual_data.get(cid, 0)

    diff = abs(ai_score - manual_score)

    # Status logic
    if diff > 10:
        status = "HIGH_INCONSISTENCY"
        inconsistencies.append(cid)
    elif diff == 10:
        status = "WARNING"
    else:
        status = "OK"

    report[cid] = {
        "ai": ai_score,
        "manual": manual_score,
        "diff": diff,
        "status": status
    }

    # Auto evaluator notes generation (simple logic)
    if ai_score >= 80:
        note = "Strong candidate performance"
    elif ai_score >= 60:
        note = "Average performance, needs improvement"
    else:
        note = "Weak candidate performance"

    evaluator_notes[cid] = note

# Sort final report
sorted_report = dict(sorted(report.items()))
sorted_notes = dict(sorted(evaluator_notes.items()))

# Save mismatch report
with open(mismatch_path, "w", encoding="utf-8") as f:
    json.dump(sorted_report, f, indent=4)

# Save inconsistency report
with open(inconsistency_path, "w", encoding="utf-8") as f:
    json.dump({
        "high_risk_candidates": inconsistencies,
        "total_high_risk": len(inconsistencies)
    }, f, indent=4)

# Save evaluator notes
with open(evaluator_notes_path, "w", encoding="utf-8") as f:
    json.dump(sorted_notes, f, indent=4)

print("✅ Full Comparison Completed (Mismatch + Inconsistency + Evaluator Notes)")