#!/usr/bin/env python
from brain_games.Congratulations_fail import Congratulations_fail

import prompt
import random


def body_progression(name):
    print('What number is missing in the progression?')
    expression = 1
    while expression <= 3:
        num1 = random.randint(1, 30)
        num2 = random.randint(30, 60)
        rnd_num = random.randint(1, 5)
        findex = random.randint(2, 10)
        correct_answer = num1 + (findex * rnd_num)
        print(correct_answer)
        progression_line = filter_string(num1, num2, correct_answer, rnd_num)
        print('Question:' + progression_line)
        answer = prompt.string('Your answer:')
        expression = Congratulations_fail(answer, correct_answer,
                                          name, expression)


def filter_string(num1, num2, correct_answer, rnd_num):
    index = 1
    result = ''
    while index < num2 and index <= 10:
        num1 = num1 + rnd_num
        x = num1 + rnd_num
        if x != correct_answer:
            result = result + " " + str(x)
            index += 1
        elif x == correct_answer:
            result += " " + ".."
            index += 1
    return result
