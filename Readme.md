# ATS System - Day 17 Testing Report

## 1. Threshold Tuning
Current system uses a fixed threshold (score >= 30) for classification. Further optimization can improve accuracy.

## 2. False Negative Reduction
Some good candidates are misclassified as weak due to strict scoring rules. This can be improved by refining keyword weights.

## 3. Borderline Score Handling
Profiles with scores in the range of 25–40 may behave inconsistently. Better weighting strategy is required for stability.

## 4. Score Normalization
Current scoring system uses raw values (0–100). Converting to a normalized scale (0–1) can improve consistency and model comparison.