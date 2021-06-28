import sys


def sum_two_numbers(number_1, number_2):
    return number_1 + number_2


def sub_two_numbers(number_1, number_2):
    if number_1 >= number_2:
        return number_1 - number_2
    return "This app can only produce positive results" 


def fac(number):
    result = 1
    for positive_int in range(1, number + 1):
        result = result * positive_int
    return result


def print_result(arguments):
    result = eval(arguments[1] + f'({arguments[2]}, {arguments[3]})')
    print(result)


if __name__ == "__main__":
    print_result(sys.argv)
