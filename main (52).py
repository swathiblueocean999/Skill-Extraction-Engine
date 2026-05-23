import subprocess
import time

modules = [
    "demo_engine/live_demo_runner.py",
    "demo_engine/architecture_explainer.py",
    "demo_engine/ai_model_explainer.py",
    "demo_engine/scoring_logic_explainer.py",
    "demo_engine/knowledge_transfer.py",
    "demo_engine/code_walkthrough_generator.py",
    "demo_engine/final_report_generator.py",
    "demo_engine/evaluation_preparation.py"
]

success = 0
failed = 0

print("=" * 60)
print("DAY 70 - FINAL DEMO & HANDOVER")
print("Zecpath AI Final System Demonstration Started")
print("=" * 60)

for module in modules:

    print("\n" + "=" * 60)
    print(f"Running Module: {module}")

    start = time.time()

    result = subprocess.run(
        ["python", module],
        text=True
    )

    end = time.time()

    if result.returncode == 0:
        print(f"SUCCESS: {module}")
        success += 1
    else:
        print(f"FAILED: {module}")
        failed += 1

    print(f"Execution Time: {round(end - start, 2)} sec")

print("\n" + "=" * 60)
print("FINAL DEMO SUMMARY")
print("=" * 60)

print(f"Successful Modules : {success}")
print(f"Failed Modules     : {failed}")

if failed == 0:
    print("\nALL FINAL DEMO MODULES EXECUTED SUCCESSFULLY")

print("\nFINAL AI SYSTEM HANDOVER COMPLETED")
print("=" * 60)