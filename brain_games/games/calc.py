import random

OPERATOR = ['+', '-', '*']
TASK = 'What is the result of the expression?'
START_NUMBER = 0
FINISH_NUMBER_ONE = 50
FINISH_NUMBER_TWO = 15


def generate_question():
    number1 = random.randint(START_NUMBER, FINISH_NUMBER_ONE)
    number2 = random.randint(START_NUMBER, FINISH_NUMBER_TWO)
    operation = random.choice(OPERATOR)
    return number1, operation, number2


def ask_question(expression):
    number1, operation, number2 = expression
    text_question = f'Question: {number1} {operation} {number2}'
    if operation == '+':
        correct_answer = str(number1 + number2)
        return text_question, correct_answer
    elif operation == '-':
        correct_answer = str(number1 - number2)
        return text_question, correct_answer
    correct_answer = str(number1 * number2)
    return text_question, correct_answer
