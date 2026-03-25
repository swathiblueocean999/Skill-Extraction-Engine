import json
import re

INPUT_FILE = "final_profiles_grouped.json"
OUTPUT_FILE = "day10_output.txt"


def extract_years(text):
    matches = re.findall(r'(\d+)\s*[-+]?\s*(\d*)\s*years?', text.lower())

    total = 0
    for m in matches:
        if m[1]:
            total += int(m[1])
        else:
            total += int(m[0])

    return total


def process():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        for i, profile in enumerate(data, 1):

            # JSON structure change
            experience_text = str(profile)

            total_exp = extract_years(experience_text)

            f.write("\n=========================\n")
            f.write(f"PROFILE {i}\n")
            f.write("=========================\n")

            f.write("\nDATA:\n")
            f.write(experience_text + "\n")

            f.write(f"\nTOTAL EXPERIENCE: {total_exp} years\n")

        
    print("✅ DONE")
    print("Profiles:", len(data))


if __name__ == "__main__":
    process()