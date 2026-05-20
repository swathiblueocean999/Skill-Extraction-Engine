import os
import sys

print("\nSTARTING FINAL HR INTERVIEW AI DEMO\n", flush=True)

os.system("python demo_engine/interview_demo.py")

print("\n" + "=" * 60, flush=True)

os.system("python demo_engine/scoring_breakdown.py")

print("\n" + "=" * 60, flush=True)

os.system("python demo_engine/hiring_recommendation.py")

print("\nFINAL HR INTERVIEW AI DEMO COMPLETED", flush=True)