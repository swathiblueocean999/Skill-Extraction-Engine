import json

job_descriptions = [

    {
        "job_id": "JD101",
        "role": "Senior Accountant",
        "required_skills": [
            "Financial Reporting",
            "GST",
            "Taxation",
            "SAP FICO",
            "ERP Systems"
        ],
        "experience_required": "4-8 Years"
    },

    {
        "job_id": "JD201",
        "role": "Accounts Executive",
        "required_skills": [
            "Accounting",
            "Invoices",
            "Ledger Management",
            "Tally ERP"
        ],
        "experience_required": "1-3 Years"
    },

    {
        "job_id": "JD301",
        "role": "Trainee Accountant",
        "required_skills": [
            "Basic Accounting",
            "MS Excel"
        ],
        "experience_required": "Fresher"
    }
]

with open("datasets/demo_job_descriptions.json", "w") as f:
    json.dump(job_descriptions, f, indent=4)

print("Job Description Dataset Generated")