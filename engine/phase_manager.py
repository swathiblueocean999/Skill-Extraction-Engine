def get_phase(question_index):

    if question_index == 0:
        return "Introduction"

    elif question_index <= 2:
        return "Core HR Questions"

    elif question_index <= 4:
        return "Role-based Evaluation"

    else:
        return "Closing"