from game.render import Render_seed
from game.grid import Grid
from unittest.mock import MagicMock
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


def test__print_frame_method__prints_a_frame_on_console__given_a_seed(capfd):
    seed_to_print = seed
    mock_grid = MagicMock(spec=Grid)
    mock_grid.calculate_next_gen = MagicMock()
    mock_grid = MagicMock(seed=seed_to_print)

    render_object = Render_seed(mock_grid)
    render_object.print_frame()
    out, _ = capfd.readouterr()

    assert out == 'x x · · \nx x · · \n· · x x \n· · x x \n\r'


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
