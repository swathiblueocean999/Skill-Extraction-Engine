import re


def check_structure(answer):

    # CLEAN ANSWER

    cleaned_answer = answer.strip().lower()

    # STRUCTURE WORDS

    structure_words = [

        "first",
        "second",
        "finally",
        "before",
        "after",
        "then",
        "because",
        "approach",
        "immediately",
        "therefore",
        "next",
        "initially",
        "lastly",
        "meanwhile",
        "consequently"
    ]

    # PROFESSIONAL FLOW WORDS

    professional_words = [

        "analyze",
        "identify",
        "verify",
        "evaluate",
        "implement",
        "improve",
        "communicate",
        "resolve",
        "support",
        "manage"
    ]

    # MATCH DETECTION

    structure_detected = []

    for word in structure_words:

        if word in cleaned_answer:
            structure_detected.append(word)

    professional_detected = []

    for word in professional_words:

        if word in cleaned_answer:
            professional_detected.append(word)

    # STRUCTURE SCORE

    structure_score = min(
        len(structure_detected) * 12,
        100
    )

    # PROFESSIONAL FLOW SCORE

    professional_score = min(
        len(professional_detected) * 10,
        100
    )

    # SENTENCE ANALYSIS

    sentences = re.split(r'[.!?]+', cleaned_answer)

    sentences = [s for s in sentences if s.strip()]

    sentence_count = len(sentences)

    if sentence_count >= 4:
        sentence_score = 100

    elif sentence_count == 3:
        sentence_score = 85

    elif sentence_count == 2:
        sentence_score = 70

    else:
        sentence_score = 40

    # WORD COUNT ANALYSIS

    word_count = len(cleaned_answer.split())

    if word_count >= 40:
        clarity_score = 100

    elif word_count >= 30:
        clarity_score = 85

    elif word_count >= 20:
        clarity_score = 70

    else:
        clarity_score = 50

    # FLOW QUALITY

    if (
        "first" in cleaned_answer and
        "then" in cleaned_answer and
        "finally" in cleaned_answer
    ):

        flow_score = 100

    elif (
        "first" in cleaned_answer and
        "then" in cleaned_answer
    ):

        flow_score = 75

    else:

        flow_score = 40

    # FINAL SCORE

    final_score = round(

        structure_score * 0.35 +

        professional_score * 0.20 +

        sentence_score * 0.20 +

        clarity_score * 0.15 +

        flow_score * 0.10

    )

    # LIMIT SCORE

    if final_score > 100:
        final_score = 100

    # FINAL LEVEL

    if final_score >= 75:
        structure_level = "strong"

    elif final_score >= 50:
        structure_level = "average"

    else:
        structure_level = "weak"

    return {

        "score": final_score,

        "structure_level": structure_level,

        "structure_detected": structure_detected,

        "professional_detected": professional_detected,

        "sentence_count": sentence_count,

        "word_count": word_count,

        "flow_score": flow_score
    }