#!/usr/bin/env python
# anw == answer
import prompt
import random


def list_quest():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + ' !')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    Question = 1
    while Question <= 3:
        number = random.randint(1, 100)
        print('Question: ' + str(number))
        anw = prompt.string('Your answer:')
        if number % 2 == 0 and anw == 'yes' or number % 2 != 0 and anw == 'no':
            Question += 1
            print('Correct!')
            if Question == 4:
                print('Congratulations, ' + name + '!')
        elif number % 2 == 0 and anw == 'no' or number == 0:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again, " + name + '!')
            break
        elif number % 2 != 0 and anw == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + '!')
            break
