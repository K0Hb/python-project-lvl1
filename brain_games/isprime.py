#!/usr/bin/env python

def isprime(number):
    for a in range(2, number):
        if (number % a) == 0:
            return False
            break
        elif (number // a) == 1:
            return True
            break
