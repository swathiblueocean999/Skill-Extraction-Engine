from fastapi import FastAPI
import json

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# MODEL LOAD (once only)
model = SentenceTransformer("all-MiniLM-L6-v2")


# -------------------------
# LOAD DATA SAFELY
# -------------------------
with open("output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# SAFE HANDLING (IMPORTANT FIX)
if isinstance(data, dict):
    profiles = data.get("profiles", [])
else:
    profiles = data


with open("jd_1.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()


# -------------------------
# TEXT BUILDER
# -------------------------
def build_profile_text(p):
    return (
        str(p.get("role", "")) + " " +
        " ".join(p.get("skills", [])) + " " +
        str(p.get("experience", ""))
    )


# -------------------------
# ROOT CHECK
# -------------------------
@app.get("/")
def home():
    return {"message": "ATS API Running Successfully"}


# -------------------------
# SCORING ENDPOINT
# -------------------------
@app.get("/score")
def score_profiles():

    jd_vec = model.encode(jd_text)

    results = []

    for p in profiles:
        text = build_profile_text(p)
        prof_vec = model.encode(text)

        score = cosine_similarity([jd_vec], [prof_vec])[0][0]

        results.append({
            "profile_id": p.get("profile_id"),
            "score": float(score)
        })

    # SORT
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return {
        "total": len(profiles),
        "shortlisted": results[:5]
    }