class InterviewState:

    def __init__(self):
        self.current_question = 0
        self.responses = []
        self.followup_allowed = True

    def save_response(self, question_id, response):

        self.responses.append({
            "question_id": question_id,
            "response": response
        })

    def next_question(self):
        self.current_question += 1