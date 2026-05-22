import json

print("Problem Statement Generation Started")

data = {
    "problem": "Manual hiring processes are slow, inconsistent, and difficult to scale.",
    "challenge": "Recruiters face screening overload and delayed hiring decisions.",
    "industry_need": "AI-driven recruitment automation"
}

with open("presentations/ai_demo_presentation.json", "w") as f:
    json.dump(data, f, indent=4)

print("Problem Statement Generated")