from unittest import result
from example_1.example import Calculator

def test__add__returns_five__when_first_number_is_three_and_second_one_is_two():
    # Arrange
    first_number = 3
    second_number = 2

    # Act
    calculator = Calculator()
    result = calculator.add(first_number, second_number)

    # Assert
    assert result == 5

def test__add__return_eight__when_first_number_is_three_and_the_second_one_is_five():
    first_number = 3
    second_number = 5

    calculator = Calculator()
    result = calculator.add(first_number, second_number)

    assert result == 8
