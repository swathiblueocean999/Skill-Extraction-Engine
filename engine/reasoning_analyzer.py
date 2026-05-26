import re


def analyze_reasoning(answer):

    # CLEAN ANSWER

    cleaned_answer = answer.strip().lower()

    # REASONING KEYWORDS

    keywords = [

        "analyze",
        "because",
        "reason",
        "compare",
        "identify",
        "explain",
        "verify",
        "prioritize",
        "understand",
        "evaluate",
        "consider",
        "approach",
        "logic",
        "therefore",
        "conclude",
        "determine",
        "assess",
        "review"
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

    # ANALYTICAL WORDS

    analytical_words = [

        "analysis",
        "critical",
        "carefully",
        "accurate",
        "logical",
        "professional",
        "effective",
        "efficient",
        "detailed",
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

    analytical_detected = []

    for word in analytical_words:

        if word in cleaned_answer:
            analytical_detected.append(word)

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

    # ANALYTICAL SCORE

    analytical_score = min(
        len(analytical_detected) * 15,
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

        analytical_score * 0.20 +

        sentence_score * 0.10 +

        clarity_score * 0.15

    )

    # LIMIT SCORE

    if final_score > 100:
        final_score = 100

    # FINAL LEVEL

    if final_score >= 75:
        reasoning_level = "strong"

    elif final_score >= 50:
        reasoning_level = "average"

    else:
        reasoning_level = "weak"

    return {

        "score": final_score,

        "reasoning_level": reasoning_level,

        "matched_keywords": matched_keywords,

        "structure_detected": structure_detected,

        "analytical_detected": analytical_detected,

        "sentence_count": sentence_count,

        "word_count": word_count
    }