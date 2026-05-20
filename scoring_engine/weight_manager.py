import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

weights_path = os.path.join(BASE_DIR, "input_data", "role_weights.json")


def get_role_weights(role="accountant"):

    with open(weights_path, "r", encoding="utf-8") as f:
        weights = json.load(f)

    return weights[role]