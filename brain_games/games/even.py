import random


Conditions = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    number = random.randint(0, 100)
    return number


def ask_question(number):
    print(f'Question: {number}')


def is_even(number):
    return number % 2 == 0


def decision(number):
    if is_even(number):
        return 'yes'
    return 'no'
