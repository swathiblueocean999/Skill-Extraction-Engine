import os

print("🚀 Starting Optimization Pipeline...\n")

os.system("python optimization_engine/transcript_cleaner.py")
os.system("python optimization_engine/anomaly_detector.py")
os.system("python optimization_engine/score_refiner.py")
os.system("python optimization_engine/followup_stability.py")
os.system("python optimization_engine/speed_optimizer.py")

print("\n✅ Day 42 Optimization Completed")