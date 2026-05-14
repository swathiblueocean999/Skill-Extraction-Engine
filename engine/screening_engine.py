def analyze_answer(answer):

    text = answer.lower().strip()

    skills = []

    if "excel" in text:
        skills.append("excel")

    if "tally" in text:
        skills.append("tally")

    if "gst" in text:
        skills.append("gst")

    if "payroll" in text:
        skills.append("payroll")

    experience = False

    if "experience" in text or "worked" in text:
        experience = True

    availability = False

    if "immediately" in text:
        availability = True

    off_topic = False

    if "movies" in text or "cricket" in text:
        off_topic = True

    uncertainty = False

    if "don't know" in text or "maybe" in text or "not sure" in text:
        uncertainty = True

    missing_answer = False

    if text == "":
        missing_answer = True

    return {
        "skills": skills,
        "experience": experience,
        "availability": availability,
        "off_topic": off_topic,
        "uncertainty": uncertainty,
        "missing_answer": missing_answer
    }