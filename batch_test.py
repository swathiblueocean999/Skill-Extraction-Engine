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


def process_jd(jd_id):
    jd_file = f"{BASE}/jds/jd_{jd_id}.txt"

    # 👉 skip if JD missing
    if not os.path.exists(jd_file):
        return None

    jd_text = load_text(jd_file)
    jd_vec = model.encode(jd_text)

    match_dir = f"{BASE}/test_resumes/jd_{jd_id}/match"
    nonmatch_dir = f"{BASE}/test_resumes/jd_{jd_id}/non_match"

    results = []

    # 👉 MATCH resumes
    if os.path.exists(match_dir):
        for f in os.listdir(match_dir):
            path = os.path.join(match_dir, f)
            vec = model.encode(load_text(path))
            score = cosine_similarity([jd_vec], [vec])[0][0]
            results.append((f, score))

    # 👉 NON-MATCH resumes
    if os.path.exists(nonmatch_dir):
        for f in os.listdir(nonmatch_dir):
            path = os.path.join(nonmatch_dir, f)
            vec = model.encode(load_text(path))
            score = cosine_similarity([jd_vec], [vec])[0][0]
            results.append((f, score))

    results.sort(key=lambda x: x[1], reverse=True)

    # 👉 SAVE separate output file
    out_file = f"{BASE}/output_jd_{jd_id}.txt"

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"===== JD {jd_id} RESULTS =====\n\n")

        for file, score in results:
            percent = int(score * 100)
            f.write(f"{file} → {percent}% → {label(score)}\n")

    print(f"✅ JD {jd_id} done")


def main():
    # 👉 JD 4 → JD 89
    for jd_id in range(4, 90):
        process_jd(jd_id)

    print("\n🎉 ALL OUTPUT GENERATED (JD 4–89)")


if __name__ == "__main__":
    main()