import random

operator = ['+', '-', '*']
Conditions = 'What is the result of the expression?'


def generate_question():
    number1 = random.randint(0, 50)
    number2 = random.randint(0, 15)
    operation = random.choice(operator)
    return number1, operation, number2


def ask_question(expression):
    number1, operation, number2 = expression
    print(f'Question: {number1} {operation} {number2}')


def decision(expression):
    number1, operation, number2 = expression
    if operation == '+':
        return str(number1 + number2)
    elif operation == '-':
        return str(number1 - number2)
    return str(number1 * number2)
