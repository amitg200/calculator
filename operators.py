import math


def add(x: float, y: float):
    return x + y


def subtract(x: float, y: float):
    return y - x


def negate(x: float):
    return -x


def multiply(x: float, y: float):
    return x * y


def divide(x: float, y: float):
    if y == 0: raise ValueError("Division by zero is not allowed")
    return y / x


def power(x: float, y: float):
    return math.pow(y, x)


def modulo(x: float, y: float):
    return y % x


def maximum(x: float, y: float):
    return x if x > y else y


def minimum(x: float, y: float):
    return x if x < y else y


def average(x: float, y: float):
    return (x + y) / 2


def invert(x: float):
    return -x


def factorial(x: float):
    if x < 0: raise ValueError("Factorial is not defined for negative numbers")
    if x % 1 != 0: raise ValueError("Factorial is only defined for integers")
    if x == 0: return 1
    return x * factorial(x - 1)


def sum_digits(x: float):
    if x < 0: raise ValueError("sum_digits is not defined for negative numbers")
    digits_in_str: str = str(x)
    total: int = 0
    for ch in digits_in_str:
        if ch.isdigit():
            total += int(ch)
    return total


operators_priority = {'+': 1, '-': 1, '*': 2, '/': 2, 'u-': 2.5, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, 'u~': 6,
                      '!': 6, '#': 6}

binary_functions = {'+': add, '-': subtract, '*': multiply, '/': divide, '^': power, '%': modulo, '$': maximum,
                    '&': minimum, '@': average}

unary_prefix_functions = {'u-': negate, 'u~': invert}

unary_postfix_functions = {'!': factorial, '#': sum_digits}
