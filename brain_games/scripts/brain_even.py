#!/usr/bin/env python

from brain_games.cli import welcome_user
from brain_games.questions import list_questions


def brain_even():
    print('Welcome to the Brain Games!')
    list_questions()


if __name__ == '__main__':
    brain_even()