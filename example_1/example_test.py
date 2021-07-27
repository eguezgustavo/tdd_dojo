from example_1.example import sum_two_numbers

# Happy path
def test__sum_two_numbers_function__returns_twelve__when_inputs_are_five_and_seven():
    number1 = 5
    number2 = 7

    actual = sum_two_numbers(number1, number2)

    assert actual == 12
