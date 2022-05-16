from question import Question
from data import questions
from quiz_brain import QuizBrain

question_bank = []
for question in questions:
    question_bank.append(Question(question["q"], question["a"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've finished the quiz!")
print(f"Your score was: {quiz.score}/{len(quiz.question_list)}")
