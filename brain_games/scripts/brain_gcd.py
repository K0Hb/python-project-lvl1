#!/usr/bin/env python

from brain_games.body_gcd import body_gcd
from brain_games.What_is_your_name import welcome_user


def main():
    name = welcome_user()
    limit_round = 3
    body_gcd(name, limit_round)


if __name__ == '__main__':
    main()
