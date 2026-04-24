# ATS Architecture

## Pipeline Flow

Resume File
   ↓
Text Extractor
   ↓
Cleaner
   ↓
Entity Detector
   ↓
Scoring Engine
   ↓
Output

## Modules
- text_extractor.py → Reads file
- cleaner.py → Cleans text
- entity_detector.py → Extracts skills & experience
- main.py → Controls pipeline

## Design Type
Modular pipeline architecture