from utils.file_handler import load_json, save_json

from engine.hesitation_detector import detect_hesitation
from engine.uncertainty_detector import detect_uncertainty
from engine.contradiction_checker import detect_contradiction
from engine.sentiment_engine import analyze_sentiment
from engine.stress_detector import detect_stress
from engine.behavioral_scorer import calculate_behavior_score
from engine.confidence_analyzer import confidence_level

responses = load_json("data/candidate_responses.json")

results = []

for item in responses:

    answer = item["answer"]

    hesitation = detect_hesitation(answer)
    uncertainty = detect_uncertainty(answer)
    contradiction = detect_contradiction(answer)
    sentiment = analyze_sentiment(answer)
    stress = detect_stress(answer)

    score = calculate_behavior_score(
        hesitation,
        uncertainty,
        contradiction,
        stress,
        sentiment
    )

    confidence = confidence_level(score)

    results.append({
        "candidate_id": item["candidate_id"],
        "analysis": {
            "hesitation_count": hesitation,
            "uncertainty": uncertainty,
            "contradiction": contradiction,
            "stress_detected": stress,
            "sentiment": sentiment
        },
        "behavior_score": score,
        "confidence_level": confidence
    })

save_json(
    "output/confidence_results.json",
    results
)

print("Confidence analysis completed.")