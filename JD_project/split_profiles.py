import json

with open("output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Total profiles found:", len(data))

for i, item in enumerate(data):
    role = item.get("role", "")
    responsibilities = item.get("responsibilities", [])
    skills = item.get("skills", [])
    experience = item.get("experience", "")
    education = item.get("education", "")

    content = f"{i+1}. {role} - Job Description\n\n"

    content += "Responsibilities:\n"
    for r in responsibilities:
        content += f"- {r}\n"

    content += "\nSkills:\n"
    for s in skills:
        content += f"- {s}\n"

    content += f"\nExperience: {experience}\n"
    content += f"Education: {education}\n"

    with open(f"jds/jd_{i+1}.txt", "w", encoding="utf-8") as f:
        f.write(content)

print("✅ All JD files created perfectly from JSON")