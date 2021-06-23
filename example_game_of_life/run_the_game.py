import sys, time, os
from game.grid import Grid
from game.cell import Cell
from .seeds import *

def render_grid(seed):
    grid = Grid(seed)
    for i in range(30):
        sys.stdout.write('\r')
        line = ''
        for x in range(len(grid.seed)):
            for y in range(len(grid.seed[0])):
                if grid.seed[x][y] == 1:
                    line += 'x '
                else:
                    line += '· '
            line += '\n'   
        os.system('clear')
        print(line, end="\r")          
        time.sleep(0.4)
        grid.calculate_next_gen()
        

if __name__ == '__main__':
    try:
        test_cell = Cell(0)
        test_grid = Grid(seed_loaf)
    except:
        print('Not implemented yet')
        sys.exit()

    try:
        render_grid(eval(sys.argv[1]))
    except:
        print('Wrong seed')
        sys.exit()