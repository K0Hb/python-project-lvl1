#!/usr/bin/env python

from brain_games.body_gcd import body_gcd
from brain_games.What_is_your_name import welcome_user
from brain_games.Congratulations_fail import Congratulations_fail


def main():
    name = welcome_user()
    (answer, correct_answer, expression) = body_gcd(name)
    Congratulations_fail()


if __name__ == '__main__':
    main()
