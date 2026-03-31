import re
import csv

# ---------- READ FILE ----------
with open("full_extracted_text.txt", "r", encoding="utf-8") as f:
    text = f.read()


# ---------- SPLIT ----------
def split_profiles(text):
    profiles = []
    for i in range(1, 90):
        pattern = rf"{i}\.\s(.*?)(?=\n{i+1}\.\s|$)"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            profiles.append(match.group(1).strip())
    return profiles


# ---------- DEGREE ----------
def extract_degree(profile):
    patterns = ["b.com", "bba", "mba", "m.com", "bachelor", "master"]
    for p in patterns:
        if p in profile.lower():
            return p.upper()
    return "Not Mentioned"


# ---------- FIELD ----------
def extract_field(profile):
    fields = ["commerce", "finance", "accounting", "business"]
    for f in fields:
        if f in profile.lower():
            return f.capitalize()
    return "Not Mentioned"


# ---------- INSTITUTION ----------
def extract_institution(profile):
    for line in profile.split("\n"):
        if "college" in line.lower() or "university" in line.lower():
            return line.strip()
    return "Not Mentioned"


# ---------- YEAR ----------
def extract_year(profile):
    match = re.search(r"(20\d{2})", profile)
    return match.group(1) if match else "Not Mentioned"


# ---------- CERTIFICATIONS ----------
def extract_certifications(profile):
    keywords = ["gst", "tally", "ca", "cma", "excel"]
    found = []

    for k in keywords:
        if k in profile.lower():
            found.append(k.upper())

    return ", ".join(found) if found else "Not Mentioned"


# ---------- NORMALIZATION ----------
def normalize_degree(degree):
    mapping = {
        "B.COM": "Bachelor of Commerce",
        "MBA": "Master of Business Administration",
        "M.COM": "Master of Commerce"
    }
    return mapping.get(degree, degree)


# ---------- CERTIFICATION TAGGING ----------
def tag_certifications(cert):
    if "CA" in cert or "CMA" in cert:
        return "Professional"
    elif "GST" in cert or "TALLY" in cert:
        return "Technical"
    elif "EXCEL" in cert:
        return "Tool आधारित"
    else:
        return "General"


# ---------- PROCESS ----------
profiles = split_profiles(text)

results = []

for i, profile in enumerate(profiles, 1):
    degree = extract_degree(profile)
    field = extract_field(profile)
    inst = extract_institution(profile)
    year = extract_year(profile)
    cert = extract_certifications(profile)

    norm_degree = normalize_degree(degree)
    cert_tag = tag_certifications(cert)

    results.append([
        i, degree, field, inst, year, cert, norm_degree, cert_tag
    ])


# ---------- SAVE ----------
with open("final_day11_full_output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "Profile", "Degree", "Field", "Institution", "Year",
        "Certifications", "Normalized Degree", "Certification Tag"
    ])

    writer.writerows(results)


print("✅ FULL OUTPUT CREATED")
print("Total Profiles:", len(results))