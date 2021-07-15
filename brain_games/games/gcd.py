import random


TASK = 'Find the greatest common divisor of given numbers.'
START_NUMBER = 0
FINISH_NUMBER_ONE = 100
FINISH_NUMBER_TWO = 100


def generate_question():
    number1 = random.randint(START_NUMBER, FINISH_NUMBER_ONE)
    number2 = random.randint(START_NUMBER, FINISH_NUMBER_TWO)
    return number1, number2


def ask_question(expression):
    number1, number2 = expression
    text_question = f'Question: {number1} {number2}'
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    correct_answer = str(number1 + number2)
    return text_question, correct_answer
