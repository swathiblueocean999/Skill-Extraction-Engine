import os
import json

from engines.aptitude_engine import analyze_answer
from engines.hr_summary_engine import generate_hr_summary


# ================================
# PATHS
# ================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

answers_file = os.path.join(BASE_DIR, "data", "candidate_answers.json")

analysis_output_file = os.path.join(BASE_DIR, "output", "interview_analysis.json")
aptitude_output_file = os.path.join(BASE_DIR, "output", "aptitude_results.json")
aptitude_summary_file = os.path.join(BASE_DIR, "output", "aptitude_summary.json")

hr_json_file = os.path.join(BASE_DIR, "output", "hr_summary_report.json")
hr_text_file = os.path.join(BASE_DIR, "output", "hr_summary_report.txt")

interview_summary_file = os.path.join(BASE_DIR, "output", "interview_summary_report.json")


# ================================
# LOAD DATA
# ================================
with open(answers_file, "r", encoding="utf-8") as f:
    candidate_answers = json.load(f)


# ================================
# ANALYZE CANDIDATES
# ================================
analysis_results = []
aptitude_results = []

for candidate in candidate_answers:

    answer = candidate.get("answer", "")

    result = analyze_answer(answer)

    full_result = {
        "candidate_id": candidate.get("candidate_id"),
        "question_id": candidate.get("question_id"),
        "answer": answer,
        "analysis": result["analysis"],
        "aptitude_score": result["aptitude_score"],
        "final_status": result["final_status"]
    }

    analysis_results.append(full_result)
    aptitude_results.append(full_result)


# ================================
# SAVE INTERVIEW ANALYSIS
# ================================
os.makedirs(os.path.join(BASE_DIR, "output"), exist_ok=True)

with open(analysis_output_file, "w", encoding="utf-8") as f:
    json.dump(analysis_results, f, indent=2)


# ================================
# SAVE APTITUDE RESULTS
# ================================
with open(aptitude_output_file, "w", encoding="utf-8") as f:
    json.dump(aptitude_results, f, indent=2)


# ================================
# GENERATE SUMMARY
# ================================
hr_summary = generate_hr_summary(analysis_results)


# ================================
# SAVE JSON SUMMARY
# ================================
with open(hr_json_file, "w", encoding="utf-8") as f:
    json.dump(hr_summary, f, indent=2)


# ================================
# SAVE TEXT REPORT
# ================================
with open(hr_text_file, "w", encoding="utf-8") as f:

    f.write("=====================================\n")
    f.write(" DAY 39 - HR SUMMARY REPORT\n")
    f.write("=====================================\n\n")

    f.write(f"Total Candidates : {hr_summary['total_candidates']}\n")
    f.write(f"Strong Candidates: {hr_summary['strong_candidates']}\n")
    f.write(f"Average Candidates: {hr_summary['average_candidates']}\n")
    f.write(f"Weak Candidates  : {hr_summary['weak_candidates']}\n\n")

    f.write("TOP CANDIDATES:\n")
    for c in hr_summary.get("top_candidates", []):
        f.write(f"- {c['candidate_id']} | Score: {c['aptitude_score']} | {c['final_status']}\n")


# ================================
# TERMINAL OUTPUT
# ================================
print("\n=====================================")
print(" DAY 39 - HR SUMMARY GENERATED")
print("=====================================\n")

print(f"Interview Analysis Saved : {analysis_output_file}")
print(f"Aptitude Results Saved   : {aptitude_output_file}")
print(f"Aptitude Summary Saved   : {aptitude_summary_file}")
print(f"HR JSON Report Saved     : {hr_json_file}")
print(f"HR Text Report Saved     : {hr_text_file}")
print(f"Interview Summary Saved  : {interview_summary_file}")

print("\n=========== FINAL SUMMARY ===========")
print(f"Total Candidates : {hr_summary['total_candidates']}")
print(f"Strong Candidates: {hr_summary['strong_candidates']}")
print(f"Average Candidates: {hr_summary['average_candidates']}")
print(f"Weak Candidates  : {hr_summary['weak_candidates']}")
print("=====================================\n")