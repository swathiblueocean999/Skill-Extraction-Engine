import os
import json
from utils.stt_engine import speech_to_text
from utils.cleaner import clean_text

audio_folder = "audio"
results = []

success = 0
failed = 0
total_confidence = 0

for file in os.listdir(audio_folder):
    if file.endswith(".wav"):
        path = os.path.join(audio_folder, file)

        # STT
        raw_text, confidence = speech_to_text(path)

        # Clean
        cleaned_text, status = clean_text(raw_text)

        # Word count
        word_count = len(cleaned_text.split()) if cleaned_text else 0

        if confidence > 0:
            success += 1
            total_confidence += confidence
        else:
            failed += 1

        results.append({
            "file": file,
            "raw_text": raw_text,
            "cleaned_text": cleaned_text,
            "confidence": confidence,
            "status": status,
            "word_count": word_count
        })

# Save output
with open("output/clean_transcripts.json", "w") as f:
    json.dump(results, f, indent=2)

# Generate report
avg_conf = total_confidence / success if success > 0 else 0

report = {
    "total_files": success + failed,
    "successful": success,
    "failed": failed,
    "average_confidence": round(avg_conf, 2)
}

with open("reports/stt_report.json", "w") as f:
    json.dump(report, f, indent=2)

print("✅ Processing Completed")