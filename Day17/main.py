from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    # text = question["question"]
    # answer = question["correct_answer"]
    question_object = Question(text, answer)
    question_bank.append(question_object)

# for question in question_bank:
#     print(question.text)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()