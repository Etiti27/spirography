class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions

    def still_more(self):
        if self.question_number < len(self.questions):
            return True
        else:
            return False
    def next_question(self):
        current_question = self.questions[self.question_number]


        self.question_number += 1
        input(f'Q {self.question_number}: {current_question.text} (True/False)  ')

