import pytest

from example_1.example import fac, eval_result, sum_two_numbers, sub_two_numbers

# Happy path
def test__sum_two_numbers_function__returns_twelve__when_inputs_are_five_and_seven():
    number_1 = 5
    number_2 = 7

    actual = sum_two_numbers(number_1, number_2)

    assert actual == 12

# Sad path
@pytest.mark.parametrize("number_1,number_2,expected", (
    ('fail', 1, 'Values must be a numbers'),
    (1, 'fail', 'Values must be a numbers'),
))
def test__sum_two_numbers_function__returns_error_msg__when_values_are_not_a_number(number_1, number_2, expected):

    actual = sum_two_numbers(number_1, number_2)

    assert actual == expected

# Happy path sub_two_numbers
def test__sub_two_numbers_function__returns_one__when_inputs_are_six_and_five():
    number_1 = 6
    number_2 = 5

    actual = sub_two_numbers(number_1, number_2)

    assert actual == 1

# Sad path sub_two_numbers
def test__sum_two_numbers_function__returns_error_msg__when_inputs_are_five_and_seven():
    number_1 = 5
    number_2 = 7
    expected = 'This app can only produce positive results'

    actual = sub_two_numbers(number_1, number_2)

    assert actual == expected

@pytest.mark.parametrize("number_1,number_2,expected", (
    ('fail', 1, 'Values must be a numbers'),
    (1, 'fail', 'Values must be a numbers'),
))
def test__sub_two_numbers_function__returns_error_msg__when_values_are_not_a_number(number_1, number_2, expected):

    actual = sub_two_numbers(number_1, number_2)

    assert actual == expected

# Happy path fac
def test__fac_function__returns_six__when_input_is_tree():
    number = 3

    actual = fac(number)

    assert actual == 6

# Sad path fac
def test__fac_function__returns_error_msg__when_input_is_not_a_number():
    number = 'not_a_number'
    expected = 'Values must be a numbers'

    actual = fac(number)

    assert actual == expected

# Happy path 
def test__eval_result_function__returns_error_msg__when_sub_two_numbers_is_passed_with_five_and_seven():
    arguments = ['example.py','sub_two_numbers','5','7']
    expected = 'This app can only produce positive results'
    
    actual = eval_result(arguments)

    assert actual == expected

def test__eval_result_function__returns_twelve__when_sum_two_numbers_is_passed_with_five_and_seven():
    arguments = ['example.py','sum_two_numbers','5','7']
    expected = 12
    
    actual = eval_result(arguments)

    assert actual == expected

def test__eval_result_function__returns_six__when_fac_is_passed_with_tree():
    arguments = ['example.py','fac','3']
    expected = 6
    
    actual = eval_result(arguments)

    assert actual == expected

# Sad path 
def test__eval_result_function__returns_error_msg__when_parameters_passed_are_not_correct():
    arguments = ['example.py','function','3']
    expected = 'Parameters are not correct'
    
    actual = eval_result(arguments)

    assert actual == expected