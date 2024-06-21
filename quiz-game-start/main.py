from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_obj = Question(i['text'], i['answer'])
    question_bank.append(question_obj)

quiz_obj = QuizBrain(question_bank)
while quiz_obj.still_has_question():
    quiz_obj.next_question()
print("You've completed the quiz.")
print(f"Your final score is {quiz_obj.score}/{quiz_obj.question_number}")
