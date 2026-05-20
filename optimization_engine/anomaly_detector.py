import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

scores_path = os.path.join(BASE_DIR, "input_data", "candidate_scores.json")
output_path = os.path.join(BASE_DIR, "output", "anomaly_report.json")

with open(scores_path, "r", encoding="utf-8") as f:
    scores = json.load(f)

anomalies = {}

for cid, score in scores.items():

    if score >= 95:
        anomalies[cid] = "Suspiciously High Score"

    elif score <= 30:
        anomalies[cid] = "Suspiciously Low Score"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(anomalies, f, indent=4)

print("✅ Anomaly Detection Completed")