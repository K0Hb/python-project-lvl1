#!/usr/bin/env python

from brain_games.calculation_rnd import generate_culc
from brain_games.What_is_your_name import welcome_user
from brain_games.Congratulations_fail import Congratulations_fail()


def main():
    name = welcome_user()
    generate_culc(name)
    Congratulations_fail()


if __name__ == '__main__':
    main()
