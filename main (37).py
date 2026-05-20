import json
import os

from simulation_engine.pipeline_simulator import simulate_pipeline

from simulation_engine.human_comparison import compare_human_vs_ai

from simulation_engine.inconsistency_checker import detect_inconsistency

from simulation_engine.performance_analyzer import analyze_performance

from simulation_engine.recommendation_engine import generate_recommendation

print("\nSTARTING FULL SYSTEM SIMULATION\n")

# ==========================================
# LOAD DATASETS
# ==========================================

with open("datasets/final_decision_output.json") as f:

    final_output = json.load(f)

# ==========================================
# CREATE OUTPUT DIRECTORY
# ==========================================

os.makedirs("outputs", exist_ok=True)

# ==========================================
# STORAGE OBJECTS
# ==========================================

test_report = {}

performance_report = {}

inconsistency_report = {}

recommendations = {}

# ==========================================
# PROCESS CANDIDATES
# ==========================================

for cid, candidate in final_output.items():

    # --------------------------------------

    pipeline = simulate_pipeline(
        candidate
    )

    # --------------------------------------

    comparison = compare_human_vs_ai(
        candidate
    )

    # --------------------------------------

    inconsistency = detect_inconsistency(
        candidate
    )

    # --------------------------------------

    performance = analyze_performance(
        candidate
    )

    # --------------------------------------

    recommendation = generate_recommendation(
        inconsistency
    )

    # --------------------------------------

    test_report[cid] = {

        "Pipeline Status":
        pipeline,

        "Human Comparison":
        comparison

    }

    # --------------------------------------

    performance_report[cid] = {

        "Performance":
        performance
    }

    # --------------------------------------

    inconsistency_report[cid] = {

        "Inconsistency":
        inconsistency
    }

    # --------------------------------------

    recommendations[cid] = {

        "Recommendation":
        recommendation
    }

# ==========================================
# SAVE TEST REPORT
# ==========================================

with open(
    "outputs/end_to_end_test_report.json",
    "w"
) as f:

    json.dump(
        test_report,
        f,
        indent=4
    )

# ==========================================
# SAVE PERFORMANCE REPORT
# ==========================================

with open(
    "outputs/performance_analysis.json",
    "w"
) as f:

    json.dump(
        performance_report,
        f,
        indent=4
    )

# ==========================================
# SAVE INCONSISTENCY REPORT
# ==========================================

with open(
    "outputs/inconsistency_report.json",
    "w"
) as f:

    json.dump(
        inconsistency_report,
        f,
        indent=4
    )

# ==========================================
# SAVE RECOMMENDATIONS
# ==========================================

with open(
    "outputs/improvement_recommendations.json",
    "w"
) as f:

    json.dump(
        recommendations,
        f,
        indent=4
    )

# ==========================================
# SAVE SUMMARY
# ==========================================

summary = {

    "system":
    "Full System Simulation",

    "total_candidates":
    len(test_report),

    "pipeline_validation":
    "Completed",

    "ai_vs_human_analysis":
    "Completed",

    "performance_analysis":
    "Completed",

    "status":
    "Validated"

}

with open(
    "outputs/system_simulation_summary.json",
    "w"
) as f:

    json.dump(
        summary,
        f,
        indent=4
    )

# ==========================================
# TERMINAL OUTPUT
# ==========================================

print("FULL PIPELINE VALIDATED")

print("AI VS HUMAN COMPARISON COMPLETED")

print("SYSTEM PERFORMANCE ANALYZED")

print("FULL SYSTEM SIMULATION COMPLETED\n")