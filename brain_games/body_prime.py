import prompt
import random
from brain_games.isprime import isprime


def body_prime():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + ' !')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    Question = 1
    while Question <= 3:
        number = random.randint(2, 103)
        print('Question:' + str(number))
        answer = prompt.string('Your answer:')
        prime = isprime(number)
        if answer == 'yes' and prime == True:
            Question += 1
            print('Correct!')
            if Question == 4:
                print('Congratulations,' + name + '!')
        elif answer == 'no' and prime == False:
            Question += 1
            print('Correct!')
            if Question == 4:
                print('Congratulations,' + name + '!')
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again," + name + '!')
            break
