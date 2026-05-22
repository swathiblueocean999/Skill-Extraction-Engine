
import json

with open('job_description_schema.json', 'r') as f:
    data = json.load(f)
    print("JSON Schema loaded successfully!")
    print(json.dumps(data, indent=4))