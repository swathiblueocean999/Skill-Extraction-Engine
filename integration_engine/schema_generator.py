def request_response_schema():

    return {

        "request_schema": {

            "candidate_id":
            "string",

            "resume":
            "file/pdf",

            "role":
            "string"

        },

        "response_schema": {

            "ats_score":
            "float",

            "screening_score":
            "float",

            "final_decision":
            "string"

        }

    }