import json
from utils.intent_classifier import classify_intent
from utils.entity_extractor import extract_entities
from utils.validator import validate_answer
from utils.formatter import format_output

# Load input data
with open("data/sample_answers.json") as f:
    data = json.load(f)

results = []

for item in data:
    candidate_id = item.get("candidate_id")
    answer = item.get("answer", "")

    # Step 1: Intent Classification
    intents = classify_intent(answer)

    # Step 2: Entity Extraction
    entities = extract_entities(answer)

    # Step 3: Validation (off-topic, missing, vague)
    issues = validate_answer(intents, entities, answer)

    # Step 4: Format structured output
    structured_data = format_output(candidate_id, answer, intents, entities, issues)

    results.append(structured_data)

# Save output
with open("output/structured_answers.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Answer Understanding Engine Completed Successfully!")