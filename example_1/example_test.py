import pytest

from example_1.example import (
  sum_two_numbers,
  sub_two_numbers,
  fac
)


def test__sum_two_numbers__returns_twelve__when_three_and_nine_are_passed():
  number_1 = 3
  number_2 = 9
  expected_sum = 12

  result = sum_two_numbers(number_1, number_2)

  assert result == expected_sum


def test__sum_two_numbers__returns_minus_ten__when_two_and_minus_twelve_are_passed():
  number_1 = 2
  number_2 = -12
  expected_sum = -10

  result = sum_two_numbers(number_1, number_2)

  assert result == expected_sum


def test__sub_two_numbers__returns_three__when_thirteen_and_ten_are_passed():
  number_1 = 13
  number_2 = 10
  expected_sum = 3

  result = sub_two_numbers(number_1, number_2)

  assert result == expected_sum


def test__sub_two_numbers__returns_a_msg__when_three_and_nine_are_passed():
  number_1 = 3
  number_2 = 9
  expected_msg = "This app can only produce positive results"

  result = sub_two_numbers(number_1, number_2)

  assert result == expected_msg


def test__fac__returns_120_when_5_is_passed():
  init_serial_number = 5
  expected_factorial = 120

  result = fac(init_serial_number)

  assert result == expected_factorial


def test__fac__returns_24_when_4_is_passed():
  init_serial_number = 4
  expected_factorial = 24

  result = fac(init_serial_number)

  assert result == expected_factorial


def test__fac__returns_6_when_3_is_passed():
  init_serial_number = 3
  expected_factorial = 6

  result = fac(init_serial_number)

  assert result == expected_factorial