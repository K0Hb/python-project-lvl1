import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
START_NUMBER = 0
FINISH_NUMBER = 100


def generate_question():
    number = random.randint(START_NUMBER, FINISH_NUMBER)
    return number


def ask_question(number):
    text_question = f'Question: {number}'
    return text_question


def is_even(number):
    return number % 2 == 0


def decision(number):
    if is_even(number):
        return 'yes'
    return 'no'
