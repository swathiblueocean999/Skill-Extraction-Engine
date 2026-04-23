from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def score_text(jd_text, profile_text):
    jd_vec = model.encode(jd_text)
    prof_vec = model.encode(profile_text)

    score = cosine_similarity([jd_vec], [prof_vec])[0][0]
    return float(score)