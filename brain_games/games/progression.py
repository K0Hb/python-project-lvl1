import random


TASK = 'What number is missing in the progression?'
START_NUBMER_LENGTH = 5
START_NUMBER_START = 0
START_NUMBER_STEP = 1
FIFNISH_NUMBER_LENGTH = 10
FIFNISH_NUMBER_START = 50
FIFNISH_NUMBER_STEP = 10


def function_gap_progression(progression):
    indexes = len(progression) - 1
    index = random.randint(0, indexes)
    correct_answer = progression[index]
    progression[index] = '..'
    return correct_answer, progression


def generate_question():
    length = random.randint(START_NUBMER_LENGTH, FIFNISH_NUMBER_LENGTH)
    start = random.randint(START_NUMBER_START, FIFNISH_NUMBER_START)
    step = random.randint(START_NUMBER_STEP, FIFNISH_NUMBER_STEP)
    stop = length * step + start

    list = []

    for i in range(start, stop, step):
        list.append(str(i))

    correct_answer, progression = function_gap_progression(list)

    progression = ' '.join(progression)
    text_question = progression
    return text_question, correct_answer
