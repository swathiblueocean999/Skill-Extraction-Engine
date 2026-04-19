import json
from ats_model import evaluate_resume

# Load dataset
with open("test_data.json", "r") as f:
    data = json.load(f)

results = []

# Metrics
tp = fp = tn = fn = 0

print("\n=== RUNNING ATS TEST ===\n")

for profile in data:

    profile_id = profile.get("profile_id", "UNKNOWN")
    expected = profile.get("expected_good", False)

    # Run model
    result = evaluate_resume(profile)

    predicted = result.get("predicted_good", False)
    score = result.get("score", 0)

    # Debug print (IMPORTANT for fixing issues)
    print(f"{profile_id} | Score: {score} | Expected: {expected} | Predicted: {predicted}")

    # Save result
    results.append({
        "profile_id": profile_id,
        "expected_good": expected,
        "predicted_good": predicted,
        "score": score
    })

    # Metrics calculation
    if expected and predicted:
        tp += 1
    elif not expected and not predicted:
        tn += 1
    elif not expected and predicted:
        fp += 1
    elif expected and not predicted:
        fn += 1

# Save output.json
with open("output.json", "w") as f:
    json.dump(results, f, indent=2)

# Final metrics
total = tp + tn + fp + fn

accuracy = (tp + tn) / total if total else 0
precision = tp / (tp + fp) if (tp + fp) else 0
recall = tp / (tp + fn) if (tp + fn) else 0

print("\n=== FINAL ATS RESULTS ===")
print("Total Profiles:", total)
print("TP:", tp, "FP:", fp, "TN:", tn, "FN:", fn)
print("Accuracy:", round(accuracy, 2))
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))