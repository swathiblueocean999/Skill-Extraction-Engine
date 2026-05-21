import os
import time

print("============================================================")
print("DAY 64 - INTERNAL REVIEW & SYSTEM WALKTHROUGH")
print("Zecpath AI Hiring System Internal Evaluation Started")
print("============================================================")

modules = [
    "review_engine/ats_review.py",
    "review_engine/screening_review.py",
    "review_engine/hr_review.py",
    "review_engine/technical_review.py",
    "review_engine/decision_review.py",
    "review_engine/performance_review.py",
    "review_engine/improvement_planner.py"
]

success = 0
failed = 0

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
        failed += 1

    print(f"Execution Time: {round(end - start, 2)} sec")

print("\n============================================================")
print("INTERNAL REVIEW EXECUTION SUMMARY")
print("============================================================")

print(f"Successful Modules : {success}")
print(f"Failed Modules     : {failed}")

if failed == 0:
    print("\nALL REVIEW MODULES EXECUTED SUCCESSFULLY")

print("\nSYSTEM INTERNAL REVIEW COMPLETED")
print("============================================================")