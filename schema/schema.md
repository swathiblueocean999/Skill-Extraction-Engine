# Transcript Data Schema

## Fields

- candidate_id: Unique candidate identifier
- job_id: Job role identifier
- question_id: HR question mapping ID
- question: Question asked
- answer: Candidate response
- timestamp: Time of response
- confidence: Speech-to-text confidence score (0-1)

## Notes

- Each candidate will have multiple records
- Each record represents one Q&A interaction
- Data should be normalized before processing