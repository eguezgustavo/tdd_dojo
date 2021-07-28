import math

def addition_two_numbers(number1, number2):
    return number1 + number2


def subtraction_two_numbers(number1, number2):
    result = number1 - number2
    if result < 0:
        return "This app can only produce positive results"
    return result


def factorial_of_number(number):
    if number < 0:
        return "Factorial does not exist for negative numbers"
    elif not isinstance(number, int):
        return "Factorial only accepts integral values"
    else:
        return math.factorial(number)

