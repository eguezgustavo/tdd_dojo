# Game of life using TDD

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970, It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. To learn more about it you can check the [Wiki](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) page.

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live(state ```1```) or dead(state ```0```), (or populated and unpopulated, respectively). Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

So, you can take these rules as our business requirements and start TDD!

Note: use the command ````python3 -m pytest -svv```` to run the test.

## Demo

If you want to try a demo of your code, you should develop a class called ```Cell``` in [cell.py](game/cell.py) which is constructed with the state of a single cell, and implements the methods to replicate the behavior of only one cell with all the rules described before, the class should have a method which returns the next state of the cell given the number of neighbors.

After that, you should develop a class called ```Grid``` in [grid.py](game/grid.py) this class is constructed with an array of two dimensions like:
```py
grid_state = [
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 1]
] 
```          
Each element represents the state of a cell. This class should have a method to return a grid with the next state. Finally, you can build a class called Render_seed, it should have methods to print the next state on the console, clear the console and repeat the process0. You can do it in [render.py](game/render.py). The test files of all of this classes atr in ./tests

## Solution

Remember that you can always check a possible solution in:

```
git checkout Exercise_2_Solution
```

## Here you can see the desired output

![pattern](/docs/static/images/pattern.gif)