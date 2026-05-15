
# Day 37 – HR Interview Scoring Engine

## Objective

This project combines HR interview responses, communication quality, confidence indicators, and consistency analysis into a structured AI-based HR interview scoring system.

The system generates explainable HR scores using a weighted scoring model and normalized evaluation process.

---

# Features

- HR response relevance scoring
- Communication score integration
- Confidence score analysis
- Consistency evaluation
- Weight-based scoring system
- Explainable score breakdown
- Score normalization
- Final HR candidate classification

---

# Project Structure

## Data

### `candidate_hr_data.json`
Stores candidate HR interview evaluation data and scoring inputs.

---

# Docs

### `scoring_logic.md`
Explains HR interview scoring methodology and evaluation flow.

### `weight_system.md`
Documents score weight distribution and scoring priorities.

### `normalization_rules.md`
Explains score normalization logic for different interview lengths.

---

# Engine Modules

### `relevance_scorer.py`
Handles HR answer relevance scoring.

### `communication_weight.py`
Processes communication score contribution.

### `confidence_weight.py`
Processes behavioral confidence score contribution.

### `consistency_checker.py`
Evaluates response consistency.

### `score_normalizer.py`
Normalizes HR scores across different interview lengths.

### `score_explainer.py`
Generates explainable score breakdown for transparency.

### `hr_score_engine.py`
Calculates final HR interview score using weighted scoring logic.

### `weight_manager.py`
Stores configurable score weight parameters.

---

# Utils

### `file_handler.py`
Handles JSON file reading and writing operations.

---

# Output

### `hr_interview_scores.json`
Stores final HR interview scoring outputs and candidate evaluation reports.

---

# Main Execution

### `main.py`
Executes the complete HR interview scoring engine.

---

# Scoring Parameters

| Parameter | Purpose |
|---|---|
| Answer Relevance | Measures relevance of HR answers |
| Communication Score | Evaluates communication quality |
| Confidence Score | Measures behavioral confidence |
| Consistency | Checks consistency across responses |

---

# Weight Distribution

| Parameter | Weight |
|---|---|
| Answer Relevance | 40% |
| Communication Score | 25% |
| Confidence Score | 20% |
| Consistency Score | 15% |

---

# Final Classification

| Score Range | Status |
|---|---|
| 75+ | Strong |
| 50–74 | Average |
| Below 50 | Weak |

---

# How to Run

```bash
python main.py