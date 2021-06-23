# TDD Example

In this example we are going to create a calculator to show the TDD principle.

## Define what our application is going to do:

This app is going to have three methods:
- A function to add two numbers so if you run:
  ```
  python3 example.py sum_two_numbers 5 7
  ```
  it will return 12 to the stdout
- A function to subtract two numbers so if you run:
  ```
  python3 example.py sub_two_numbers 5 7
  ```
  it will return "This app can only produce positive results" to the stdout
- A function get the factorial of a number so if you run:
  ```
  python3 example.py fac 3
  ```
  it will return 6 to the stdout


## Create the project structure:
```
    ├── example.py
    └── example_test.py
```
   At this point you can do ```pytest -svv``` and no test will be run.

## Adding two Numbers

The first requirement (to add two numbers) is used to write the test. For this, let's open the example_test.py in your favorite code editor.
 1. Write a function to test sum_two_numbers:
   First, import the functions from example.py, which are not written yet.
  ```py
from example import sum_two_numbers
  ```
  Write the test based on the requirements:
  ```py
def test_sum_two_numbers():
    number_1 = 5
    number_2 = 7

    result = sum_two_numbers(number_1, number_2)

    assert result == 12
  ```
  If you run the test, the test will fail because ```sum_two_numbers``` is not implemented yet.

 2. Write the necessary code to pass the test:
   
   Define the function in example.py and run the test again:

```py
def sum_two_numbers(number_1, number_2):
    result = number_1 + number_2
    return result    
```

   Now you can run the test with ```pytest -svv``` and it will pass.

 3. Refactor the function:
   In this example you can simply write the function like this:

```py
def sum_two_numbers(number_1, number_2):
    return number_1 + number_2    
```
  The test will still pass.


## Subtracting two Numbers

The second requirement is: to subtract two numbers, for this, let's open the example_test.py again and write a test.

**Note:** The requirements say that this app can only produce positive results, but now the simple step that we can do is to implement a function to subtract two numbers.
 1. Write a function to test sub_two_numbers:
   First, import the functions from example.py, which are not written yet.
  ```py
from example import sum_two_numbers, sub_two_numbers
  ```
  Write the test based on the requirements:
  ```py
def test_sub_two_numbers():
    number_1 = 10
    number_2 = 7

    result = sub_two_numbers(number_1, number_2)

    assert result == 3
  ```
  If you run the test, the test will fail because ```sub_two_numbers``` is not implemented yet.

 2. Write the necessary code to pass the test:
   
   Define the function in example.py and run the test again:

```py
def sub_two_numbers(number_1, number_2):
    result = number_1 - number_2
    return result    
```

   Now you can run the test with ```pytest -svv``` and it will pass.

 3. Refactor the function:
   In this example you can simply write the function like this:

```py
def sub_two_numbers(number_1, number_2):
    return number_1 - number_2    
```
  The test will still pass.


## Subtract exceptions:

Part of the second requirement is to produce only positive results:
 1. Write a function to test sub_two_numbers to ensure that the function only returns positive numbers:
   
  Write the test based on the requirements:
  ```py
def test_if_sub_two_numbers_returns_only_positive_result():
    number_1 = 5
    number_2 = 7

    result = sub_two_numbers(number_1, number_2)

    assert result == "This app can only produce positive results"
  ```
  If you run the test, the test will fail because ```sub_two_numbers``` does not have this requirement yet.
  
  2. Refactor the function to comply with the requirements:
```py
def sub_two_numbers(number_1, number_2):
    try:
        result = number_1 - number_2
        if result < 0:
            raise ValueError
        return result
    except ValueError:
        return "This app can only produce positive results"   
```
  3. Now the application is working as expected and we can continue working.

## The Factorial of a number

 The third requirement is to return the factorial of a number, so, let's write a test!.
 1. Write a function to test sub_two_numbers:
   First, import the functions from example.py, which are not written yet.
  ```py
from example import sum_two_numbers, sub_two_numbers, fac
  ```
  Write the test based on the requirements:
  ```py
def test_fac():
    number_1 = 3

    result = fac(number_1)

    assert result == 6
  ```
  If you run the test, the test will fail because ```fac``` is not implemented yet.

 2. Write the necessary code to pass the test:
   
   You can implement the factorial of a number with one loop:
```py
def fac(number_1):
    result = 1
    for i in range(1, number_1 + 1):
        result = result * i
    return result
```

   Now you can run the test with ```pytest -svv``` and it will pass.

 3. In this case, refactoring is not necessary but you can do:
   
```py
from functools import reduce
def fac(number_1):
    return reduce(lambda x, y: x*y, range(1, number_1 + 1))
```
 And the test should still run.

 ## Presentation requirement

 The functions work, but to use them you need import them from another script. The requirements tell us that to run the app you can simply pass the function name and the values as command-line arguments and it will run. So, we need a function called print_result, which takes an array with arguments passed to the script, and prints result of the desired operation.
 1. Write a test for the print_result function:
   ```py
def test_print_result(capfd):
    arguments = ['example.py', 'sum_two_numbers', '5', '7']

    print_result(arguments)

    out, _ = capfd.readouterr()

    assert out == "12\n"
   ```
   In this test, we use capfd, a build-in pytest fixture which allow us check the stdout and make assertions with this.

 2. Write a function to pass the test:

   ```py
def print_result(arguments):
    result = eval(arguments[1] + f'({arguments[2]}, {arguments[3]})')
    print(result)
   ```
 3. The test should pass!!
 4. Finally, we can write the __main__ method of the app.

```py
if __name__ == "__main__":
    print_result(sys.argv)
```
  Don't forget to import the sys module.
