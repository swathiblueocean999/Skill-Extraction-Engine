import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

profiles_path = os.path.join(BASE_DIR, "demo_data", "candidate_profiles.json")
transcripts_path = os.path.join(BASE_DIR, "demo_data", "interview_transcripts.json")
scores_path = os.path.join(BASE_DIR, "demo_data", "demo_scores.json")

with open(profiles_path, "r", encoding="utf-8") as f:
    profiles = json.load(f)

with open(transcripts_path, "r", encoding="utf-8") as f:
    transcripts = json.load(f)

with open(scores_path, "r", encoding="utf-8") as f:
    scores = json.load(f)

print("\n HR INTERVIEW DEMO STARTED\n")

for cid, profile in profiles.items():

    print("=" * 50)

    print(f"Candidate ID : {cid}")
    print(f"Candidate Name : {profile['name']}")
    print(f"Role : {profile['role']}")
    print(f"Experience : {profile['experience']} years")

    print("\nInterview Transcript:")
    print(transcripts[cid])

    print(f"\nUnified Score : {scores[cid]}")

    print("=" * 50)

print("\n Interview Simulation Completed")