#!/usr/bin/env python
# anw == answer

import prompt
import random
from brain_games.no_yes import no_yes


def list_quest(name, limit_round):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    Question = 1
    while Question <= limit_round:
        number = random.randint(1, 100)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer:')
        if number % 2 == 0:
            correct_answer = 'yes'
        elif number % 2 != 0 or number == 0:
            correct_answer = 'no'
        Question = no_yes(name, correct_answer, answer, Question)
