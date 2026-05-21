import json

print("Demo Summary Generation Started")

# Load Pipeline Results
with open("outputs/pipeline_simulation_output.json", "r") as f:
    pipeline_results = json.load(f)

selected = 0
rejected = 0
hold = 0

for candidate in pipeline_results:

    result = candidate["final_result"]

    if result == "Selected":
        selected += 1

    elif result == "Rejected":
        rejected += 1

    else:
        hold += 1

summary = {
    "total_candidates": len(pipeline_results),
    "selected_candidates": selected,
    "rejected_candidates": rejected,
    "on_hold_candidates": hold
}

# Save Summary
with open("outputs/demo_summary.json", "w") as f:
    json.dump(summary, f, indent=4)

print("Demo Summary Generated")