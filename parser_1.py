import re
import json


# ------------------------
# READ TEXT FILE
# ------------------------
def read_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("️", "")
    text = re.sub(r"\n{2,}", "\n", text)

    return text


# ------------------------
# SPLIT PROFILES
# ------------------------
def split_profiles(text):
    matches = list(re.finditer(r"\d{1,3}\.\s", text))

    profiles = []

    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        chunk = text[start:end].strip()

        if len(chunk) > 100:
            profiles.append(chunk)

    return profiles


# ------------------------
# PARSE PROFILE (FINAL)
# ------------------------
def parse_profile(text):
    data = {
        "profile_id": None,
        "role": None,
        "responsibilities": [],
        "skills": [],
        "experience": None,
        "education": None
    }

    lines = [l.strip() for l in text.split("\n") if l.strip()]

    # ------------------------
    # ROLE
    # ------------------------
    if lines:
        first_line = lines[0]
        first_line = re.sub(r"^\d+\.\s*", "", first_line)
        first_line = re.sub(r"Job Description.*", "", first_line, flags=re.IGNORECASE)
        data["role"] = first_line.strip()

    # ------------------------
    # RESPONSIBILITIES
    # ------------------------
    resp_section = re.search(
        r"Key Responsibilities[:\-]?(.*?)(Required Skills|Qualifications|Experience|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )
    if resp_section:
        items = re.findall(r"[•\-\*]\s*(.*)", resp_section.group(1))
        data["responsibilities"] = [i.strip() for i in items if i.strip()]

    # ------------------------
    # SKILLS + EDUCATION (IMPORTANT FIX)
    # ------------------------
    skills_section = re.search(
        r"(Required Skills.*?|Qualifications.*?)[:\-]?(.*?)(Experience|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    skills = []
    education = None

    if skills_section:
        items = re.findall(r"[•\-\*]\s*(.*)", skills_section.group(2))

        for item in items:
            item = item.strip()

            # 🎓 EDUCATION detect
            if re.search(r"(Bachelor|Master|B\.Com|M\.Com|Degree|Graduate|CA|CMA)", item, re.IGNORECASE):
                if not education:
                    education = item
                continue

            # 💼 SKILLS
            skills.append(item)

    data["skills"] = skills
    data["education"] = education

    # ------------------------
    # EXPERIENCE
    # ------------------------
    exp_patterns = [
        r"\d+\s*[-–]\s*\d+\s*years",
        r"\d+\s*to\s*\d+\s*years",
        r"\d+\+\s*years",
        r"\d+\s*years"
    ]

    for pattern in exp_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            data["experience"] = match.group(0)
            break

    return data


# ------------------------
# MAIN
# ------------------------
if __name__ == "__main__":
    input_file = "full_extracted_text.txt"
    output_file = "output.json"

    text = read_text(input_file)
    profiles = split_profiles(text)

    print("Total Profiles Found:", len(profiles))

    results = []

    for i, profile in enumerate(profiles, start=1):
        parsed = parse_profile(profile)
        parsed["profile_id"] = i
        results.append(parsed)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print("Parsing Completed Successfully!")