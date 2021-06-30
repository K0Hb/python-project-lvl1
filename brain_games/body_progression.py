#!/usr/bin/env python
from brain_games.Congratulations_fail import Congratulations_fail

import prompt
import random


def body_progression(name, limit_round):
    print('What number is missing in the progression?')
    Question = 1
    while Question <= limit_round:
        num1 = random.randint(1, 30)
        num2 = random.randint(30, 60)
        rnd_num = random.randint(1, 5)
        findex = random.randint(2, 10)
        correct_answer = num1 + (findex * rnd_num)
        progression_line = filter_string(num1, num2, correct_answer, rnd_num)
        print('Question:' + progression_line)
        answer = prompt.string('Your answer:')
        Question = Congratulations_fail(answer, correct_answer,
                                        name, Question)


def filter_string(num1, correct_answer, rnd_num):
    list = []
    for i in range(num1, num1 + 10, rnd_num):
        if i == correct_answer:
            i = '..'
    list.append(i)
    return list
