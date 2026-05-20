import json
import os

from documentation_engine.architecture_documenter import architecture_documentation

from documentation_engine.api_documenter import api_documentation

from documentation_engine.scoring_logic_documenter import scoring_logic

from documentation_engine.data_model_documenter import data_models

from documentation_engine.workflow_generator import workflow_documentation

from documentation_engine.deployment_guide_generator import deployment_guide

from documentation_engine.onboarding_guide_generator import onboarding_guide

print("\nSTARTING DOCUMENTATION MASTER SYSTEM\n")

# ==========================================
# CREATE OUTPUT DIRECTORY
# ==========================================

os.makedirs("outputs", exist_ok=True)

# ==========================================
# TECHNICAL HANDBOOK
# ==========================================

handbook = {

    "architecture":
    architecture_documentation(),

    "apis":
    api_documentation(),

    "scoring_logic":
    scoring_logic(),

    "data_models":
    data_models(),

    "workflow":
    workflow_documentation()

}

with open(
    "outputs/zecpath_ai_technical_handbook.json",
    "w"
) as f:

    json.dump(
        handbook,
        f,
        indent=4
    )

# ==========================================
# SYSTEM ARCHITECTURE DOCUMENTATION
# ==========================================

architecture = architecture_documentation()

with open(
    "outputs/system_architecture_documentation.json",
    "w"
) as f:

    json.dump(
        architecture,
        f,
        indent=4
    )

# ==========================================
# DEVELOPER ONBOARDING GUIDE
# ==========================================

onboarding = onboarding_guide()

with open(
    "outputs/developer_onboarding_guide.json",
    "w"
) as f:

    json.dump(
        onboarding,
        f,
        indent=4
    )

# ==========================================
# WORKFLOW DOCUMENTATION
# ==========================================

workflow = workflow_documentation()

with open(
    "outputs/workflow_documentation.json",
    "w"
) as f:

    json.dump(
        workflow,
        f,
        indent=4
    )

# ==========================================
# DOCUMENTATION SUMMARY
# ==========================================

summary = {

    "system":
    "Documentation Master File",

    "technical_handbook":
    "Generated",

    "architecture_documentation":
    "Completed",

    "developer_onboarding":
    "Prepared",

    "deployment_guide":
    deployment_guide(),

    "status":
    "Completed"

}

with open(
    "outputs/documentation_summary.json",
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

print("AI TECHNICAL HANDBOOK GENERATED")

print("SYSTEM ARCHITECTURE DOCUMENTED")

print("WORKFLOW DOCUMENTATION CREATED")

print("DEVELOPER ONBOARDING GUIDE READY")

print("DOCUMENTATION MASTER FILE COMPLETED\n")