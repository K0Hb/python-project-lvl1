#!/usr/bin/env python

def Congratulations_fail(answer, correct_answer, name, Question):
    if int(answer) == correct_answer and Question == 3:
        print('Congratulations, ' + name + '!')
        Question += 1
        return Question
    elif int(answer) == correct_answer:
        Question += 1
        print('Correct!')
        return Question
    elif int(answer) != correct_answer:
        print(
            f'{answer} is wrong answer ;(. '
            + f'Correct answer was {correct_answer}.'
        )
        print(f"Let's try again, {name}!")
        Question += 3
        return Question
