#!/usr/bin/env python
import prompt


def what_is_you_name():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + ' !')
    return name
