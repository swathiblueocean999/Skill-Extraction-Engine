import re
import csv

def extract_years(text):
    matches = re.findall(r'(\d+)\s*year', text.lower())
    return sum(int(m) for m in matches)

def check_relevance(text):
    return "HIGH" if "account" in text.lower() else "LOW"

def detect_gap(text):
    return "YES" if "gap" in text.lower() else "NO"

def calculate_score(exp, relevance, gap):

    score = 0

    if relevance == "HIGH":
        score += 50

    if exp >= 5:
        score += 30
    elif exp >= 2:
        score += 20

    if gap == "NO":
        score += 20

    return score


def process():

    input_file = "day10_output.txt"
    output_file = "final_profiles.csv"

    with open(input_file, "r", encoding="utf-8") as f:
        data = f.read()

    profiles = re.split(r'\bPROFILE\s+\d+\b', data)[1:]
    profiles = [p.strip() for p in profiles if p.strip()]

    with open(output_file, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        # header
        writer.writerow(["Profile", "Experience", "Relevance", "Gap", "Score"])

        for i, profile in enumerate(profiles, 1):

            exp = extract_years(profile)
            relevance = check_relevance(profile)
            gap = detect_gap(profile)
            score = calculate_score(exp, relevance, gap)

            writer.writerow([i, exp, relevance, gap, score])

    print("CSV FILE CREATED")
    print("Profiles:", len(profiles))


process()