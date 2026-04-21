from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

print("Loading model... please wait ⏳")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Read file content
def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# ✅ YOUR FOLDER PATH (DON'T CHANGE)
resume_folder = "JD_Project/resumes"
jd_folder = "JD_Project/jds"

# Load resumes
resumes = {}
for file in os.listdir(resume_folder):
    if file.endswith(".txt"):
        resumes[file] = read_text(os.path.join(resume_folder, file))

# Load job descriptions
jds = {}
for file in os.listdir(jd_folder):
    if file.endswith(".txt"):
        jds[file] = read_text(os.path.join(jd_folder, file))

# Similarity function
def get_similarity(text1, text2):
    emb1 = model.encode(text1)
    emb2 = model.encode(text2)
    return cosine_similarity([emb1], [emb2])[0][0]

# Matching process
print("\n=== SEMANTIC MATCHING RESULTS ===\n")

for r_name, r_text in resumes.items():
    for j_name, j_text in jds.items():
        score = get_similarity(r_text, j_text)

        # Match level
        if score > 0.75:
            label = "Strong Match"
        elif score > 0.5:
            label = "Moderate Match"
        else:
            label = "Low Match"

        print(f"Resume: {r_name} | JD: {j_name} | Score: {round(score*100,2)}% | {label}")

print("\n=== DONE ✅ ===")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("results here")