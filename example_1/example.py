def sum_two_numbers(number_1, number_2):
    try:
        int(number_1)
        int(number_2)
        return number_1 + number_2
        
    except ValueError:
        return 'Values must be a numbers'
