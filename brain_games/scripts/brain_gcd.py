#!/usr/bin/env python

from brain_games.body_gcd import body_gcd
from brain_games.What_is_your_name import welcome_user


def main():
    name = welcome_user()
    body_gcd(name)


if __name__ == '__main__':
    main()
