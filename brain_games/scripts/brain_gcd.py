#!/usr/bin/env python

from brain_games.body_gcd import body_gcd
from brain_games.What_is_your_name import welcome_user
from brain_games.Congratulations_fail import Congratulations_fail


def main():
    welcome_user()
    body_gcd()
    Congratulations_fail()


if __name__ == '__main__':
    main()
