import re


def evaluate_scenario(answer):

    # CLEAN ANSWER

    cleaned_answer = answer.strip().lower()

    # SCENARIO KEYWORDS

    keywords = [

        "professional",
        "customer",
        "teamwork",
        "support",
        "issue",
        "resolve",
        "solution",
        "communicate",
        "calm",
        "respectfully",
        "manage",
        "understand",
        "assist",
        "cooperate",
        "respond",
        "handle",
        "guide",
        "help",
        "service",
        "relationship"
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

    # PROFESSIONAL BEHAVIOR WORDS

    professional_words = [

        "responsible",
        "carefully",
        "effective",
        "efficient",
        "organized",
        "accurate",
        "positive",
        "ethical",
        "patient",
        "confident"
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
        len(matched_keywords) * 7,
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
        scenario_level = "strong"

    elif final_score >= 50:
        scenario_level = "average"

    else:
        scenario_level = "weak"

    return {

        "score": final_score,

        "scenario_level": scenario_level,

        "matched_keywords": matched_keywords,

        "structure_detected": structure_detected,

        "professional_detected": professional_detected,

        "sentence_count": sentence_count,

        "word_count": word_count
    }