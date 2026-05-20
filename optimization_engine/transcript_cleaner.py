import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_path = os.path.join(BASE_DIR, "input_data", "raw_transcripts.json")
output_path = os.path.join(BASE_DIR, "output", "cleaned_transcripts.json")

with open(input_path, "r", encoding="utf-8") as f:
    transcripts = json.load(f)

cleaned = {}

for cid, text in transcripts.items():

    text = re.sub(r"\b(umm|uh|ah|ahh)\b", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text).strip()

    cleaned[cid] = text

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(cleaned, f, indent=4)

print("✅ Transcript Cleanup Completed")