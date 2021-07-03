import random


Conditions = 'Find the greatest common divisor of given numbers.'


def generate_question():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    return number1, number2


def ask_question(expression):
    number1, number2 = expression
    print(f'Question: {number1} {number2}')


def decision(expression):
    number1, number2 = expression
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return str(number1 + number2)
