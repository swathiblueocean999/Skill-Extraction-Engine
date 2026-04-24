import json
from ats_model import evaluate_resume

# Load dataset
with open("test_data.json", "r") as f:
    data = json.load(f)

results = []

# Metrics
tp = fp = tn = fn = 0

# Threshold
THRESHOLD = 30

# Log collector (for file output)
log_lines = []

print("\n=== RUNNING ATS TEST ===\n")
log_lines.append("=== RUNNING ATS TEST ===\n")

for profile in data:

    profile_id = profile.get("profile_id", "UNKNOWN")
    expected = profile.get("expected_good", False)

    # Run model
    result = evaluate_resume(profile)

    score = result.get("score", 0)

    # Prediction logic
    predicted = score >= THRESHOLD

    line = f"PROCESSING: {profile_id}\n{profile_id} | Score: {score} | Expected: {expected} | Predicted: {predicted}"

    # ✔️ PRINT + SAVE BOTH
    print(line)
    log_lines.append(line)

    # Save structured result
    results.append({
        "profile_id": profile_id,
        "expected_good": expected,
        "predicted_good": predicted,
        "score": score
    })

    # Confusion matrix
    if expected and predicted:
        tp += 1
    elif not expected and not predicted:
        tn += 1
    elif not expected and predicted:
        fp += 1
    elif expected and not predicted:
        fn += 1

# Metrics
total = tp + tn + fp + fn

accuracy = (tp + tn) / total if total else 0
precision = tp / (tp + fp) if (tp + fp) else 0
recall = tp / (tp + fn) if (tp + fn) else 0
f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0

# Final report
final_report = f"""
=== FINAL ATS RESULTS ===
Total Profiles: {total}
TP: {tp} FP: {fp} TN: {tn} FN: {fn}
Accuracy: {round(accuracy, 2)}
Precision: {round(precision, 2)}
Recall: {round(recall, 2)}
F1 Score: {round(f1, 2)}
"""

# ✔️ PRINT + SAVE FINAL REPORT
print(final_report)
log_lines.append(final_report)

# Save JSON output
output_data = {
    "metrics": {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    },
    "results": results
}

with open("output.json", "w") as f:
    json.dump(output_data, f, indent=2)

# ✔️ Save FULL TEXT LOG (FIXED)
with open("output.txt", "w") as f:
    f.write("\n".join(log_lines))

print("✔️ ALL OUTPUTS SAVED SUCCESSFULLY")