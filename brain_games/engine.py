import prompt

QUANTITY_ROUND = 3


def play(game):
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    counter_rounds = QUANTITY_ROUND
    while counter_rounds:
        text_question, correct_answer = game.generate_question()
        print(f'Question: {text_question}')
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
            counter_rounds -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            break
    if not counter_rounds:
        print(f'Congratulations, {name}!')
