import pytest

from example_1.example import sum_two_numbers, sub_two_numbers

# Happy path
def test__sum_two_numbers_function__returns_twelve__when_inputs_are_five_and_seven():
    number1 = 5
    number2 = 7

    actual = sum_two_numbers(number1, number2)

    assert actual == 12

# Sad path
@pytest.mark.parametrize("number1,number2,expected", (
    ('fail', 1, 'Values must be a numbers'),
    (1, 'fail', 'Values must be a numbers'),
))
def test__sum_two_numbers_function__returns_error_msg__when_numbers_are_not_a_number(number1, number2, expected):

    actual = sum_two_numbers(number1, number2)

    assert actual == expected

# Happy path sub_two_numbers
def test__sub_two_numbers_function__returns_one__when_inputs_are_six_and_five():
    number1 = 6
    number2 = 5

    actual = sub_two_numbers(number1, number2)

    assert actual == 1

# Sad path sub_two_numbers
def test__sum_two_numbers_function__returns_error_msg__when_inputs_are_five_and_seven():
    number1 = 5
    number2 = 7
    expected = 'This app can only produce positive results'

    actual = sub_two_numbers(number1, number2)

    assert actual == expected