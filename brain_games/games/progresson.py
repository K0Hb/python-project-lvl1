import random


Conditions = 'What number is missing in the progression?'


def progression_generate(progression):
    indexes = len(progression) - 1
    index = random.randint(0, indexes)
    correct_answer = progression[index]
    progression[index] = '..'
    return correct_answer, progression


def generate_question():
    length = random.randint(5, 10)
    start = random.randint(0, 50)
    step = random.randint(1, 10)
    stop = length * step + start

    list = []

    for i in range(start, stop, step):
        list.append(str(i))

    expression = progression_generate(list)
    return expression


def ask_question(expression):
    correct_answer, progression = expression
    progression = ' '.join(progression)
    print(f'Question: {progression}')


def decision(expression):
    correct_answer, progression = expression
    return correct_answer
