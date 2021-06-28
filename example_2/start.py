import sys

from game.render import Render_seed
from game.grid import Grid
from seeds import *

if __name__ == '__main__':
    
    render = Render_seed(
        Grid(eval(sys.argv[1]))
    )
    
    render.render_n_frames(30)
