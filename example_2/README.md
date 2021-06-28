# Game of life using TDD

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970, It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. To learn more about it you can check the [Wiki](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) page.

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live(state ```1```) or dead(state ```0```), (or populated and unpopulated, respectively). Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

So, we are going to take these rules as our business requirements and start TDD!
Note: use the command ```python3 -m pytest -svv``` to run the test.

## Cell state

Before starting with the rules, we should begin defining the states allowed for a cell.
In Life, a cell can be in two states: 
- dead which will be represented as 0
- alive which will be represented as 1
  
To do this, in the file [cell_test.py](test/cell_test.py) write the first test:
```py
from game.cell import Cell
import pytest

def test__Cell_class__should_store_state__when_dead_state_is_passed():
    state = 0
    
    dead_cell = Cell(state)

    assert dead_cell.state == 0
```
Following the rules of TDD, you should make the test fail. So, if you run the test with ```python3 -m pytest -svv```, it will fail because the class Cell is not defined yet.

Next, in the file [cell.py](game/cell.py) you should implement the minimum code to make this test pass:
```py
class Cell:
    def __init__(self, state):
        self.state = 0
```
If you run the test, it will pass.


Now lest test when the cell is alive:

```py
def test__Cell_class__should_store_state__when_alive_state_is_passed():
    state = 1

    alive_cell = Cell(state)

    assert alive_cell.state == 1
```

Now, you should make the test fail. So, if you run the test with ```python3 -m pytest -svv```, it will fail because the class Cell is not defined yet.

Next, in the file [cell.py](game/cell.py) you should implement the minimum code to make this test pass:
```py
class Cell:
    def __init__(self, state):
        self.state = state
```
If you run the test, it will pass.

but it is not a good implementation, because cell.state can be any value. To validate the states that a cell can have, we write the next test:
```py
def test__Cell_class__should_raise_an_exception___when_invalid_state_is_passed():
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
def test__update_state_method__update_state_to_dead__when_less_than_two_neighbors_live():
    live_cell_with_1_neighbor = Cell(1)
    live_cell_with_2_neighbor = Cell(1)

    live_cell_with_1_neighbor.update_state(0)
    live_cell_with_2_neighbor.update_state(1)

    assert live_cell_with_1_neighbor.state == 0
    assert live_cell_with_2_neighbor.state == 0

```
The test fails and it tells us the logic we have to write to make the test pass on [cell.py](game/cell.py).
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
def test__update_state_method__update_state_to_live__when_state_is_live_and_two_or_three_neighbors_live():
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
def test__update_state_method__update_state_to_dead__when_state_is_live_and_more_than_three_neighbors_live():
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
def test__update_state_method__update_state_to_live__when_state_is_dead_and_three_neighbors_live():
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
To make this game act like a game, you can develop a function that gets the state of an array of cells and calculates the next state.
With this feature, you can iterate to get the states of n generations and print on the console to show the evolution of the game. 
So let's create a class called Grid, this class should have a method to update the state of a given array of cells and return it

## Grid

### First we have to test that this method accepts an array as input and stores it. So, the first test is:
```py
from game.grid import Grid

seed = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]

seed_next_generation = [
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 1]
    ]

def test__Grid_class__seed_should_be_saved__when_the_class_is_instantiated():
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
def test__calculate_neighbors_method__return_live_neighbors__given_location():
    grid = Grid(seed)

    neighbors = grid.calculate_neighbors([1, 1])

    assert neighbors == 4 
```
if you check the cell [1, 51 on the seed array it has 3 neighbors:
```
| 1, 1, 0 |
| 1, 1, 0 |
| 0, 0, 1 |
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
                is_neighbor_alive = self.seed[y + i][x + j]
                neighbors += is_neighbor_alive

        return neighbors
```
It is ok if we calculate the internal cells, but what about the outer cells?. Lets write a test for this scenario.

```py
def test__calculate_neighbors_method__return_live_neighbors__given_location_on_the_edge():
    grid = Grid(seed)

    neighbors = grid.calculate_neighbors([0, 0])

    assert neighbors == 2
```

if you check the cell [0 ,0] on the seed array it has 2 neighbors:
```
| 1, 1 |
| 1, 0 |

```
Now the test fails, and we can refactor the method.

```py
class Grid:

    ...

    def calculate_neighbors(self, location):
        location_in_x= location[0]
        location_in_y= location[1]

        neighbors = 0 - self.seed[location_in_y][location_in_x]

        for neighbor_in_y in [-1, 0, 1]:
            for neighbor_in_x in [-1, 0 , 1]:
                neighbor_location_x = location_in_x + neighbor_in_x
                neighbor_location_y = location_in_y + neighbor_in_y
                
                if neighbor_location_y in range(len(self.seed)) and neighbor_location_x in range(len(self.seed[0])):
                    is_neighbor_alive = self.seed[neighbor_location_y][neighbor_location_x]
                else:
                    is_neighbor_alive = 0
                neighbors += is_neighbor_alive

        return neighbors
```
Now it should pass the test and we can continue, note that we have refactor the naming of the variables.

### Update the seed.

A method in Grid should iterate for every cell and update the state of each cell.


Let's write a test for that:
```py
def test__calculate_next_gen_method__return_the_next_generation__when_a_seed_is_given():
    grid = Grid(seed)
    
    grid.calculate_next_gen()

    assert grid.seed == seed_next_generation
```
And write the necessary code to pass the test:

We need to iterate every cell and update it with the methods that we already wrote.

```py
class Grid:

    ...

    def calculate_next_gen(self):
        next_gen = []
        for location_in_y in range(len(self.seed)):
            next_gen_y= []
            for location_in_x in range(len(self.seed[0])):
                cell = Cell(self.seed[location_in_y][location_in_x])
                neighbors = self.calculate_neighbors([location_in_x, location_in_y])
                cell.update_state(neighbors)
                next_gen_y.append(cell.state)
            next_gen.append(next_gen_y)
        self.seed = next_gen
```

### Displaying the game of life on the console.

To display the seeds on the console we can create a new class called Render_seed. Since we have to use the two classes that we create before in this class, is a good idea to use the **Dependency Injection** for this class. Dependency Injection is a way to create loosely coupled units, which is really helpful if we need to mock any method of the dependencies.

```py

from .grid import Grid

class Render_seed():

    def __init__(self, grid: Grid):
        self.seed = grid.seed
        self.grid = grid

```
Now, we can mock any method or attribute of Grid that we may use.
Let's define the requirements for this Class:
 - A method ```next_frame``` which updates the seed, with the next generation seed. This seed is a frame which will be printed on the terminal.
 - A method ```print_frame``` to print the actual seed on the terminal.
 - A method ```render_n_frames``` to print n seeds on the terminal.
 
### ```next_frame``` 

Let´s write a test for a method ```next_frame```, it takes the seed on Grid.seed and updates it to the next generation.


```py
from game.render import Render_seed
from game.grid import Grid
from unittest.mock import MagicMock, Mock, mock_open
import unittest


seed = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]

seed_next_generation = [
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 1]
    ]

def test__next_frame_method__saves_next_gen_on_self_seed__given_a_seed():
    start_seed = seed
    next_seed = seed_next_generation
    mock_grid = Grid(start_seed)
    mock_grid.calculate_next_gen = MagicMock()
    mock_grid = MagicMock(seed=next_seed)

    render_object = Render_seed(mock_grid)
    render_object.next_frame()

    assert next_seed == render_object.seed
```
Let's write code to pass this test.
```py
import os, time, sys

from .grid import Grid
from seeds import *
class Render_seed():

    def __init__(self, grid: Grid):
        self.seed = grid.seed
        self.grid = grid

    def next_frame(self):
        self.grid.calculate_next_gen()
        next_gen = self.grid.seed
        self.seed = next_gen
```

## ```print_frame```

This test, reeds the seed on the class, and print it on the terminal, for esthetic reasons, the "1s" are replaced with "x" and the "0" with "·". The test is as follows.

```py
def test__print_frame_method__prints_a_frame_on_console__given_a_seed(capfd):
    seed_to_print = seed
    mock_grid = MagicMock(spec=Grid)
    mock_grid.calculate_next_gen = MagicMock()
    mock_grid = MagicMock(seed=seed_to_print)

    render_object = Render_seed(mock_grid)
    render_object.print_frame()
    out, _ = capfd.readouterr()

    assert out == 'x x · · \nx x · · \n· · x x \n· · x x \n\r'

```
And the implementation of this is:

```py
    def print_frame(self):
        line = ''
        for x_location in range(len(self.seed)):
            for y_location in range(len(self.seed[0])):
                if self.seed[x_location][y_location] == 1:
                    line += 'x '
                else:
                    line += '· '
            line += '\n'
        print(line, end="\r")        

```
## ```render_n_frames```

Finally we need a function to render the frames like an animation, clearing the screen after every frame and printing the others. The test is as follows.

```py
@unittest.mock.patch('os.system')
def test__render_n_frames_method__prints_frames_on_console__given_seed(os_system):
    seed_to_print = seed
    grid = Grid(seed_to_print)
    n_frames = 9
    number_of_clear = n_frames - 1

    render_object = Render_seed(grid)
    render_object.render_n_frames(n_frames)
    
    os_system.assert_called_with('clear')
    assert os_system.call_count == number_of_clear
```
Note that we test how many times the os.system('clear') is called, this way we can test how many times the seeds were printed.

```py
    def render_n_frames(self, n: int):
        for frame in range(1, n):
            os.system('clear')
            self.print_frame()
            time.sleep(0.3)
            self.next_frame()

```

Finally, we are done!!
If you followed this tutorial correctly, you can call an axillary script [start.py](/games/start.py) to print the output of a given seed.
```
python3 run_the_game.py [name of a seed in seeds.py]
``` 
For example:

```
python3 start.py seed_star
```

Prints:

![pattern](/docs/static/images/pattern.gif)

