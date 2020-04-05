from math import log, floor

def no_decimal_digit(num):
    return floor(log(num+1, 10)) + 1

