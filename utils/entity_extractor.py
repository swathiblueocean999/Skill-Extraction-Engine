import re

def extract_entities(answer):
    # Safety check (important)
    if not answer:
        return {
            "experience": None,
            "salary": None,
            "skills": [],
            "availability": None
        }

    answer = answer.lower()

    # 🔹 Extract experience (e.g., "2 years")
    exp_match = re.search(r'(\d+)\s+years?', answer)
    experience = exp_match.group(1) if exp_match else None

    # 🔹 Extract salary (numbers like 30000, 50000)
    sal_match = re.search(r'(\d{4,6})', answer)
    salary = sal_match.group(1) if sal_match else None

    # 🔹 Extract skills
    skills_list = ["tally", "excel", "python", "erp"]
    skills = [skill for skill in skills_list if skill in answer]

    # 🔹 Extract availability
    if "immediately" in answer:
        availability = "immediate"
    elif "notice" in answer:
        availability = "notice_period"
    else:
        availability = None

    # 🔥 FINAL RETURN (MOST IMPORTANT)
    return {
        "experience": experience,
        "salary": salary,
        "skills": skills,
        "availability": availability
    }