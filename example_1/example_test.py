from .example import sum_two_numbers, sub_two_numbers, fac, print_result
from faker import Faker 
import math


fake = Faker()
Faker.seed()


def test__sum_two_numbers_function__returns_twelve__when_inputs_are_five_and_seven():
    number_1 = 5
    number_2 = 7

    result = sum_two_numbers(number_1, number_2)

    assert result == 12


def test__sum_two_numbers_function__returns_the_sum__when_inputs_are_random():
    number_1 = fake.random_int()
    number_2 = fake.random_int()

    result = sum_two_numbers(number_1, number_2)

    assert result == sum([number_1, number_2])  


def test__sub_two_numbers_function__returns_three__when_inputs_are_ten_and_seven():
    number_1 = 10
    number_2 = 7

    result = sub_two_numbers(number_1, number_2)

    assert result == 3


def test__sub_two_numbers_function__returns_the_subtraction__when_first_input_is_grater_than_second_input():
    number_1 = fake.random_int(51, 100)
    number_2 = fake.random_int(0, 50)

    result = sub_two_numbers(number_1, number_2)

    assert result == sum([number_1, - number_2])


def test__sub_two_numbers_function__returns_error_message__when_second_input_is_grater_than_first_input():
    number_1 = fake.random_int(0, 50)
    number_2 = fake.random_int(51, 100)

    result = sub_two_numbers(number_1, number_2)

    assert result == "This app can only produce positive results"


def test__fac_function__returns_six__when_input_is_3():
    number_1 = 3

    result = fac(number_1)

    assert result == 6


def test__fac_function__returns_the_factorial__when_input_is_a_random_number():
    number = fake.random_int(0, 50)

    result = fac(number)

    assert result == math.factorial(number)


def test__print_result_function__prints_the_result__when_arguments_are_provided(capfd):
    arguments = ['example.py', 'sum_two_numbers', '5', '7']

    print_result(arguments)
    out, _ = capfd.readouterr()

    assert out == "12\n"
