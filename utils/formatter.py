import json


def format_questions(input_file, template_file, output_file):
    with open(input_file) as f:
        questions = json.load(f)

    with open(template_file) as f:
        templates = json.load(f)

    formatted = []

    for q in questions:
        template = templates.get(q["answer_type"], "{question}")

        q["formatted_question"] = template.replace("{question}", q["question"])

        # defaults
        if q["answer_type"] == "yes_no":
            q.setdefault("options", ["Yes", "No"])

        if q["answer_type"] == "number":
            q.setdefault("min", 0)
            q.setdefault("max", 10)

        formatted.append(q)

    with open(output_file, "w") as f:
        json.dump(formatted, f, indent=2)

    print("✅ Questions formatted successfully")