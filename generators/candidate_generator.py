import json
import random


skills_pool = [

    "Accounting",
    "Excel",
    "GST",
    "Tally",
    "Communication",
    "Leadership",
    "Python",
    "SQL",
    "Recruitment",
    "Problem Solving"

]


def generate_candidates():

    candidates = []

    for i in range(1, 101):

        candidate = {

            "candidate_id":
            f"C{i:03}",

            "name":
            f"Candidate_{i}",

            "skills":
            random.sample(skills_pool, 4),

            "experience":
            random.randint(0, 10),

            "score":
            random.randint(40, 98)
        }

        candidates.append(candidate)


    with open(
        "datasets/resumes/generated_100_candidates.json",
        "w"
    ) as file:

        json.dump(
            candidates,
            file,
            indent=4
        )


    print("100 Candidates Generated Successfully")