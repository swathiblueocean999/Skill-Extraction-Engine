import json


def load_question_bank():
    with open("data/question_bank.json", "r") as file:
        return json.load(file)


def generate_questions(level, role_type):
    question_bank = load_question_bank()

    if level in question_bank:
        if role_type in question_bank[level]:
            return question_bank[level][role_type]

    return []