import os
import json
import sys

# Make sure to add the parent directory to the path so we can import the scoring logic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scoring.scoring_logic import calculate_score

def run_tests():
    print("--- 🔍 Testing AI Scoring System ---")

    # test1. scoring
    test_skills = ["Python", "SQL"]
    job_reqs = ["Python", "SQL", "Docker"]
    expected_score = 66.67
    
    actual_score = calculate_score(test_skills, job_reqs)
    
    if actual_score == expected_score:
        print("✅ Test 1: Scoring Logic Passed!")
    else:
        print(f"❌ Test 1: Scoring Logic Failed! (Expected {expected_score}, got {actual_score})")

    # test2. JSON file creation
    json_path = "scoring/resume_scores.json"
    if os.path.exists(json_path):
        print(f"✅ Test 2: JSON File '{json_path}' successfully created!")
        
    
        with open(json_path, 'r') as f:
            data = json.load(f)
            if len(data) > 0:
                print(f"✅ Test 3: JSON File contains {len(data)} candidate records.")
            else:
                print("❌ Test 3: JSON File is empty!")
    else:
        print(f"❌ Test 2: JSON File not found at {json_path}!")

if __name__ == "__main__":
    run_tests()