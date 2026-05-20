import json
import os

from optimization_engine.false_positive_analysis import analyze_false_decisions

from optimization_engine.threshold_optimizer import optimize_thresholds

from optimization_engine.consistency_checker import check_consistency

from optimization_engine.intent_refinement import refine_intent

from optimization_engine.speed_optimizer import optimize_speed

from optimization_engine.scoring_refinement import refine_scoring

print("\nSTARTING OPTIMIZATION & REFINEMENT ENGINE\n")

# ==========================================
# LOAD DATASETS
# ==========================================

with open("datasets/final_decision_output.json") as f:

    final_output = json.load(f)

with open("datasets/candidate_ai_profiles.json") as f:

    profiles = json.load(f)

# ==========================================
# STORE RESULTS
# ==========================================

optimization_results = {}

# ==========================================
# PROCESS CANDIDATES
# ==========================================

for cid, candidate in final_output.items():

    profile = profiles[cid]

    false_analysis = analyze_false_decisions(
        candidate
    )

    threshold_status = optimize_thresholds(
        candidate["final_hiring_score"]
    )

    consistency = check_consistency(
        candidate
    )

    intent = refine_intent(
        profile
    )

    scoring = refine_scoring(
        candidate["final_hiring_score"]
    )

    optimization_results[cid] = {

        "False Decision Analysis":
        false_analysis,

        "Threshold Optimization":
        threshold_status,

        "Consistency Status":
        consistency,

        "Intent Analysis":
        intent,

        "Scoring Confidence":
        scoring

    }

# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

os.makedirs("outputs", exist_ok=True)

# ==========================================
# SAVE OPTIMIZATION REPORT
# ==========================================

with open(
    "outputs/optimization_report.json",
    "w"
) as f:

    json.dump(
        optimization_results,
        f,
        indent=4
    )

# ==========================================
# SAVE REFINED SCORING LOGIC
# ==========================================

refined_logic = {

    "Selected Threshold":
    ">= 85",

    "Review Threshold":
    ">= 70",

    "Reject Threshold":
    "< 70",

    "Integrity Risk Limit":
    "< 60"

}

with open(
    "outputs/refined_scoring_logic.json",
    "w"
) as f:

    json.dump(
        refined_logic,
        f,
        indent=4
    )

# ==========================================
# SAVE SUMMARY
# ==========================================

summary = {

    "system":
    "Optimization & Refinement Engine",

    "total_candidates":
    len(optimization_results),

    "processing_speed":
    optimize_speed(
        len(optimization_results)
    ),

    "optimization_features": {

        "false_positive_analysis":
        True,

        "threshold_refinement":
        True,

        "intent_refinement":
        True,

        "consistency_optimization":
        True,

        "speed_optimization":
        True,

        "scoring_refinement":
        True

    },

    "status":
    "Completed"

}

with open(
    "outputs/accuracy_summary.json",
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

print("ALL OPTIMIZATION REPORTS GENERATED")

print("OPTIMIZATION & REFINEMENT COMPLETED\n")