import re

def extract_experience(text):
    """
    Extract experience in years from text.
    Handles:
    - "2 years experience" → 2
    - "fresher" / "no work experience" → 0
    - unrelated text → None
    """

    if not text:
        return None

    text = text.lower()

    # Handle fresher cases explicitly
    if "fresher" in text or "no work experience" in text:
        return 0

    # Extract numeric experience
    match = re.search(r"(\d+)\s+years?", text)
    if match:
        return int(match.group(1))

    # If nothing found
    return None


def normalize_text(text, rules):
    """
    Normalize raw text using rules:
    - lowercase
    - remove fillers
    - remove special characters
    - trim spaces
    """

    if not text:
        return ""

    # Lowercase
    if rules.get("lowercase"):
        text = text.lower()

    # Remove filler words
    for word in rules.get("remove_fillers", []):
        text = re.sub(rf"\b{word}\b", "", text)

    # Remove special characters
    if rules.get("remove_special_chars"):
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Trim extra spaces
    if rules.get("trim_spaces"):
        text = " ".join(text.split())

    return text