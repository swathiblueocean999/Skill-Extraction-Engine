import re

def extract_years(text):
    matches = re.findall(r'(\d+)\s*year', text.lower())
    return sum(int(m) for m in matches)

def check_relevance(text):
    return "HIGH" if "account" in text.lower() else "LOW"

def detect_gap(text):
    return "YES" if "gap" in text.lower() else "NO"

def calculate_score(exp, relevance, gap):

    score = 0

    # 🔥 relevance weight
    if relevance == "HIGH":
        score += 50

    # 🔥 experience weight
    if exp >= 5:
        score += 30
    elif exp >= 2:
        score += 20

    # 🔥 gap weight
    if gap == "NO":
        score += 20

    return score


def process():

    input_file = "day10_output.txt"
    output_file = "ranked_profiles.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        data = f.read()

    profiles = re.split(r'\bPROFILE\s+\d+\b', data)[1:]
    profiles = [p.strip() for p in profiles if p.strip()]

    with open(output_file, "w", encoding="utf-8") as f:

        for i, profile in enumerate(profiles, 1):

            exp = extract_years(profile)
            relevance = check_relevance(profile)
            gap = detect_gap(profile)

            score = calculate_score(exp, relevance, gap)

            f.write(f"""
=========================
PROFILE {i}
=========================

EXPERIENCE: {exp} years
RELEVANCE: {relevance}
GAP: {gap}
SCORE: {score}

""")

    print("✅ RANKING DONE")
    print("Profiles:", len(profiles))


process()