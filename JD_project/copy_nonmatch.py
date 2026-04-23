import shutil
import os

BASE = "jd_project/test_resumes"

source = f"{BASE}/jd_1/non_match"

for i in range(4, 90):
    target = f"{BASE}/jd_{i}/non_match"

    shutil.copytree(source, target, dirs_exist_ok=True)

print("✅ Non-match copied to JD 4–89")