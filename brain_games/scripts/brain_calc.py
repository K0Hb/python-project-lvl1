#!/usr/bin/env python

from brain_games.cli import welcome_user
from brain_games.calculation_rnd import generate_culc


def brain_calc():
    print('Welcome to the Brain Games!')
    generate_culc()


if __name__ == '__main__':
    brain_even()