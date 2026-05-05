import json
from engine.eligibility_engine import check_eligibility

# Load rules
with open("rules/job_rules.json") as f:
    job_rules = json.load(f)

# Load ATS results
with open("input/ats_output.json") as f:
    ats_data = json.load(f)

final_results = []

# Loop profiles
for profile in ats_data["results"]:

    # Loop roles
    for role, rule in job_rules.items():

        status = check_eligibility(profile, rule)

        final_results.append({
            "profile_id": profile["profile_id"],
            "role": role,
            "score": profile["score"],
            "status": status
        })

# Save output
with open("output/eligibility_results.json", "w") as f:
    json.dump(final_results, f, indent=2)

print("✅ Done: Eligibility Results Generated")