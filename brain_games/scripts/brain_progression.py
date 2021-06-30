#!/usr/bin/env python

from brain_games.body_progression import body_progression
from brain_games.What_is_your_name import welcome_user


def main():
    name = welcome_user()
    limit_round = 3
    body_progression(name, limit_round)


if __name__ == '__main__':
    main()
