import sys


def sum_two_numbers(number_1, number_2):
  return number_1 + number_2


def sub_two_numbers(number_1, number_2):
  if number_1 < number_2:
    return "This app can only produce positive results"

  return number_1 - number_2


def fac(number):
  if number == 0 or number == 1:
    f = 1

  if number > 1:
    f = number * fac(number - 1)

  return f


def print__fac_result(args):
  _dir, func_name, number = args
  return eval(f"{func_name}({number})")


def print_sum_result(args):
  _dir, func_name, number_1, number_2 = args
  return eval(f"{func_name}({number_1}, {number_2})")


def print_result(args):
  try:
    if args[1] == 'fac':
      result = print__fac_result(args)

    if args[1] != 'fac':
      result = print_sum_result(args)

    print(result)
  except ValueError:
    print('ValueError: Only integers are accepted')


if __name__ == '__main__':
  print_result(sys.argv)
