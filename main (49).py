
import os
import time

print("============================================================")
print("DAY 67 - MOCK DEMO DAY")
print("Zecpath AI Hiring System Demo Practice Started")
print("============================================================")

modules = [

    "demo_engine/mock_demo_runner.py",
    "demo_engine/stakeholder_qa_simulator.py",
    "demo_engine/explanation_review.py",
    "demo_engine/confidence_improver.py",
    "demo_engine/demo_timing_optimizer.py",
    "demo_engine/feedback_report_generator.py",
    "demo_engine/presentation_improver.py",
    "demo_engine/final_demo_readiness.py"

]

success = 0
failed = []

for module in modules:

    print("\n============================================================")
    print(f"Running Module: {module}")

    start = time.time()

    result = os.system(f'python "{module}"')

    end = time.time()

    if result == 0:
        print(f"SUCCESS: {module}")
        success += 1
    else:
        print(f"FAILED: {module}")
        failed.append(module)

    print(f"Execution Time: {round(end-start,2)} sec")

print("\n============================================================")
print("MOCK DEMO SUMMARY")
print("============================================================")

print(f"Successful Modules : {success}")
print(f"Failed Modules     : {len(failed)}")

if failed:
    print("\nFAILED MODULES:")
    for module in failed:
        print(f"- {module}")
else:
    print("\nALL DEMO MODULES EXECUTED SUCCESSFULLY")

print("\nFINAL DEMO PREPARATION COMPLETED")
print("============================================================")

