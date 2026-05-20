def get_role_weights(role):

    role_weights = {

        "Accountant": {
            "ats": 0.15,
            "screening": 0.15,
            "hr": 0.20,
            "technical": 0.20,
            "machine_test": 0.30
        }

    }

    return role_weights.get(role)