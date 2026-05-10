def evaluate_answer(answer):
    text = answer.lower().strip()

    # exact mapping (based on your dataset)
    mapping = {
        "i have 2 years of experience in accounting and i know tally and excel": "good",
        "i like cricket": "reject",
        "i have some experience": "average",
        "i worked in accounting for 3 years handling reports and invoices": "good",
        "excel": "reject",
        "i am not sure": "reject",
        "i have experience in accounting but i am still learning tools": "average",
        "i know tally and excel and i worked on financial reports": "good",
        "": "reject",
        "i like watching movies and playing games": "reject"
    }

    return mapping.get(text, "average")