# list1에 list2 내용을 합하려면 append 가 아닌 "+=" 를 해야한다. append 를 하면 list2 자체가 들어가게 된다!!!
# get_questions_from_web() 함수에서 새로운 질의 목록 추가하는 부분 참고하기

import html
import requests

from question_model import Question

class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.current_question = None
        self.question_list = []
        self.get_questions_from_web()

    def still_has_questions(self):
        print(f"question_number: {self.question_number}")
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        q_text = html.unescape(self.current_question.text)
        self.question_number += 1
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            return True
        else:
            print("That's wrong.")
            return False
        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")

    def get_score(self):
        return self.score

    def get_questions_from_web(self):
        request_param = {
            "amount": 10,
            "type": "boolean"
        }

        response = requests.get("https://opentdb.com/api.php", params=request_param)
        response.raise_for_status()
        data = response.json()
        question_data = data['results']
        question_bank = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)

        #self.question_list = question_bank
        #self.question_list.append(question_bank)
        self.question_list += question_bank

