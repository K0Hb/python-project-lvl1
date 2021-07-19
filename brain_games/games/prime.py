import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_NUBMER = 2
FINISH_NUMBER = 57


def generate_question():
    number = random.randint(START_NUBMER, FINISH_NUMBER)
    text_question = number
    if is_prime(number):
        correct_answer = 'yes'
        return text_question, correct_answer
    correct_answer = 'no'
    return text_question, correct_answer


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, (number // 2) + 1):
        if number % divisor == 0:
            return False
    return True
