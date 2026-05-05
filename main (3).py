import os
from utils.formatter import format_questions


def main():
    input_file = "data/hr_questions.json"
    template_file = "templates/question_templates.json"
    output_file = "output/formatted_questions.json"

    print("🚀 Running HR Screening Pipeline...\n")

    format_questions(input_file, template_file, output_file)

    if os.path.exists(output_file):
        print(f"✅ Output generated: {output_file}")
    else:
        print("❌ Error generating output")


if __name__ == "__main__":
    main()