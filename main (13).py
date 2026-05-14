import json

from engine.edge_detector import detect_edge_case
from engine.retry_handler import retry_logic
from engine.fallback_manager import fallback_action


with open("data/test_cases.json", "r") as file:
    test_cases = json.load(file)

results = []

for case in test_cases:

    candidate_id = case["candidate_id"]
    answer = case["answer"]

    detected_issue = detect_edge_case(answer)

    retry_message = retry_logic(detected_issue)

    fallback = fallback_action(detected_issue)

    result = {
        "candidate_id": candidate_id,
        "answer": answer,
        "detected_issue": detected_issue,
        "retry_message": retry_message,
        "fallback_action": fallback
    }

    results.append(result)


with open("output/edge_case_report.json", "w") as file:
    json.dump(results, file, indent=2)


print("✅ Edge Case Handling Completed")