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
        if prime == bool(True) and number > 1:
            correct_answer = 'yes'
        elif not prime or number <= 1:
            correct_answer = 'no'
        Question = no_yes(name, correct_answer, answer, Question)


def isprime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True
