def optimize_speed(total_candidates):

    if total_candidates <= 5:

        return "Fast Processing"

    elif total_candidates <= 20:

        return "Moderate Processing"

    return "High Processing Load"