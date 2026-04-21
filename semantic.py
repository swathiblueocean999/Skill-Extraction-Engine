from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_semantic_score(text1, text2):
    if not text1 or not text2:
        return 0

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])

    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return float(score)