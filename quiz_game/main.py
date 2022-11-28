from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []
for item in question_data:
    questionBank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(questionBank)

# for piece in quiz.questionList:
#     print(piece.text)
#     print(piece.answer)
while quiz.stillHasQuestions():
    quiz.nextQuestion()

print("You have completed the quiz.")
print("Your final score is {}/{}".format(quiz.score, len(questionBank)))
