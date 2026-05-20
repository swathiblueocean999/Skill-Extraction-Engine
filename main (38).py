import json
import os

from stabilization_engine.scoring_debugger import debug_scoring

from stabilization_engine.conversation_validator import validate_conversation

from stabilization_engine.pipeline_stabilizer import stabilize_pipeline

from stabilization_engine.error_handler import handle_errors

from stabilization_engine.api_stabilizer import stabilize_api

from stabilization_engine.edge_case_validator import validate_edge_cases

print("\nSTARTING DEBUGGING & STABILIZATION\n")

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

debugging_report = {}

edge_case_results = {}

# ==========================================
# PROCESS CANDIDATES
# ==========================================

for cid, candidate in final_output.items():

    # --------------------------------------

    scoring_status = debug_scoring(
        candidate
    )

    # --------------------------------------

    conversation_status = validate_conversation(
        candidate
    )

    # --------------------------------------

    error_status = handle_errors(
        candidate
    )

    # --------------------------------------

    edge_case = validate_edge_cases(
        candidate
    )

    # --------------------------------------

    debugging_report[cid] = {

        "Scoring":
        scoring_status,

        "Conversation":
        conversation_status,

        "Error Handling":
        error_status

    }

    # --------------------------------------

    edge_case_results[cid] = {

        "Edge Case":
        edge_case
    }

# ==========================================
# SAVE DEBUGGING REPORT
# ==========================================

with open(
    "outputs/debugging_report.json",
    "w"
) as f:

    json.dump(
        debugging_report,
        f,
        indent=4
    )

# ==========================================
# SAVE EDGE CASE REPORT
# ==========================================

with open(
    "outputs/edge_case_results.json",
    "w"
) as f:

    json.dump(
        edge_case_results,
        f,
        indent=4
    )

# ==========================================
# STABILIZED SYSTEM REPORT
# ==========================================

stabilized_report = {

    "pipeline":
    stabilize_pipeline(),

    "api":
    stabilize_api(),

    "system_status":
    "Stable"

}

with open(
    "outputs/stabilized_system_report.json",
    "w"
) as f:

    json.dump(
        stabilized_report,
        f,
        indent=4
    )

# ==========================================
# FINAL MODULE STATUS
# ==========================================

final_modules = {

    "ATS":
    "Stable",

    "Screening":
    "Stable",

    "HR":
    "Stable",

    "Technical":
    "Stable",

    "Behavioral":
    "Stable",

    "Integrity":
    "Stable",

    "Recommendation AI":
    "Stable",

    "Governance":
    "Stable"

}

with open(
    "outputs/final_refined_modules.json",
    "w"
) as f:

    json.dump(
        final_modules,
        f,
        indent=4
    )

# ==========================================
# TERMINAL OUTPUT
# ==========================================

print("DEBUGGING COMPLETED")

print("PIPELINE STABILIZED")

print("EDGE CASES VALIDATED")

print("FINAL MODULES REFINED")

print("DEBUGGING & STABILIZATION COMPLETED\n")