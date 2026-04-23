import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

BASE = "jd_project"


def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def label(score):
    if score >= 0.8:
        return "STRONG MATCH"
    elif score >= 0.6:
        return "GOOD MATCH"
    elif score >= 0.4:
        return "WEAK MATCH"
    else:
        return "NOT A MATCH"


def process_jd(jd_id, report):
    jd_path = f"{BASE}/jds/jd_{jd_id}.txt"

    if not os.path.exists(jd_path):
        return

    jd_vec = model.encode(load_text(jd_path))

    match_folder = f"{BASE}/test_resumes/jd_{jd_id}/match"
    nonmatch_folder = f"{BASE}/test_resumes/jd_{jd_id}/non_match"

    results = []

    # MATCH
    if os.path.exists(match_folder):
        for f in os.listdir(match_folder):
            path = os.path.join(match_folder, f)
            vec = model.encode(load_text(path))
            score = cosine_similarity([jd_vec], [vec])[0][0]
            results.append((f, score))

    # NON-MATCH
    if os.path.exists(nonmatch_folder):
        for f in os.listdir(nonmatch_folder):
            path = os.path.join(nonmatch_folder, f)
            vec = model.encode(load_text(path))
            score = cosine_similarity([jd_vec], [vec])[0][0]
            results.append((f, score))

    results.sort(key=lambda x: x[1], reverse=True)

    # TOP CANDIDATES
    top1 = results[0] if len(results) > 0 else None
    top2 = results[1] if len(results) > 1 else None

    report.append(f"\n===== JD {jd_id} =====")

    if top1:
        report.append(f"🥇 Top 1: {top1[0]} → {round(top1[1]*100)}%")

    if top2:
        report.append(f"🥈 Top 2: {top2[0]} → {round(top2[1]*100)}%")


    # SAVE INDIVIDUAL OUTPUT
    out_file = f"{BASE}/output_jd_{jd_id}.txt"

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"===== JD {jd_id} RESULTS =====\n\n")

        for file, score in results:
            f.write(f"{file} → {round(score*100)}% → {label(score)}\n")

    print(f"✅ JD {jd_id} done")


def main():
    final_report = []

    # 🔥 FULL RANGE: JD 1 → JD 89
    for jd_id in range(1, 90):
        process_jd(jd_id, final_report)

    # FINAL REPORT FILE
    with open(f"{BASE}/FINAL_REPORT.txt", "w", encoding="utf-8") as f:
        for line in final_report:
            f.write(line + "\n")

    print("\n🎉 FINAL REPORT GENERATED (JD 1–89)")


if __name__ == "__main__":
    main()