#!/usr/bin/env python
import prompt
import random
from brain_games.filter_string import filter_string

def body_progression():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + ' !')
    print('What number is missing in the progression?')
    progression = 1 
    while progression <= 3:
        number1 = random.randint(1, 30)
        number2 = random.randint(30, 60)
        rnd_number = random.randint(1, 5)
        findex = random.randint(1, 10)
        number_x = number1 + (findex*rnd_number)
        print(filter_string(number1, number2, number_x, rnd_number))
        answer = prompt.string('Your answer:')
        if int(answer) == number_x:
            progression += 1
            print('Correct!')
            if progression == 4:
                print('Congratulations,' + name + '!')
        elif int(answer) != number_x:
            print(str(answer) + ' is wrong answer ;(. Correct answer was' + str(number_x) + ". \n Let's try again," + name + '!')
            break


