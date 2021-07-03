import random


Conditions = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    number = random.randint(0, 30)
    return number


def ask_question(number):
    print(f'Question: {number}')


def is_prime(number):
    start = 2
    while number > start:
        if number % start == 0:
            break
        start += 1
    return number == start


def decision(number):
    if is_prime(number):
        return 'yes'
    return 'no'
