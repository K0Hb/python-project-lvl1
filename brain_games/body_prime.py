#!/usr/bin/env python

import prompt
import random
from brain_games.no_yes import no_yes


def body_prime(name, limit_round):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    Question = 1
    while Question <= limit_round:
        number = random.randint(-10, 103)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer:')
        prime = isprime(number)
        if prime == bool(True):
            correct_answer = 'yes'
        elif not prime or number <= 1:
            correct_answer = 'no'
        Question = no_yes(name, correct_answer, answer, Question)


def isprime(number):
    for a in range(2, number):
        if (number % a) == 0:
            return False
        elif (number // a) == 1:
            return True
