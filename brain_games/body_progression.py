#!/usr/bin/env python

import prompt
import random
from brain_games.filter_string import filter_string


def body_progression():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + ' !')
    print('What number is missing in the progression?')
    progression = 1
    while progression <= 3:
        number1 = random.randint(1, 30)
        number2 = random.randint(30, 60)
        rnd_number = random.randint(1, 5)
        findex = random.randint(2, 10)
        zvx = number1 + (findex * rnd_number)
        progression_line = filter_string(number1, number2, zvx, rnd_number)
        print('Question:' + progression_line)
        answer = prompt.string('Your answer:')
        if int(answer) == zvx:
            progression += 1
            print('Correct!')
            if progression == 4:
                print('Congratulations, ' + name + '!')
        elif int(answer) != zvx:
            print(f'{answer} is wrong answer ;(. Correct answer was {zvx}.')
            print("Let's try again, " + name + '!')
            break
