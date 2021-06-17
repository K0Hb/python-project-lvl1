def isprime(number):
    if number == 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
        else:
            return True