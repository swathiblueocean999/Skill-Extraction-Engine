import json
from utils.hesitation_detector import detect_hesitation
from utils.sentiment_analyzer import analyze_sentiment
from utils.behavior_analyzer import analyze_behavior
from utils.confidence_scorer import calculate_confidence

# Load input
with open("data/structured_answers.json") as f:
    data = json.load(f)

results = []

for item in data:
    text = item["raw_answer"]

    hesitation = detect_hesitation(text)
    sentiment = analyze_sentiment(text)
    behavior = analyze_behavior(text)

    confidence_score = calculate_confidence(hesitation, sentiment, behavior)

    result = {
        "candidate_id": item["candidate_id"],
        "hesitation": hesitation,
        "sentiment": sentiment,
        "behavior": behavior,
        "confidence_score": confidence_score
    }

    results.append(result)

# Save output
with open("output/communication_report.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Confidence & Sentiment Analysis Completed")