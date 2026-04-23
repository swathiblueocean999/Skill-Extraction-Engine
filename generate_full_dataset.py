import os
import shutil
import random

BASE = "jd_project/test_resumes"

JD_START = 4
JD_END = 90   # 89까지

# 👉 simple resume skill pool
skills = [
    "Excel", "Tally", "GST", "TDS", "Accounting",
    "Ledger", "Reconciliation", "Invoicing",
    "Financial Reporting", "Bookkeeping"
]


# ----------------------------
# 1. CREATE JD STRUCTURE
# ----------------------------
def create_folders():
    for i in range(JD_START, JD_END):
        os.makedirs(f"{BASE}/jd_{i}/match", exist_ok=True)
        os.makedirs(f"{BASE}/jd_{i}/non_match", exist_ok=True)

    print("✅ JD folders created (4–89)")


# ----------------------------
# 2. COPY SAME NON-MATCH (from jd_1)
# ----------------------------
def copy_non_match():
    source = f"{BASE}/jd_1/non_match"

    for i in range(JD_START, JD_END):
        target = f"{BASE}/jd_{i}/non_match"

        if not os.path.exists(source):
            print("❌ jd_1 non_match missing")
            return

        if not os.path.exists(target):
            shutil.copytree(source, target)

    print("✅ Non-match copied to all JD folders")


# ----------------------------
# 3. GENERATE UNIQUE MATCH RESUMES
# ----------------------------
def generate_match():
    for i in range(JD_START, JD_END):
        folder = f"{BASE}/jd_{i}/match"

        for j in range(1, 5):
            text = f"""
Candidate Profile (JD {i})

Skills:
{random.choice(skills)}, {random.choice(skills)}, {random.choice(skills)}

Experience:
Worked on accounting tasks, financial records, and reporting.

Responsibilities:
Handled invoices, ledger updates, and reconciliation tasks.
"""

            with open(f"{folder}/match_{j}.txt", "w", encoding="utf-8") as f:
                f.write(text)

    print("✅ Unique match resumes generated")


# ----------------------------
# MAIN
# ----------------------------
def main():
    create_folders()
    copy_non_match()
    generate_match()

    print("\n🎉 FULL DATASET READY (JD 4–89)")


if __name__ == "__main__":
    main()