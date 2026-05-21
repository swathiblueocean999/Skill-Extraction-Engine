import json

print("Pipeline Simulation Started")

# Load Interview Results
with open("outputs/interview_demo_results.json", "r") as f:
    interview_results = json.load(f)

pipeline_output = []

for candidate in interview_results:

    final_score = (
        candidate["screening_score"] +
        candidate["interview_score"]
    ) / 2

    pipeline_output.append({
        "candidate_id": candidate["candidate_id"],
        "name": candidate["name"],
        "final_pipeline_score": final_score,
        "final_result": candidate["final_result"]
    })

# Save Results
with open("outputs/pipeline_simulation_output.json", "w") as f:
    json.dump(pipeline_output, f, indent=4)

print("Pipeline Simulation Completed")