import os

print("Architecture Diagram Generation Started")

os.makedirs("presentation_outputs", exist_ok=True)

diagram = """
Zecpath AI Hiring System Architecture

Candidate Resume
        |
        v
ATS Simulator
        |
        v
Screening Simulator
        |
        v
HR Interview Simulator
        |
        v
Technical Interview Simulator
        |
        v
Decision Engine
        |
        v
Final Hiring Report
"""

with open(
    "presentation_outputs/system_architecture.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(diagram)

print("Architecture Diagram Generated")