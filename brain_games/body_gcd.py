#!/usr/bin/env python

import prompt
import random


def body_gcd():
    print('Find the greatest common divisor of given numbers.')
    expression = 1
    while expression <= 3:
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 50)
        print(f'Question: {number1} {number2}')
        correct_answer = gcd_func(number1, number2)
        answer = prompt.string('Your answer:')
        return (answer, correct_answer, name, expression)


def gcd_func(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    gcd = number1 + number2
    return gcd
