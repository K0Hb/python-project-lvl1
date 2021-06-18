#!/usr/bin/env python

def filter_string(number1, number2, zvx, rnd_number):
    index = 1
    result = ''
    while index < number2 and index <= 10:
        number1 = number1 + rnd_number
        x = number1 + rnd_number
        if x != zvx:
            result = result + " " + str(x)
            index += 1
        elif x == zvx:
            result += " " + ".."
            index += 1
    return result
