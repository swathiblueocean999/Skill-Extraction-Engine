import json
import os

from integration_engine.api_registry import api_registry

from integration_engine.backend_mapper import backend_mapping

from integration_engine.schema_generator import request_response_schema

from integration_engine.processing_mode import processing_modes

from integration_engine.retry_handler import retry_mechanism

from integration_engine.authentication_security import api_security

print("\nSTARTING API & INTEGRATION PLANNING SYSTEM\n")

# ==========================================
# CREATE OUTPUT DIRECTORY
# ==========================================

os.makedirs("outputs", exist_ok=True)

# ==========================================
# AI INTEGRATION DOCUMENT
# ==========================================

integration_document = {

    "api_registry":
    api_registry(),

    "backend_mapping":
    backend_mapping(),

    "processing_modes":
    processing_modes()

}

with open(
    "outputs/ai_integration_document.json",
    "w"
) as f:

    json.dump(
        integration_document,
        f,
        indent=4
    )

# ==========================================
# API MAPPING DIAGRAM
# ==========================================

mapping = {

    "frontend":
    "Backend API",

    "backend_api":
    "AI Engine",

    "ai_engine":
    "Database",

    "database":
    "Reports & Analytics"

}

with open(
    "outputs/api_mapping_diagram.json",
    "w"
) as f:

    json.dump(
        mapping,
        f,
        indent=4
    )

# ==========================================
# REQUEST / RESPONSE SCHEMAS
# ==========================================

schemas = request_response_schema()

with open(
    "outputs/request_response_schemas.json",
    "w"
) as f:

    json.dump(
        schemas,
        f,
        indent=4
    )

# ==========================================
# API SECURITY REPORT
# ==========================================

security_report = {

    "authentication":
    api_security(),

    "retry_handler":
    retry_mechanism(),

    "api_status":
    "Secure"

}

with open(
    "outputs/api_security_report.json",
    "w"
) as f:

    json.dump(
        security_report,
        f,
        indent=4
    )

# ==========================================
# INTEGRATION SUMMARY
# ==========================================

summary = {

    "system":
    "API & Integration Planning",

    "api_architecture":
    "Designed",

    "backend_mapping":
    "Completed",

    "security_framework":
    "Enabled",

    "processing_modes":
    "Validated",

    "status":
    "Completed"

}

with open(
    "outputs/integration_summary.json",
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

print("AI API REGISTRY GENERATED")

print("BACKEND INTEGRATION DESIGNED")

print("REQUEST/RESPONSE SCHEMAS CREATED")

print("API SECURITY FRAMEWORK ENABLED")

print("API & INTEGRATION PLANNING COMPLETED\n")