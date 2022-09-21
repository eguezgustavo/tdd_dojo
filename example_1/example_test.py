from example_1.example import Calculator
import random
import pytest


def test__add__returns_the_sum_of_two_numbers():
    # Arrange
    first_number = random.randint(1, 9)
    second_number = random.randint(1, 9)

    # Act
    calculator = Calculator()
    result = calculator.add(first_number, second_number)

    # Assert
    expected_result = first_number + second_number
    assert result == expected_result

def test__add__returns_the_same_number_if_it_is_summed_with_zero():
    first_number = 0
    second_number = random.randint(1, 9)

    calculator = Calculator()
    result = calculator.add(first_number, second_number)

    assert result == second_number

@pytest.mark.parametrize(
    "first_number, second_number",
    [
        (-1, 1),
        (1, -1),
    ]
)
def test__add__raises_an_error_when_the_first_number_is_negative(
    first_number,
    second_number,
):
    calculator = Calculator()

    with pytest.raises(ValueError) as error:
        calculator.add(first_number, second_number)
    assert str(error.value) == "A number shouldn't be negative"


@pytest.mark.parametrize(
    "first_number, second_number",
    [
        ("abc", 1),
        ([], -1),
        (1, ()),
    ]
)
def test_add_raises_an_error__when_the_parameters_are_not_integers(
    first_number,
    second_number,
):
    calculator = Calculator()

    with pytest.raises(ValueError) as error:
        calculator.add(first_number, second_number)
    assert str(error.value) == "Input shouldn be numbers"
