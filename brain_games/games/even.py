import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
START_NUMBER = 0
FINISH_NUMBER = 100


def generate_question():
    number = random.randint(START_NUMBER, FINISH_NUMBER)
    return number


def ask_question(number):
    text_question = f'Question: {number}'
    if is_even(number):
        correct_answer = 'yes'
    correct_answer = 'no'
    return text_question, correct_answer


def is_even(number):
    return number % 2 == 0
