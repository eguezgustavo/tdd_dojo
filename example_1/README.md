# TDD Exercise 1 - Solution

In this example we are going to create a calculator to show the TDD principle.

## Requirements:

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
 1. In the first requirement, an example is given. So, let's write a test for that: 
   First, import a function ```sum_two_numbers``` from example.py, which is not written yet.
  ```py
from .example import sum_two_numbers
  ```
  Write the test based on the requirements:
  
  ```py
def test__sum_two_numbers_function__returns_twelve__when_inputs_are_five_and_seven():
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
    return 12
```
   Now you can run the test with ```pytest -svv``` and it will pass.

 3. What if the numbers are not five and seven?
 Now, we have to test that any pair of numbers provided by the user returns the correct answer. To do this we need a library to generate random numbers.
 [```faker```](https://faker.readthedocs.io/en/master/) is a good option when we need to generate fake data to test.
 
```py
from faker import Faker 

fake = Faker()
Faker.seed()


...



def test__sum_two_numbers_function__returns_the_sum__when_inputs_are_random():
    number_1 = fake.random_int()
    number_2 = fake.random_int()

    result = sum_two_numbers(number_1, number_2)

    assert result == sum([number_1, number_2])  
```

Now if we run the test, it will fail because the function always returns 12.
Let´s refactor the code to pass this test:

```py
def sum_two_numbers(number_1, number_2):
    return number_1 + number_2
```

The test will pass and we can continue with the next requirement.


## Subtracting two Numbers

The second requirement is: to subtract two numbers, for this, let's open the example_test.py again and write a test.

**Note:** The requirements say that this app can only produce positive results. So first, we consider what users are supposed to do when using our application, this is called "happy path".
To test the happy path we simply test that given two numbers the function returns the subtraction.

 1. Write a function to test sub_two_numbers returns 3 given 10 and 7:
   First, import the functions from example.py, which are not written yet.
  ```py
from .example import sum_two_numbers, sub_two_numbers
  ```
  Write the test:
  ```py
def test__sub_two_numbers_function__returns_three__when_inputs_are_ten_and_seven():
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
    return 3    
```

   Now you can run the test with ```pytest -svv``` and it will pass.

 3. Next we need to ensure that the application works when the user gives any pair of numbers that produce a positive result (happy path).
 Let's write a test for that.
```py
def test__sub_two_numbers_function__returns_the_subtraction__when_first_input_is_grater_than_second_input():
    number_1 = fake.random_int(51, 100)
    number_2 = fake.random_int(0, 50)

    result = sub_two_numbers(number_1, number_2)

    assert result == sum([number_1, - number_2])
```
4.  Refactor the code to pass the test:

```py
def sub_two_numbers(number_1, number_2):
    return number_1 - number_2    
```
  The test will still pass.

## Subtract exceptions:

Testing the "unhappy paths", or the many ways that users can break our app is important, since it will help handling errors.
Part of the second requirement is to produce only positive results:
 1. Write a function to test sub_two_numbers to ensure that the function returns an error message when the result is negative:
   
  Write the test based on the requirement:
  ```py
def test__sub_two_numbers_function__returns_error_message__when_second_input_is_grater_than_first_input():
    number_1 = fake.random_int(0, 50)
    number_2 = fake.random_int(51, 100)

    result = sub_two_numbers(number_1, number_2)

    assert result == "This app can only produce positive results"
  ```
  If you run the test, the test will fail because ```sub_two_numbers``` does not have this requirement yet.
  
  2. Refactor the function to comply with the requirements:
```py
def sub_two_numbers(number_1, number_2):
    if number_1 >= number_2:
        return number_1 - number_2
    return "This app can only produce positive results"   
```
  3. Now the application is working as expected and we can continue working.

## The Factorial of a number

 The third requirement is to return the factorial of a number, so, let's write a test!.
 1. Write a function to test sub_two_numbers:
   First, import the functions from example.py, which are not written yet.
  ```py
from .example import sum_two_numbers, sub_two_numbers, fac
  ```
  Write the test based on the requirements:
  ```py
def test__fac_function__returns_six__when_input_is_3():
    number_1 = 3

    result = fac(number_1)

    assert result == 6
  ```
  If you run the test, the test will fail because ```fac``` is not implemented yet.

 2. Write the necessary code to pass the test:
   
   You can implement the factorial of a number with one loop:
```py
def fac(number_1):
    return 6
```
   Now you can run the test with ```pytest -svv``` and it will pass.

 3. But what about other numbers:
 Let's write a test to check if the function works with a random number.
   ```py
import math

...

def test__fac_function__returns_the_factorial__when_input_is_a_random_number():
    number = fake.random_int(0, 50)

    result = fac(number)

    assert result == math.factorial(number)
  ```
  4. Write the necessary code to pass the test:
   
   Since the factorial is the product of all positive integers less than or equal to the number, you can implement the factorial of a number with one loop:
```py
def fac(number):
    result = 1
    for positive_int in range(1, number + 1):
        result = result * positive_int
    return result
```
 Now the test should pass.

 ## Presentation requirement

 The functions work, but to use them you need to import them from another script. The requirements tell us that to run the app you can simply pass the function name and the values as command-line arguments and it will run. So, we need a function called print_result, which takes an array with arguments passed to the script, and prints the result of the desired operation.
 1. Write a test for the print_result function:
   ```py
def test__print_result_function__prints_the_result__when_arguments_are_provided(capfd):
    arguments = ['example.py', 'sum_two_numbers', '5', '7']

    print_result(arguments)
    out, _ = capfd.readouterr()

    assert out == "12\n"
   ```
   In this test, we use capfd, a built-in pytest fixture which allows us to check the stdout and make assertions with this.

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
