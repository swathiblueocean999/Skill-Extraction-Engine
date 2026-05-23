import json

print("AI Model Explanation Started")

models = {
    "resume_parser": "NLP Based Extraction",
    "ats_engine": "Keyword Matching AI",
    "screening_engine": "Rule-Based Filtering",
    "interview_engine": "Behavioral Scoring AI",
    "decision_engine": "Final Candidate Ranking"
}

with open(
    "final_outputs/ai_model_summary.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(models, file, indent=4)

print("AI Model Explanation Completed")