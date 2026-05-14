import json

from engine.screening_engine import analyze_answer
from engine.scoring_engine import calculate_score
from engine.confidence_engine import confidence_level
from engine.report_generator import generate_report


with open("data/demo_candidates.json", "r") as file:
    candidates = json.load(file)

results = []

for candidate in candidates:

    candidate_id = candidate["candidate_id"]
    answer = candidate["answer"]

    analysis = analyze_answer(answer)

    score = calculate_score(analysis)

    confidence = confidence_level(answer)

    final_report = generate_report(
        candidate_id,
        analysis,
        score,
        confidence
    )

    results.append(final_report)


with open("output/final_screening_results.json", "w") as file:
    json.dump(results, file, indent=2)

with open("output/live_demo_output.json", "w") as file:
    json.dump(results, file, indent=2)

print("✅ AI Screening System Finalization Completed")