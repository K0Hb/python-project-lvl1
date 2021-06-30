#!/usr/bin/env python

from brain_games.body_prime import body_prime
from brain_games.What_is_your_name import welcome_user


def main():
    name = welcome_user()
    limit_round = 3
    body_prime(name, limit_round)


if __name__ == '__main__':
    main()
