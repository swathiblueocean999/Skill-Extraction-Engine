import json
from utils.evaluator import evaluate_answer
from utils.comparator import compare
from utils.metrics import calculate_metrics

with open("data/test_cases.json") as f:
    test_cases = json.load(f)

with open("data/expected_output.json") as f:
    expected = json.load(f)

results = []

for case in test_cases:
    cid = case["candidate_id"]
    answer = case["answer"]

    ai_result = evaluate_answer(answer)
   

    expected_result = next(
        item["expected_status"] for item in expected if item["candidate_id"] == cid
    )

    status = compare(ai_result, expected_result)

    results.append({
        "candidate_id": cid,
        "ai_result": ai_result,
        "expected": expected_result,
        "status": status
    })

with open("output/test_results.json", "w") as f:
    json.dump(results, f, indent=2)

report = calculate_metrics(results)

with open("output/final_report.json", "w") as f:
    json.dump(report, f, indent=2)

print("✅ Done")
print("Accuracy:", report["accuracy"])