#!/usr/bin/env python
from brain_games.Congratulations_fail import Congratulations_fail

import prompt
import operator
import random


def generate_culc(name):
    print('What is the result of the expression?')
    expression = 1
    while expression <= 3:
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 50)
        addition = '+'
        subtraction = "-"
        multiplication = '*'
        rnd_oper = random.choice([addition, subtraction, multiplication])
        print(f"Question: {str(number1)} {rnd_oper} {str(number2)}")
        correct_answer = eval_binary_expr(number1, rnd_oper, number2)
        answer = prompt.string('Your answer:')
        Congratulations_fail(answer, correct_answer, name, expression)


def eval_binary_expr(op1, oper, op2,
                     get_operator_fn={
                         '+': operator.add,
                         '-': operator.sub,
                         '*': operator.mul, }.get):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)
