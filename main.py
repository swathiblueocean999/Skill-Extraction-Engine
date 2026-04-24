import time
from optimizer.text_extractor import extract_text
from optimizer.cleaner import clean_text
from optimizer.entity_detector import extract_skills, extract_experience


file_path = "optimizer/utils/data/sample_resume.txt"


def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, round(end - start, 6)


try:
    print("\n=== ATS OPTIMIZATION PIPELINE STARTED ===\n")

    # STEP 1: TEXT EXTRACTION
    text, t1 = measure_time(extract_text, file_path)

    # STEP 2: CLEANING
    cleaned_text, t2 = measure_time(clean_text, text)

    # STEP 3: SKILLS EXTRACTION
    skills, t3 = measure_time(extract_skills, cleaned_text)

    # STEP 4: EXPERIENCE EXTRACTION
    experience, t4 = measure_time(extract_experience, cleaned_text)

    # TOTAL TIME
    total_time = round(t1 + t2 + t3 + t4, 6)

    # OUTPUT PRINT (TERMINAL)
    print("Skills:", skills)
    print("Experience:", experience)

    print("\n--- PERFORMANCE REPORT ---")
    print(f"Extraction Time : {t1} sec")
    print(f"Cleaning Time   : {t2} sec")
    print(f"Skills Time     : {t3} sec")
    print(f"Experience Time : {t4} sec")
    print("--------------------------------")
    print(f"Total Pipeline Time: {total_time} sec")

    # WARNINGS
    if not skills:
        print("WARNING: No skills detected")

    if not experience:
        print("WARNING: No experience detected")

    print("\n=== PIPELINE COMPLETED SUCCESSFULLY ===")

    # =========================
    # SAVE OUTPUT TO FILE
    # =========================
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("=== ATS OPTIMIZATION REPORT ===\n\n")

        f.write(f"Skills: {skills}\n")
        f.write(f"Experience: {experience}\n\n")

        f.write("--- Performance ---\n")
        f.write(f"Extraction Time : {t1} sec\n")
        f.write(f"Cleaning Time   : {t2} sec\n")
        f.write(f"Skills Time     : {t3} sec\n")
        f.write(f"Experience Time : {t4} sec\n")
        f.write("--------------------------------\n")
        f.write(f"Total Pipeline Time: {total_time} sec\n")

except Exception as e:
    print("ERROR OCCURRED:", str(e))