import json

print("Demo Timing Optimization Started")

timing = {
    "total_demo_time": "12 Minutes",
    "recommended_timing": {
        "Introduction": "2 Minutes",
        "System Demo": "6 Minutes",
        "Q&A": "4 Minutes"
    },
    "optimization_status": "Optimized"
}

with open(
    "demo_outputs/timing_optimization.json",
    "w"
) as f:
    json.dump(timing, f, indent=4)

print("Demo Timing Optimization Completed")