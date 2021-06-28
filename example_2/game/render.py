import os, time, sys

from .grid import Grid
class Render_seed():

    def __init__(self, grid: Grid):
        self.seed = grid.seed
        self.grid = grid

    def next_frame(self):
        self.grid.calculate_next_gen()
        next_gen = self.grid.seed
        self.seed = next_gen
    
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
    
    def render_n_frames(self, n: int):
        for frame in range(1, n):
            os.system('clear')
            self.print_frame()
            time.sleep(0.3)
            self.next_frame()
