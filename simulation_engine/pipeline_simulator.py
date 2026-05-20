def simulate_pipeline(candidate):

    return {

        "resume_upload":
        "Completed",

        "ats_scoring":
        "Completed",

        "screening":
        "Completed",

        "hr_interview":
        "Completed",

        "technical_interview":
        "Completed",

        "machine_test":
        "Completed",

        "behavioral_analysis":
        "Completed",

        "integrity_check":
        "Completed",

        "final_decision":
        candidate["final_decision"]

    }