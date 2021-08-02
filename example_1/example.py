def sum_two_numbers(num_1, num_2):
    if (num_1 == None):
        num_1 = 0
    if (num_2 == None):
        num_2 = 0
    
    return num_1 + num_2

def sub_two_numbers(num_1, num_2):
    if (num_1 - num_2 < 0):
        return "This app can only produce positive results"
    else:
        return num_1 - num_2

def factorial(num):
    result = 1
    if (num == 1):
        return 1
    else:
        for next_int in range(2, num + 1):
            result *= next_int

    return result