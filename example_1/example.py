import sys

def sum_two_numbers(number_1, number_2):
    if is_number(number_1) and is_number(number_2):
        return number_1 + number_2

    return 'Values must be a numbers'
            

def sub_two_numbers(number_1, number_2):
    if is_number(number_1) and is_number(number_2):
        result = number_1 - number_2
        
        if result < 0:
            return 'This app can only produce positive results'
        
        return result
    return 'Values must be a numbers'


def fac(number):
    if is_number(number):
        if number > 1: 
            return number * fac(number - 1)
        return 1
    return 'Values must be a numbers'


def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
         return False

def eval_result(arguments):
    if len(arguments) == 4:
        result = eval(arguments[1] + f'({arguments[2]}, {arguments[3]})')
    if len(arguments) == 3:
        result = eval(arguments[1] + f'({arguments[2]})')    
    return result


if __name__ == "__main__":
    print(eval_result(sys.argv)) 
