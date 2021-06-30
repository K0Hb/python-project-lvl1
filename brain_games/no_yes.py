#!/usr/bin/env python

def no_yes(name, correct_answer, answer, Question):
    if answer == correct_answer and Question == 3:
        print(f'Congratulations, {name}!')
        Question += 1
        return Question
    elif answer == correct_answer:
        Question += 1
        print('Correct!')
        return Question
    elif answer != correct_answer:
        print(
            f'{answer} is wrong answer ;(. '
            + f'Correct answer was {correct_answer}.'
        )
        print(f"Let's try again, {name}!")
        Question += 3
        return Question
