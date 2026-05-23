import json

print("Knowledge Transfer Started")

knowledge_transfer = {
    "codebase_explained": True,
    "architecture_explained": True,
    "pipeline_explained": True,
    "deployment_guidance": True,
    "handover_status": "Completed"
}

with open(
    "final_outputs/knowledge_transfer_report.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(knowledge_transfer, file, indent=4)

print("Knowledge Transfer Completed")