import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 👉 Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

BASE_PATH = "jd_project"


def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# 👉 Label logic
def get_label(score):
    if score >= 0.8:
        return "STRONG MATCH"
    elif score >= 0.6:
        return "GOOD MATCH"
    elif score >= 0.4:
        return "WEAK MATCH"
    else:
        return "NOT A MATCH"


def main(jd_id=1):
    # 👉 Load JD
    jd_path = f"{BASE_PATH}/jds/jd_{jd_id}.txt"
    jd_text = load_text(jd_path)
    jd_emb = model.encode(jd_text)

    # 👉 Folders
    match_folder = f"{BASE_PATH}/test_resumes/jd_{jd_id}/match"
    nonmatch_folder = f"{BASE_PATH}/test_resumes/jd_{jd_id}/non_match"

    results = []

    # 👉 Process MATCH resumes
    for file in os.listdir(match_folder):
        path = os.path.join(match_folder, file)
        text = load_text(path)
        emb = model.encode(text)

        score = cosine_similarity([jd_emb], [emb])[0][0]
        results.append((file, score))

    # 👉 Process NON-MATCH resumes
    for file in os.listdir(nonmatch_folder):
        path = os.path.join(nonmatch_folder, file)
        text = load_text(path)
        emb = model.encode(text)

        score = cosine_similarity([jd_emb], [emb])[0][0]
        results.append((file, score))

    # 👉 Sort results
    results.sort(key=lambda x: x[1], reverse=True)

    print("\n📊 RESULTS (Simple & Readable):\n")

    output_lines = []

    for file, score in results:
        percent = int(score * 100)
        label = get_label(score)

        line = f"{file} → {percent}% → {label}"
        print(line)
        output_lines.append(line)

    # 👉 Save to file
    os.makedirs(f"{BASE_PATH}", exist_ok=True)
    with open(f"{BASE_PATH}/output.txt", "w", encoding="utf-8") as f:
        for line in output_lines:
            f.write(line + "\n")

    print("\n✅ Output saved to jd_project/output.txt")


if __name__ == "__main__":
    main(jd_id=3)