def build_profile_text(p):
    return (
        p.get("role", "") + " " +
        " ".join(p.get("skills", [])) + " " +
        p.get("experience", "")
    )