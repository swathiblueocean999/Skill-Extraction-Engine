class ConversationState:
    def __init__(self):
        self.current_question = 0
        self.answers = []
        self.retry_count = 0
        self.max_retries = 2

    def next_question(self):
        self.current_question += 1
        self.retry_count = 0

    def add_answer(self, answer):
        self.answers.append(answer)

    def repeat_question(self):
        self.retry_count += 1

    def can_retry(self):
        return self.retry_count < self.max_retries