import json

print("Architecture Explanation Started")

architecture = {
    "frontend": "Recruiter Dashboard",
    "backend": "Python AI Engine",
    "database": "JSON Structured Storage",
    "pipeline": [
        "Resume Parsing",
        "ATS",
        "Screening",
        "Interview",
        "Decision"
    ],
    "deployment": "Production Ready"
}

with open(
    "final_outputs/architecture_summary.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(architecture, file, indent=4)

print("Architecture Explanation Completed")