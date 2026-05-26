import re


def check_problem_solving(answer):

    # CLEAN ANSWER

    cleaned_answer = answer.strip().lower()

    # PROBLEM SOLVING KEYWORDS

    keywords = [

        "solve",
        "improve",
        "fix",
        "correct",
        "manage",
        "reduce",
        "efficient",
        "identify",
        "verify",
        "support",
        "analyze",
        "compare",
        "evaluate",
        "approach",
        "process",
        "solution",
        "workflow",
        "optimize",
        "implement",
        "resolve"
    ]

    # STRUCTURE WORDS

    structure_words = [

        "first",
        "then",
        "finally",
        "before",
        "after",
        "because",
        "therefore",
        "immediately"
    ]

    # PROFESSIONAL WORDS

    professional_words = [

        "professional",
        "accurate",
        "responsible",
        "carefully",
        "efficiently",
        "effectively",
        "organized",
        "systematic"
    ]

    # MATCH DETECTION

    matched_keywords = []

    for word in keywords:

        if word in cleaned_answer:
            matched_keywords.append(word)

    structure_detected = []

    for word in structure_words:

        if word in cleaned_answer:
            structure_detected.append(word)

    professional_detected = []

    for word in professional_words:

        if word in cleaned_answer:
            professional_detected.append(word)

    # KEYWORD SCORE

    keyword_score = min(
        len(matched_keywords) * 8,
        100
    )

    # STRUCTURE SCORE

    structure_score = min(
        len(structure_detected) * 20,
        100
    )

    # PROFESSIONAL SCORE

    professional_score = min(
        len(professional_detected) * 15,
        100
    )

    # SENTENCE ANALYSIS

    sentences = re.split(r'[.!?]+', cleaned_answer)

    sentences = [s for s in sentences if s.strip()]

    sentence_count = len(sentences)

    if sentence_count >= 3:
        sentence_score = 100

    elif sentence_count == 2:
        sentence_score = 75

    else:
        sentence_score = 50

    # WORD COUNT

    word_count = len(cleaned_answer.split())

    if word_count >= 35:
        clarity_score = 100

    elif word_count >= 25:
        clarity_score = 80

    elif word_count >= 15:
        clarity_score = 60

    else:
        clarity_score = 40

    # FINAL SCORE

    final_score = round(

        keyword_score * 0.35 +

        structure_score * 0.20 +

        professional_score * 0.20 +

        sentence_score * 0.10 +

        clarity_score * 0.15

    )

    # LIMIT SCORE

    if final_score > 100:
        final_score = 100

    # FINAL LEVEL

    if final_score >= 75:
        performance_level = "strong"

    elif final_score >= 50:
        performance_level = "average"

    else:
        performance_level = "weak"

    return {

        "score": final_score,

        "performance_level": performance_level,

        "matched_keywords": matched_keywords,

        "structure_detected": structure_detected,

        "professional_detected": professional_detected,

        "sentence_count": sentence_count,

        "word_count": word_count
    }