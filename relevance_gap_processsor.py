import re

def check_relevance(text):
    return "HIGH" if "account" in text.lower() else "LOW"

def detect_gap(text):
    return "YES" if "gap" in text.lower() else "NO"

def process():

    input_file = "day10_output.txt"
    output_file = "final_with_relevance.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        data = f.read()

    # ✅ correct split
    profiles = re.split(r'\bPROFILE\s+\d+\b', data)[1:]
    profiles = [p.strip() for p in profiles if p.strip()]

    print("Profiles Found:", len(profiles))

    with open(output_file, "w", encoding="utf-8") as f:

        for i, profile in enumerate(profiles, 1):

            relevance = check_relevance(profile)
            gap = detect_gap(profile)

            f.write(f"""
=========================
PROFILE {i}
=========================

DATA:
{profile}

RELEVANCE: {relevance}
GAP DETECTED: {gap}

""")

    print("✅ DONE")

process()