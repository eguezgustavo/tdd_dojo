import pytest
from .example import *

def test__addition_two_numbers__returns_twelve__when_inputs_are_five_and_seven():
    number1 = 5
    number2 = 7

    result = addition_two_numbers(number1,number2)

    assert result==12


def test__subtraction_two_numbers__returns_an_error_message__when_difference_is_negative():
    number1 = 5
    number2 = 7

    result = subtraction_two_numbers(number1,number2)

    assert result=="This app can only produce positive results"


def test__subtraction_two_numbers__returns_difference__when_difference_is_positive():
    number1 = 8
    number2 = 7

    result = subtraction_two_numbers(number1,number2)

    assert result==1


def test__factorial_of_number__returns_factorial__when_number_is_positive():
    number = 3

    result = factorial_of_number(number)

    assert result==6


def test__factorial_of_number__returns_an_error_message__when_number_is_negative():
    number = -1

    result = factorial_of_number(number)

    assert result=="Factorial does not exist for negative numbers"


def test__factorial_of_number__returns_an_error_message__when_number_is_not_integer():
    number = 3.3

    result = factorial_of_number(number)

    assert result=="Factorial only accepts integral values"