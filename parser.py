import re
import json


# ------------------------
# READ TEXT FILE
# ------------------------
def read_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Clean text
    text = text.replace("️", "")
    text = re.sub(r"\n{2,}", "\n", text)

    return text


# ------------------------
# SPLIT PROFILES (NUMBER BASED)
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
# PARSE PROFILE (FINAL FIX)
# ------------------------
def parse_profile(text):
    data = {
        "role": None,
        "responsibilities": [],
        "skills": [],
        "experience": None,
        "education": None
    }

    lines = [l.strip() for l in text.split("\n") if l.strip()]

    # ROLE
    if lines:
        role = re.sub(r"^\d+\.\s*", "", lines[0])
        data["role"] = role

    # RESPONSIBILITIES
    resp_section = re.search(
        r"Key Responsibilities[:\-]?(.*?)(Required Skills|Qualifications|Experience|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )
    if resp_section:
        items = re.findall(r"[•\-]\s*(.*)", resp_section.group(1))
        data["responsibilities"] = [i.strip() for i in items if i.strip()]

    # SKILLS
    skills_section = re.search(
        r"(Required Skills|Qualifications & Skills)[:\-]?(.*?)(Experience|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )
    if skills_section:
        items = re.findall(r"[•\-]\s*(.*)", skills_section.group(2))
        data["skills"] = [i.strip() for i in items if i.strip()]

    # EXPERIENCE (ONLY VALID PATTERNS)
    exp_patterns = [
        r"\d+\s*[-–]\s*\d+\s*years",
        r"\d+\s*to\s*\d+\s*years",
        r"\d+\+\s*years",
        r"\d+\s*years"
    ]

    for pattern in exp_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            data["experience"] = match.group(0).strip()
            break

    # EDUCATION (ONLY VALID DEGREE LINES)
    edu_patterns = [
        r"Bachelor[’'s]* degree.*",
        r"Master[’'s]* degree.*",
        r"B\.Com.*",
        r"M\.Com.*",
        r"CA\b.*",
        r"CMA\b.*",
        r"Degree in.*",
        r"Graduate in.*"
    ]

    for pattern in edu_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            data["education"] = match.group(0).strip()
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

    for profile in profiles:
        parsed = parse_profile(profile)
        results.append(parsed)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print("Parsing Completed Successfully!")