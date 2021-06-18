#!/usr/bin/env python

import prompt
import random
from brain_games.gcd_func import gcd_func


def body_gcd():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + ' !')
    print('Find the greatest common divisor of given numbers.')
    expression = 1
    while expression <= 3:
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 50)
        print('Question: ' + str(number1) + ' ' + str(number2))
        result = gcd_func(number1, number2)
        answer = prompt.string('Your answer:')
        if int(answer) == result:
            expression += 1
            print('Correct!')
            if expression == 4:
                print('Congratulations, ' + name + '!')
        elif int(answer) != result:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}.')
            print("Let's try again, " + name + '!')
            break
