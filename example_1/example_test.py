from example_1.example import Calculator
import random


def test__add__returns_the_sum_of_two_numbers():
    first_number = random.randint(0, 9)
    second_number = random.randint(0, 9)

    calculator = Calculator()
    result = calculator.add(first_number, second_number)

    expected_result = first_number + second_number
    assert result == expected_result
