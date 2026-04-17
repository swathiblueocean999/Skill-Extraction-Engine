import re

def normalize_text(text):
    if not text:
        return ""
    return text.lower().strip()


def normalize_experience(exp):
    if not exp:
        return 0
    match = re.search(r'\d+', exp)
    return int(match.group()) if match else 0


def normalize_skills(skills):
    if not skills:
        return []
    return [skill.lower().strip() for skill in skills]