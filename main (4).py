import json
from utils.normalizer import normalize_text, extract_experience
from utils.formatter import format_transcript

# Load input
with open("data/sample_transcripts.json", "r") as f:
    transcripts = json.load(f)

# Load rules
with open("rules/normalization_rules.json", "r") as f:
    rules = json.load(f)

output = []

for record in transcripts:
    # Normalize text
    normalized_text = normalize_text(record["answer"], rules)

    # ✅ ONLY extract for experience category
    if record.get("category") == "experience":
        exp = extract_experience(normalized_text)
    else:
        exp = None   # IMPORTANT FIX

    # Format output
    formatted = format_transcript(record, normalized_text, exp)

    output.append(formatted)

# Save output
with open("output/structured_transcripts.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ Transcript processing completed successfully")