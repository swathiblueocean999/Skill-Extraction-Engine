# Day 35 – Communication Skill Evaluation

## Objective
This project evaluates candidate communication skills using AI-based analysis.  
The system measures fluency, grammar quality, vocabulary usage, clarity of explanation, answer structure, and filler word usage to generate a normalized communication score.

---

# Features

- Fluency evaluation
- Grammar quality checking
- Vocabulary analysis
- Clarity detection
- Answer structure evaluation
- Filler word detection
- Communication score generation (0–100)
- Bias normalization for fair scoring
- Communication level classification

---

# Project Structure

## Data
- `candidate_answers.json`
  - Stores sample candidate answers for evaluation.

## Docs
- `evaluation_notes.md`
  - Explains communication evaluation behavior and observations.

- `scoring_formula.md`
  - Documents communication scoring formula and logic.

## Engine
- `bias_normalizer.py`
  - Reduces scoring bias and normalizes scores.

- `clarity_analyzer.py`
  - Evaluates clarity of candidate explanations.

- `communication_scorer.py`
  - Calculates final communication score.

- `filler_detector.py`
  - Detects filler words such as “umm”, “uh”, and “like”.

- `fluency_checker.py`
  - Evaluates sentence continuity and fluency.

- `grammar_checker.py`
  - Checks grammar quality and sentence correctness.

- `structure_evaluator.py`
  - Evaluates answer structure and organization.

- `vocabulary_analyzer.py`
  - Analyzes vocabulary quality and word diversity.

## Utils
- `file_handler.py`
  - Handles JSON file reading and writing operations.

## Output
- `communication_scores.json`
  - Stores final communication evaluation outputs.

## Main
- `main.py`
  - Executes the complete communication evaluation system.

---

# Communication Evaluation Metrics

| Metric | Description |
|---|---|
| Fluency | Sentence continuity and smoothness |
| Grammar | Grammar quality and correctness |
| Vocabulary | Word variety and technical vocabulary |
| Clarity | Clarity of explanation |
| Structure | Answer organization and readability |
| Fillers | Detection of filler words |

---

# Communication Level Classification

| Score Range | Level |
|---|---|
| 75+ | Strong |
| 45–74 | Average |
| Below 45 | Weak |

---

# How to Run

```bash
python main.py