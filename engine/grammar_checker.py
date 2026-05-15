def check_grammar(answer):

    answer = answer.lower()

    score = 100

    grammar_issues = [
        "myself",
        "little bit",
        "okay communication",
        "i knows",
        "me worked"
    ]

    for issue in grammar_issues:

        if issue in answer:
            score -= 20

    if len(answer.split()) < 4:
        score -= 20

    return max(score, 20)