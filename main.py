import os

def main():

    print("\n====================================")
    print(" DAY 41 - UNIFIED SCORING ENGINE ")
    print("====================================\n")

    os.system("python scoring_engine/unified_score.py")

    report_text = """
====================================
 DAY 41 - UNIFIED SCORING ENGINE
====================================

✅ Accountant Unified Scoring Completed

Unified scoring completed successfully.
Reports saved in output folder.
"""

    with open("reports/day41_execution_report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)

    print("\nExecution report saved successfully.\n")


if __name__ == "__main__":
    main()