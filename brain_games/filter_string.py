def filter_string(number1, number2, number_x, rnd_number):
    index = 0
    result = ''
    while index < number2 and index <= 10:
        number1 = number1 + rnd_number
        x = number1 + rnd_number
        if x != number_x :
            result = result + " " + str(x)
            index += 1
        elif x == number_x :
            result += " " + ".."  
            index += 1
    return result