from .example import sum_two_numbers, sub_two_numbers, factorial

def test__sum_two_numbers__returns_positive_number__when_there_is_numbers():
    result = sum_two_numbers(1, 2)
    assert result == 3

def test__sum_two_numbers__returns_positive_number__when_there_is_no_number_1():
    result = sum_two_numbers(None, 2)
    assert result == 2

def test__sum_two_numbers__returns_positive_number__when_there_is_no_number_2():
    result = sum_two_numbers(1, None)
    assert result == 1

def test__sum_two_numbers__returns_algebraic_number__when_there_is_negative_numbers():
    result = sum_two_numbers(1, -2)
    assert result == -1

def test__sub_two_numbers__returns_positive_number__when_there_is_numbers():
    result = sub_two_numbers(2, 1)
    assert result == 1

def test__sub_two_numbers__returns_text_message__when_result_is_negative():
    result = sub_two_numbers(1, 2)
    assert result == "This app can only produce positive results"

def test__factorial__returns_positive_number__when_number_is_one():
    result = factorial(1)
    assert result == 1

def test__factorial__returns_positive_number__when_number_is_greater_than_one():
    result = factorial(4)
    assert result == 24