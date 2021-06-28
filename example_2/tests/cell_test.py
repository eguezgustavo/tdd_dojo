from game.cell import Cell
import pytest

def test__Cell_class__should_store_state__when_dead_state_is_passed():
    state = 0
    
    dead_cell = Cell(state)

    assert dead_cell.state == 0
    
def test__Cell_class__should_store_state__when_alive_state_is_passed():
    state = 1

    alive_cell = Cell(state)

    assert alive_cell.state == 1

def test__Cell_class__should_raise_an_exception___when_invalid_state_is_passed():
    state = 3

    with pytest.raises(Exception) as e_info:
        Cell(state)
    
    assert e_info.value.args[0] == 'Invalid state'

def test__update_state_method__update_state_to_dead__when_less_than_two_neighbors_live():
    live_cell_with_1_neighbor = Cell(1)
    live_cell_with_2_neighbor = Cell(1)

    live_cell_with_1_neighbor.update_state(0)
    live_cell_with_2_neighbor.update_state(1)

    assert live_cell_with_1_neighbor.state == 0
    assert live_cell_with_2_neighbor.state == 0

def test__update_state_method__update_state_to_live__when_state_is_live_and_two_or_three_neighbors_live():
    live_cell_with_2_neighbor = Cell(1)
    live_cell_with_3_neighbor = Cell(1)

    live_cell_with_2_neighbor.update_state(2)
    live_cell_with_3_neighbor.update_state(3)

    assert live_cell_with_2_neighbor.state == 1
    assert live_cell_with_3_neighbor.state == 1

def test__update_state_method__update_state_to_dead__when_state_is_live_and_more_than_three_neighbors_live():
    live_cell_with_4_neighbor = Cell(1)

    live_cell_with_4_neighbor.update_state(4)

    assert live_cell_with_4_neighbor.state == 0

def test__update_state_method__update_state_to_live__when_state_is_dead_and_three_neighbors_live():
    dead_cell_with_3_live_neighbor = Cell(0)

    dead_cell_with_3_live_neighbor.update_state(3)

    assert dead_cell_with_3_live_neighbor.state == 1
    