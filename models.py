from datetime import datetime

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options  # List of options
        self.answer = answer    # Correct answer (string)

    def check_answer(self, user_answer):
        return user_answer == self.answer

class CBT:
    def __init__(self, questions):
        self.questions = questions  # List of Question objects
        self.current_index = 0
        self.score = 0
        self.start_time = datetime.now()
        self.end_time = None

    def get_current_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def submit_answer(self, user_answer):
        question = self.get_current_question()
        if question and question.check_answer(user_answer):
            self.score += 1
        self.current_index += 1
        if self.current_index == len(self.questions):
            self.end_time = datetime.now()

    def is_finished(self):
        return self.current_index >= len(self.questions)

    def get_duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        return None