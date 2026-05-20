def get_recommendation(decision):

    if decision == "Selected":
        return "Recommended for hiring"

    elif decision == "Hold / Review":
        return "Requires recruiter review"

    return "Not recommended for hiring"