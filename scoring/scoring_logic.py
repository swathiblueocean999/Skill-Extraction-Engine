# scoring/scoring_logic.py
import json

def calculate_score(candidate_skills, job_requirements):
    
    if not job_requirements:
        return 0.0
    
    # candidate_skills, job_requirements removing case sensitivity and extra spaces
    candidate_skills = [s.lower().strip() for s in candidate_skills]
    job_requirements = [r.lower().strip() for r in job_requirements]
    
    matched = [s for s in candidate_skills if s in job_requirements]
    
    # score = matched skills / total job requirements * 100
    score = (len(matched) / len(job_requirements)) * 100
    return round(score, 2)

# 4 resume datasets(Latest Data 2026)
candidates = [
    {
        "name": "Rachelle Beaudry",
        "skills": ["Financial Analysis", "Budgeting", "Risk Management", "Taxation", "Accounting Software"]
    },
    {
        "name": "Sebastian Bennett",
        "skills": ["Auditing", "Financial Accounting", "Expense Reporting", "Accounts Receivable", "Leadership"]
    },
    {
        "name": "Richard Sanchez",
        "skills": ["Design Process", "Project Management", "Digital Marketing", "Negotiation", "Critical Thinking"]
    },
    {
        "name": "Juliana Silva",
        "skills": ["Critical Thinking", "Digital Marketing", "Graphic Design", "Project Management"]
    }
]

# skills (Job Description)
job_reqs = ["Financial Analysis", "Taxation", "Accounting Software", "Auditing", "Budgeting"]

if __name__ == "__main__":
    print("\n--- RESUME SCORING RESULTS (2026) ---")
    print(f"{'Candidate Name':<20} | {'Score':<10}")
    print("-" * 35)

    for person in candidates:
        score = calculate_score(person["skills"], job_reqs)
        print(f"{person['name']:<20} | {score}%")


        import json # JSON file handling library for saving results

results_data = []

for person in candidates:
    score = calculate_score(person["skills"], job_reqs)
    # data dictionary for each candidate to be saved in JSON
    results_data.append({
        "name": person["name"],
        "score": score,
        "matched_skills_count": len(set(person["skills"]).intersection(set(job_reqs)))
    })

# JSON file path to save the results
file_path = "scoring/resume_scores.json"
with open(file_path, "w") as json_file:
    json.dump(results_data, json_file, indent=4)

print(f"\n✅ Successfully saved results to '{file_path}'!")