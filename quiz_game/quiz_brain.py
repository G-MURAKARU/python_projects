class QuizBrain:
    def __init__(self, questionList) -> None:
        self.questionNumber = 0
        self.score = 0
        self.questionList = questionList

    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionList)

    def checkAnswer(self, guess, answer):
        if guess.lower() == answer.lower():
            self.score += 1
            print(
                "You are correct! Your score is {}/{}.".format(
                    self.score, self.questionNumber
                )
            )
        else:
            print(
                "You're wrong. Final score is {}/{}.".format(
                    self.score, self.questionNumber
                )
            )

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        guess = input(
            "Q.{} {} (True/False?)".format(self.questionNumber, currentQuestion.text)
        )

        self.checkAnswer(guess, currentQuestion.answer)
