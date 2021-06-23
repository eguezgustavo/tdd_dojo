# Game of life using TDD

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970, It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. To learn more about it you can check the [Wiki](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) page.

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

So, we are going to take these rules as our business requirements and start TDD!
Note: use the command ````python3 -m pytest -svv```` to run the test.
## Cell state

Before starting with the rules, we should begin defining the states allowed for a cell.
In Life, a cell can be in two states: 
- dead which will be represented as 0
- alive which will be represented as 1
  
To do this, in the file [cell_test.py](test/cell_test.py) write the first test:
```py
from game.cell import Cell
import pytest

def test_cell_state_can_be_dead_or_alive():
    state = 0
    dead_cell = Cell(state)
    state = 1
    alive_cell = Cell(state)

    assert dead_cell.state == 0
    assert alive_cell.state == 1
```
Following the rules of TDD, you should make the test fail. So, if you run the test with ```python3 -m pytest -svv```, it will fail because the class Cell is not defined yet.

Next, in the file [cell.py](game/cell.py) you should implement the minimum code to make this test pass:
```py
class Cell:
    def __init__(self, state):
        self.state = state
```
If you run the test, it will pass, but it is not a good implementation, because cell.state can be any value. To validate the states that a cell can have, we write the next test:
```py
def test_cell_should_raise_an_exception_if_invalid_state():
    state = 3

    with pytest.raises(Exception) as e_info:
        Cell(state)
    
    assert e_info.value.args[0] == 'Invalid state'
```
And if you run the test it will fail, so let's implement the logic in [cell.py](game/cell.py).
```py
class Cell:
    def __init__(self, state):
        self.state = state

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        if not state in [0, 1]:
            raise Exception("Invalid state")
        self._state = state
```
As you can see, the state is defined as a property of the class, and we can build a setter method to validate the state. Now the test should pass and we can continue with the game rules.

## 1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.

Now we can write a test that will fail in [cell_test.py](test/cell_test.py).

```py
# Any live cell with fewer than two live neighbors dies, as if by underpopulation.
def test_a_live_cell_should_die_if_less_than_two_cells_are_alive():
    live_cell_with_1_neighbor = Cell(1)
    live_cell_with_2_neighbor = Cell(1)

    live_cell_with_1_neighbor.update_state(0)
    live_cell_with_2_neighbor.update_state(1)

    assert live_cell_with_1_neighbor.state == 0
    assert live_cell_with_2_neighbor.state == 0

```
The test fails and it tell us the logic we have to write to make the test pass on [cell.py](game/cell.py).
We have to define a method update_state which takes the number of neighbors and returns if the cell is alive or dead. The simplest logic to implement this is as follows:
```py
class Cell:

    ...

    def update_state(self, neighbors):
        self.state = 0
```
So the test passes and we can continue with the TDD!

## 2. Any live cell with two or three live neighbors lives on to the next generation.

We continue with TDD and define a test for this requirement on [cell_test.py](test/cell_test.py) :
```py
# Any live cell with two or three live neighbors lives on to the next generation.
def test_a_live_cell_should_keep_alive_if_2_or_3_live_neighbors():
    live_cell_with_2_neighbor = Cell(1)
    live_cell_with_3_neighbor = Cell(1)

    live_cell_with_2_neighbor.update_state(2)
    live_cell_with_3_neighbor.update_state(3)

    assert live_cell_with_2_neighbor.state == 1
    assert live_cell_with_3_neighbor.state == 1
```
So to pass this test, we need to refactor the update_state method on [cell.py](game/cell.py):
```py
class Cell:

    ...

    def update_state(self, neighbors):
        if neighbors >= 2:
            self.state = 1
            return
        self.state = 0
```

The test passes and we can continue.

## 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
As always, we define a test for this requirements:

```py
# Any live cell with more than three live neighbors dies, as if by overpopulation.
def test_a_live_cell_should_die_if_more_than_3_live_neighbors():
    live_cell_with_4_neighbor = Cell(1)

    live_cell_with_4_neighbor.update_state(4)

    assert live_cell_with_4_neighbor.state == 0
```
Run the test, and ensure that it fails.
Now refactor the code so it pass the test:

```py
class Cell:

    ...

    def update_state(self, neighbors):
            if neighbors in [2, 3] and self.state == 1:
                self.state = 1
                return
            self.state = 0
```
Now that the test has passed, we can continue.

## 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

We write a test for this requirement and make it fail.

```py
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
def test_a_dead_cell_should_live_if_exactly_3_live_neighbors():
    dead_cell_with_3_live_neighbor = Cell(0)

    dead_cell_with_3_live_neighbor.update_state(3)

    assert dead_cell_with_3_live_neighbor.state == 1
```

Now, refactor the code to pass the test:

```py
class Cell:

    ...

    def update_state(self, neighbors):
        if neighbors in [2, 3] and self.state == 1:
            self.state = 1
            return
        if neighbors == 3 and self.state == 0:
            self.state = 1
            return
        self.state = 0
```
That's it!! if you followed the tutorial to this point, you have implemented the logic of the game with all the requirements. 
To make this game act like a game, you can develop a function that get the state of an array of cells and calculates the next state.
With this feature, you can iterate to get the states of n generations and print on the console to show the evolution of the game. 
So lets create a class called Grid, this class should have a method to update the state of a given array of cells and return it

## Grid

### First we have to test that this method accepts an array as input and stores it. So, the first test is:
```py
from game.grid import Grid

seed = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

seed_next_generation = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]



def test_a_grid_should_be_created_with_a_seed():
    grid = Grid(seed)

    assert grid.seed == seed 

```
And we write code on [grid](game/grid.py) to pass this test.

```py
class Grid:

    def __init__(self, seed):
        self.seed = seed
```

### Return alive neighbors
Now, given the location of the cell to update, a method should calculate the number of alive neighbors, so let's test that:
```py
def test_given_a_cell_location_the_neighbors_should_be_calculated():
    grid = Grid(seed)

    neighbors = grid.calculate_neighbors([8, 5])

    assert neighbors == 3
```
if you check the cell [8, 5] on the seed array it has 3 neighbors:
```
| 0, 1, 0 |
| 0, 1, 0 |
| 0, 1, 1 |
```
Now, let's write the code to pass this test:
```py
from .cell import Cell

class Grid:

    ...

    def calculate_neighbors(self, location):
        x = location[0]
        y = location[1]

        neighbors = 0 - self.seed[y][x]

        for i in [-1, 0, 1]:
            for j in [-1, 0 , 1]:
                try:
                    is_neighbor_alive = self.seed[y + i][x + j]
                except:
                    is_neighbor_alive = 0
                neighbors += is_neighbor_alive

        return neighbors
```

Now it should pass the test and we can continue.

### Update the seed.

A method in Grid should iterate for every cell and update the state of each cell.
Let's write a test for that:
```py
def test_given_a_seed_the_next_state_should_be_calculated():
    grid = Grid(seed)
    grid.calculate_next_gen()

    assert grid.seed == seed_next_generation
```
And write the necessary code to pass the test:

```py
    def calculate_next_gen(self):
        nex_gen = []
        for i in range(len(self.seed)):
            nex_gen_y = []
            for j in range(len(self.seed[0])):
                cell = Cell(self.seed[i][j])
                neighbors = self.calculate_neighbors([j, i])
                cell.update_state(neighbors)
                nex_gen_y.append(cell.state)
            nex_gen.append(nex_gen_y)
        self.seed = nex_gen
```

Finally, we are done!!
If you followed this tutorial correctly, you can call an axillary script to print the output of a given seed.
```
python3 run_the_game.py [name of a seed in seeds.py]
``` 
For example:

```
python3 run_the_game.py seed_star
```

Prints:

![pattern](/docs/static/images/pattern.gif)