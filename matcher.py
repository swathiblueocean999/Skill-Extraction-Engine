import json
import re


# ------------------------
# LOAD DATA
# ------------------------
with open("output.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

with open("resume.txt", "r", encoding="utf-8") as f:
    resume = f.read().lower()


# ------------------------
# CLEAN TEXT FUNCTION
# ------------------------
def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9 ]', '', text.lower())


resume_clean = clean_text(resume)


# ------------------------
# SMART MATCH FUNCTION
# ------------------------
def calculate_match(job, resume_text):
    score = 0
    total = 0

    skills = job.get("skills", [])

    for skill in skills:
        skill_clean = clean_text(skill)

        if not skill_clean:
            continue

        total += 1

        # 🔥 partial match check
        if skill_clean in resume_text:
            score += 1
        else:
            # check word-level match
            words = skill_clean.split()
            if any(word in resume_text for word in words):
                score += 0.5   # partial credit

    if total == 0:
        return 0

    return round((score / total) * 100, 2)


# ------------------------
# GENERATE REPORT
# ------------------------
with open("matching_report.txt", "w", encoding="utf-8") as report:

    report.write("=== Semantic Matching Results ===\n\n")

    for job in jobs:
        role = job.get("role") if job.get("role") else "Unknown Role"
        profile_id = job.get("profile_id", "N/A")

        score = calculate_match(job, resume_clean)

        report.write(f"Profile: {profile_id}\n")
        report.write(f"Role: {role}\n")
        report.write(f"Match Score: {score}%\n")
        report.write("------------------------------\n")

print("Matching report saved as 'matching_report.txt'")