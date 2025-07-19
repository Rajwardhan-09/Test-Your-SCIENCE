class MCQ:
    def __init__(self, questionID, question, AnswerKey, option1, option2, option3, option4):
        self.questionID = questionID
        self.question = question
        self.AnswerKey = AnswerKey
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
      

    def __str__(self):
        return f"{self.questionID}: {self.question} (Answer: {self.AnswerKey})"
    
