#!/usr/bin/env python3


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


for quest in question_data:
    question = Question(quest['question'], quest['correct_answer'])
    question_bank.append(question)
    

quiz = QuizBrain(question_bank)

while quiz.still_has_questions:
    quiz.next_question()

print("You've completed the quiz")
print("Your final score was: {0}/{1}".format(quiz.score, quiz.question_number))