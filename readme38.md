# Day 38 – Aptitude Logic Design

## Objective

This project adds cognitive reasoning and situational evaluation into the AI HR interview system.

The system evaluates logical thinking, problem-solving ability, reasoning clarity, and situational judgment using structured AI evaluation logic.

---

# Features

- Reasoning-based question analysis
- Situational judgment evaluation
- Logical thinking scoring
- Problem-solving analysis
- Structured answer evaluation
- Decision-making analysis
- Explainable aptitude scoring

---

# Folder Structure

## Data

### `aptitude_questions.json`
Stores aptitude interview questions.

### `candidate_answers.json`
Stores candidate aptitude responses.

---

# Docs

### `aptitude_design.md`
Explains aptitude AI architecture.

### `reasoning_rules.md`
Documents reasoning evaluation logic.

### `scenario_framework.md`
Explains situational judgment framework.

### `scoring_logic.md`
Documents aptitude score calculation logic.

---

# Engine Modules

### `reasoning_analyzer.py`
Analyzes logical reasoning quality.

### `scenario_evaluator.py`
Evaluates situational handling capability.

### `logic_scorer.py`
Calculates final aptitude score.

### `clarity_detector.py`
Measures explanation clarity.

### `structure_checker.py`
Checks answer structure quality.

### `problem_solving_checker.py`
Evaluates problem-solving capability.

### `decision_analyzer.py`
Measures decision-making strength.

### `aptitude_engine.py`
Generates final aptitude evaluation status.

---

# Utils

### `file_handler.py`
Handles JSON file operations.

---

# Output

### `aptitude_results.json`
Stores final aptitude evaluation outputs.

---

# Final Status Classification

| Score | Status |
|---|---|
| 75+ | Strong |
| 50–74 | Average |
| Below 50 | Weak |

---

# How to Run

```bash
python main.py