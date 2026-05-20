def refine_intent(profile):

    strengths = profile["Strengths"]

    weaknesses = profile["Weaknesses"]

    risks = profile["Risk Indicators"]

    # ==========================================
    # REMOVE DEFAULT VALUES
    # ==========================================

    actual_strengths = [

        item for item in strengths

        if item != "No major strength identified"
    ]

    actual_weaknesses = [

        item for item in weaknesses

        if item != "No major weakness identified"
    ]

    actual_risks = [

        item for item in risks

        if item != "No major risk detected"
    ]

    # ==========================================
    # INTENT ANALYSIS
    # ==========================================

    if len(actual_strengths) > len(actual_weaknesses):

        return "Positive Intent Detected"

    elif len(actual_weaknesses) > len(actual_strengths):

        return "Negative Intent Detected"

    elif len(actual_risks) > 0:

        return "Risk-Based Intent Alert"

    return "Neutral Intent"