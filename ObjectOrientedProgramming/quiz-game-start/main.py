#!/usr/bin/env python3


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


for quest in question_data:
    question = Question(quest['text'], quest['answer'])
    question_bank.append(question)
    

quiz = QuizBrain(question_bank)
quiz.next_question()