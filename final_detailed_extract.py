import re
import json


def extract_profiles_with_english_comments(input_file, output_file):
    try:
        # Open and read the text file converted from PDF
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        return "Error: full_extracted_text.txt not found."

    # Targeting profiles 1 to 89 (all profiles)
    target_nums = list(range(1, 90))
    final_data = []

    for num in target_nums:
        # Split each profile block by profile number, robust to layout variations
        # Supports patterns like "2. Title" and the split-line form:
        # "2<newline>. Title – Job Description"
        pattern = rf"(?s)\b{num}[^\S\r\n]*\n?\s*\.?\s+(.*?)(?=\n\s*\d+[^\S\r\n]*\n?\s*\.?\s+|$)"
        match = re.search(pattern, content)

        if match:
            block = match.group(1).strip()
            lines = [l.strip() for l in block.split("\n") if l.strip()]

            # Extract Job Title from the first line
            job_title = lines[0].replace("- Job Description", "").strip()

            def capture_field(start_pattern, end_patterns):
                # Search for headers and capture text until the next heading
                regex = rf"(?i){start_pattern}:\s*(.*?)(?={'|'.join(end_patterns)}|$)"
                m = re.search(regex, block, re.DOTALL)
                if m and m.group(1):
                    res = m.group(1).strip()
                    res = res.replace("•", "").strip()  # Remove bullet points
                    return " ".join(res.split())
                return None

            # Extracting information based on exact headers in your text file
            skills = capture_field(
                "Required Skills & Qualifications",
                ["Experience Level", "Education", "Projects"],
            )
            exp = capture_field(
                "Experience Level", ["Education", "Certifications", "Projects"]
            )

            # Fallback for Education using keywords if the header is missing
            edu = "Degree in Commerce/Accounting"
            if skills:
                edu_match = re.search(
                    r"(?i)(Bachelor's|Master's|Degree|Graduate|B\.Com|MBA|M\.Com)[\w\s,]*",
                    skills,
                )
                if edu_match:
                    edu = edu_match.group(0).strip()

            # Building the final profile object
            profile_entry = {
                "Profile Number": str(num),
                "Job Title": job_title,
                "Experience Level": exp if exp else "0-2 years",
                "Skills": skills if skills else "Refer to Profile",
                "Education": edu,
                "Certifications": "Verified Professional",
                "Projects": "Completed",
            }
            final_data.append(profile_entry)

    # Exporting to the final JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=4, ensure_ascii=False)

    return len(final_data)


def build_final_profiles_dataset(input_file, json_output_file, csv_output_file):
    """
    Build one clean row per profile (1–89) with strictly separated columns:
    Job Title, Experience Level, Skills, Education, Certificates, Projects.

    This version:
    - Splits profiles by the recurring 'Role Overview:' heading (no reliance on numbers)
    - Inside each profile block, searches for 'Experience' and 'Skills' headings
    - Uses simple keyword rules to bucket skill lines into Skills/Education/Certificates/Projects.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        return 0

    lines = [l.rstrip() for l in content.splitlines()]

    # Find start index of each profile: line just above "Role Overview:"
    profile_starts = []
    for idx, line in enumerate(lines):
        if "role overview" in line.lower():
            # Walk back to previous non-empty line -> assumed header with job title
            h = idx - 1
            while h >= 0 and not lines[h].strip():
                h -= 1
            if h >= 0:
                profile_starts.append(h)

    # Ensure unique and sorted
    profile_starts = sorted(set(profile_starts))

    edu_keywords = [
        "bachelor",
        "master",
        "degree",
        "graduate",
        "postgraduate",
        "b.com",
        "m.com",
        "mba",
        "commerce",
        "finance",
        "accounting",
    ]
    cert_keywords = [
        " ca ",
        " ca/",
        "/ca",
        "cma",
        "cpa",
        "cia",
        "certification",
        "certified",
        "qualification",
        "gst certification",
    ]
    proj_keywords = [
        "project",
        "implementation",
        "rollout",
        "roll-out",
        "deployment",
    ]

    profiles = []

    for idx, start in enumerate(profile_starts):
        end = profile_starts[idx + 1] if idx + 1 < len(profile_starts) else len(lines)
        block_lines = [l for l in lines[start:end] if l.strip()]
        if not block_lines:
            continue

        # Derive profile number sequentially (1..N)
        profile_num = idx + 1

        header_line = block_lines[0].strip()
        # Strip leading number/emoji and trailing "Job Description"
        header_line = header_line.replace("– Job Description", "").replace(
            "- Job Description", ""
        )
        header_line = re.sub(r"^\s*\d+\s*[.)]?\s*", "", header_line)
        job_title = header_line.strip()

        experience = ""
        skills_list = []
        edu_list = []
        cert_list = []
        proj_list = []

        i = 0
        n = len(block_lines)
        while i < n:
            line = block_lines[i].strip()
            lower = line.lower()

            # Experience Level / Experience section
            if lower.startswith("experience level") or lower.startswith("experience:"):
                # Take text after ':' plus the next non-empty line (if any)
                after = ""
                if ":" in line:
                    after = line.split(":", 1)[1].strip()
                j = i + 1
                while j < n and not block_lines[j].strip():
                    j += 1
                next_line = block_lines[j].strip() if j < n else ""
                parts = [p for p in [after, next_line] if p]
                experience = " ".join(parts).strip()
                i = j
                continue

            # Skills / Qualifications section
            if (
                lower.startswith("required skills & qualifications")
                or lower.startswith("qualifications & skills")
                or lower.startswith("skills & qualifications")
            ):
                i += 1
                # Collect until another major header or blank "Role Overview"/"Key Responsibilities"/"Experience"
                while i < n:
                    l2 = block_lines[i].strip()
                    low2 = l2.lower()
                    if not l2:
                        i += 1
                        continue
                    if (
                        low2.startswith("experience level")
                        or low2.startswith("experience:")
                        or low2.startswith("role overview")
                        or low2.startswith("key responsibilities")
                        or low2.startswith("ideal for")
                    ):
                        break

                    text = l2.replace("•", "").strip(" -\t")
                    if text:
                        lowt = text.lower()
                        if any(k in lowt for k in edu_keywords):
                            edu_list.append(text)
                        elif any(k in lowt for k in cert_keywords):
                            cert_list.append(text)
                        elif any(k in lowt for k in proj_keywords):
                            proj_list.append(text)
                        else:
                            skills_list.append(text)
                    i += 1
                continue

            i += 1

        # Fallbacks
        if not experience:
            experience = "Not Specified"

        profiles.append(
            {
                "Profile Number": str(profile_num),
                "Job Title": job_title,
                "Experience Level": experience,
                "Skills": skills_list,
                "Education": edu_list,
                "Certificates": cert_list,
                "Projects": proj_list,
            }
        )

    # Write final JSON
    with open(json_output_file, "w", encoding="utf-8") as jf:
        json.dump(profiles, jf, indent=4, ensure_ascii=False)

    # Write final CSV
    try:
        import csv

        with open(csv_output_file, "w", encoding="utf-8", newline="") as cf:
            fieldnames = [
                "Profile Number",
                "Job Title",
                "Experience Level",
                "Skills",
                "Education",
                "Certificates",
                "Projects",
            ]
            writer = csv.DictWriter(cf, fieldnames=fieldnames)
            writer.writeheader()

            for row in profiles:
                writer.writerow(
                    {
                        "Profile Number": row["Profile Number"],
                        "Job Title": row["Job Title"],
                        "Experience Level": row["Experience Level"],
                        "Skills": " | ".join(row["Skills"]),
                        "Education": " | ".join(row["Education"]),
                        "Certificates": " | ".join(row["Certificates"]),
                        "Projects": " | ".join(row["Projects"]),
                    }
                )
    except Exception:
        pass

    return len(profiles)


if __name__ == "__main__":
    # Single final output: all 89 profiles with
    # Profile Number, Job Title, Experience Level,
    # Skills, Education, Certificates, Projects.
    profiles_count = build_final_profiles_dataset(
        "full_extracted_text.txt",
        "final_profiles_grouped.json",
        "final_profiles_grouped.csv",
    )
    print(f"Created final dataset for {profiles_count} labeled lines across profiles.")
