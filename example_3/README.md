# TDD Exercise 3

In this example we are going to create a calculator similar to what we did on Example 1, but with one assumption:
There is another team working in a dependency call ```calculator```, since we don't have control of this code, we cannot make changes on it, the only thing we know
about it is that it has two methods ```calculator.sum``` which returns the sum of two numbers passed and ```calculator.mul``` which returns the multiplication of two numbers. In this exercise, we have to implement a class to fulfill the requirements but now that we depend on the code of the other team, using Dependency Injection is a good idea.

## Dependency Injection

Using dependencies could be a problem for our code, because the code becomes highly coupled with the dependencies that you're using. Dependency Injection helps you with this. With DI, we don't have to import the dependency in the class or module where we want to use it, instead we send it as a parameter to the constructor and let another part of the code create the dependency's objects. DI is a pattern design that says: "If a class uses an object of a certain type, we should not make that class responsible for creating that object". This approach makes testing and refactoring easier. Here is an [example of DI](https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html).

## Requirements

This app is going to have a class with three methods:

- A method to add two numbers.
  - It can overflow if the result is greater than 100, so it should return: "OverflowError".
  
- A method to subtract two numbers.
  
- A method to get the factorial of a number.

## Starting

This folder has two python files:

    ├── [main.py](/example_3/main.py) - Here you can write your code
    └── [main_test.py](/example_3/main_test.py) - Here you can write your test

You can start working in this exercise. Don't forget to use the naming [recommendations](./../README.md) for the exercises.

## Solution

### sum

Let's begin considering the happy path, so let test ```6 + 4 = 9```:

```py
from .main import Calculator


def test__sum_method__returns_nine__when_inputs_are_six_and_three(mocker):
    number_1 = 6
    number_2 = 3
    calculator = mocker.Mock(sum=mocker.Mock(return_value=9))

    calculator_test = Calculator(calculator)
    result = calculator_test.sum(number_1, number_2)

    assert result == 9
```

If we run the test, it will fail, so let's write the class and the method to continue:

```py
class Calculator:

    def __init__(self, calculator):
        self.calculator = calculator

    def sum(self, number_1, number_2):
        return 9
```

Now the test passes.
Note: The calculator dependency is not being instantiated in main.py, instead, an instance of calculator should be passed or injected to the class whenever it is used. For testing we are using [pytest-mock](https://pypi.org/project/pytest-mock/) which helps us create test doubles or mocks. This package is already installed in the requirements.txt

Now, let's try with other numbers to make the test fail and refactor the code.

```py
def test__sum_method__returns_seven__when_inputs_are_four_and_three(mocker):
    number_1 = 4
    number_2 = 3
    calculator = mocker.Mock(sum=mocker.Mock(return_value=7))

    calculator_test = Calculator(calculator)
    result = calculator_test.sum(number_1, number_2)

    assert result == 7
```

The refactored code is as follows:

```py

    def sum(self, number_1, number_2):
        return self.calculator.sum(number_1, number_2)
```

Now, it is working better, but let's test some "unhappy paths". Test that an error message should be return if the sum is greater than 100:

```py
def test__sum_method__returns_overflow_error__when_result_is_grater_than_one_hundred(mocker):
    number_1 = 110
    number_2 = 2
    calculator = mocker.Mock(sum=mocker.Mock(return_value=112))

    calculator_test = Calculator(calculator)
    result = calculator_test.sum(number_1, number_2)

    assert result == 'OverflowError'
```

The refactor of this code is:

```py

class Calculator:

    def __init__(self, calculator):
        self.calculator = calculator
    
    def sum(self, number_1, number_2):
        result = self.calculator.sum(number_1, number_2)
        if result > 100:
            return "OverflowError"
        return result

```

### sub

The procedure for the subtraction method is similar. Let's write the first test:

```py
def test__sub_method__returns_two__when_inputs_are_six_and_four(mocker):
    number_1 = 6
    number_2 = 4
    calculator = mocker.Mock(sum=mocker.Mock(return_value=2))

    calculator_test = Calculator(calculator)
    result = calculator_test.sub(number_1, number_2)

    assert result == 2
```

To pass this test we can do:
```py
class Calculator:

    ...

    def sub(self, number_1, number_2):
        return 2
    
```

This is not good for all the possible numbers so let's write another test:

```py
def test__sub_method__returns_seven__when_inputs_are_nine_and_two(mocker):
    number_1 = 9
    number_2 = 2
    calculator = mocker.Mock(sum=mocker.Mock(return_value=7))

    calculator_test = Calculator(calculator)
    result = calculator_test.sub(number_1, number_2)

    assert result == 7
```

Now we refactor the code to pass the test:

```py
class Calculator:

    ...
    
    def sub(self, number_1, number_2):
        return self.calculator.sum(number_1, - number_2)
```

Since, we don't have any restriction for the subtraction method, we can leave like that.

### fac

For the fac method, we can write a test for a number:

```py
def test__fac_method__returns_six__when_input_is_three(mocker):
    number = 3
    calculator = mocker.Mock(mul=mocker.Mock(side_effect=lambda number_1, number_2 : number_1 * number_2))

    calculator_test = Calculator(calculator)
    result = calculator_test.fac(number)

    assert result == 6
```

To past the test, the simplest step is:

```py
class Calculator:

    ...
    
    def fac(self, number):
        return 6

```

Now, let's try with other numbers:

```py
def test__fac_method__returns_362880__when_input_is_nine(mocker):
    number = 9
    calculator = mocker.Mock(mul=mocker.Mock(side_effect=lambda number_1, number_2 : number_1 * number_2))

    calculator_test = Calculator(calculator)
    result = calculator_test.fac(number)

    assert result == 362880

```

The test will fail, so we need to refactor the function:

```py
class Calculator:

    ...
    
    def fac(self, number):
        result = 1
        for positive_int in range(1, number + 1):
            result = self.calculator.mul(result, positive_int)
        return result

```
**Note:** The mock for the calculator.mul in this case is a little more complex, because we need that it actually returns the multiplication of two numbers.
