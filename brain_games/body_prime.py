#!/usr/bin/env python

import prompt
import random


def body_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    Question = 1
    while Question <= 3:
        number = random.randint(3, 103)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer:')
        prime = isprime(number)
        if answer == 'yes' and prime == bool(True):
            Question += 1
            print('Correct!')
            if Question == 4:
                print(f'Congratulations, {name}!')
        elif answer == 'no' and not prime:
            Question += 1
            print('Correct!')
            if Question == 4:
                print(f'Congratulations, {name}!')
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break


def isprime(number):
    for a in range(2, number):
        if (number % a) == 0:
            return False
            break
        elif (number // a) == 1:
            return True
            break
