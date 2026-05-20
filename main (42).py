import json
import os

from monitoring_engine.api_logger import api_logs

from monitoring_engine.model_output_tracker import model_output_tracking

from monitoring_engine.error_monitor import error_monitoring

from monitoring_engine.metrics_collector import metrics_collection

from monitoring_engine.alerting_engine import alerting_rules

from monitoring_engine.dashboard_designer import dashboard_design

from monitoring_engine.audit_log_system import audit_logs

print("\nSTARTING AI MONITORING & OBSERVABILITY SYSTEM\n")

# ==========================================
# CREATE OUTPUT DIRECTORY
# ==========================================

os.makedirs("outputs", exist_ok=True)

# ==========================================
# AI OBSERVABILITY PLAN
# ==========================================

observability = {

    "api_logging":
    api_logs(),

    "model_tracking":
    model_output_tracking(),

    "error_monitoring":
    error_monitoring(),

    "metrics":
    metrics_collection()

}

with open(
    "outputs/ai_observability_plan.json",
    "w"
) as f:

    json.dump(
        observability,
        f,
        indent=4
    )

# ==========================================
# LOGGING STRUCTURE
# ==========================================

logging_structure = {

    "api_logs":
    True,

    "model_logs":
    True,

    "error_logs":
    True,

    "audit_logs":
    True,

    "logging_framework":
    "Centralized"

}

with open(
    "outputs/logging_structure.json",
    "w"
) as f:

    json.dump(
        logging_structure,
        f,
        indent=4
    )

# ==========================================
# MONITORING DASHBOARD DESIGN
# ==========================================

dashboard = dashboard_design()

with open(
    "outputs/monitoring_dashboard_design.json",
    "w"
) as f:

    json.dump(
        dashboard,
        f,
        indent=4
    )

# ==========================================
# ALERTING RULES
# ==========================================

alerts = alerting_rules()

with open(
    "outputs/alerting_rules.json",
    "w"
) as f:

    json.dump(
        alerts,
        f,
        indent=4
    )

# ==========================================
# OBSERVABILITY SUMMARY
# ==========================================

summary = {

    "system":
    "AI Monitoring & Observability",

    "logging_system":
    "Enabled",

    "dashboard_monitoring":
    "Designed",

    "alerting_system":
    "Configured",

    "audit_logging":
    audit_logs(),

    "status":
    "Completed"

}

with open(
    "outputs/observability_summary.json",
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

print("API LOGGING ENABLED")

print("AI METRICS COLLECTION ENABLED")

print("ERROR MONITORING CONFIGURED")

print("ALERTING RULES CREATED")

print("OBSERVABILITY DASHBOARD DESIGNED")

print("AI MONITORING & OBSERVABILITY COMPLETED\n")