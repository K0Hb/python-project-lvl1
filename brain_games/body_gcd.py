#!/usr/bin/env python
from brain_games.Congratulations_fail import Congratulations_fail

import prompt
import random


def body_gcd(name, limit_round):
    print('Find the greatest common divisor of given numbers.')
    Question = 1
    while Question <= limit_round:
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 50)
        print(f'Question: {number1} {number2}')
        correct_answer = gcd_func(number1, number2)
        answer = prompt.string('Your answer:')
        Question = Congratulations_fail(answer, correct_answer,
                                        name, Question)


def gcd_func(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    gcd = number1 + number2
    return gcd
