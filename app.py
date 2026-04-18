from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/output")
def output_json():
    try:
        # JSON file read 
        with open("output.json", "r") as f:
            profiles = json.load(f)

        results = []

        for profile in profiles:
            score = score_resume(profile)

            results.append({
                "name": profile.get("name") or profile.get("profile_id"),
                "score": score
            })

        shortlisted = shortlist_candidates(results)

        return {
            "total": len(profiles),
            "shortlisted": shortlisted
        }

    except Exception as e:
        return {"error": str(e)}


# 🔹 Score calculation
def score_resume(profile):
    experience = profile.get("experience", 0)

    # None or empty 
    if not experience:
        experience = 0

    # string format handle like "5 years" or "3-5 years"    
    elif isinstance(experience, str):
        try:
            if "-" in experience:
                exp_part = experience.split("-")[-1]
                experience = int(exp_part.split()[0])
            else:
                experience = int(experience.split()[0])
        except:
            experience = 0

    # ensure integer
    elif not isinstance(experience, int):
        experience = 0

    skills = len(profile.get("skills", []))

    return experience * 2 + skills

# 🔹 Shortlist logic
def shortlist_candidates(results):
    return sorted(results, key=lambda x: x["score"], reverse=True)[:5]