# ATS Demo Notes

## How to Run
python optimizer/main.py

## System Flow
1. Extract text from resume
2. Clean the text
3. Extract skills
4. Extract experience
5. Calculate score
6. Classify profile (Good / Average / Bad)

## Demo Profiles
- good_profile.txt → High score (Strong candidate)
- average_profile.txt → Medium score (Average candidate)
- bad_profile.txt → Low score (Weak candidate)

## Scoring Logic
The system checks:
- Relevant skills (Accounting, Excel, ERP, etc.)
- Years of experience

Based on these, a score is assigned.

## Output
- Skills extracted
- Experience detected
- Processing time
- Final classification

## Note
The system is optimized for fast processing and handles noisy resume data.