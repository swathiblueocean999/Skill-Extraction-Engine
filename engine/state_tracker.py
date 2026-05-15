class ConversationState:

    def __init__(self):

        self.current_question = 0
        self.followups = []

    def next_question(self):

        self.current_question += 1

    def add_followup(self, question):

        self.followups.append(question)

    def already_asked(self, question):

        return question in self.followups