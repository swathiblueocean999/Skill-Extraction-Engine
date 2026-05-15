def detect_fillers(answer):

    fillers = [
        "umm",
        "uh",
        "like",
        "actually",
        "basically",
        "you know"
    ]

    answer = answer.lower()

    filler_count = 0

    for filler in fillers:

        filler_count += answer.count(filler)

    penalty = filler_count * 5

    return {
        "filler_count": filler_count,
        "penalty": penalty
    }