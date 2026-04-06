def get_similarity_score(text1, text2):
    if not text1 or not text2:
        return 0.0

    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    common = words1 & words2

    return len(common) / max(len(words2), 1)