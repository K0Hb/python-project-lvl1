#!/usr/bin/env python

def Congratulations_fail(answer, correct_answer, name, expression):
    if int(answer) == correct_answer:
        expression += 1
        print('Correct!')
        if expression == 4:
            print('Congratulations, ' + name + '!')
    elif int(answer) != correct_answer:
        print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
        print(f"Let's try again, {name}")
    