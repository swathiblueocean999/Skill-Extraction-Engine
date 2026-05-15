from engine.fluency_checker import check_fluency
from engine.grammar_checker import check_grammar
from engine.vocabulary_analyzer import analyze_vocabulary
from engine.clarity_analyzer import analyze_clarity
from engine.filler_detector import detect_fillers
from engine.structure_evaluator import evaluate_structure
from engine.bias_normalizer import normalize_score


def evaluate_communication(answer):

    fluency = check_fluency(answer)

    grammar = check_grammar(answer)

    vocabulary = analyze_vocabulary(answer)

    clarity = analyze_clarity(answer)

    structure = evaluate_structure(answer)

    filler_data = detect_fillers(answer)

    weighted_score = (

        fluency * 0.20 +
        grammar * 0.20 +
        vocabulary * 0.15 +
        clarity * 0.20 +
        structure * 0.15

    )

    final_score = weighted_score - filler_data["penalty"]

    final_score = normalize_score(final_score)

    if final_score >= 75:
        level = "strong"

    elif final_score >= 45:
        level = "average"

    else:
        level = "weak"

    return {

        "fluency_score": fluency,
        "grammar_score": grammar,
        "vocabulary_score": vocabulary,
        "clarity_score": clarity,
        "structure_score": structure,
        "filler_count": filler_data["filler_count"],
        "communication_score": final_score,
        "communication_level": level
    }