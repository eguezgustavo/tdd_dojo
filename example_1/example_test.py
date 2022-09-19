def test__add__returns_five__when_first_number_is_three_and_second_one_is_two():
    # Arrange
    first_number = 3
    second_number = 2

    # Act
    calculator = Calculator()
    result = calculator.add(first_number, second_number)

    # Assert
    assert result == 5
