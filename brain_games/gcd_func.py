#!/usr/bin/env python

def gcd_func(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    gcd = number1 + number2
    return gcd
