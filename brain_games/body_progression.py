#!/usr/bin/env python
from brain_games.Congratulations_fail import Congratulations_fail

import prompt
import random


def body_progression(name):
    print('What number is missing in the progression?')
    expression = 1
    while expression <= 3:
        number1 = random.randint(1, 30)
        number2 = random.randint(30, 60)
        rnd_number = random.randint(1, 5)
        findex = random.randint(2, 10)
        correct_answer = number1 + (findex * rnd_number)
        progression_line = filter_string(number1, number2, correct_answer, rnd_number)
        print('Question:' + progression_line)
        answer = prompt.string('Your answer:')
        Congratulations_fail(answer, correct_answer, name, expression)


def filter_string(number1, number2, zvx, rnd_number):
    index = 1
    result = ''
    while index < number2 and index <= 10:
        number1 = number1 + rnd_number
        x = number1 + rnd_number
        if x != zvx:
            result = result + " " + str(x)
            index += 1
        elif x == zvx:
            result += " " + ".."
            index += 1
    return result
