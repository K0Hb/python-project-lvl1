#!/usr/bin/env python

def Congratulations_fail(answer, correct_answer, name, expression):
    if int(answer) == correct_answer and expression == 3:
        print('Congratulations, ' + name + '!')
        expression += 1
        return expression
    elif int(answer) == correct_answer:
        expression += 1
        print('Correct!')
        return expression
    elif int(answer) != correct_answer:
        print(
            f'{answer} is wrong answer ;(. ' +
            f'Correct answer was {correct_answer}.'
        )
        print(f"Let's try again, {name}!")
        expression += 3
        return expression
