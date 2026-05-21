import os
import time

print("=" * 60)
print("DAY 63 - DEMO DATASET CREATION")
print("Zecpath AI Hiring System Simulation Started")
print("=" * 60)

modules = [

    # Dataset Generators
    "dataset_engine/resume_generator.py",
    "dataset_engine/job_description_generator.py",
    "dataset_engine/candidate_response_generator.py",

    # AI Simulations
    "dataset_engine/ats_simulator.py",
    "dataset_engine/screening_simulator.py",
    "dataset_engine/interview_simulator.py",
    "dataset_engine/pipeline_simulator.py",
    "dataset_engine/demo_summary_generator.py"
]

success_count = 0
failed_modules = []

for module in modules:

    print(f"\nRunning Module: {module}")

    start_time = time.time()

    result = os.system(f"python {module}")

    end_time = time.time()

    execution_time = round(end_time - start_time, 2)

    if result == 0:
        print(f"SUCCESS: {module}")
        print(f"Execution Time: {execution_time} sec")
        success_count += 1

    else:
        print(f"FAILED: {module}")
        failed_modules.append(module)

print("\n" + "=" * 60)
print("AI PIPELINE EXECUTION SUMMARY")
print("=" * 60)

print(f"Successful Modules : {success_count}")
print(f"Failed Modules     : {len(failed_modules)}")

if failed_modules:
    print("\nFAILED MODULES:")
    for failed in failed_modules:
        print(f"- {failed}")

else:
    print("\nALL MODULES EXECUTED SUCCESSFULLY")

print("\nFULL AI PIPELINE SIMULATION COMPLETED")
print("=" * 60)