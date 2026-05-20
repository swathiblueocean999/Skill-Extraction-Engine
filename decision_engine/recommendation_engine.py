from decision_engine.decision_logic import get_final_decision
from decision_engine.confidence_calculator import calculate_confidence
from decision_engine.risk_analyzer import analyze_risk


def generate_recommendation(score, behavior, integrity):

    decision = get_final_decision(score, behavior, integrity)

    confidence = calculate_confidence(
        score,
        behavior,
        integrity
    )

    risk = analyze_risk(
        behavior,
        integrity
    )

    return {
        "decision": decision,
        "confidence_score": confidence,
        "risk_factor": risk
    }