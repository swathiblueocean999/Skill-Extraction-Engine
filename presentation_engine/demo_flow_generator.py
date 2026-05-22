import json

print("Demo Flow Generation Started")

flow = {
    "step_1": "Upload Candidate Resume",
    "step_2": "ATS Score Calculation",
    "step_3": "Screening Evaluation",
    "step_4": "HR Assessment",
    "step_5": "Technical Interview",
    "step_6": "Final Hiring Decision"
}

with open("presentations/hiring_pipeline_flow.json", "w") as f:
    json.dump(flow, f, indent=4)

print("Demo Flow Generated")