#!/usr/bin/env python

from brain_games.calculation_rnd import generate_culc
from brain_games.What_is_your_name import welcome_user


def main():
    name = welcome_user()
    limit_round = 3
    generate_culc(name, limit_round)


if __name__ == '__main__':
    main()
