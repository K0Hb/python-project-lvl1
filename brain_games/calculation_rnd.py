#!/usr/bin/env python
import prompt
import random
from brain_games.operator import eval_binary_expr


def generate_culc():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    expression = 1
    while expression <= 3:
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 50)
        addition = '+'
        subtraction = "-"
        multiplication = '*'
        rnd_oper = random.choice([addition, subtraction, multiplication])
        print('Question: ' + str(number1) + ' ' + rnd_oper + ' ' + str(number2))
        result = eval_binary_expr(number1, rnd_oper, number2)
        answer = prompt.string('Your answer:')
        if int(answer) == result:
            expression += 1
            print('Correct!')
            if expression == 4:
                print('Congratulations, ' + name + '!')
        elif int(answer) != result:
            print(str(answer) + ' is wrong answer ;(. Correct answer was ' + str(result) + ".")
            print("Let's try again, " + name + '!')
            break
