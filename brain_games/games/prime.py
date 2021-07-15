import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_NUBMER = 2
FINISH_NUMBER = 55


def generate_question():
    number = random.randint(START_NUBMER, FINISH_NUMBER)
    return number


def ask_question(number):
    text_question = f'Question: {number}'
    return text_question


def is_prime(number):
    START_NUBMER = 2
    for number_enumeration in range(START_NUBMER, number+1):
        if number % number_enumeration == 0:
            break
    return number == number_enumeration


def decision(number):
    if is_prime(number):
        return 'yes'
    return 'no'
