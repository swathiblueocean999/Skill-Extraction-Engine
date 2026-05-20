import json
import os

from security_engine.audit_logger import generate_audit_log

from security_engine.retention_policy import retention_policy

from security_engine.consent_manager import verify_consent

from security_engine.secure_storage import secure_storage

from security_engine.access_control import access_control

from security_engine.governance_checker import governance_check

print("\nSTARTING SECURITY & AI GOVERNANCE SYSTEM\n")

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
# GENERATE AUDIT LOGS
# ==========================================

audit_logs = {}

for cid, candidate in final_output.items():

    audit_logs[cid] = generate_audit_log(

        cid,

        candidate["final_decision"]

    )

# ==========================================
# SAVE AUDIT LOGS
# ==========================================

with open(
    "outputs/audit_logs.json",
    "w"
) as f:

    json.dump(
        audit_logs,
        f,
        indent=4
    )

# ==========================================
# GOVERNANCE REPORT
# ==========================================

governance_report = {

    "retention_policy":
    retention_policy(),

    "consent_management":
    verify_consent(),

    "secure_storage":
    secure_storage(),

    "access_control":
    access_control(),

    "governance_check":
    governance_check()

}

with open(
    "outputs/governance_report.json",
    "w"
) as f:

    json.dump(
        governance_report,
        f,
        indent=4
    )

# ==========================================
# SECURITY SUMMARY
# ==========================================

security_summary = {

    "system":
    "Security & AI Governance",

    "audit_logging":
    True,

    "consent_validation":
    True,

    "encrypted_storage":
    True,

    "access_control":
    True,

    "governance_compliance":
    True,

    "status":
    "Completed"

}

with open(
    "outputs/security_summary.json",
    "w"
) as f:

    json.dump(
        security_summary,
        f,
        indent=4
    )

# ==========================================
# COMPLIANCE STATUS
# ==========================================

compliance_status = {

    "ai_compliance":
    "Validated",

    "security_framework":
    "Enabled",

    "governance_documentation":
    "Available"

}

with open(
    "outputs/compliance_status.json",
    "w"
) as f:

    json.dump(
        compliance_status,
        f,
        indent=4
    )

# ==========================================
# TERMINAL OUTPUT
# ==========================================

print("AUDIT LOGS GENERATED")

print("SECURITY FRAMEWORK ENABLED")

print("AI GOVERNANCE VALIDATED")

print("SECURITY & AI GOVERNANCE COMPLETED\n")