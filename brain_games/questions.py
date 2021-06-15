#!/usr/bin/env python
import prompt
import random
from brain_games.cli import welcome_user


def list_questions():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + ' !')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    Question = 1
    while Question <= 3 :
        number = random.randint(1, 100)
        print('Question:' + str(number) )
        answer = prompt.string('Your answer:')
        if number % 2 == 0 and answer == 'yes':
            Question += 1
            print('Correct! \n Congratulations,' + name +'!')
        elif number % 2 != 0 and answer == 'no':
            Question += 1
            print('Correct! \n Congratulations,' + name +'!')
        elif number % 2 == 0 and answer == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.\n Let's try again," + name + '!' )
            break
        elif number % 2 != 0 and answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again," + name + '!' )
            break

