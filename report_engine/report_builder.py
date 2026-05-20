from report_engine.ats_summary import get_ats_summary
from report_engine.hr_insights import get_hr_insight
from report_engine.technical_summary import get_technical_summary
from report_engine.behavioral_analysis import get_behavioral_analysis
from report_engine.recommendation_summary import get_recommendation


def build_candidate_report(candidate_data):

    # ==========================================
    # GENERATE SUMMARIES
    # ==========================================

    ats_summary = get_ats_summary(
        candidate_data["ats_score"]
    )

    hr_summary = get_hr_insight(
        candidate_data["hr_score"]
    )

    technical_summary = get_technical_summary(
        candidate_data["technical_score"]
    )

    behavioral_summary = get_behavioral_analysis(
        candidate_data["behavioral_score"]
    )

    recommendation = get_recommendation(
        candidate_data["final_decision"]
    )

    # ==========================================
    # INITIALIZE ANALYSIS LISTS
    # ==========================================

    strengths = []

    weaknesses = []

    risks = []

    # ==========================================
    # STRENGTH ANALYSIS
    # ==========================================

    if candidate_data["technical_score"] >= 80:
        strengths.append(
            "Strong technical performance"
        )

    if candidate_data["hr_score"] >= 75:
        strengths.append(
            "Good communication"
        )

    if candidate_data["behavioral_score"] >= 85:
        strengths.append(
            "Highly focused behavior"
        )

    if candidate_data["integrity_score"] >= 85:
        strengths.append(
            "High interview integrity"
        )

    # ==========================================
    # WEAKNESS ANALYSIS
    # ==========================================

    if candidate_data["technical_score"] < 60:
        weaknesses.append(
            "Weak technical capability"
        )

    if candidate_data["hr_score"] < 60:
        weaknesses.append(
            "Weak HR interaction"
        )

    if candidate_data["behavioral_score"] < 65:
        weaknesses.append(
            "Behavioral concern"
        )

    # ==========================================
    # RISK ANALYSIS
    # ==========================================

    if candidate_data["integrity_score"] < 60:
        risks.append(
            "Integrity concern"
        )

    if candidate_data["final_hiring_score"] < 65:
        risks.append(
            "Low hiring confidence"
        )

    # ==========================================
    # EMPTY VALUE HANDLING
    # ==========================================

    if not strengths:
        strengths.append(
            "No major strength identified"
        )

    if not weaknesses:
        weaknesses.append(
            "No major weakness identified"
        )

    if not risks:
        risks.append(
            "No major risk detected"
        )

    # ==========================================
    # FINAL REPORT OBJECT
    # ==========================================

    return {

        "ATS Summary":
        ats_summary,

        "HR Insight":
        hr_summary,

        "Technical Summary":
        technical_summary,

        "Behavioral Analysis":
        behavioral_summary,

        "Strengths":
        strengths,

        "Weaknesses":
        weaknesses,

        "Risk Indicators":
        risks,

        "Final Recommendation":
        recommendation

    }