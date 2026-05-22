import os
import time

print("=" * 60)
print("DAY 66 - PRESENTATION PREPARATION")
print("Zecpath AI Hiring System Demo Presentation Started")
print("=" * 60)

modules = [
    "presentation_engine/problem_statement_generator.py",
    "presentation_engine/ai_solution_generator.py",
    "presentation_engine/architecture_generator.py",
    "presentation_engine/demo_flow_generator.py",
    "presentation_engine/business_impact_generator.py",
    "presentation_engine/demo_script_generator.py",
    "presentation_engine/presentation_summary_generator.py"
]

success = 0
failed = []

for module in modules:
    print(f"\nRunning Module: {module}")

    start = time.time()
    result = os.system(f"python {module}")
    end = time.time()

    if result == 0:
        print(f"SUCCESS: {module}")
        success += 1
    else:
        print(f"FAILED: {module}")
        failed.append(module)

    print(f"Execution Time: {round(end - start, 2)} sec")

print("\n" + "=" * 60)
print("PRESENTATION PREPARATION SUMMARY")
print("=" * 60)

print(f"Successful Modules : {success}")
print(f"Failed Modules     : {len(failed)}")

if failed:
    print("\nFAILED MODULES:")
    for item in failed:
        print("-", item)
else:
    print("\nALL PRESENTATION MODULES EXECUTED SUCCESSFULLY")

print("\nAI DEMO PRESENTATION READY")
print("=" * 60)