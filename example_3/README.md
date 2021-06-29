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

Remember that you can always check a possible solution in:

```sh
git checkout Exercise_3_Solution
```
