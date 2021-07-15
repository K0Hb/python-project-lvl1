import prompt

QUANTITY_ROUND = 3


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play(game):
    name = welcome_user()
    print(game.TASK)
    counter_rounds = QUANTITY_ROUND
    while counter_rounds:
        question = game.generate_question()
        text_question = game.ask_question(question)
        print(text_question)
        user_answer = prompt.string('Your answer: ')
        correct_answer = game.decision(question)
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
