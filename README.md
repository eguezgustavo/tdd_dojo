# Test Driven Development
 
Test Driven Development, shortened as TDD, is a set of techniques that “encourages simple designs and test suites that inspire conﬁdence”. To use TDD, your work should be divided in the simplest steps possible, each step is focused in only one task. Every step should follow this algorithm:
 
1. Write a test for the new function or piece of code that you want to implement. The test should fail.
2. Write only enough code to pass this test.
3. Refactor the code.
4. Goto 1

<img src="./docs/static/images/TDD.png" alt="drawing" width="1000"/>

## Project Setup

### Install Python

Before starting, make sure you have installed [Python](https://www.python.org/downloads/). In this tutorial, Python 3.8 is used.

### Setting up venv

Is a good practice to isolate the project that we are working on from the rest of the system.

```
$ python3 -m venv .venv
$ source env/bin/activate
(env)$
```
### Install Pytest

For testing we're going to use [pytest](pytest.org) as a testing framework. so you can install with pip:
```
pip install pytest
```
## TDD Example 1

In the first example we are going to create a calculator using TDD. To follow this example, goto [Example](./example/README.md).

If you want to check the answer for this dojo, do:
```
git checkout git checkout TDD-Example
```

## TDD Example 2

In the second example we are going to build the [Game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) using TDD. To follow this example, goto [Example](./example_game_of_life/README.md).

If you want to check the answer for this dojo, do:
```
git checkout git checkout TDD-game-of-life
```
