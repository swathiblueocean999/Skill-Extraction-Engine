import json

# example output (your API result)
result = {
    "total": 89,
    "shortlisted": [
        {"profile_id": 1, "score": 0.78},
        {"profile_id": 9, "score": 0.68},
        {"profile_id": 3, "score": 0.68},
        {"profile_id": 5, "score": 0.62},
        {"profile_id": 6, "score": 0.62}
    ]
}

# SAVE TO FILE
with open("final_output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)

print("final_output.json created successfully")