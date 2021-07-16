from  application.services.calculator import Calculator


def test__sum_method__returns_nine__when_inputs_are_six_and_three():
    number_1 = 6
    number_2 = 3

    calculator_test = Calculator()
    result = calculator_test.sum(number_1, number_2)

    assert result == 9


def test__sum_method__returns_seven__when_inputs_are_four_and_three():
    number_1 = 4
    number_2 = 3

    calculator_test = Calculator()
    result = calculator_test.sum(number_1, number_2)

    assert result == 7


def test__sub_method__returns_two__when_inputs_are_six_and_four():
    number_1 = 6
    number_2 = 4

    calculator_test = Calculator()
    result = calculator_test.sub(number_1, number_2)

    assert result == 2


def test__sub_method__returns_seven__when_inputs_are_nine_and_two():
    number_1 = 9
    number_2 = 2

    calculator_test = Calculator()
    result = calculator_test.sub(number_1, number_2)

    assert result == 7


def test__fac_method__returns_six__when_input_is_three():
    number = 3

    calculator_test = Calculator()
    result = calculator_test.fac(number)

    assert result == 6


def test__fac_method__returns_362880__when_input_is_nine():
    number = 9

    calculator_test = Calculator()
    result = calculator_test.fac(number)

    assert result == 362880
